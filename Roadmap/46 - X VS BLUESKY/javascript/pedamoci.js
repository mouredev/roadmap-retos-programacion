import { randomBytes } from 'node:crypto'
import readline from 'readline'

const PREVIOUS_USERS_BY_ID = {
  "a1b2c3d4": {
    username: "carlos",
    posts: ["p1k2l3m4", "p0j1k2l3", "p9i0j1k2", "p8h9i0j1", "p7g8h9i0", "p6f7g8h9", "p5e6f7g8", "p4d5e6f7", "p3c4d5e6", "p2b3c4d5", "p1a2b3c4"],
    followings: ["e5f6g7h8", "i9j0k1l2", "m3n4o5p6", "f8g9h0i1"],
    likedPosts: ["p22a2b3c", "p33a2b3c", "p44a2b3c", "p55k2l3m", "p56l3m4n"]
  },
  "e5f6g7h8": {
    username: "ana",
    posts: ["p23b3c4d", "p22a2b3c"],
    followings: ["a1b2c3d4", "m3n4o5p6", "f8g9h0i1"],
    likedPosts: ["p1a2b3c4", "p9i0j1k2", "p46c4d5e", "p52i0j1k"]
  },
  "i9j0k1l2": {
    username: "luis",
    posts: ["p34b3c4d", "p33a2b3c"],
    followings: ["a1b2c3d4", "e5f6g7h8", "f8g9h0i1"],
    likedPosts: ["p2b3c4d5", "p23b3c4d", "p55k2l3m", "p1k2l3m4"]
  },
  "m3n4o5p6": {
    username: "sofia",
    posts: ["p54k2l3m", "p53j1k2l", "p52i0j1k", "p51h9i0j", "p50g8h9i", "p49f7g8h", "p48e6f7g", "p47d5e6f", "p46c4d5e", "p45b3c4d", "p44a2b3c"],
    followings: ["a1b2c3d4", "e5f6g7h8", "i9j0k1l2", "f8g9h0i1"],
    likedPosts: ["p1a2b3c4", "p4d5e6f7", "p22a2b3c", "p34b3c4d", "p56l3m4n"]
  },
  "f8g9h0i1": {
    username: "diego",
    posts: ["p56l3m4n", "p55k2l3m"],
    followings: ["a1b2c3d4", "m3n4o5p6", "i9j0k1l2"],
    likedPosts: ["p9i0j1k2", "p44a2b3c", "p52i0j1k", "p1k2l3m4", "p33a2b3c"]
  },
}

const PREVIOUS_USERS_BY_USERNAME = {
  "carlos": "a1b2c3d4",
  "ana": "e5f6g7h8",
  "luis": "i9j0k1l2",
  "sofia": "m3n4o5p6",
  "diego": "f8g9h0i1"
}

