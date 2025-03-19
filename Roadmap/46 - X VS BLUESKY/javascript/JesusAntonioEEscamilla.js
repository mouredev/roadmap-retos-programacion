/** #46 - JavaScript -> Jesus Antonio Escamilla */

/**
 * X VS BLUESKY.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

class User {
    constructor(id, name) {
        this.id = id;
        this.name = name;
        this.following = new Set();
        this.posts = [];
    }

    follow(user){
        if (this.id === user.id) {
            throw new Error('No puedes seguirte a ti mismo.');
        }
        if (this.following.has(user.id)) {
            throw new Error('Ya sigues a este usuario.');
        }

        this.following.add(user.id);
    }

    unfollow(user){
        if (!this.following.has(user.id)) {
            throw new Error('No estás siguiendo a este usuario.');
        }

        this.following.delete(user.id);
    }

    createPost(text){
        if (text.length > 200) {
            throw new Error('El texto del post no puede exceder los 200 caracteres.');
        }

        const post = {
            id: Date.now(),
            userId: this.id,
            userName: this.name,
            text,
            date: new Date(),
            likes: new Set()
        };

        this.posts.push(post);
        return post;
    }

    deletePost(postId){
        const index = this.posts.findIndex(post => post.id === postId);
        if (index === -1) {
            throw new Error('El post no existe.');
        }

        this.posts.splice(index, 1);
    }

    likePost(post){
        if (post.likes.has(this.id)) {
            throw new Error('Ya has dado like a este post.');
        }

        post.likes.add(this.id);
    }

    unlikePost(post){
        if (!post.likes.has(this.id)) {
            throw new Error('No has dado like a este post.');
        }

        post.likes.delete(this.id);
    }

    getFeed(limit = 10){
        return this.posts
            .sort((a, b) => b.delete - a.delete)
            .slice(0, limit)
    }

    getFollowingFeed(users, limit = 10){
        const followingPost = [];
        for(const userId of this.following){
            const user = users.find(u => u.id === userId);
            if (user) {
                followingPost.push(...user.getFeed());
            }
        }
        return followingPost
            .sort((a, b) => b.date - a.date)
            .slice(0, limit);
    }
}

function displayPost(post) {
    console.log(`ID de Usuario: ${post.userId}`);
    console.log(`Nombre de Usuario: ${post.userName}`);
    console.log(`Texto: ${post.text}`);
    console.log(`Fecha de Creación: ${post.date}`);
    console.log(`Número de Likes: ${post.likes.size}\n`);
}

// Datos del ejemplo
const users = [];
const user1 = new User(1, 'Alice');
const user2 = new User(2, 'Bob');
const user3 = new User(3, 'Charlie');

users.push(user1, user2, user3);

// Registrar de post:
const post1 = user1.createPost('Hola, este es mi primer post.');
const post2 = user1.createPost('¿Alguien más está emocionado por el nuevo lanzamiento?');
const post3 = user2.createPost('¡Hola a todos! Este es mi primer post.');

// Seguimientos de usuarios
user1.follow(user2);
user1.follow(user3);

// Like a un post
user1.likePost(post2);

// Visualización de feed de un usuario
console.log('Feed de Alice:');
user1.getFeed().forEach(displayPost);

// Visualización de feed de un usuario con las publicaciones de los usuarios que sigue
console.log('Feed de Alice con publicaciones de usuarios que sigue:');
user1.getFollowingFeed(users).forEach(displayPost);