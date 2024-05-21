import Foundation

// ESTE PROGRAMA PARA SU CORRECTRO FUNCIONAMIENTO SIN LOS METODOS sleep() SE TIENE QUE USAR EN UN PLAYGROUND.

var webUrlString = "https://www.swift.org"
guard let webUrl = URL(string: webUrlString) else {
    print("URL inválida")
    exit(1)
}

// Crear una solicitud URLRequest.
var webRequest = URLRequest(url: webUrl)
webRequest.httpMethod = "GET"

// Crear una sesión URLSession.
let session = URLSession.shared

// Crear una tarea de datos
let task = session.dataTask(with: webRequest) { (data, response, error) in
    // Verificar si hay algún error
    if let error = error {
        print("Error: \(error).")
        return
    }

    // Verificar si se recibió una respuesta HTTP.
    guard let httpResponse = response as? HTTPURLResponse else {
        print("Respuesta HTTP inválida.")
        return
    }

    // Verificar si la solicitud fue exitosa (código de estado 2xx).
    guard (200...299).contains(httpResponse.statusCode) else {
        print("Error en la solicitud. Código de estado: \(httpResponse.statusCode).")
        return
    }

    // Verificar si se recibieron datos.
    guard let responseData = data else {
        print("No se recibieron datos.")
        return
    }
    
    // Imprime el contenido html de la pagina.
    if let dataString = String(data: responseData, encoding: .utf8) {
        print(dataString)
    } else {
        print("No hay datos que mostrar.")
    }
}

// Empezar la tarea
task.resume()
sleep(1)




// DIFICULTAD EXTRA
print("\nDIFICULTAD EXTRA.\n")


// Pide por consola el nombre del pokemon para añadirlo al endpoint
print("Introduce el nombre del pokemon que quieras ver la info:")
guard let pokemonName = readLine() else {
    fatalError()
}


// Structuras para la info del pokemon
struct Pokemon: Codable {
    let gameIndices: [GameIndex]
    let height: Int
    let id: Int
    let name: String
    let types: [PokemonType]
    let weight: Int
    
    private enum CodingKeys: String, CodingKey {
        case gameIndices = "game_indices"
        case height, id, name, types, weight
    }
}

struct GameIndex: Codable {
    let gameIndex: Int
    let version: Version
    
    private enum CodingKeys: String, CodingKey {
        case gameIndex = "game_index"
        case version
    }
}

struct Version: Codable {
    let name: String
    let url: String
}

struct PokemonType: Codable {
    let slot: Int
    let type: Type
    
    private enum CodingKeys: String, CodingKey {
        case slot, type
    }
}

struct Type: Codable {
    let name: String
    let url: String
}


// Solicitud para la info del pokemon
var apiUrlString = "https://pokeapi.co/api/v2/pokemon/\(pokemonName)"
guard var apiUrl = URL(string: apiUrlString) else {
    print("URL inválida")
    exit(1)
}

// Crear una solicitud URLRequest.
var apiRequest = URLRequest(url: apiUrl)
apiRequest.httpMethod = "GET"

// Crear una sesión URLSession.
let apiSession = URLSession.shared

// Crear una tarea de datos
let apiTask = apiSession.dataTask(with: apiRequest) { (data, response, error) in
    // Verificar si hay algún error
    if let error = error {
        print("Error: \(error).")
        return
    }
    
    // Verificar si se recibió una respuesta HTTP.
    guard let httpResponse = response as? HTTPURLResponse else {
        print("Respuesta HTTP inválida.")
        return
    }
    
    // Verificar si la solicitud fue exitosa (código de estado 2xx).
    guard (200...299).contains(httpResponse.statusCode) else {
        print("Error en la solicitud. Código de estado: \(httpResponse.statusCode).")
        return
    }
    
    // Verificar si se recibieron datos.
    guard let responseData = data else {
        print("No se recibieron datos.")
        return
    }
    
    let decoder = JSONDecoder()
    
    do {
        let pokemon = try decoder.decode(Pokemon.self, from: responseData)
        print("Nombre: \(pokemon.name)")
        print("ID: \(pokemon.id)")
        print("Peso: \(pokemon.weight)")
        print("Altura: \(pokemon.height)")
        
        print("Typos: ")
        for type in pokemon.types {
            print("\t\(type.type.name)")
        }
        
        print("Juegos: ")
        for game in pokemon.gameIndices {
            print("\t\(game.version.name)")
        }
    } catch {
        print(error)
    }
}

// Empezar la tarea
apiTask.resume()
sleep(1)
