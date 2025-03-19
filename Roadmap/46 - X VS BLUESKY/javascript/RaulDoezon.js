/*
  EJERCICIO:
  La alternativa descentralizada a X, Bluesky, comienza a atraer
  a nuevos usuarios. ¿Cómo funciona una red de este estilo?
  
  Implementa un sistema que simule el comportamiento de estas
  redes sociales.
  
  Debes crear las siguientes operaciones:
  - Registrar un usuario por nombre e identificador único.
  - Un usuario puede seguir/dejar de seguir a otro.
  - Creación de post asociado a un usuario. Debe poseer
    texto (200 caracteres máximo), fecha de creación 
    e identificador único.
  - Eliminación de un post.
  - Posibilidad de hacer like (y eliminarlo) en un post.
  - Visualización del feed de un usuario con sus 10 publicaciones
    más actuales ordenadas desde la más reciente.
  - Visualización del feed de un usuario con las 10 publicaciones
    más actuales de los usuarios que sigue ordenadas 
    desde la más reciente.
    
  Cuando se visualiza un post, debe mostrarse:
  ID de usuario, nombre de usuario, texto del post, 
  fecha de creación y número total de likes.
  
  Controla errores en duplicados o acciones no permitidas.
*/

class Register {
  constructor() {
    this.users = [];
  }

  createUser(name, userName) {
    this.name = name;
    this.userName = userName;
    this.checkUserName = this.users.findIndex((user) => user.user_name === this.userName);

    if (this.checkUserName === -1) {
      this.users.push({ name: this.name, user_name: this.userName, following: [], posts: [] });
    } else {
      console.error(`El nombre de usuario "${this.userName}" ya existe.`);
    }
  }

  follow(follower, userToFollow) {
    const checkFollower = this.users.findIndex((user) => user.user_name === follower);
    const checkUserToFollow = this.users.findIndex((user) => user.user_name === userToFollow);

    if (checkFollower > -1 && checkUserToFollow > -1) {
      if (follower !== userToFollow) {
        this.users[checkFollower].following.push(userToFollow);

        console.log(`${follower} sigue a ${userToFollow}`);
      } else {
        console.error("El usuario no puede seguirse a sí mismo.");
      }
    } else {
      console.error(`No es posible seguir al usuario "${userToFollow}"`);
    }
  }

  unfollow(follower, userToUnfollow) {
    const checkFollower = this.users.findIndex((user) => user.user_name === follower);
    const checkUserToUnfollow = this.users[checkFollower].following.findIndex((user) => user === userToUnfollow);

    if (checkFollower > -1 && checkUserToUnfollow > -1) {
      this.users[checkFollower].following.splice(checkUserToUnfollow, 1);

      console.log(`${follower} dejó de seguir a ${userToUnfollow}`);
    } else {
      console.error(`No es posible dejar de seguir al usuario "${userToUnfollow}"`);
    }
  }

  createPost(postByUser, postContent) {
    const checkUser = this.users.findIndex((user) => user.user_name === postByUser);

    if (checkUser > -1) {
      let postIndex = this.users[checkUser].posts.length;

      this.users[checkUser].posts.push({ content: postContent, date: new Date(), id: `${checkUser}${postIndex}`, likes: [] });

      console.log(`"${postByUser}" creó un post.`);
    } else {
      console.error(`No se puede crear el post porque el usuario "${postByUser}" no existe`);
    }
  }

  removePost(postByUser, postID) {
    const checkUser = this.users.findIndex((user) => user.user_name === postByUser);
    const checkPostID = this.users[checkUser].posts.findIndex((post) => post.id === postID);

    if (checkUser > -1 && checkPostID > -1) {
      this.users[checkUser].posts.splice(checkPostID, 1);

      console.log(`El post ${checkPostID} del usuario ${postByUser} fue eliminado`);
    } else {
      console.error(`No fue posible eliminar el post. Posiblemente el usuario "${postByUser}" no existe o, el post con ID "${postID}"`);
    }
  }

