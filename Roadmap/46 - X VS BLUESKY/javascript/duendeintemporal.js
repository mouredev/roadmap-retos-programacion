//#46 - X VS BLUESKY
/*
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

let log = console.log;

window.addEventListener('load', () => {
    const body = document.querySelector('body');
    const title = document.createElement('h1');

    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');

    title.textContent = 'Retosparaprogramadores #46.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');

    body.appendChild(title);

    setTimeout(() => {
        alert('Retosparaprogramadores #46. Please open the Browser Developer Tools.');
    }, 2000);
    
    log('Retosparaprogramadores #46');
});

class User {
    constructor(name, id) {
        this.name = name;
        this.id = id;
        this.following = new Set();
        this.posts = [];
    }

    follow(user) {
        this.following.add(user);
        log(`${this.name} followed ${user.name}`);
    }

    unfollow(user) {
        this.following.delete(user);
        log(`${this.name} unfollowed ${user.name}`);
    }

    createPost(text) {
        if (text.length > 200) {
            throw new Error("Post text cannot exceed 200 characters.");
        }
        const post = new Post(this, text);
        this.posts.push(post);
        log(`${this.name} created a post: "${text}"`);
        return post;
    }

    deletePost(post) {
        const index = this.posts.indexOf(post);
        if (index === -1) {
            throw new Error("Post not found.");
        }
        this.posts.splice(index, 1);
        log(`${this.name} deleted a post: "${post.text}"`);
    }

    getFeed() {
        const feed = this.posts.slice().sort((a, b) => b.createdAt - a.createdAt).slice(0, 10);
        log(`${this.name}'s feed:`, feed.map(post => post.toString()));
        return feed;
    }

    getFollowingFeed() {
        const feed = [];
        for (const user of this.following) {
            feed.push(...user.posts.slice().sort((a, b) => b.createdAt - a.createdAt).slice(0, 10));
        }
        feed.sort((a, b) => b.createdAt - a.createdAt);
        log(`${this.name}'s following feed:`, feed.map(post => post.toString()));
        return feed.slice(0, 10);
    }
}

class Post {
    constructor(user, text) {
        this.id = crypto.randomUUID();
        this.user = user;
        this.text = text;
        this.createdAt = new Date();
        this.likes = new Set();
    }

    like(user) {
        this.likes.add(user);
        log(`${user.name} liked a post: "${this.text}" by ${this.user.name}`);
    }

    unlike(user) {
        this.likes.delete(user);
        log(`${user.name} unliked a post: "${this.text}" by ${this.user.name}`);
    }

    getTotalLikes() {
        return this.likes.size;
    }

    toString() {
        return `Post by ${this.user.name}: "${this.text}" (Likes: ${this.getTotalLikes()})`;
    }
}

const user1 = new User("Niko Zen", 1);
const user2 = new User("Bob Marley", 2);
const user3 = new User("Psicotrogato", 3);

user1.follow(user2);
user1.follow(user3);

const post1 = user1.createPost("I'm almost finishing this roadmap for developers.");
const post1_1 = user1.createPost("I'm thinking in the possibility of start some of the developer course in mouredev, to get more possibilities to find a remote job.");
const post1_2 = user1.createPost("I start to feel comfortable with Javascript and its ecosystem, right now I'm studying Next.js.");
const post2 = user2.createPost("But Jamming!");
const post2_1 = user2.createPost("I'm not going to wait in vain for your love!");
const post2_2 = user2.createPost("I shot the sheriff, but I didn't shoot the deputy!");
const post3 = user3.createPost("In a society that has abolished every kind of adventure, the only adventure that remains is abolishing the society.");
const post3_1 = user3.createPost("My life is perfect because I accept it as it is.");

post1.like(user2);
post1.like(user3);

// Log the feeds with informative output
log("User Feeds:");
log("User 1 Feed:", user1.getFeed());
log("User 1 Following Feed:", user1.getFollowingFeed());
log("User 2 Feed:", user2.getFeed());
log("User 2 Following Feed:", user2.getFollowingFeed());
log("User 3 Feed:", user3.getFeed());
log("User 3 Following Feed:", user3.getFollowingFeed());


  
/*  Output Example:
Niko Zen followed Bob Marley
46.js:64 Niko Zen followed Psicotrogato
46.js:78 Niko Zen created a post: "I'm almost finishing this roadmap for developers."
46.js:78 Niko Zen created a post: "I'm thinking in the possibility of start some of the developer course in mouredev, to get more possibilities to find a remote job."
46.js:78 Niko Zen created a post: "I start to feel comfortable with Javascript and its ecosystem, right now I'm studying Next.js."
46.js:78 Bob Marley created a post: "But Jamming!"
46.js:78 Bob Marley created a post: "I'm not going to wait in vain for your love!"
46.js:78 Bob Marley created a post: "I shot the sheriff, but I didn't shoot the deputy!"
46.js:78 Psicotrogato created a post: "In a society that has abolished every kind of adventure, the only adventure that remains is abolishing the society."
46.js:78 Psicotrogato created a post: "My life is perfect because I accept it as it is."
46.js:119 Bob Marley liked a post: "I'm almost finishing this roadmap for developers." by Niko Zen
46.js:119 Psicotrogato liked a post: "I'm almost finishing this roadmap for developers." by Niko Zen
46.js:156 User Feeds:
46.js:93 Niko Zen's feed: (3) [`Post by Niko Zen: "I'm thinking in the possibility…e possibilities to find a remote job." (Likes: 0)`, `Post by Niko Zen: "I start to feel comfortable wit…stem, right now I'm studying Next.js." (Likes: 0)`, `Post by Niko Zen: "I'm almost finishing this roadmap for developers." (Likes: 2)`]
46.js:157 User 1 Feed: (3) [Post, Post, Post]
46.js:103 Niko Zen's following feed: (5) ['Post by Psicotrogato: "In a society that has aboli…at remains is abolishing the society." (Likes: 0)', 'Post by Psicotrogato: "My life is perfect because I accept it as it is." (Likes: 0)', `Post by Bob Marley: "I shot the sheriff, but I didn't shoot the deputy!" (Likes: 0)`, `Post by Bob Marley: "I'm not going to wait in vain for your love!" (Likes: 0)`, 'Post by Bob Marley: "But Jamming!" (Likes: 0)']
46.js:158 User 1 Following Feed: (5) [Post, Post, Post, Post, Post]
46.js:93 Bob Marley's feed: (3) [`Post by Bob Marley: "I shot the sheriff, but I didn't shoot the deputy!" (Likes: 0)`, `Post by Bob Marley: "I'm not going to wait in vain for your love!" (Likes: 0)`, 'Post by Bob Marley: "But Jamming!" (Likes: 0)']
46.js:159 User 2 Feed: (3) [Post, Post, Post]
46.js:103 Bob Marley's following feed: []
46.js:160 User 2 Following Feed: []
46.js:93 Psicotrogato's feed: (2) ['Post by Psicotrogato: "In a society that has aboli…at remains is abolishing the society." (Likes: 0)', 'Post by Psicotrogato: "My life is perfect because I accept it as it is." (Likes: 0)']
46.js:161 User 3 Feed: (2) [Post, Post]
46.js:103 Psicotrogato's following feed: []
46.js:162 User 3 Following Feed: []
46.js:51 Retosparaprogramadores #46
*/
