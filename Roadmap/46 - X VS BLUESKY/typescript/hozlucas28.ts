import type {UUID} from 'crypto'
import {randomUUID} from 'crypto'
import readline from 'node:readline/promises'

/* -------------------------------------------------------------------------- */
/*                                   CLASSES                                  */
/* -------------------------------------------------------------------------- */

/* ---------------------------------- Post ---------------------------------- */

interface IPost {
    getID: () => UUID
    getContent: () => string
    getDate: () => Date
    getAuthor: () => string
    getLikes: () => string[]

    addLike: (uName: string) => void
    removeLike: (uName: string) => void
}

interface PostConstructor {
    author: string
    content: string
}

class Post implements IPost {
    private likes: string[]
    private readonly author: string
    private readonly content: string
    private readonly date: Date
    private readonly id: UUID

    public constructor({author, content}: PostConstructor) {
        if (content.length > 200)
            throw new Error(
                'Content of the post exceed the maximum length (200 chars)'
            )

        this.author = author
        this.content = content
        this.date = new Date()
        this.id = randomUUID()
        this.likes = []
    }

    public getAuthor(): string {
        return this.author
    }

    public getContent(): string {
        return this.content
    }

    public getDate(): Date {
        return this.date
    }

    public getID(): UUID {
        return this.id
    }

    public getLikes(): string[] {
        return this.likes
    }

    private getLikeIndex(uName: string): number {
        return this.likes.findIndex((likeUName) => likeUName === uName)
    }

    public addLike(uName: string): void {
        const likeI: number = this.getLikeIndex(uName)
        if (likeI != -1) throw new Error(`"${uName}" like already exists`)

        this.likes.push(uName)
    }

    public removeLike(uName: string): void {
        const likeI: number = this.getLikeIndex(uName)
        if (likeI == -1) throw new Error(`"${uName}" like doesn't  exist`)

        this.likes.splice(likeI, 1)
    }
}

/* ---------------------------------- User ---------------------------------- */

interface IUser {
    getUName: () => string
    getFollowers: () => string[]
    getFollowings: () => string[]
    getPosts: () => UUID[]

    __addFollower: (uName: string) => void
    __removeFollower: (uName: string) => void
    createPost: (content: string) => void
    deletePost: (id: UUID) => void
    follow: (uName: string) => void
    likePost: (id: UUID) => void
    unfollow: (uName: string) => void
    unlikePost: (id: UUID) => void
}

interface UserConstructor {
    uName: string
}

class User implements IUser {
    private followers: string[]
    private followings: string[]
    private posts: UUID[]
    private readonly uName: string

    public constructor({uName}: UserConstructor) {
        this.followers = []
        this.followings = []
        this.posts = []
        this.uName = uName
    }

    public getFollowers(): string[] {
        return this.followers
    }

    public getFollowings(): string[] {
        return this.followings
    }

    public getPosts(): UUID[] {
        return this.posts
    }

    public getUName(): string {
        return this.uName
    }

    private getFollowerIndex(uName: string): number {
        return this.followers.findIndex(
            (followerUName) => followerUName == uName
        )
    }

    private getFollowingIndex(uName: string): number {
        return this.followings.findIndex(
            (followingUName) => followingUName == uName
        )
    }

    private getPostIndex(id: UUID): number {
        return this.posts.findIndex((postID) => postID == id)
    }

    public createPost(content: string): void {
        const post: IPost = new Post({author: this.uName, content})
        const database: IDatabase = Database.getInstance()

        database.__addNewPost(post)
        this.posts.push(post.getID())
    }

    public deletePost(id: UUID): void {
        const postI: number = this.getPostIndex(id)
        if (postI == -1)
            throw new Error(
                `"${this.uName}" doesn't posted the post with "${id}" id`
            )

        const database: IDatabase = Database.getInstance()

        database.__deletePost(id)
        this.posts.splice(postI, 1)
    }

    public follow(uName: string): void {
        const followingI: number = this.getFollowingIndex(uName)
        if (followingI != -1)
            throw new Error(`"${this.uName}" already follows "${uName}"`)

        const database: IDatabase = Database.getInstance()

        const userFollowed: IUser | undefined = database.getUser(uName)
        if (!userFollowed) throw new Error(`"${this.uName}" doesn't exist`)

        userFollowed.__addFollower(this.uName)
        this.followings.push(uName)
    }

