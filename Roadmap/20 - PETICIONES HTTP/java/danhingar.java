import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;

public class danhingar {

    public static void main(String[] args) throws IOException, InterruptedException {
        makeRequest();
        pokemonApi();
    }

    public static void makeRequest() {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://medium.com/"))
                .build();
        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            System.out.println(response.body());
        } catch (Exception e) {
            System.out.println("Error en la petición");
        }
    }

    // EXTRA
    private static void pokemonApi() {
        System.out.print("Introduce el nombre o número del pokemon: ");
        Scanner sc = new Scanner(System.in);
        String value = sc.nextLine();
        sc.close();
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://pokeapi.co/api/v2/pokemon/" + value+"/"))
                .build();


        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            String content = response.body();
            JsonObject convertedObject = new Gson().fromJson(content, JsonObject.class);

            String name = convertedObject.get("name").getAsString();
            String id =convertedObject.get("id").getAsString();
            String weight = convertedObject.get("weight").getAsString();
            String height = convertedObject.get("height").getAsString();
            JsonArray types=convertedObject.get("types").getAsJsonArray();
            List<String> typesName=types.asList().stream().map(i-> i.getAsJsonObject().get("type").getAsJsonObject().get("name").getAsString()).toList();
            System.out.printf("Name: %s, Id: %s, Weight: %s, Height: %s, Type: %s%n",name, id, weight,height, typesName);

            getEvolutions(id);

            JsonArray games=convertedObject.get("game_indices").getAsJsonArray();
            List<String> gamesName=games.asList().stream().map(i-> i.getAsJsonObject().get("version").getAsJsonObject().get("name").getAsString()).toList();
            System.out.printf("Games: %s%n",gamesName);


        } catch (Exception e) {
            System.out.println("Error en la petición");
        }

        System.exit(1);


    }

    private static void getEvolutions(String id) {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://pokeapi.co/api/v2/pokemon-species/" + id))
                .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            String content = response.body();
            JsonObject convertedObject = new Gson().fromJson(content, JsonObject.class);
            String url = convertedObject.get("evolution_chain").getAsJsonObject().get("url").getAsString();

            HttpRequest request2 = HttpRequest.newBuilder()
                    .uri(URI.create(url))
                    .build();
            HttpResponse<String> response2 = client.send(request2, HttpResponse.BodyHandlers.ofString());
            String content2 = response2.body();
            JsonObject convertedObject2 = new Gson().fromJson(content2, JsonObject.class);

            System.out.println("Cadena de evoluciones: "+getEvolution(convertedObject2.getAsJsonObject("chain"),new ArrayList<>()));

        } catch (Exception e) {
            System.out.println("Error al obtener las evoluciones");
        }
    }

    public static List<String> getEvolution(JsonObject json,List<String> evolutions){
        evolutions.add(json.get("species").getAsJsonObject().get("name").getAsString());
        if(!json.getAsJsonArray("evolves_to").isEmpty()){
            for(JsonElement element:json.getAsJsonArray("evolves_to")){
                getEvolution(element.getAsJsonObject(),evolutions);
            }
        }else{
            return evolutions;
        }
        return evolutions;
    }

}
