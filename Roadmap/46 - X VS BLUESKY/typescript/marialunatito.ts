/**
 *
 * 1. creacion de un usuario (validar por email)
 * 2. agregar post, with created_at and id (200 caract. max.)
 *  2.1 al ver un post mostrar id user, nombre, text, fecha de creacion y likes
 * 3. puedo dar like a post
 * 3. eliminar post
 * 4. un usuario puede seguir o dejar de seguir a otro usuario
 * 5. ver feed of user with her/his 10 publications recently
 * 6. ver feed de usuarios q tengan las 10 publicaciones mas recientes
 */

import { randomUUID } from "crypto";

class User {
  id: string;
  name: string;
  createdAt: Date;
  posts: Map<string, Post> = new Map();
  followers: Map<string, User> = new Map();

  private constructor(name: string) {
    this.id = randomUUID();
    this.name = name;
    this.createdAt = new Date();
  }

  static create(name: string): User {
    return new User(name);
  }
}

class Post {
  id: string;
  userId: string;
  post: string;
  createdAt: Date;
  countLike: number = 0;
  listUserLike: Map<string, User> = new Map();

  private constructor(post: Post["id"], userId: User["id"]) {
    this.id = randomUUID();
    this.post = post;
    this.createdAt = new Date();
    this.userId = userId;
  }

  static create(post: Post["id"], userId: User["id"]): Post {
    return new Post(post, userId);
  }
}

interface UserRepository {
  createUser(user: User): Promise<User>;
  createPost(post: Post): Promise<Post>;
  follow(follower: string, followed: string): Promise<boolean>;
  unFollow(follower: string, followed: string): Promise<boolean>;
  like(userIdTo: string, userIdFrom: string, postId: string): Promise<boolean>;
  unLike(
    userIdTo: string,
    userIdFrom: string,
    postId: string
  ): Promise<boolean>;
}

class UserRepository implements UserRepository {
  private store: Map<string, User> = new Map();

  createUser(user: User): Promise<User> {
    this.store.set(user.id, user);
    return Promise.resolve(user);
  }

  createPost(post: Post): Promise<Post> {
    const user = this.store.get(post.userId);

    if (!user) throw new Error(`User ${post.userId} no found`);
    user.posts.set(post.id, post);

    return Promise.resolve(post);
  }

  follow(follower: string, followed: string): Promise<boolean> {
    try {
      const user = this.store.get(follower);

      if (!user) throw new Error(`User ${follower} no found`);
      const _followed_ = this.store.get(followed);

      if (!_followed_) throw new Error(`User ${_followed_} no found`);
      user.followers.set(_followed_.id, _followed_);

      return Promise.resolve(true);
    } catch (err) {
      console.log(err);
      return Promise.resolve(true);
    }
  }

  unFollow(follower: string, followed: string): Promise<boolean> {
    try {
      const user = this.store.get(follower);

      if (!user) throw new Error(`User ${follower} no found`);
      const _followed_ = this.store.get(followed);

      if (!_followed_) throw new Error(`User ${_followed_} no found`);
      user.followers.delete(_followed_.id);

      return Promise.resolve(true);
    } catch (err) {
      console.log(err);
      return Promise.resolve(true);
    }
  }

  like(userIdTo: string, userIdFrom: string, postId: string): Promise<boolean> {
    try {
      const userTo = this.store.get(userIdTo);

      if (!userTo) throw new Error(`User ${userIdTo} not found`);
      const userFrom = this.store.get(userIdFrom);

      if (!userFrom) throw new Error(`User ${userFrom} not found`);
      const _posts = userFrom.posts.get(postId);

      if (!_posts) throw new Error(`Post ${postId} not found`);
      _posts.countLike++;
      _posts.listUserLike.set(userFrom.id, userFrom);

      return Promise.resolve(true);
    } catch (err) {
      console.log(err);
      return Promise.resolve(true);
    }
  }

  unLike(
    userIdTo: string,
    userIdFrom: string,
    postId: string
  ): Promise<boolean> {
    try {
      const userTo = this.store.get(userIdTo);

      if (!userTo) throw new Error(`User ${userIdTo} not found`);
      const userFrom = this.store.get(userIdFrom);

      if (!userFrom) throw new Error(`User ${userFrom} not found`);
      const _posts = userFrom.posts.get(postId);

      if (!_posts) throw new Error(`Post ${postId} not found`);
      _posts.countLike--;
      _posts.listUserLike.delete(userFrom.id);

      return Promise.resolve(true);
    } catch (err) {
      console.log(err);
      return Promise.resolve(true);
    }
  }

  listStore() {
    return this.store;
  }
}

class UserUseCase {
  constructor(private repository: UserRepository) {}

  create(name: string) {
    const user = User.create(name);
    return this.repository.createUser(user);
  }

  createPost(post: string, userId: string) {
    console.log({ post, userId });
    const _post = Post.create(post, userId);
    return this.repository.createPost(_post);
  }
}

(async () => {
  const repository = new UserRepository();
  const userCases = new UserUseCase(repository);
  const user1 = await userCases.create("Maria");
  const user2 = await userCases.create("Carmen");
  const user3 = await userCases.create("Veronica");

  userCases.createPost("this is a post", user2.id);

  const map = repository.listStore();
  for (const [id, user] of map) {
    console.log({
      id,
      user,
    });
  }
})();
