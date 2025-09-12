import fuel.Fuel
import fuel.get
import kotlinx.coroutines.async
import kotlinx.coroutines.runBlocking
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json


/*
 Una peticion http  utiliza el protocolo Hypertext Transfer Protocol (HTTP). para comunicar
 datos atravez  de la red. esta peticion suele hacerse a un servidor o backend para obtener
 datos.

 una solicitud http se componene de los siguintes elementos:
  un metodo (GET, POST, PUT, DELETE, PATCH)
  una url (url de la peticion)
  un encabezado (cabeceras)
  version del protocolo (HTTP/1.1)

 Glosario basico de conceptos

 el metodo (GET, POST, PUT, DELETE, PATCH) es un verbo que se utiliza para
 saber la operacion que se va a realizar. por ejemplo:

 GET: obtiene informacion
 POST: permite enviar datos al servidor
 PUT:  nos permite enviar datos para actualizar
 DELETE: elimina datos

 el encabezado (cabeceras) es un conjunto de datos que se envia con la peticion
 estos pueden aportar informacion  adcional al servidor. por ejemplo:

  Accept: acepta informacion de la peticion ya sea JSON o XML o texto plano

Peticiones Http en kotlin

para poder hacer peticiones http en kotlin se pueden usar librarias como retrofit o okhttp o fuel
en este caso vamos utilizar fuel y kotlinx.serialization para trasformar los datos de la peticion
a una clase de kotlin y por utlimo como esta peticion puede durar un tiempo usaremos kotlinxcoroutines
para poder hacer las llamadas asincronas.

https://github.com/kittinunf/fuel
https://github.com/Kotlin/kotlinx.coroutines
https://kotlinlang.org/docs/serialization.html

*/

//1.- preparar clase kotlin para  deserializar la peticion
@Serializable
data class ChuckNorrisResponse(
   @SerialName("icon_url")
    val iconUrl:String,
    val id:String,
    val url:String,
    val value:String
)

// configuracion por si no necesitas todos los campos de json
private val json = Json { ignoreUnknownKeys = true }


fun exampleHttpRequest() = runBlocking{
    //2.- hacer la peticion
    val result= async {
        Fuel.get("https://api.chucknorris.io/jokes/random").body
    }
   //3.- esperar por la respuesta y convertirla a una clase de kotlin
    try {
        val response = result.await()
        val data = json.decodeFromString<ChuckNorrisResponse>(response)
        println("the joke is ${data.value}")
    }catch (e : Exception){
        println(e)
    }
}

/*Ejecicio extra */

@Serializable
data class Pokemon(
    val id: Int,
    val name: String,
    val types: List<PokemonType>,
    @SerialName("game_indices")
    val games: List<GameIndex>,
    val forms: List<PokeForms>,
    val height: Int,
    val weight: Int
)

@Serializable
data class PokeForms(
    val name: String,
    val url: String
)


// clases para los subtipos de games

@Serializable
data class GameIndex(
    @SerialName("game_index")
    val gameIndex: Int,
    val version: PokeVersion
)

@Serializable
data class PokeVersion(
    val name: String,
    val url: String
)

// clases para los subtipos de types de pokemon
@Serializable
data class PokemonType(
    val slot: Int,
    val type: PokeType
)
@Serializable
data class PokeType(
    val name: String,
    val url: String
)

// crear  clase para buscar pokemons

class Pokedex {
    private lateinit var pokemonSearch: String
    private var isSearchForID = false


    fun askForPokemon() {
        val regex = "[0-9]".toRegex()
        println("Enter a pokemon name or ID")
        this.pokemonSearch = readLine().toString()
        if (regex.matches(this.pokemonSearch)) {
            this.isSearchForID = true
        }
    }

    fun searchPokemon() {
        val params = if (this.isSearchForID) this.pokemonSearch.toInt() else this.pokemonSearch
        val url = "https://pokeapi.co/api/v2/pokemon/$params"
        runBlocking {
            val result = async {
                Fuel.get(url).body
            }

            try {
                val response = result.await()
                val pokemon= json.decodeFromString<Pokemon>(response)
                printPokemon(pokemon)

            } catch (e: Exception) {
                println(e)
            }

        }

    }

    private fun printPokemon(poke:Pokemon) {
       val info= """
         ID : ${poke.id}   
         Name : ${poke.name}
         Type : ${poke.types.map {it.type.name}}
         Game : ${poke.games.map {it.version.name}}
         Forms : ${poke.forms.map {it.name}}
         Height : ${poke.height}
         Weight : ${poke.weight}
            
        """.trimIndent()
        println(info)
    }

}




fun main() {
 //exampleHttpRequest()
 val poke=Pokedex()
 poke.askForPokemon()
 poke.searchPokemon()
}