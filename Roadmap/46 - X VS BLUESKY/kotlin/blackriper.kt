import com.mongodb.client.model.Filters
import com.mongodb.client.model.Filters.eq
import com.mongodb.client.model.Updates
import com.mongodb.kotlin.client.coroutine.MongoClient
import com.mongodb.kotlin.client.coroutine.MongoDatabase
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.async
import kotlinx.coroutines.flow.firstOrNull
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.flow.toList
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import org.bson.codecs.pojo.annotations.BsonId
import org.bson.codecs.pojo.annotations.BsonProperty
import org.bson.types.ObjectId
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

/*
Base de Datos  a utilizar MongoDB
Driver de Koltin para mongo usando suspend
https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/quick-start/
*/

//obtener  base de datos de mongo y crear enum de colecciones

const val URI_MONGO="YOUR_MONGO_URI or MONGO_SRV"
const val MONGO_DATABASE="Bluesky"
enum class Collections{
    Posts,
    Users
}


val getDatabaseMongo={
    databaseName: String ->
    val mongoClient=MongoClient.create(connectionString =URI_MONGO )
    val database= mongoClient.getDatabase(databaseName)
    Pair(mongoClient,database)
}


//1.-Capa Modelos

class UserNotFound(message: String): Exception(message)

data class User constructor(
    @BsonId
    val id: ObjectId= ObjectId(),
    var name : String="",
    val following: MutableList<ObjectId> = mutableListOf<ObjectId>()
     )

fun userBuilder(block:User.()-> Unit):User= User().apply(block)

data class Post constructor(
    @BsonId
    val id: ObjectId= ObjectId(),
    @BsonProperty("user_id")
    var userId: String="",
    @BsonProperty("user_name")
    var username: String="",
    var content: String="",
    @BsonProperty("total_likes")
    var totalLikes: Long=0,
    @BsonProperty("created_At")
    val createdAt: LocalDateTime= LocalDateTime.now()
)
fun postBuilder(block :Post.()-> Unit):Post=Post().apply(block)

interface UserRepository{
    suspend fun registerUser():User
    suspend fun unOrfollowing(userId: ObjectId, follUser: ObjectId, isFollowing: Boolean)
    suspend fun findUser(userName: String):User
}


interface PostRepository{
    suspend fun createNewPost(actualUser:User): Boolean
    suspend fun deletePost(postId: ObjectId): Boolean
    suspend fun unOrLike(postId: ObjectId,unlike: Boolean)
    suspend fun getRecentPost(): List<Post>
    suspend fun  getPostByUserId(userId: ObjectId): List<Post>
}


interface SocialMedia{
   suspend fun  renderUserMenu()
}

//2.- capa repository

class UserRepo(private  val database: MongoDatabase):UserRepository{
    private val userColl=database.getCollection<User>(collectionName = Collections.Users.name)

    override suspend fun registerUser(): User {
       println("Enter your username")
       val nameUser=readLine()?:"default"
       val user=userBuilder {
           name=nameUser.lowercase()
       }
        userColl.insertOne(user).also {
            println("user added with id= ${it.insertedId}")
        }
        return user
    }

    override suspend fun unOrfollowing(userId: ObjectId, follUser: ObjectId, isFollowing: Boolean) {
        val user=userColl.find(Filters.eq("_id",userId)).firstOrNull()
        var newFollowing= mutableListOf<ObjectId>()

        if (user!=null) newFollowing=user.following
        else throw UserNotFound("user with $userId not found")

        if (isFollowing){
            newFollowing.removeIf{it==follUser}
            userColl.updateOne(
                Filters.eq("_id",userId),
                Updates.set("following",newFollowing)
            ).also {
                println("${follUser}  has remove you follwing list")
            }
        }

        if (! isFollowing ){
            newFollowing.add(follUser)
            userColl.updateOne(
                Filters.eq("_id",userId),
                Updates.set("following",newFollowing)
            ).also {
                println("${follUser}  has added you follwing list")
            }
        }
    }

    override suspend fun findUser(userName: String): User {
       val user= userColl.find(Filters.eq("name",userName.lowercase())).firstOrNull()
       if(user!=null)  return user
       else throw UserNotFound("user $userName not found")
      }


}

class RepoPost(private val database: MongoDatabase):PostRepository{
      private val postColl=database.getCollection<Post>(collectionName = Collections.Posts.name)

    override suspend fun createNewPost( actualUser:User): Boolean {
        var validContent=false
        var postContent=""
        while (validContent!=true){
            println("write content post ")
            postContent = readLine()!!
            if (postContent.length>200) println("the post can only contanins 200 caracters ")
            else validContent=true
        }
        val newPost=postBuilder {
            userId=actualUser.id.toHexString()
            username=actualUser.name
            content= postContent
        }

        val result=postColl.insertOne(newPost)

        return  result.insertedId!=null
    }

    override suspend fun deletePost(postId: ObjectId): Boolean =
       postColl.deleteOne(Filters.eq("_id",postId)).let {  it.deletedCount== 1L }

