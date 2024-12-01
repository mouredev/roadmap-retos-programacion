const users = new Map();
let idCounter = 0;

class User {
    constructor(name) {
        this.id = idCounter++;
        this.name = name;
        this.following = [];
        this.posts = [];
    }

    follow(user) {
        if (!this.following.includes(user)) {
            this.following.push(user);
        }
    }

    unfollow(user) {
        const index = this.following.indexOf(user);
        if (index !== -1) {
            this.following.splice(index, 1);
        }
    }

    addPost(post) {
        this.posts.push(post);
    }

    deletePost(postId) {
        const index = this.posts.findIndex(post => post.id === postId);
        if (index !== -1) {
            this.posts.splice(index, 1);
            return true;
        }
        return false;
    }

    getMyFeed() {
        return this.posts.slice().sort((a, b) => b.creationDate - a.creationDate).slice(0, 10);
    }

    getFollowingFeed() {
        let feed = [];
        this.following.forEach(user => {
            feed = feed.concat(user.posts);
        });
        return feed.sort((a, b) => b.creationDate - a.creationDate).slice(0, 10);
    }
}

class Post {
    constructor(user, content) {
        this.id = idCounter++;
        this.user = user;
        this.content = content;
        this.creationDate = new Date();
        this.likes = new Set();
    }

    addLike(user) {
        this.likes.add(user);
    }

    removeLike(user) {
        this.likes.delete(user);
    }

    toString() {
        return `Post de ${this.user.name}: ${this.content} | Likes: ${this.likes.size}`;
    }
}

function registerUser() {
    const name = prompt("Ingrese el nombre de usuario: ");
    if (users.has(name)) {
        console.log("Error: El usuario ya existe.");
    } else {
        const newUser = new User(name);
        users.set(name, newUser);
        console.log("Usuario registrado exitosamente: " + name);
    }
}

function followUser() {
    const userName = prompt("Tu nombre de usuario: ");
    const user = users.get(userName);
    const toFollowName = prompt("Nombre del usuario a seguir: ");
    const toFollow = users.get(toFollowName);
    if (user && toFollow) {
        user.follow(toFollow);
        console.log(`Ahora sigues a ${toFollow.getName()}`);
    }
}

function unfollowUser() {
    const userName = prompt("Tu nombre de usuario: ");
    const user = users.get(userName);
    const toUnfollowName = prompt("Nombre del usuario a dejar de seguir: ");
    const toUnfollow = users.get(toUnfollowName);
    if (user && toUnfollow) {
        user.unfollow(toUnfollow);
        console.log(`Has dejado de seguir a ${toUnfollow.getName()}`);
    }
}

function createPost() {
    const userName = prompt("Tu nombre de usuario: ");
    const user = users.get(userName);
    if (user) {
        const content = prompt("Ingrese el texto del post (máximo 200 caracteres): ");
        if (content.length > 200) {
            console.log("Error: El texto excede los 200 caracteres.");
        } else {
            const post = new Post(user, content);
            user.addPost(post);
            console.log("Post creado exitosamente: " + post);
        }
    }
}

function deletePost() {
    const userName = prompt("Tu nombre de usuario: ");
    const user = users.get(userName);
    if (user) {
        const postId = prompt("Ingrese el ID del post a eliminar: ");
        const success = user.deletePost(postId);
        if (success) {
            console.log("Post eliminado exitosamente.");
        } else {
            console.log("Error: No se encontró el post con ese ID.");
        }
    }
}

function likePost() { // No implementado
    const userName = prompt("Tu nombre de usuario: ");
    const user = users.get(userName);
    if (user) {
        const authorName = prompt("Ingrese el nombre del usuario que publicó el post: ");
        const author = users.get(authorName);
        if (author) {
            let postNumber;
            do {
                try {
                    postNumber = parseInt(prompt("Ingrese el número del post que desea dar like (1 para el primero, 2 para el segundo, etc.): "));
                    break;
                } catch (error) {
                    console.log("Debe ingresar un número entero.");
                }
            } while (true);
            const posts = author.posts;
            if (postNumber > 0 && postNumber <= posts.length) {
                const post = posts[postNumber - 1];
                post.addLike(user);
                console.log("Diste like al post de " + author.name);
            } else {
                console.log("Error: Número de post inválido.");
            }
        } else {
            console.log("Error: Usuario no encontrado.");
        }
    }
}

function unlikePost() {
    const userName = prompt("Tu nombre de usuario: ");
    const user = users.get(userName);
    if (user) {
        const postId = prompt("Ingrese el ID del post a eliminar like: ");
        let post = null;
        for (let u of users.values()) {
            post = u.posts.find(p => p.id === postId);
            if (post) break;
        }
        if (post) {
            post.removeLike(user);
            console.log("Eliminaste tu like del post.");
        } else {
            console.log("Error: No se encontró el post con ese ID.");
        }
    }
}

function viewMyFeed() {
    const userName = prompt("Tu nombre de usuario: ");
    const user = users.get(userName);
    if (user) {
        console.log("Tu feed:");
        user.getMyFeed().forEach(post => console.log(post.toString()));
    }
}

function viewFollowingFeed() {
    const userName = prompt("Tu nombre de usuario: ");
    const user = users.get(userName);
    if (user) {
        console.log("Feed de usuarios que sigues:");
        user.getFollowingFeed().forEach(post => console.log(post.toString()));
    }
}

function listUsers() {
    if (users.size === 0) {
        console.log("No hay usuarios registrados actualmente.");
    } else {
        console.log("Usuarios registrados:");
        users.forEach(user => {
            console.log(`- ${user.name} (ID: ${user.id})`);
        });
    }
}

function main() {
    let option;
    do {
        console.log("\nMenú:");
        console.log("1. Registrar usuario");
        console.log("2. Seguir a un usuario");
        console.log("3. Dejar de seguir a un usuario");
        console.log("4. Crear un post");
        console.log("5. Eliminar un post");
        console.log("6. Dar like a un post");
        console.log("7. Eliminar like de un post");
        console.log("8. Ver mi feed");
        console.log("9. Ver feed de usuarios seguidos");
        console.log("10. Listar usuarios registrados");
        console.log("11. Salir");
        do {
            try {
                option = parseInt(prompt("Seleccione una opción: "));
            } catch (error) {
                console.log("Debe ingresar un número entero.");
            }
        } while (isNaN(option));
        switch (option) {
            case 1: registerUser(); break;
            case 2: followUser(); break;
            case 3: unfollowUser(); break;
            case 4: createPost(); break;
            case 5: deletePost(); break;
            case 6: likePost(); break;
            case 7: unlikePost(); break;
            case 8: viewMyFeed(); break;
            case 9: viewFollowingFeed(); break;
            case 10: listUsers(); break;
            case 11: console.log("Saliendo de la red social..."); break;
            default: console.log("Opción inválida. Intente nuevamente."); break;
        }
    } while (option !== 11);
}

main();
