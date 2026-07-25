/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#46 X VS BLUESKY
-------------------------------------------------------
* EJERCICIO:
 * La alternativa descentralizada a X, Bluesky, comienza a atraer
 * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 * 
 * Implementa un sistema que simule el comportamiento de estas
 * redes sociales.
 * 
 * Debes crear las siguientes operaciones:
 * - Registrar un usuario por nombre e identificador único.
 * - Un usuario puede seguir/dejar de seguir a otro.
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.   
 * - Eliminación de un post.
 * - Posibilidad de hacer like (y eliminarlo) en un post.
 * - Visualización del feed de un usuario con sus 10 publicaciones
 *   más actuales ordenadas desde la más reciente.
 * - Visualización del feed de un usuario con las 10 publicaciones
 *   más actuales de los usuarios que sigue ordenadas 
 *   desde la más reciente.
 *   
 * Cuando se visualiza un post, debe mostrarse:
 * ID de usuario, nombre de usuario, texto del post, 
 * fecha de creación y número total de likes.
 * 
 * Controla errores en duplicados o acciones no permitidas.
 */
// ________________________________________________________
const { format } = require('util');

const log = {
    info: (message, ...args) => console.log(`[INFO] ${format(message, ...args)}`),
    warning: (message, ...args) => console.warn(`[WARN] ${format(message, ...args)}`),
    error: (message, ...args) => console.error(`[ERROR] ${format(message, ...args)}`),
};

class Posts {
    constructor() {
        this.__post_dt = {};
    }

    __verifyPost(idUser, idPost, nameFunc) {
        if (!(idUser in this.__post_dt)) {
            log.error("'%s': El ID %s no tiene posts.", nameFunc, idUser);
            return false;
        }

        if (!(idPost in this.__post_dt[idUser])) {
            log.error("'%s': El Post (%s) no existe.", nameFunc, idPost);
            return false;
        }

        return true;
    }

    createPost(idUser, content) {
        if (content.length > 200) {
            log.error("'createPost': content > 200 caracteres.");
            return;
        }

        if (!(idUser in this.__post_dt)) {
            this.__post_dt[idUser] = {};
        }

        const idPost = Object.keys(this.__post_dt[idUser]).length + 1;
        this.__post_dt[idUser][idPost] = {
            content,
            timestamp: new Date(),
            likes: new Set(),
        };

        log.info("El ID %s creó un post(ID: %s).", idUser, idPost);
    }

    deletePost(idUser, idPost) {
        if (this.__verifyPost(idUser, idPost, "deletePost")) {
            delete this.__post_dt[idUser][idPost];
            log.info("El post: %s de usuario: %s ha sido eliminado.", idPost, idUser);
        }
    }

    likePost(idUser, idAuthor, idPost) {
        if (this.__verifyPost(idAuthor, idPost, "likePost")) {
            this.__post_dt[idAuthor][idPost].likes.add(idUser);
            log.info("El usuario %s dio like al post %s de usuario %s.", idUser, idPost, idAuthor);
        }
    }

    removeLike(idUser, idAuthor, idPost) {
        if (this.__verifyPost(idAuthor, idPost, "removeLike")) {
            this.__post_dt[idAuthor][idPost].likes.delete(idUser);
            log.info("El usuario %s anuló el like al post %s de usuario %s.", idUser, idPost, idAuthor);
        }
    }

    getRecentPosts(idUser, limit = 10) {
        if (idUser in this.__post_dt) {
            const sortedPosts = Object.values(this.__post_dt[idUser])
                .sort((a, b) => b.timestamp - a.timestamp);

            return sortedPosts.slice(0, limit);
        }

        return [];
    }
}

class Users {
    constructor() {
        this.__users_dt = {};
    }

    __idExists(id, nameFunc = "") {
        if (id in this.__users_dt) {
            return true;
        }

        log.warning("'%s': ID: %s no encontrada.", nameFunc, id);
        return false;
    }

    addUser(name) {
        const id = Object.keys(this.__users_dt).length + 1;
        this.__users_dt[id] = {
            name,
            following: new Set(),
            followers: new Set(),
        };

        log.info("Usuario %s-%s registrado.", id, name);
    }

    followUser(id, toId) {
        if (this.__idExists(id, "followUser") && this.__idExists(toId, "followUser")) {
            this.__users_dt[id].following.add(toId);
            this.__users_dt[toId].followers.add(id);
            log.info("ID: %s está siguiendo a ID: %s.", id, toId);
        }
    }

    unfollowUser(id, toId) {
        if (this.__idExists(id, "unfollowUser") && this.__idExists(toId, "unfollowUser")) {
            this.__users_dt[id].following.delete(toId);
            this.__users_dt[toId].followers.delete(id);
            log.info("El ID: %s dejó de seguir al ID: %s.", id, toId);
        }
    }

    getName(idUser) {
        if (this.__idExists(idUser, "getName")) {
            return this.__users_dt[idUser].name;
        }

        return "";
    }
}

// ________________________________________________________
class Program {
    constructor(posts, users) {
        this.__posts = new posts();
        this.__users = new users();
    }

    __printFeed(idUser) {
        const name = this.__users.getName(idUser);
        if (!name) {
            console.log(`Usuario ID: ${idUser} no encontrado.`);
            return;
        }

        const last10 = this.__posts.getRecentPosts(idUser, 10);
        console.log(`\nFeed\n_______\nID: '${idUser}' - Nombre: '${name}'`);
        if (last10.length === 0) {
            console.log("No tiene publicaciones.");
            return;
        }

        last10.forEach(post => {
            console.log(`_______\n${post.content}`);
            console.log(`Creado: '${post.timestamp}'`);
            console.log(`Likes: '${post.likes.size}'`);
        });
    }

    run() {
        // CLI
    }

    tests() {
        this.__users.addUser("Ken"); // id=1
        this.__users.addUser("Zoe"); // id=2

        this.__users.followUser(1, 2);
        this.__users.followUser(2, 1);
        this.__users.unfollowUser(2, 1);

        this.__posts.createPost(2, "Primer post."); // id=1
        this.__posts.createPost(2, "Segundo post."); // id=2
        this.__posts.deletePost(2, 2);
        this.__posts.createPost(2, "Otro post."); // id=2
        this.__posts.likePost(1, 2, 1);
        this.__posts.removeLike(1, 2, 1);
        this.__posts.likePost(1, 2, 2);

        this.__printFeed(2);
        this.__printFeed(1);
    }
}

// _______________________________________
const program = new Program(Posts, Users);
program.tests();
// program.run();
