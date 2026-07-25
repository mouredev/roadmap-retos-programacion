// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

#include <iostream>
#include <string>
#include <curl/curl.h>
#include <json/json.h>

// Función para manejar la respuesta de cURL
static size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

// Función para obtener el token de acceso
std::string getAccessToken(const std::string& client_id, const std::string& client_secret) {
    CURL* curl;
    CURLcode res;
    std::string readBuffer;

    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, "https://accounts.spotify.com/api/token");
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

        struct curl_slist* headers = nullptr;
        headers = curl_slist_append(headers, "Content-Type: application/x-www-form-urlencoded");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        std::string data = "grant_type=client_credentials&client_id=" + client_id + "&client_secret=" + client_secret;
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data.c_str());

        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
    }

    Json::Reader reader;
    Json::Value jsonData;
    reader.parse(readBuffer, jsonData);
    return jsonData["access_token"].asString();
}

// Función para obtener los datos de la banda
Json::Value getArtistData(const std::string& artist_name, const std::string& token) {
    CURL* curl;
    CURLcode res;
    std::string readBuffer;

    curl = curl_easy_init();
    if(curl) {
        std::string url = "https://api.spotify.com/v1/search?q=" + artist_name + "&type=artist&limit=1";
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

        struct curl_slist* headers = nullptr;
        std::string authHeader = "Authorization: Bearer " + token;
        headers = curl_slist_append(headers, authHeader.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
    }

    Json::Reader reader;
    Json::Value jsonData;
    reader.parse(readBuffer, jsonData);
    return jsonData["artists"]["items"][0];
}

// Comparación entre Oasis y Linkin Park
void compareBands() {
    std::string client_id = "your_client_id";
    std::string client_secret = "your_client_secret";
    std::string token = getAccessToken(client_id, client_secret);

    Json::Value oasis_data = getArtistData("Oasis", token);
    Json::Value linkin_park_data = getArtistData("Linkin Park", token);

    std::cout << "Oasis: " << oasis_data["followers"]["total"].asInt() << " seguidores" << std::endl;
    std::cout << "Linkin Park: " << linkin_park_data["followers"]["total"].asInt() << " seguidores" << std::endl;

    if (oasis_data["followers"]["total"].asInt() > linkin_park_data["followers"]["total"].asInt()) {
        std::cout << "Oasis es más popular en seguidores." << std::endl;
    } else {
        std::cout << "Linkin Park es más popular en seguidores." << std::endl;
    }
}

int main() {
    compareBands();
    return 0;
}