    override suspend fun unOrLike(postId: ObjectId, unlike: Boolean) {
        val post=postColl.find(Filters.eq("_id",postId)).firstOrNull()
        var likes=0L
        if (post!=null && unlike){
            likes=post.totalLikes+1
            postColl.updateOne(
                Filters.eq("_id",postId),
                Updates.set("total_likes",likes)
            ).also {
                println("you liked the post ${post.id}")
            }
        }

        if (post!=null && !unlike){
            likes=post.totalLikes-1
            postColl.updateOne(
                Filters.eq("_id",postId),
                Updates.set("total_likes",likes)
            ).also {
                println("you unliked the post ${post.id}")
            }
        }

    }

    override suspend fun getRecentPost(): List<Post> =
        postColl.find().limit(10).toList().sortedBy { it.createdAt }

    override suspend fun getPostByUserId(userId: ObjectId): List<Post> =
        postColl.find(Filters.eq("user_id",userId.toHexString())).toList()


}

class BlueSky(private val userRepo: UserRepo,private val postRepo: RepoPost):SocialMedia{

    private lateinit var actualUser: User

   suspend fun loginOrRegisterUser(){
        println("Login user o Register user [L] Login [R] Register")
        val option=readLine()!!.uppercase()

        when(option){
            "L"-> runCatching {
                    println("Enter a username to login ")
                    val name=readLine()!!
                    userRepo.findUser(name)
                }.onFailure {  println("error find user cause is  ${it.message}")  }
                .onSuccess { actualUser=it  }

            "R"-> runCatching { userRepo.registerUser()}
                .onFailure {  println("error register user cause is  ${it.message}")  }
                .onSuccess { actualUser=it  }
        }
    }

    override suspend fun renderUserMenu() {
        var number=0
        while (number!=3){
            println(":::::BlueSky Simulate::::::")
            println("welcome ${actualUser.name}")
            println("1.-view feed")
            println("2.- administrate post")
            println("3.- Exit")
            println("Select option")
            number=readLine()!!.toInt()
            if (number==3) break
            if (number>3) {
                println("incorrect option")
                return
            }
            when(number){
                1-> renderFeed()
                2-> administratePost()
            }

        }
    }

    private suspend fun administratePost() {
        var numpost=1
        var option=""
        while (option!="E") {
            val posts = postRepo.getPostByUserId(actualUser.id)
            actualUser=userRepo.findUser(actualUser.name)
            posts.forEach { post ->
              val post = """
              numPost: ${numpost}
              postId: ${post.id}
              ${post.content}
              createdAt: ${post.createdAt.format(DateTimeFormatter.ofPattern("dd/MM/YYYY"))}
              totalLikes: ${post.totalLikes}
             """.trimIndent()
                println(post)
                numpost++
            }
            numpost=1

            println("select action post [A] Add new Post [D] delete post E[Exit]")
            option=readLine()!!.uppercase()
            if (option=="E") break

               when (option) {
                    "A" -> postRepo.createNewPost(actualUser)
                    "D"-> {
                        println("select a post number: ")
                        var selectNum = readLine()!!.toInt()
                        if (selectNum > posts.size){
                            println("number post incorrect")
                            return
                        }
                        val post=posts[selectNum-1]
                        postRepo.deletePost(post.id)
                    }
                }


        }

    }
    private suspend fun renderFeed() {
        var numpost=1
        var option=""
      while (option!="E") {
          val posts = postRepo.getRecentPost()
          actualUser=userRepo.findUser(actualUser.name)
          posts.forEach { post ->
              val post = """
              numPost: ${numpost}
              postId: ${post.id}
              userName: ${post.username}
              ${post.content}
              createdAt: ${post.createdAt.format(DateTimeFormatter.ofPattern("dd/MM/YYYY"))}
              totalLikes: ${post.totalLikes}
              following: ${if (actualUser.following.count { it== ObjectId(post.userId) }==1) "following" else "follow"}
          """.trimIndent()
              println(post)
              numpost++
          }
          numpost=1

          println("select action post [L] like [D] diske [F] following user post [UN] unfollowing user[E] exit")
          option=readLine()!!.uppercase()
          if (option=="E") break
          println("select a post number: ")
          var selectNum = readLine()!!.toInt()
          if (selectNum > posts.size){
              println("number post incorrect")
              return
          }else {
              val post=posts[selectNum-1]
              when (option) {
                  "L" -> postRepo.unOrLike(post.id,true)
                  "D"-> postRepo.unOrLike(post.id,false)
                  "F"-> followingUser(ObjectId(post.userId),false)
                  "UN"->followingUser(ObjectId(post.userId),true)
               }
          }

      }

    }

    private  suspend fun followingUser(userId: ObjectId, isFollowing: Boolean=false){
       if (userId==actualUser.id) println("you can't follow yourself don't be a cheater")
       else userRepo.unOrfollowing(actualUser.id, userId, isFollowing)
    }

  }




fun main(): Unit= runBlocking {
    runCatching { getDatabaseMongo(MONGO_DATABASE) }
        .onFailure { println("failed to connect database ${it.message}") }
        .onSuccess {
           val job=launch {
               val userRepo = UserRepo(it.second)
               val postRepo = RepoPost(it.second)
               val social = BlueSky(userRepo, postRepo)
               social.loginOrRegisterUser()
               social.renderUserMenu()
           }
            job.join()
            it.first.close()
        }
}