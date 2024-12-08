import io.ktor.client.HttpClient
import io.ktor.client.call.body
import io.ktor.client.request.get
import io.ktor.client.statement.HttpResponse
import io.ktor.client.statement.bodyAsText
import io.ktor.http.ContentType
import io.ktor.http.HttpStatusCode
import io.ktor.http.contentType

suspend fun main() {
    // Petición HTTP a una página web
    val client = HttpClient()
    val response: HttpResponse = client.get("https://www.example.com")
    
    if (response.status == HttpStatusCode.OK) {
        println("Petición exitosa, contenido de la web:")
        println(response.bodyAsText())
    } else {
        println("Error en la petición: ${response.status}")
    }

    // Consulta de información de un Pokémon a través de la PokéAPI
    println("\nConsulta de información de un Pokémon:")
    val pokemonName = "pikachu"
    val pokemonInfo = getPokemonInfo(pokemonName)
    
    println("Nombre: ${pokemonInfo.name}")
    println("ID: ${pokemonInfo.id}")
    println("Peso: ${pokemonInfo.weight}")
    println("Altura: ${pokemonInfo.height}")
    println("Tipos: ${pokemonInfo.types.map { it.type.name }.joinToString(", ")}")
    
    println("\nCadena de evolución:")
    pokemonInfo.evolutionChain.forEach { evolution ->
        println("- ${evolution.name}")
    }
    
    println("\nJuegos en los que aparece:")
    pokemonInfo.games.forEach { game ->
        println("- ${game.name}")
    }
}

suspend fun getPokemonInfo(name: String): PokemonInfo {
    val client = HttpClient()
    val response: HttpResponse = client.get("https://pokeapi.co/api/v2/pokemon/$name") {
        contentType(ContentType.Application.Json)
    }
    
    if (response.status == HttpStatusCode.OK) {
        return response.body()
    } else {
        throw Exception("Error al obtener información del Pokémon: ${response.status}")
    }
}

data class PokemonInfo(
    val name: String,
    val id: Int,
    val weight: Int,
    val height: Int,
    val types: List<PokemonType>,
    val evolutionChain: List<Evolution>,
    val games: List<Game>
)

data class PokemonType(
    val type: TypeInfo
)

data class TypeInfo(
    val name: String
)

data class Evolution(
    val name: String
)

data class Game(
    val name: String
)