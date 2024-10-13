import com.google.gson.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

/**
 * #20 PETICIONES HTTP
 * <dependency>
 * <groupId>com.google.code.gson</groupId>
 * <artifactId>gson</artifactId>
 * <version>2.10.1</version>
 * </dependency>
 *
 * @author martinbohorquez
 */
public class martinbohorquez {
    public static void main(String[] args) throws IOException, URISyntaxException {
        getHttpResponse("https://www.moure.dev/");

        /*
         * DIFICULTAD EXTRA
         */
        System.out.print("Introduce un nombre o número de Pokémon a buscar: ");
        Scanner sc = new Scanner(System.in);
        String pokemon = sc.nextLine().toLowerCase();

        pokemonInfo(pokemon);
    }

    private static HttpURLConnection getResponse(String url) throws URISyntaxException, IOException {
        HttpURLConnection response = null;
        int responseCode;

        while (true) {
            URL obj = (new URI(url)).toURL();
            response = (HttpURLConnection) obj.openConnection();
            response.setRequestMethod("GET");
            response.setConnectTimeout(5000);
            response.setReadTimeout(5000);

            responseCode = response.getResponseCode();

            if (responseCode >= 300 && responseCode < 400)
                System.out.printf("Redirecting to: %s%n", url = response.getHeaderField("Location"));
            else break;
        }
        return response;
    }

    private static void getHttpResponse(String url) throws IOException, URISyntaxException {
        HttpURLConnection response = getResponse(url);
        int responseCode = response.getResponseCode();

        if (responseCode >= 200 && responseCode < 300)
            try (BufferedReader in = new BufferedReader(new InputStreamReader(response.getInputStream()))) {
                System.out.println(in.lines().collect(Collectors.joining()));
            }
        else System.out.printf("Error response código %d al realizar la petición", response.getResponseCode());
    }

    private static void pokemonInfo(String pokemon) throws URISyntaxException, IOException {
        HttpURLConnection response = getResponse("https://pokeapi.co/api/v2/pokemon/" + pokemon);
        int responseCode = response.getResponseCode();
        if (responseCode >= 200 && responseCode < 300) {
            try (BufferedReader in = new BufferedReader(new InputStreamReader(response.getInputStream()))) {
                String jsonString = in.lines().collect(Collectors.joining());
                Gson gson = new Gson();
                JsonObject jsonObject = gson.fromJson(jsonString, JsonObject.class);

                System.out.printf("Nombre: %s%n", jsonObject.get("name").getAsString());
                System.out.printf("ID: %s%n", jsonObject.get("id").getAsString());
                System.out.printf("Peso: %s%n", jsonObject.get("weight").getAsString());
                System.out.printf("Altura: %s%n", jsonObject.get("height").getAsString());

                List<String> types = StreamSupport.stream(jsonObject.getAsJsonArray("types").spliterator(), false)
                        .map(JsonElement::getAsJsonObject)
                        .map(typeObject -> typeObject.getAsJsonObject("type").get("name").getAsString())
                        .toList();
                System.out.printf("Tipo(s): %s%n", types);
                evolutionChain(pokemon);
                List<String> juegos = StreamSupport.stream(jsonObject.getAsJsonArray("game_indices").spliterator(), false)
                        .map(JsonElement::getAsJsonObject)
                        .map(typeObject -> typeObject.getAsJsonObject("version").get("name").getAsString())
                        .toList();
                System.out.printf("Juegos: %s%n", juegos);

            }
        } else System.out.printf("Error %d: Pokémon no encontrado!", response.getResponseCode());
    }

    private static void evolutionChain(String pokemon) throws URISyntaxException, IOException {
        HttpURLConnection response = getResponse("https://pokeapi.co/api/v2/pokemon-species/" + pokemon);
        int responseCode = response.getResponseCode();
        if (responseCode >= 200 && responseCode < 300) {
            try (BufferedReader in = new BufferedReader(new InputStreamReader(response.getInputStream()))) {
                String jsonString = in.lines().collect(Collectors.joining());
                Gson gson = new Gson();
                JsonObject jsonObject = gson.fromJson(jsonString, JsonObject.class);

                String url = jsonObject.get("evolution_chain").getAsJsonObject().get("url").getAsString();
                response = getResponse(url);
                responseCode = response.getResponseCode();
                if (responseCode >= 200 && responseCode < 300) {
                    try (BufferedReader inS = new BufferedReader(new InputStreamReader(response.getInputStream()))) {
                        jsonString = inS.lines().collect(Collectors.joining());
                        gson = new Gson();
                        jsonObject = gson.fromJson(jsonString, JsonObject.class);

                        StringBuilder evolutionChain = new StringBuilder();
                        JsonObject chainObject = jsonObject.getAsJsonObject("chain");

                        System.out.println("Cadena(s) de evolución:");
                        Map<Integer, String> evolutionMap = new LinkedHashMap<>();
                        getEvolveTo(evolutionMap, evolutionChain, chainObject).values().forEach(System.out::println);
                    }
                } else System.out.printf("Error %d: obteniendo evoluciones!", response.getResponseCode());
            }
        } else System.out.printf("Error %d: obteniendo evoluciones!", response.getResponseCode());
    }

    private static Map<Integer, String> getEvolveTo(Map<Integer, String> evolutionMap, StringBuilder evolutionChain, JsonObject chainObject) {
        Set<String> evolutionSet = new LinkedHashSet<>();
        JsonElement element = chainObject.getAsJsonObject("species").get("name");
        evolutionChain.append(element);

        JsonArray evolutions = chainObject.getAsJsonArray("evolves_to");
        for (int i = 0; i < evolutions.size(); i++) {
            if (i != 0) {
                int indexIni = evolutionChain.reverse().indexOf(" >- ");
                int length = evolutionChain.reverse().length();
                evolutionChain.delete(length - indexIni - 4, length);
                evolutionSet = new LinkedHashSet<>();
            }
            evolutionChain.append(" -> ");
            getEvolveTo(evolutionMap, evolutionChain, evolutions.get(i).getAsJsonObject());
            evolutionSet.add(evolutionChain.toString());
            if (!evolutionMap.containsValue(evolutionSet.toString())) evolutionMap.put(i, evolutionSet.toString());
        }
        return evolutionMap;
    }
}
