// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <vector>
#include <string>
#include <curl/curl.h>
#include <json/json.h>  // Incluye la biblioteca JSONcpp (debe estar instalada)

// Función callback para manejar la respuesta HTTP y almacenarla en una cadena
size_t WriteCallback(void* contents, size_t size, size_t nmemb, std::string* s) {
    s->append((char*)contents, size * nmemb);
    return size * nmemb;
}

// Realiza la solicitud HTTP a la API de Twitch y devuelve la respuesta como cadena
std::string make_request(const std::string& url, const std::string& auth_token) {
    CURL* curl;
    CURLcode res;
    std::string response_string;

    curl = curl_easy_init();
    if (curl) {
        struct curl_slist* headers = NULL;
        headers = curl_slist_append(headers, ("Authorization: Bearer " + auth_token).c_str());
        headers = curl_slist_append(headers, "Client-ID: YOUR_CLIENT_ID");
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response_string);

        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
    }
    return response_string;
}

// Procesa la respuesta JSON para obtener el número de seguidores y la fecha de creación
void process_data(const std::vector<std::string>& participants, const std::string& auth_token) {
    Json::CharReaderBuilder readerBuilder;
    Json::Value root;
    std::string errs;
    
    for (const auto& user : participants) {
        std::string url = "https://api.twitch.tv/helix/users?login=" + user;
        std::string response = make_request(url, auth_token);

        // Parseamos la respuesta JSON
        std::stringstream ss(response);
        if (Json::parseFromStream(readerBuilder, ss, &root, &errs)) {
            const auto& data = root["data"];
            if (!data.empty()) {
                const std::string userId = data[0]["id"].asString();
                const std::string creationDate = data[0]["created_at"].asString();

                // Solicitar el número de seguidores para este usuario
                std::string followers_url = "https://api.twitch.tv/helix/users/follows?to_id=" + userId;
                std::string followers_response = make_request(followers_url, auth_token);
                
                Json::Value followers_root;
                std::stringstream ss_followers(followers_response);
                if (Json::parseFromStream(readerBuilder, ss_followers, &followers_root, &errs)) {
                    int total_followers = followers_root["total"].asInt();

                    // Imprime la información del usuario
                    std::cout << "Usuario: " << user << "\n";
                    std::cout << "Seguidores: " << total_followers << "\n";
                    std::cout << "Fecha de creación: " << creationDate << "\n\n";
                } else {
                    std::cerr << "Error al parsear la respuesta de seguidores de " << user << ": " << errs << "\n";
                }
            } else {
                std::cout << "El usuario " << user << " no existe en Twitch.\n\n";
            }
        } else {
            std::cerr << "Error al parsear la respuesta de Twitch para " << user << ": " << errs << "\n";
        }
    }
}

int main() {
    std::vector<std::string> participants = {"user1", "user2", "user3"};  // Lista de participantes
    std::string auth_token = "YOUR_AUTH_TOKEN";  // Debes usar un token válido

    process_data(participants, auth_token);

    return 0;
}

// Para cmpilar el programa en un sistema tipo UNIX usa la siguiente instruccion 
// g++ -std=c++11 -lcurl -ljsoncpp -o twitch_ranking twitch_ranking.cpp