  likePost(userLike, postUser, postID) {
    const checkUserPost = this.users.findIndex((user) => user.user_name === postUser);
    const checkUserLike = this.users.findIndex((user) => user.user_name === userLike);
    const checkPostID = this.users[checkUserPost].posts.findIndex((post) => post.id === postID);

    if (checkUserPost > -1 && checkUserLike > -1 && checkPostID > -1) {
      this.users[checkUserPost].posts[checkPostID].likes.push(userLike);

      console.log(`El usuario "${userLike}" dió Me Gusta al post ${postID}.`);
    } else {
      console.error("No fue posible dar Me gusta al post.");
    }
  }

  unlikePost(userUnlike, postUser, postID) {
    const checkUserPost = this.users.findIndex((user) => user.user_name === postUser);
    const checkUserUnlike = this.users.findIndex((user) => user.user_name === userUnlike);
    const checkPostID = this.users[checkUserPost].posts.findIndex((post) => post.id === postID);

    if (checkUserPost > -1 && checkUserUnlike > -1 && checkPostID > -1) {
      this.users[checkUserPost].posts[checkPostID].likes.splice(checkPostID, 1);

      console.log(`Al usuario "${userUnlike}" ya No le Gusta el post ${postID}.`);
    } else {
      console.error("No fue posible quitar el Me gusta al post.");
    }
  }

  feed(userName) {
    const checkUserName = this.users.findIndex((user) => user.user_name === userName);

    if (checkUserName > -1) {
      const user = this.users[checkUserName].name;
      const userName = this.users[checkUserName].user_name;

      console.log(`\n+++++++++ Feed de ${userName} +++++++++`);

      for (const post of this.users[checkUserName].posts.reverse()) {
        console.log(`Publicación: ${post.content}.\nFecha: ${post.date}.\nNombre: ${user}.\nID: ${userName}.\nNúmero de Me Gusta: ${post.likes.length}.`);
      }
    }
  }

  followingFeed(userName) {
    const checkUserName = this.users.findIndex((user) => user.user_name === userName);

    if (checkUserName > -1) {
      console.log(`\n+++++++++ Feed de los seguidores de ${userName} +++++++++`);

      for (const following of this.users[checkUserName].following) {
        const searchUser = this.users[this.users.findIndex((user) => user.user_name === following)];
        const userPosts = searchUser.posts.reverse();

        for (const post of userPosts) {
          console.log(`Publicación: ${post.content}.\nFecha: ${post.date}.\nNombre: ${searchUser.name}.\nID: ${searchUser.user_name}.\nNúmero de Me Gusta: ${post.likes.length}.`);
        }
      }
    }
  }

  viewArray() {
    console.log(this.users);
  }
}

let user = new Register();

user.createUser('Ana', 'Anna');
user.createUser('Raúl', 'RaulDoezon');
user.createUser('Francisco', 'Paco');
user.createUser('Ana', 'Anna');

user.follow('RaulDoezon', 'Anna');
user.follow('RaulDoezon', 'Paco');
user.follow('Anna', 'RaulDoezon');
user.follow('Anna', 'Paco');

user.unfollow('RaulDoezon', 'Paco');

user.createPost('Anna', 'Romanos 3:23 RVR60');
user.createPost('Anna', '1 Juan 1:9 RVR60');
user.createPost('RaulDoezon', 'Juan 3:16 RVR60');
user.createPost('RaulDoezon', 'Porque de tal manera amó Dios al mundo que ha dado a su hijo unigénito.');
user.createPost('RaulDoezon', 'Para que todo aquel que en Él cree no se pierda, mas tenga vida eterna.');
user.createPost('Paco', 'Colosenses 3:23 RVR60');

user.removePost('RaulDoezon', '11');

user.likePost('Anna', 'RaulDoezon', '10');
user.likePost('Anna', 'RaulDoezon', '12');
user.likePost('Anna', 'Paco', '20');
user.likePost('RaulDoezon', 'Anna', '00');
user.likePost('RaulDoezon', 'Paco', '20');
user.likePost('Paco', 'RaulDoezon', '12');
user.likePost('Paco', 'Anna', '00');

user.unlikePost('Anna', 'RaulDoezon', '10');

user.feed('Anna')

user.followingFeed('Anna');

user.viewArray();
