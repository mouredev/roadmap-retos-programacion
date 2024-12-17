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

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #46.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #46. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #46'); 
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
    }
  
    unfollow(user) {
      this.following.delete(user);
    }
  
    createPost(text) {
      if (text.length > 200) {
        throw new Error("Post text cannot exceed 200 characters.");
      }
      const post = new Post(this, text);
      this.posts.push(post);
      return post;
    }
  
    deletePost(post) {
      const index = this.posts.indexOf(post);
      if (index === -1) {
        throw new Error("Post not found.");
      }
      this.posts.splice(index, 1);
    }
  
    getFeed() {
      const feed = this.posts.slice().sort((a, b) => b.createdAt - a.createdAt).slice(0, 10);
      return feed;
    }
  
    getFollowingFeed() {
      const feed = [];
      for (const user of this.following) {
        feed.push(...user.posts.slice().sort((a, b) => b.createdAt - a.createdAt).slice(0, 10));
      }
      feed.sort((a, b) => b.createdAt - a.createdAt);
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
    }
  
    unlike(user) {
      this.likes.delete(user);
    }
  
    getTotalLikes() {
      return this.likes.size;
    }
  }
  
  const user1 = new User("Niko Zen", 1);
  const user2 = new User("Bob Marley", 2);
  const user3 = new User("Psicotrogato", 3);
  
  user1.follow(user2);
  user1.follow(user3);
  
  const post1 = user1.createPost("I'm almost finishing this roadmap for developers.");
  const post1_1 = user1.createPost("I'm thinking in the possibility of start some of the developer course in mouredev, to get more possibilities to find a remote job.");
  const post1_2 = user1.createPost("I start to feel confortable with Javascript and it's ecosystem, right now i'm studing Next.js");
  const post2 = user2.createPost("But Jamming!");
  const post2_1 = user2.createPost("I'm don't going to wait in vain for your love!");
  const post2_2 = user2.createPost("I shot the sherif, but I didn't shot the deputy!");
  const post3 = user3.createPost("In a society that has abolish every kind of adventure, the only adventure that remains is abolish the society.");
  const post3_1 = user3.createPost("My life is perfect cause I acept it as it is.");
  
  post1.like(user2);
  post1.like(user3);
  
  log(user1.getFeed()); 
  log(user1.getFollowingFeed()); 
  log(user2.getFeed()); 
  log(user2.getFollowingFeed()); 
  log(user3.getFeed()); 
  log(user3.getFollowingFeed()); 
  
/*  Output Example:
ʾ(3) [Post, Post, Post]
ʾ(5) [Post, Post, Post, Post, Post]
ʾ(3) [Post, Post, Post]
ʾ[]
ˇ(2) [Post, Post]0: PostcreatedAt: Wed Dec 11 2024 16:39:03 GMT-0400 (hora de Venezuela) {}id: "b6612f37-d80f-4a44-95da-a6759b0272c1"likes: Set(0) {size: 0}text: "In a society that has abolish every kind of adventure, the only adventure that remains is abolish the society."user: User {name: 'Psicotrogato', id: 3, following: Set(0), posts: Array(2)}[[Prototype]]: Object1: PostcreatedAt: Wed Dec 11 2024 16:39:03 GMT-0400 (hora de Venezuela) {}id: "899c11dc-974b-4d07-a23d-709aa4631dcb"likes: Set(0) {size: 0}text: "My life is perfect cause I acept it as it is."user: User {name: 'Psicotrogato', id: 3, following: Set(0), posts: Array(2)}[[Prototype]]: Objectlength: 2[[Prototype]]: Array(0)
ʾ[]
*/
ˇʾ