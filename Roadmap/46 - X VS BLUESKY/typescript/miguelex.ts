import readline from 'readline';

class User {
    id: string;
    name: string;
    following: string[];
    posts: Post[];

    constructor(id: string, name: string) {
        this.id = id;
        this.name = name;
        this.following = [];
        this.posts = [];
    }

    follow(user: User): void {
        if (this.following.includes(user.id)) {
            console.log(`${this.name} ya sigue a ${user.name}.`);
            return;
        }
        this.following.push(user.id);
        console.log(`${this.name} comenzó a seguir a ${user.name}.`);
    }

    unfollow(user: User): void {
        if (!this.following.includes(user.id)) {
            console.log(`${this.name} no sigue a ${user.name}.`);
            return;
        }
        this.following = this.following.filter(id => id !== user.id);
        console.log(`${this.name} dejó de seguir a ${user.name}.`);
    }
}

class Post {
    id: string;
    text: string;
    userId: string;
    createdAt: Date;
    likes: number;

    constructor(id: string, text: string, userId: string) {
        this.id = id;
        this.text = text.slice(0, 200);
        this.userId = userId;
        this.createdAt = new Date();
        this.likes = 0;
    }

    like(): void {
        this.likes++;
    }

    unlike(): void {
        if (this.likes > 0) {
            this.likes--;
        }
    }
}

class SocialNetwork {
    users: Record<string, User>;
    posts: Record<string, Post>;

    constructor() {
        this.users = {};
        this.posts = {};
    }

    registerUser(id: string, name: string): void {
        if (this.users[id]) {
            console.log(`El usuario con ID ${id} ya existe.`);
            return;
        }
        this.users[id] = new User(id, name);
        console.log(`Usuario ${name} registrado con éxito.`);
    }

    createPost(userId: string, text: string): void {
        if (!this.users[userId]) {
            console.log(`El usuario con ID ${userId} no existe.`);
            return;
        }
        const postId = `post_${Date.now()}`;
        const post = new Post(postId, text, userId);
        this.posts[postId] = post;
        this.users[userId].posts.push(post);
        console.log(`Post creado con éxito.`);
    }

    deletePost(postId: string): void {
        const post = this.posts[postId];
        if (!post) {
            console.log(`El post con ID ${postId} no existe.`);
            return;
        }
        const user = this.users[post.userId];
        user.posts = user.posts.filter(p => p.id !== postId);
        delete this.posts[postId];
        console.log(`Post eliminado con éxito.`);
    }

    likePost(postId: string): void {
        const post = this.posts[postId];
        if (!post) {
            console.log(`El post con ID ${postId} no existe.`);
            return;
        }
        post.like();
        console.log(`Post ${postId} recibió un like.`);
    }

    unlikePost(postId: string): void {
        const post = this.posts[postId];
        if (!post) {
            console.log(`El post con ID ${postId} no existe.`);
            return;
        }
        post.unlike();
        console.log(`Like eliminado del post ${postId}.`);
    }

    viewFeed(userId: string): void {
        const user = this.users[userId];
        if (!user) {
            console.log(`El usuario con ID ${userId} no existe.`);
            return;
        }

        const posts = user.posts.sort((a, b) => b.createdAt.getTime() - a.createdAt.getTime());

        console.log(`Feed de ${user.name}:`);
        posts.slice(0, 10).forEach(post => this.displayPost(post));
    }

    viewFollowedFeed(userId: string): void {
        const user = this.users[userId];
        if (!user) {
            console.log(`El usuario con ID ${userId} no existe.`);
            return;
        }

        let followedPosts: Post[] = [];
        user.following.forEach(followedId => {
            const followedUser = this.users[followedId];
            if (followedUser) {
                followedPosts = followedPosts.concat(followedUser.posts);
            }
        });

        followedPosts.sort((a, b) => b.createdAt.getTime() - a.createdAt.getTime());

        console.log(`Feed de usuarios seguidos por ${user.name}:`);
        followedPosts.slice(0, 10).forEach(post => this.displayPost(post));
    }

    displayPost(post: Post): void {
        console.log(`ID: ${post.id}, Usuario: ${post.userId}, Texto: ${post.text}, Fecha: ${post.createdAt.toISOString()}, Likes: ${post.likes}`);
    }

    async interactiveMenu(): Promise<void> {
        const rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });

        const ask = (question: string): Promise<string> => new Promise(resolve => rl.question(question, resolve));

        while (true) {
            console.log(`\n--- Menú Principal ---`);
            console.log(`1. Registrar usuario`);
            console.log(`2. Crear post`);
            console.log(`3. Eliminar post`);
            console.log(`4. Dar like a un post`);
            console.log(`5. Quitar like de un post`);
            console.log(`6. Ver feed del usuario`);
            console.log(`7. Ver feed de usuarios seguidos`);
            console.log(`8. Seguir a un usuario`);
            console.log(`9. Dejar de seguir a un usuario`);
            console.log(`10. Salir`);

            const option = await ask(`Seleccione una opción: `);

            switch (option) {
                case "1":
                    const id = await ask(`Ingrese ID del usuario: `);
                    const name = await ask(`Ingrese nombre del usuario: `);
                    this.registerUser(id, name);
                    break;
                case "2":
                    const userId = await ask(`Ingrese ID del usuario: `);
                    const text = await ask(`Ingrese texto del post: `);
                    this.createPost(userId, text);
                    break;
                case "3":
                    const postId = await ask(`Ingrese ID del post: `);
                    this.deletePost(postId);
                    break;
                case "4":
                    const likePostId = await ask(`Ingrese ID del post: `);
                    this.likePost(likePostId);
                    break;
                case "5":
                    const unlikePostId = await ask(`Ingrese ID del post: `);
                    this.unlikePost(unlikePostId);
                    break;
                case "6":
                    const feedUserId = await ask(`Ingrese ID del usuario: `);
                    this.viewFeed(feedUserId);
                    break;
                case "7":
                    const followedFeedUserId = await ask(`Ingrese ID del usuario: `);
                    this.viewFollowedFeed(followedFeedUserId);
                    break;
                case "8":
                    const followerId = await ask(`Ingrese tu ID: `);
                    const followId = await ask(`Ingrese ID del usuario a seguir: `);
                    if (this.users[followerId] && this.users[followId]) {
                        this.users[followerId].follow(this.users[followId]);
                    } else {
                        console.log(`Usuario no encontrado.`);
                    }
                    break;
                case "9":
                    const unfollowerId = await ask(`Ingrese tu ID: `);
                    const unfollowId = await ask(`Ingrese ID del usuario a dejar de seguir: `);
                    if (this.users[unfollowerId] && this.users[unfollowId]) {
                        this.users[unfollowerId].unfollow(this.users[unfollowId]);
                    } else {
                        console.log(`Usuario no encontrado.`);
                    }
                    break;
                case "10":
                    rl.close();
                    console.log(`Saliendo...`);
                    return;
                default:
                    console.log(`Opción no válida.`);
            }
        }
    }
}

(async () => {
    const socialNetwork = new SocialNetwork();
    await socialNetwork.interactiveMenu();
})();
