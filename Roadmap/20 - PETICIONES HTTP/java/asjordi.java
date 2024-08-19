package dev.asjordi.r20;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws Exception {
        getRequest("https://www.google.com");
        getPokemon();
    }

    /**
     * EJERCICIO:
     * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
     * una petición a la web que tú quieras, verifica que dicha petición
     * fue exitosa y muestra por consola el contenido de la web.
     */
    public static void getRequest(String url) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() != 200) throw new Exception("Request failed with status code: " + response.statusCode());
        else System.out.println(response.body());
    }

    /**
     * DIFICULTAD EXTRA (opcional):
     * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
     * terminal al que le puedas solicitar información de un Pokémon concreto
     * utilizando su nombre o número.
     * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
     * - Muestra el nombre de su cadena de evoluciones
     * - Muestra los juegos en los que aparece
     * - Controla posibles errores
     */
    public static void getPokemon() {
        Scanner sc = new Scanner(System.in);
        Gson gson = new Gson();

        System.out.println("Introduce el nombre o número del Pokémon:");
        String param = sc.nextLine();

        String baseUrl = String.format("https://pokeapi.co/api/v2/pokemon/%s", param);
        var getBaseResponse = sendRequest(baseUrl);
        if (getBaseResponse.statusCode() != 200) System.out.println("Error: " + getBaseResponse.statusCode());
        String baseResponseBody = getBaseResponse.body();
        JsonObject data = gson.fromJson(baseResponseBody, JsonObject.class);

        String id = data.get("id").getAsString();
        String name = data.get("name").getAsString();
        String weight = data.get("weight").getAsString();
        String height = data.get("height").getAsString();

        String chainUrl = String.format("https://pokeapi.co/api/v2/evolution-chain/%s", id);
        var getChainResponse = sendRequest(chainUrl);
        if (getChainResponse.statusCode() != 200) System.out.println("Error: " + getChainResponse.statusCode());
        String chainResponseBody = getChainResponse.body();
        JsonObject chainData = gson.fromJson(chainResponseBody, JsonObject.class);

        var types = data.getAsJsonArray("types");
        StringBuilder typeNames = new StringBuilder();
        for (int i = 0; i < types.size(); i++) {
            JsonObject type = types.get(i).getAsJsonObject().getAsJsonObject("type");
            typeNames.append(type.get("name").getAsString());
            if (i < types.size() - 1) typeNames.append(", ");
        }

        var gameIndices = data.getAsJsonArray("game_indices");
        StringBuilder gameNames = new StringBuilder();
        for (int i = 0; i < gameIndices.size(); i++) {
            JsonObject game = gameIndices.get(i).getAsJsonObject().getAsJsonObject("version");
            gameNames.append(game.get("name").getAsString());
            if (i < gameIndices.size() - 1) gameNames.append(", ");
        }

        var chain = chainData.getAsJsonObject("chain");
        StringBuilder evolutionNames = new StringBuilder();
        getEvolutions(chain, evolutionNames);

        System.out.println("ID: " + id);
        System.out.println("Nombre: " + name);
        System.out.println("Peso: " + weight);
        System.out.println("Altura: " + height);
        System.out.println("Tipos: " + typeNames.toString());
        System.out.println("Las evoluciones de " + name + " son: " + evolutionNames.toString());
        System.out.println("Aparece en los juegos: " + gameNames.toString());
    }

    private static void getEvolutions(JsonObject chain, StringBuilder evolutionNames) {
        String chainName = chain.getAsJsonObject("species").get("name").getAsString();
        evolutionNames.append(chainName);

        var evolutions = chain.getAsJsonArray("evolves_to");
        for (int i = 0; i < evolutions.size(); i++) {
            evolutionNames.append(" -> ");
            getEvolutions(evolutions.get(i).getAsJsonObject(), evolutionNames);
        }
    }

    private static HttpResponse<String> sendRequest(String url) {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest getRequest = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .GET()
                .build();
        HttpResponse<String> getResponse = null;

        try {
            getResponse = client.send(getRequest, HttpResponse.BodyHandlers.ofString());
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        return getResponse;
    }
}
