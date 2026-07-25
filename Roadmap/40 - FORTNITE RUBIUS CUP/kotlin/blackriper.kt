import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.engine.cio.CIO
import io.ktor.client.plugins.contentnegotiation.ContentNegotiation
import io.ktor.client.request.forms.FormDataContent
import io.ktor.client.request.get
import io.ktor.client.request.headers
import io.ktor.client.request.post
import io.ktor.client.request.setBody
import io.ktor.client.statement.bodyAsText
import io.ktor.http.HttpHeaders
import io.ktor.http.parameters
import io.ktor.serialization.kotlinx.json.json
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.async
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.asFlow
import kotlinx.coroutines.flow.toList
import kotlinx.coroutines.runBlocking
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json
import java.time.Instant
import java.time.LocalDateTime
import java.time.ZoneId
import java.time.format.DateTimeFormatter


//1.- traer lista de usuarios
val participans= listOf(
    "Abby","Ache","Adricontreras",
    "Agustin","Alexby","Ampeter",
    "Ander","AriGameplays","AriGeli",
    "Auronplay","Axozer","Beniju",
    "ByCalitos","Byviruzz","Carrera",
    "Celopan","Cheeto","CrystalMolly",
    "DarioEmehache","Dheylo","DjMariio",
    "Doble","Elvisa","Elyas360","Folagor",
    "Grefg","Guanyar","Hika","Hiper",
    "Ibai","Ibelky","illojuan","Imantado",
    "IrinaIsasia","Jesskiu","Jopa","JordiWild",
    "KenaiSouza","Keroro","KiddKeo","KikoRivera",
    "Knekro","Koko","KronnoZomber","Leviathan","LitKillan",
    "Lolalolita","Lolito","Luh","Luzu","Mangel","Mayichi",
    "Melo","MissaSinfonia","MixWell","MrJagger","NateGentile7",
    "Nexxuz","Nia","NilOjeda","Nissaxter","Ollie","Orslok","Outconsumer",
    "PapiGavi","Paracetamor","Patica","PaulaGonu","Pausenpall","Perxitaa",
    "Plex","PolisPol","Quackitty","Recuerdop","Reven","Rivers","Roberttpg","Roier",
    "Rojuu","Rubius","Shadoune","Silithur","Spoksponha","Spreen","Spursito","Staxx",
    "Suzyroxx","Vicens","Vituber","Werlyb","Xavi","Xcry","Xokas","Zarcort","Zeling","Zorman")

//2.- Configurar cliente Http Ktor
//https://ktor.io/docs/client-create-new-application.html

val ktorClient= HttpClient(CIO){
    install(ContentNegotiation){
        json(Json{
            prettyPrint=true
            ignoreUnknownKeys=true
        })
    }
}

//3.-Data clases para response , request
const val CLIENTID="<YOUR CLIENT ID>"
const val SECRET="<YOUR SECRET>"

@Serializable
data class Token(
    @SerialName("access_token")
    val token: String
)


@Serializable
data class Data(val data: List<TwitchUserDto>)

@Serializable
data class TwitchUserDto(
    val id: String,
    @SerialName("display_name")
    val userName: String,
    @SerialName("created_at")
    val createdAt: String
)

@Serializable
data class Followers(val total: Long)


data class TwitchUser(
    val userName: String,
    val createdAt: LocalDateTime,
    val followers: Long
)

//extension para convertir el usuario
fun TwitchUserDto.toTwicthUser(total: Long):TwitchUser{
    val created= Instant.parse(createdAt).let {
       it.atZone(ZoneId.systemDefault()).toLocalDateTime()
    }
    return TwitchUser(
        userName = userName,
        createdAt=created,
        followers = total
    )
}

//4.- clase para consumir la Api y clase para retornar rakings
class ParticipansApi{
   lateinit var  token: String

   suspend fun getJwtToken(){
       val response=ktorClient.post("https://id.twitch.tv/oauth2/token"){
           headers {
              append(HttpHeaders.ContentType,"application/x-www-form-urlencoded")
           }
           setBody(FormDataContent(parameters {
               append("client_id",CLIENTID)
               append("client_secret",SECRET)
               append("grant_type","client_credentials")
           }))
       }
       if (response.status.value!=200) throw Exception("error conecting twitch ${response.bodyAsText()}")

       token=response.body<Token>().token
   }

  suspend fun getTwitchUser(userName:String):TwitchUserDto?{
      val response=ktorClient.get("https://api.twitch.tv/helix/users?login=$userName"){
          headers {
              append(HttpHeaders.Authorization,"Bearer $token")
              append("Client-Id",CLIENTID)
          }
      }
      if (response.status.value!=200) return null
      return if (response.body<Data>().data.isEmpty()) null else response.body<Data>().data.first()
  }

  suspend fun getNumberFollwers(userId: String): Long {
      val response = ktorClient.get("https://api.twitch.tv/helix/channels/followers?broadcaster_id=$userId") {
          headers {
              append(HttpHeaders.Authorization, "Bearer $token")
              append("Client-Id", CLIENTID)
          }
      }
      if (response.status.value != 200) return 0
      return response.body<Followers>().total
  }

}

class Ranking(private val api:ParticipansApi){

  suspend fun getListTwitchUsers(): Flow<TwitchUser> = coroutineScope {
     return@coroutineScope async(Dispatchers.IO){
          val users= mutableListOf<TwitchUser>()
          for (par in participans){
              val user=api.getTwitchUser(par)
              if (user==null) users.add(TwitchUser(par, LocalDateTime.now(),0))
              if (user!=null){
                  val followers=api.getNumberFollwers(user.id)
                  users.add(user.toTwicthUser(followers))
              }

          }
         users.asFlow()
      }.await()
  }

  suspend fun rankOfFollowers(usersTwitch: List<TwitchUser>){
     usersTwitch.sortedByDescending{ it.followers }.run {
         println("Ranking for followers")
         this.forEach {
             if (it.followers==0L) println("The user ${it.userName} does not have a twitch account")
             else println("${it.userName}  followers: ${it.followers}")
         }
     }

  }

    suspend fun rankOfCreatedAt(usersTwitch: List<TwitchUser>){
        usersTwitch.sortedBy{ it.createdAt }.run {
            println("Ranking for Created At")
            this.forEach {
                if (it.followers==0L) println("The user ${it.userName} does not have a twitch account")
                else println("${it.userName}  createdAr: ${it.createdAt.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"))}")
            }
        }

    }

}


fun main(): Unit= runBlocking {
    val api = ParticipansApi()
    api.getJwtToken()
    val rank=Ranking(api)
    val usersTwitch=rank.getListTwitchUsers().toList()
    rank.rankOfFollowers(usersTwitch)
    rank.rankOfCreatedAt(usersTwitch)

}
