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
import io.ktor.util.decodeBase64String
import kotlinx.coroutines.async
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.flow.asFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.transform
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json
import java.util.Base64
import java.util.Comparator


//1.-data para reponses y request
const val CLIENT_ID="YOUR_CLIENT_ID"
const val CLIENT_SECRET="YOUR_CLIENT_SECRET"

object Endpoints{
    const val TOKEND="https://accounts.spotify.com/api/token"
    val searhArtist={name: String->"https://api.spotify.com/v1/search?q=$name&type=artist&limit=1"}
    val getArtistOrTrack={id: String,isTrack: Boolean->
        if (isTrack) "https://api.spotify.com/v1/artists/$id/top-tracks"
        else "https://api.spotify.com/v1/artists/$id"
    }
}


val base64Credentials=Base64.getEncoder().encodeToString("$CLIENT_ID:$CLIENT_SECRET".toByteArray())

@Serializable
data class ResponseToken(
    @SerialName("access_token")
    val accessToken: String
)

//obtener el id del artista gracias ala configuracion de json puedo omitir campos que no necesito
@Serializable
data class Item(val id: String)

@Serializable
data class DataArtist( val items: List<Item>)


@Serializable
data class ResponseArtistID(
    val artists:DataArtist
)


@Serializable
data class Artist(val name: String,val followers: Follower, val popularity: Int){
    companion object{
        fun toArtistDto(artist: Artist,track: Track):ArtistDto{
            return ArtistDto(
                artist.name,
                artist.followers,
                artist.popularity,
                track
            )
        }
    }
}

@Serializable
data class Follower(val total: Long)


@Serializable
data class Track(val name: String,val popularity: Int)

@Serializable
data class Tracks(val tracks: List<Track>)

// creando una clase adicional para poder hacer mas optima la comparacion
data class ArtistDto(val name: String,val followers: Follower, val popularity: Int,val track: Track)



//2.-configurar cliente para  solicitudes http con ktor
//https://ktor.io/docs/client-create-new-application.html
val client= HttpClient(CIO){
    install(ContentNegotiation){
        json(Json{
            prettyPrint=true
            ignoreUnknownKeys=true
         })
    }
}




//3.-obtener token para poder acceder ala api

suspend fun getToken(): String{
   val response=client.post(Endpoints.TOKEND){
       headers {
           append(HttpHeaders.Authorization,"Basic $base64Credentials")
           append(HttpHeaders.ContentType,"application/x-www-form-urlencoded")
       }
       setBody(FormDataContent(parameters {
           append("grant_type","client_credentials")
       }))
   }
    if (response.status.value!=200) throw Exception("error conecting spotify ${response.bodyAsText()}")

    return response.body<ResponseToken>().accessToken
}


//4.-consultar informacion de artista
suspend fun getArtistID(token: String,name: String): String{
    val response=client.get(Endpoints.searhArtist(name)){
        headers {
            append(HttpHeaders.Authorization,"Bearer $token")
        }
    }
    if (response.status.value!=200) throw Exception("error to get Artist Id  for name $name")
    return response.body<ResponseArtistID>().artists.items[0].id
}


//5.-obtener informacion del artista
suspend fun getDataArtist(token: String,id: String):Artist{
    val response=client.get(Endpoints.getArtistOrTrack(id,false)){
        headers {
            append(HttpHeaders.Authorization,"Bearer $token")
        }
    }
    if (response.status.value!=200) throw Exception("error to get artist data ${response.bodyAsText()}")
    return response.body<Artist>()
}


//6.-optener la cancion mas popular
suspend fun getTopTrack(token: String,id: String):Track{
    val response=client.get(Endpoints.getArtistOrTrack(id,true)){
        headers {
            append(HttpHeaders.Authorization,"Bearer $token")
        }
    }
    if (response.status.value!=200) throw Exception("error to get artist data ${response.bodyAsText()}")
    val bestTrack=response.body<Tracks>().tracks.maxByOrNull { it.popularity }
    return bestTrack?:Track("",0)
}


suspend fun comparateArtist(artists: List<ArtistDto>){
    var counter1: Int=0
    var counter2: Int=0

    println("Comparate Artist")
    println("${artists.get(0).name} vs ${artists.get(1).name} ")

    //seguidores
    println("Comparate followers")
    val winnerfoll=artists.maxByOrNull { it.followers.total }
    if (winnerfoll!=null) {
        println("artist ${winnerfoll.name} is more popular in number of followers")
        if (artists.get(0).name==winnerfoll.name) counter1++
        else counter2++
    }
    else println("tie no artist is more followers than another ")


    //popularidad
    println("Comparate popularity")
    val winnerPop=artists.maxByOrNull { it.popularity }
    if (winnerPop!=null){
        println("artist ${winnerPop.name} is most popular artist")
        if (artists.get(0).name==winnerPop.name) counter1++
        else counter2++
    }
    else println(" no artist is more popular than another ")

    println("Comparate popularity song")
    val winnerTrack=artists.maxByOrNull { it.track.popularity }
    if (winnerTrack!=null){
        println("the song ${winnerTrack.track.name} is most popular")
        if (artists.get(0).name==winnerTrack.name) counter1++
        else counter2++
    }

    if (counter1>counter2){
        println("the ${artists.get(0).name} is most popular artist")
    }

    if (counter2>counter1){
        println("the ${artists.get(1).name} is most popular artist")
    }

    if (counter1==counter2){
        println("it´s like seeging the gods of Olympus")
    }

}




fun main()= runBlocking {
    //tokens
   val token= async{ getToken()}.await()
    //ids
   val artistIDOne= async{getArtistID(token,"JoseJose")}.await()
   val artistIDTwo= async{getArtistID(token,"JuanGabriel")}.await()
    // artist data
   val info1=async{getDataArtist(token,artistIDOne)}.await()
   val info2=async{getDataArtist(token,artistIDTwo)}.await()

   //best track
   val topTrack1=async{getTopTrack(token,artistIDOne)}.await()
   val topTrack2= async{getTopTrack(token,artistIDTwo)}.await()

   val  job= launch{
       val artistsDto=listOf<ArtistDto>(Artist.toArtistDto(info1,topTrack1),Artist.toArtistDto(info2,topTrack2))
       comparateArtist(artistsDto)
   }

   job.join()
}