    public likePost(id: UUID): void {
        const database: IDatabase = Database.getInstance()
        const post: IPost | undefined = database.getPost(id)
        if (!post) throw new Error(`${id} post doesn't exist`)

        post.addLike(this.uName)
    }

    public unfollow(uName: string): void {
        const followingI: number = this.getFollowingIndex(uName)
        if (followingI == -1)
            throw new Error(`"${this.uName}" doesn't follow "${uName}"`)

        const database: IDatabase = Database.getInstance()

        const userUnfollowed: IUser | undefined = database.getUser(uName)
        if (!userUnfollowed) throw new Error(`"${this.uName}" doesn't exist`)

        userUnfollowed.__removeFollower(this.uName)
        this.followings.splice(followingI, 1)
    }

    public unlikePost(id: UUID): void {
        const database: IDatabase = Database.getInstance()
        const post: IPost | undefined = database.getPost(id)
        if (!post) throw new Error(`${id} post doesn't exist`)

        post.removeLike(this.uName)
    }

    public __addFollower(uName: string): void {
        this.followers.push(uName)
    }

    public __removeFollower(uName: string): void {
        const followerI: number = this.getFollowerIndex(uName)
        if (followerI == -1)
            throw new Error(`"${this.uName}" isn't follow by "${uName}"`)

        this.followers.splice(followerI, 1)
    }
}

/* -------------------------------- Database -------------------------------- */

interface IDatabase {
    getPosts: () => IPost[]
    getUsers: () => IUser[]

    getUser: (uName: string) => IUser | undefined

    getPost: (id: UUID) => IPost | undefined
    getUserFollowingsPosts: (uName: string) => IPost[]
    getUserPosts: (uName: string) => IPost[]

    deleteUser: (uName: string) => void
    postUser: (newUser: IUser) => void
    __addNewPost: (newPost: IPost) => void
    __deletePost: (post: UUID) => void
}

class Database implements IDatabase {
    private static instance: IDatabase

    private posts: IPost[]
    private users: IUser[]

    public constructor() {
        this.posts = []
        this.users = []
    }

    public static getInstance(): IDatabase {
        if (!Database.instance) Database.instance = new Database()
        return Database.instance
    }

    public getPosts(): IPost[] {
        return this.posts
    }

    public getUsers(): IUser[] {
        return this.users
    }

    public getUser(uName: string): IUser | undefined {
        return this.users.find((user) => user.getUName() == uName)
    }

    public getPost(id: UUID): IPost | undefined {
        return this.posts.find((post) => post.getID() == id)
    }

    public getUserFollowingsPosts(uName: string): IPost[] {
        const user: IUser | undefined = this.getUser(uName)
        if (!user) throw new Error(`"${uName} doesn't exist"`)

        const followings: string[] = user.getFollowings()

        let followingPosts: IPost[]
        let followingsPosts: IPost[] = []

        for (const following of followings) {
            followingPosts = this.getUserPosts(following)
            followingsPosts.push(...followingPosts)
        }

        return followingsPosts
    }

    public getUserPosts(uName: string): IPost[] {
        const user: IUser | undefined = this.getUser(uName)
        if (!user) throw new Error(`"${uName} doesn't exist"`)

        const userPostsIDs: UUID[] = user.getPosts()

        let post: IPost | undefined
        const userPosts: IPost[] = []

        for (const postID of userPostsIDs) {
            post = this.getPost(postID)
            if (post) userPosts.push(post)
        }

        return userPosts
    }

    public deleteUser(uName: string): void {
        const userI: number = this.users.findIndex(
            (user) => user.getUName() === uName
        )
        if (userI == -1) throw new Error(`"${uName}" doesn't exist`)

        this.users.splice(userI, 1)
    }

    public postUser(newUser: IUser): void {
        if (this.getUserIndex(newUser) != -1)
            throw new Error(`"${newUser.getUName()}" already exists`)

        this.users.push(newUser)
    }

    public __addNewPost(newPost: IPost): void {
        this.posts.push(newPost)
    }

    public __deletePost(post: UUID): void {
        const postI: number = this.getPostIndex(post)
        if (postI == -1) throw new Error(`"${post}" doesn't exist`)

        this.posts.splice(postI, 1)
    }

    private getUserIndex(user: IUser): number {
        return this.users.findIndex((u) => u.getUName() === user.getUName())
    }

