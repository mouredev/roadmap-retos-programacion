// Autor: Héctor Adán 
// Github: https://github.com/hectorio23

#include <iostream>
#include <curl/curl.h>
#include <json/json.h>  // Usamos la biblioteca JSON para manejar las respuestas JSON
#include <sstream>

// Callback function to handle the data returned by cURL
// Función de callback para manejar los datos devueltos por cURL
size_t WriteCallback(void* contents, size_t size, size_t nmemb, std::string* s) {
    s->append((char*)contents, size * nmemb);  // Añade los datos recibidos al buffer de la string
    return size * nmemb;  // Devuelve el tamaño de los datos procesados
}

// Function to fetch data from a given URL
// Función para obtener datos de una URL dada
std::string fetch_data(const std::string& url) {
    // Puntero para la instancia de cURL
    CURL* curl;  

    // Código de resultado de la operación cURL
    CURLcode res;  

    // Buffer para almacenar la respuesta
    std::string readBuffer;  

    // Inicializa cURL
    curl = curl_easy_init();  
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());  // Establece la URL objetivo
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);  // Define la función de callback
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);  // Define el buffer de destino para los datos
        res = curl_easy_perform(curl);  // Realiza la petición HTTP
        if(res != CURLE_OK) {
            // Manejo de errores en caso de fallo en la petición HTTP
            std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
        }
        // Limpia la instancia de cURL
        curl_easy_cleanup(curl);  
    }
    // Devuelve la respuesta 
    return readBuffer;  
}

// Function to print Pokémon details
// Función para imprimir los detalles de un Pokémon
void print_pokemon_details(const Json::Value& pokemon) {
    std::cout << "Name: " << pokemon["name"].asString() << std::endl;
    std::cout << "ID: " << pokemon["id"].asInt() << std::endl;
    std::cout << "Height: " << pokemon["height"].asInt() << std::endl;
    std::cout << "Weight: " << pokemon["weight"].asInt() << std::endl;

    std::cout << "Types: ";
    for (const auto& type : pokemon["types"]) {
        std::cout << type["type"]["name"].asString() << " ";
    }
    std::cout << std::endl;

    // Obtiene e imprime la cadena de evoluciones
    std::string evolution_url = pokemon["species"]["url"].asString();
    std::string species_data = fetch_data(evolution_url);
    Json::Value species_json;
    std::stringstream(species_data) >> species_json;
    std::string evolution_chain_url = species_json["evolution_chain"]["url"].asString();
    std::string evolution_data = fetch_data(evolution_chain_url);
    Json::Value evolution_json;
    std::stringstream(evolution_data) >> evolution_json;
    
    std::cout << "Evolution Chain: ";
    Json::Value current_evolution = evolution_json["chain"];
    while(!current_evolution.isNull()) {
        std::cout << current_evolution["species"]["name"].asString() << " ";
        current_evolution = current_evolution["evolves_to"][0];
    }
    std::cout << std::endl;

    // Imprime los juegos en los que aparece el Pokémon
    std::cout << "Games: ";
    for (const auto& game : pokemon["game_indices"]) {
        std::cout << game["version"]["name"].asString() << " ";
    }
    std::cout << std::endl;
}

int main() {
    // Primera parte: realizar una petición HTTP a un sitio web de ejemplo
    // Puntero para la instancia de cURL
    CURL* curl;  

    // Código de resultado de la operación cURL
    CURLcode res;  
    
    // Buffer para almacenar la respuesta
    std::string readBuffer;  

    // Inicializa cURL
    curl = curl_easy_init();  
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, "https://www.example.com");  // Establece la URL objetivo
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);  // Define la función de callback
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);  // Define el buffer de destino para los datos
        res = curl_easy_perform(curl);  // Realiza la petición HTTP
        if(res != CURLE_OK) {
            // Manejo de errores en caso de fallo en la petición HTTP
            std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
        } else {
            // Imprime la respuesta de la petición HTTP
            std::cout << readBuffer << std::endl;
        }
        curl_easy_cleanup(curl);  // Limpia la instancia de cURL
    }

    // Segunda parte: interacción con la PokéAPI
    std::string pokemon_name_or_id;  // Variable para almacenar el nombre o ID del Pokémon
    std::cout << "Enter the name or ID of the Pokémon: ";
    std::cin >> pokemon_name_or_id;

    std::string url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name_or_id;  // Construye la URL de la API
    std::string data = fetch_data(url);  // Obtiene los datos de la API

    Json::Value pokemon_json;  // Variable para almacenar los datos JSON del Pokémon
    std::stringstream(data) >> pokemon_json;  // Convierte la respuesta en un objeto JSON

    if(pokemon_json.isNull()) {
        // Manejo de errores en caso de que la respuesta JSON sea nula
        std::cerr << "Error fetching Pokémon data. Please check the name or ID and try again." << std::endl;
        return 1;  // Termina el programa con código de error
    }

    print_pokemon_details(pokemon_json);  // Imprime los detalles del Pokémon

    return 0;  // Termina el programa exitosamente
}

// Instrucción para compilar el código: g++ -o pokeapi hectorio23.cpp -lcurl -ljsoncpp
// Ejecucion: ./pokeapi