const PREVIOUS_POSTS = {
  "p1k2l3m4": { text: "¡Viernes al fin!", date: "2022-10-21T17:00:00Z", userId: "a1b2c3d4", likes: 2 },
  "p0j1k2l3": { text: "Probando un nuevo restaurante coreano.", date: "2022-10-21T13:00:00Z", userId: "a1b2c3d4", likes: 0 },
  "p9i0j1k2": { text: "Nueva configuración de escritorio lista.", date: "2022-10-20T11:10:00Z", userId: "a1b2c3d4", likes: 2 },
  "p8h9i0j1": { text: "Extrañando las vacaciones.", date: "2022-10-19T14:20:00Z", userId: "a1b2c3d4", likes: 0 },
  "p7g8h9i0": { text: "Cocinando pasta para la cena.", date: "2022-10-18T20:45:00Z", userId: "a1b2c3d4", likes: 0 },
  "p6f7g8h9": { text: "Viendo una película clásica.", date: "2022-10-17T21:30:00Z", userId: "a1b2c3d4", likes: 0 },
  "p5e6f7g8": { text: "El clima está increíble hoy.", date: "2022-10-16T12:00:00Z", userId: "a1b2c3d4", likes: 0 },
  "p4d5e6f7": { text: "Hoy salí a correr 5km.", date: "2022-10-15T07:00:00Z", userId: "a1b2c3d4", likes: 1 },
  "p3c4d5e6": { text: "¿Alguien recomienda un buen libro?", date: "2022-10-14T18:00:00Z", userId: "a1b2c3d4", likes: 0 },
  "p2b3c4d5": { text: "Aprendiendo Node.js desde cero.", date: "2022-10-13T10:15:00Z", userId: "a1b2c3d4", likes: 1 },
  "p1a2b3c4": { text: "Disfrutando de un café por la mañana.", date: "2022-10-12T08:30:00Z", userId: "a1b2c3d4", likes: 2},
  "p23b3c4d": { text: "Mi gata no me deja trabajar.", date: "2024-01-16T10:00:00Z", userId: "e5f6g7h8", likes: 1 },
  "p22a2b3c": { text: "El viaje a la montaña fue espectacular.", date: "2024-01-15T09:15:22Z", userId: "e5f6g7h8", likes: 2 },
  "p34b3c4d": { text: "Terminando mi primer proyecto con React.", date: "2026-03-21T15:30:00Z", userId: "i9j0k1l2", likes: 1 },
  "p33a2b3c": { text: "La inteligencia artificial es fascinante.", date: "2026-03-20T11:05:44Z", userId: "i9j0k1l2", likes: 2 },
  "p54k2l3m": { text: "Feliz semana a todos.", date: "2015-05-20T08:00:00Z", userId: "m3n4o5p6", likes: 0 },
  "p53j1k2l": { text: "Escuchando jazz.", date: "2015-05-19T20:00:00Z", userId: "m3n4o5p6", likes: 0 },
  "p52i0j1k": { text: "Pintando con acuarelas.", date: "2015-05-18T17:45:00Z", userId: "m3n4o5p6", likes: 2 },
  "p51h9i0j": { text: "Nuevo lienzo en blanco.", date: "2015-05-17T11:30:00Z", userId: "m3n4o5p6", likes: 0 },
  "p50g8h9i": { text: "Paz mental.", date: "2015-05-16T14:00:00Z", userId: "m3n4o5p6", likes: 0 },
  "p49f7g8h": { text: "Mi jardín está floreciendo.", date: "2015-05-15T09:00:00Z", userId: "m3n4o5p6", likes: 0 },
  "p48e6f7g": { text: "Mirando las estrellas.", date: "2015-05-14T22:00:00Z", userId: "m3n4o5p6", likes: 0 },
  "p47d5e6f": { text: "El té de jazmín es lo mejor.", date: "2015-05-13T10:10:00Z", userId: "m3n4o5p6", likes: 0 },
  "p46c4d5e": { text: "Leyendo bajo la lluvia.", date: "2015-05-12T16:20:00Z", userId: "m3n4o5p6", likes: 1 },
  "p45b3c4d": { text: "Caminata nocturna.", date: "2015-05-11T23:00:00Z", userId: "m3n4o5p6", likes: 0 },
  "p44a2b3c": { text: "Un pequeño poema para el alma.", date: "2015-05-10T22:45:10Z", userId: "m3n4o5p6", likes: 2 },
  "p56l3m4n": { text: "La disciplina vence al talento.", date: "2025-02-28T09:30:00Z", userId: "f8g9h0i1", likes: 2 },
  "p55k2l3m": { text: "Entrenando duro para el maratón.", date: "2025-02-27T08:00:15Z", userId: "f8g9h0i1", likes: 2 }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

const createErrorMsg = msg => {
  return  `\n****************************************************************\n` +
          `Error: ${msg}` +
          `\n****************************************************************\n`
}
const createSuccessMsg = msg => {
  return  `\n----------------------------------------------------------------\n` +
          `Success: ${msg}` +
          `\n----------------------------------------------------------------\n`
}
const createMenuMsg = () => {
  return  "--------------------- ACTIONS ----------------------\n" +
          "| 1. Register user               2. Follow user    |\n" +
          "| 3. Unfollow user               4. Create post    |\n" +
          "| 5. Delete post                 6. Like post      |\n" +
          "| 7. Unlike post                 8. View user feed |\n" +
          "| 9. View followings feed        10. Exit          |\n" +
          "----------------------------------------------------"
}

const createPostMsg = info => {
  return  `~~~~~~~~~~~~~~~~~~~~~ POST ~~~~~~~~~~~~~~~~~~~~~~\n` + 
          `${info.text}\n` + 
          `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n` + 
          `Date: ${new Date(info.date).toLocaleString()}                Likes:${info.likes}\n` +
          `User: ${info.username}                   Post ID: ${info.postId}\n` +
          `User ID: ${info.userId}\n`
}

const ask = q => new Promise(r => rl.question(q,r))

class Renderer {
  static error(msg) {
    console.error(createErrorMsg(msg))
  }

  static success(msg) {
    console.log(createSuccessMsg(msg))
  }

  static menu() {
    console.log(createMenuMsg())
  }

  static post(info) {
    console.log(createPostMsg(info))
  }
}

class Validator {
  static isValidUsername(username) {
    if (!username) throw new Error("The username cannot be empty")
    return username
  }

  static isValidText(text) {
    if (!text || text.length > 200) throw new Error("The text is invalid")
    return text
  }
}

class IdHelper {
  static createId() { return randomBytes(4).toString("hex") }

  static getValidId(usersIds, postsId) {
    let i = 0

    while (i < 10) {
      const id = IdHelper.createId()
      if (!usersIds[id] && !postsId[id]) return id
      i++
    }

    throw new Error("The ID could not be created correctly. Please try again later.")
  }
}

class FeedHelper {
  static getPostsId(usersId, users) {
    const postsId = usersId.flatMap(userId => users[userId].posts)
    return postsId
  }

  static getOrderPosts(postsId, posts) {
    const orderPostsId = [...postsId].sort((postIdOne, postIdTwo) => {
      if (posts[postIdOne].date > posts[postIdTwo].date) return -1
      return 1
    }).slice(0, 10)
    return orderPostsId
  }
}

class InputHelper {
  static async getExistingUsername(users) {
    const username = Validator.isValidUsername((await ask("Enter the username: ")).trim())
    if (!users[username]) throw new Error("The username does not exists")
    return username
  }

  static async getExistingPostId(postsId) {
    const id = (await ask("Enter the post id: ")).trim()
    if (!postsId[id]) throw new Error("There is no post with this ID")
    return id
  }
}

class User {
  constructor(username) {
    this.username = username
    this.posts = []
    this.followings = []
    this.likedPosts = []
  }
}

class Post {
  constructor(userId, text) {
    this.text = text
    this.userId = userId
    this.date = new Date()
    this.likes = 0
  }
}

class UserService {
  constructor(usersById, usersByUsername) {
    this.usersById = usersById
    this.usersByUsername = usersByUsername
  }

  registerUser(userId, username) {
    this.usersById[userId] = new User(username)
    this.usersByUsername[username] = userId
    return Renderer.success("The user has successfully registered")
  }

  followUser(sourceUserId, targetUserId) {
    this.usersById[sourceUserId].followings.push(targetUserId)
    return Renderer.success(`${this.usersById[sourceUserId].username} started following ${this.usersById[targetUserId].username}`)
  }

  unfollowUser(sourceUserId, targetUserId) {
    this.usersById[sourceUserId].followings = this.usersById[sourceUserId].followings.filter(fId => fId !== targetUserId)
    return Renderer.success(`${this.usersById[sourceUserId].username} has unfollowing ${this.usersById[targetUserId].username}`)
  }
}

class PostService {
  constructor(usersById, posts) {
    this.usersById = usersById
    this.posts = posts
  }

  createPost(userId, postId, text) {
    this.posts[postId] = new Post(userId, text)
    this.usersById[userId].posts.push(postId)
    return Renderer.success("The post has successfully crated")
  }

  deletePost(userId, postId) {
    for (const userInfo of Object.values(this.usersById)) {
      if (userInfo.likedPosts.includes(postId)) userInfo.likedPosts = userInfo.likedPosts.filter(pId => pId !== postId)
    }
    delete this.posts[postId]
    this.usersById[userId].posts = this.usersById[userId].posts.filter(pId => pId !== postId)
    return Renderer.success("The post has successfully deleted")
  }

  likePost(userId, postId) {
    this.posts[postId].likes++
    this.usersById[userId].likedPosts.push(postId)
    return Renderer.success(`${this.usersById[userId].username} has liked the post`)
  }

  unlikePost(userId, postId) {
    this.posts[postId].likes--
    this.usersById[userId].likedPosts = this.usersById[userId].likedPosts.filter(pId => pId !== postId)
    return Renderer.success(`${this.usersById[userId].username} has unliked the post`)
  }
}

class FeedService {
  constructor(usersById, posts) {
    this.usersById = usersById
    this.posts = posts
  }

  viewFeed(userId) {
    const orderPostsId = FeedHelper.getOrderPosts(this.usersById[userId].posts, posts)
    for (const postId of orderPostsId) {
      Renderer.post({
        text: posts[postId].text,
        date: posts[postId].date,
        likes: posts[postId].likes,
        userId,
        username: this.usersById[userId].username,
        postId
      })
    }
  }

  viewFollowingsFeed(userId) {
    const orderPostsId = FeedHelper.getOrderPosts(FeedHelper.getPostsId(this.usersById[userId].followings, this.usersById), this.posts)
    for (const postId of orderPostsId) {
      Renderer.post({
        text: this.posts[postId].text,
        date: this.posts[postId].date,
        likes: this.posts[postId].likes,
        userId: this.posts[postId].userId,
        username: this.usersById[posts[postId].userId].username,
        postId
      })
    }
  }
}

class Program {
  constructor(userService, postService, feedService) {
    this.usersById = PREVIOUS_USERS_BY_ID
    this.usersByUsername = PREVIOUS_USERS_BY_USERNAME
    this.posts = PREVIOUS_POSTS
    this.userService = new userService(this.usersById, this.usersByUsername)
    this.postService = new postService(this.usersById, this.posts)
    this.feedService = new feedService(this.usersById, this.posts)
  }

  async start() {
    let opt
    do {
      Renderer.menu()
      opt = (await ask("Enter the number of the action: ")).trim()
      try {
        await this.setOption(opt)
      } catch (e) {
        Renderer.error(e.message)
      }
    } while (opt !== "10")
    rl.close()
  }

  async setOption(opt) {
    switch (opt) {
      case "1":{
        const username = await Validator.isValidUsername((await ask("Enter the username: ")).trim())
        if (this.usersByUsername[username]) throw new Error("The username already exists")
        const id = IdHelper.getValidId(this.usersById, this.posts)
        this.userService.registerUser(id, username)
        break}
      case "2":{
        const sourceUserId = this.usersByUsername[await InputHelper.getExistingUsername(this.usersByUsername)]
        const targetUserId = this.usersByUsername[await InputHelper.getExistingUsername(this.usersByUsername)]
        if (sourceUserId === targetUserId) throw new Error("You can't follow yourself")
        if (this.usersById[sourceUserId].followings.includes(targetUserId)) throw new Error("You already follow this user")
        this.userService.followUser(sourceUserId, targetUserId)
        break}
      case "3":{
        const sourceUserId = this.usersByUsername[await InputHelper.getExistingUsername(this.usersByUsername)]
        const targetUserId = this.usersByUsername[await InputHelper.getExistingUsername(this.usersByUsername)]
        if (!this.usersById[sourceUserId].followings.includes(targetUserId)) throw new Error("You don't follow this user")
        this.userService.unfollowUser(sourceUserId, targetUserId)
        break}
      case "4":{
        const userId = this.usersByUsername[await InputHelper.getExistingUsername(this.usersByUsername)]
        const text = await Validator.isValidText((await ask("Enter the text: ")).trim())
        const postId = IdHelper.getValidId(this.usersById, this.posts)
        this.postService.createPost(userId, postId, text)
        break}
      case "5":{
        const userId = this.usersByUsername[await InputHelper.getExistingUsername(this.usersByUsername)]
        const postId = await InputHelper.getExistingPostId(this.posts)
        if (!this.usersById[userId].posts.includes(postId)) throw new Error("The user has no posts with that ID")
        this.postService.deletePost(userId, postId)
        break}
      case "6":{
        const userId = this.usersByUsername[await InputHelper.getExistingUsername(this.usersByUsername)]
        const postId = await InputHelper.getExistingPostId(this.posts)
        if (this.usersById[userId].posts.includes(postId)) throw new Error("You can't like your own post")
        if (this.usersById[userId].likedPosts.includes(postId)) throw new Error("You've already liked that post")
        this.postService.likePost(userId, postId)
        break}
      case "7":{
        const userId = this.usersByUsername[await InputHelper.getExistingUsername(this.usersByUsername)]
        const postId = await InputHelper.getExistingPostId(this.posts)
        if (!this.usersById[userId].likedPosts.includes(postId)) throw new Error("You haven't liked that post")
        this.postService.unlikePost(userId, postId)
        break}
      case "8":{
        const userId = this.usersByUsername[await InputHelper.getExistingUsername(this.usersByUsername)]
        if (this.usersById[userId].posts.length === 0) throw new Error("The user has no posts")
        this.feedService.viewFeed(userId)
        break}
      case "9":{
        const userId = this.usersByUsername[await InputHelper.getExistingUsername(this.usersByUsername)]
        if (this.usersById[userId].followings.length === 0) throw new Error("The user doesn't follow anyone")
        this.feedService.viewFollowingsFeed(userId)
        break}
      case "0":{
        console.log(this.usersById)
        console.log(this.posts)
        break}
      default:break;
    }
  }
}

const program = new Program(UserService, PostService, FeedService)
program.start()