    private getPostIndex(post: UUID): number {
        return this.posts.findIndex((p) => p.getID() === post)
    }
}

/* -------------------------------------------------------------------------- */
/*                                    MAIN                                    */
/* -------------------------------------------------------------------------- */

;(async () => {
    const database: IDatabase = Database.getInstance()

    const rl: readline.Interface = readline.createInterface({
        output: process.stdout,
        input: process.stdin,
    })

    let input01: string
    let input02: string
    let uName: string
    let user: IUser | undefined
    let posts: IPost[]
    let postContent: string
    let postID: UUID
    let post: IPost
    let i: number

    do {
        console.log(
            '> Available operations...\n\n' +
                '  1 - Sign up a new user.\n' +
                '  2 - Sign in as user.\n' +
                '  0 - Exit.'
        )

        input01 = (await rl.question('\n> Enter an operation: ')).trim()

        switch (input01) {
            case '0':
                break

            case '1':
                uName = (await rl.question('\n> Username: ')).trim()
                user = new User({uName})
                database.postUser(user)
                break

            case '2':
                uName = (await rl.question('\n> Username: ')).trim()
                user = database.getUser(uName)
                if (!user) {
                    console.log('> Username not found.')
                    break
                }

                do {
                    console.log(
                        '\n> Available operations...\n\n' +
                            '  1 - Create a new post.\n' +
                            '  2 - Show personal feed.\n' +
                            '  3 - Show following feed.\n' +
                            '  4 - Delete post.\n' +
                            '  5 - Follow user.\n' +
                            '  6 - Unfollow user.\n' +
                            '  7 - Like post.\n' +
                            '  8 - Unlike post.\n' +
                            '  0 - Exit.'
                    )

                    input02 = (
                        await rl.question('\n> Enter an operation: ')
                    ).trim()

                    switch (input02) {
                        case '0':
                            break

                        case '1':
                            postContent = (
                                await rl.question(
                                    '\n> Post content (maximum 200 characters): '
                                )
                            ).trim()
                            user.createPost(postContent)
                            break

                        case '2':
                            posts = database.getUserPosts(user.getUName())

                            posts = posts.sort(
                                (a, b) =>
                                    b.getDate().valueOf() -
                                    a.getDate().valueOf()
                            )

                            for (i = 0; i < 10 && i < posts.length; i++) {
                                post = posts[i]
                                console.log(`\n> ID: "${post.getID()}".`)
                                console.log(`> Author: "${post.getAuthor()}".`)
                                console.log(
                                    `> Content: "${post.getContent()}".`
                                )
                                console.log(
                                    `> Creation date: "${post.getDate()}".`
                                )
                                console.log(
                                    `> Likes: ${post.getLikes().length}.`
                                )
                            }
                            break

                        case '3':
                            posts = database.getUserFollowingsPosts(
                                user.getUName()
                            )

                            posts = posts.sort(
                                (a, b) =>
                                    b.getDate().valueOf() -
                                    a.getDate().valueOf()
                            )

                            for (i = 0; i < 10 && i < posts.length; i++) {
                                post = posts[i]
                                console.log(`\n> ID: "${post.getID()}".`)
                                console.log(`> Author: "${post.getAuthor()}".`)
                                console.log(
                                    `> Content: "${post.getContent()}".`
                                )
                                console.log(
                                    `> Creation date: "${post.getDate()}".`
                                )
                                console.log(
                                    `> Likes: ${post.getLikes().length}.`
                                )
                            }
                            break

                        case '4':
                            postID = (
                                await rl.question('\n> Post ID: ')
                            ).trim() as UUID
                            user.deletePost(postID)
                            break

                        case '5':
                            uName = (await rl.question('\n> Username: ')).trim()
                            user.follow(uName)
                            break

                        case '6':
                            uName = (await rl.question('\n> Username: ')).trim()
                            user.unfollow(uName)
                            break

                        case '7':
                            postID = (
                                await rl.question('\n> Post ID: ')
                            ).trim() as UUID
                            user.likePost(postID)
                            break

                        case '8':
                            postID = (
                                await rl.question('\n> Post ID: ')
                            ).trim() as UUID
                            user.unlikePost(postID)
                            break

                        default:
                            console.log('\n> Invalid operation! Try again...')
                    }
                } while (input02 != '0')
                break

            default:
                console.log('\n> Invalid operation! Try again...')
        }

        console.log()
    } while (input01 != '0')

    rl.close()
})()
