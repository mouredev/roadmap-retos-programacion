// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

class SocialNetwork {
    constructor() {
        this.users = new Map();
        this.posts = new Map();
        this.following = new Map();
    }

    registerUser(userId, name) {
        if (this.users.has(userId)) {
            throw new Error("User ID already exists.");
        }
        this.users.set(userId, { name, posts: [] });
        this.following.set(userId, new Set());
    }

    toggleFollow(followerId, followedId) {
        if (!this.users.has(followerId) || !this.users.has(followedId)) {
            throw new Error("User ID not found.");
        }
        const following = this.following.get(followerId);
        if (following.has(followedId)) {
            following.delete(followedId);
        } else {
            following.add(followedId);
        }
    }

    createPost(userId, postId, text) {
        if (!this.users.has(userId)) {
            throw new Error("User ID not found.");
        }
        if (this.posts.has(postId)) {
            throw new Error("Post ID already exists.");
        }
        if (text.length > 200) {
            throw new Error("Text exceeds maximum length of 200 characters.");
        }
        const post = {
            postId,
            userId,
            text,
            createdAt: new Date(),
            likes: 0
        };
        this.posts.set(postId, post);
        this.users.get(userId).posts.push(post);
    }

    deletePost(postId) {
        if (!this.posts.has(postId)) {
            throw new Error("Post ID not found.");
        }
        const post = this.posts.get(postId);
        this.users.get(post.userId).posts = this.users.get(post.userId).posts.filter(p => p.postId !== postId);
        this.posts.delete(postId);
    }

    toggleLike(postId) {
        if (!this.posts.has(postId)) {
            throw new Error("Post ID not found.");
        }
        const post = this.posts.get(postId);
        post.likes = post.likes === 0 ? 1 : 0;
    }

    getUserFeed(userId) {
        if (!this.users.has(userId)) {
            throw new Error("User ID not found.");
        }
        const posts = [...this.users.get(userId).posts];
        posts.sort((a, b) => b.createdAt - a.createdAt);
        this.displayFeed(posts.slice(0, 10));
    }

    getFollowingFeed(userId) {
        if (!this.users.has(userId)) {
            throw new Error("User ID not found.");
        }
        const feed = [];
        for (const followedId of this.following.get(userId)) {
            const followedPosts = this.users.get(followedId).posts;
            feed.push(...followedPosts);
        }
        feed.sort((a, b) => b.createdAt - a.createdAt);
        this.displayFeed(feed.slice(0, 10));
    }

    displayFeed(posts) {
        posts.forEach(post => {
            const userName = this.users.get(post.userId).name;
            console.log(`User ID: ${post.userId}, Name: ${userName}, Text: ${post.text}, `
                        + `Created At: ${post.createdAt}, Likes: ${post.likes}`);
        });
    }
}

// Example Usage
const sn = new SocialNetwork();
sn.registerUser("u1", "Alice");
sn.registerUser("u2", "Bob");

sn.toggleFollow("u1", "u2");

sn.createPost("u1", "p1", "Hello, this is Alice!");
sn.createPost("u2", "p2", "Hi, this is Bob's post.");
sn.toggleLike("p2");

console.log("\n[+] - User Feed for Alice:");
sn.getUserFeed("u1");

console.log("\n[+] - Following Feed for Alice:");
sn.getFollowingFeed("u1");

sn.deletePost("p1");
console.log("\n[+] - After Deleting Alice's Post:");
sn.getUserFeed("u1");
