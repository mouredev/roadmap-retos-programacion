import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpResponse.BodyHandlers;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Josegs95 {
    public static void main(String[] args) {
        //Ejercicio
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://www.google.es"))
                .GET()
                .build();
        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            //Si no salta excepción, la petición fue exitosa.
            if (response.statusCode() != 200)
                System.out.println("Ha habido algún problema con la conexión. Cod: " + response.statusCode());
            else{
                System.out.println("La conexión ha sido un éxito.");
                System.out.println(response.body());
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        //Reto
        retoFinal();
    }

    public static void retoFinal(){
        //Voy a escribirlo todo en un método para hacerlo más sencillo y porque ya existen librerías especializadas
        //en trabajar con la pokeapi.

        Scanner sc = new Scanner(System.in);
        System.out.print("Introduzca el nombre o el número del Pokémon: ");
        String pokemon = sc.nextLine().toLowerCase();

        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://pokeapi.co/api/v2/pokemon/" + pokemon))
                .build();
        try {
            HttpResponse<String> response = client.send(request, BodyHandlers.ofString());

            if(response.statusCode() != 200)
                System.out.println("Error " + response.statusCode() + ". Pokémon desconocido.");
            else{
                JsonObject pokemonData = JsonParser.parseString(response.body()).getAsJsonObject();

                //ID, nombre, peso, altura y tipos
                String id = pokemonData.get("id").getAsString();
                String name = pokemonData.get("name").getAsString();
                double weight = pokemonData.get("weight").getAsDouble() / 10.0;
                double height = pokemonData.get("height").getAsDouble() / 10.0;

                List<String> typeList = new ArrayList<>();
                for (JsonElement type : pokemonData.get("types").getAsJsonArray()) {
                    JsonObject aux = type.getAsJsonObject();
                    typeList.add(aux.get("type").getAsJsonObject().get("name").getAsString());
                }

                System.out.println("ID: " + id);
                System.out.println("Nombre: " + name);
                System.out.println("Peso: " + weight + " kg.");
                System.out.println("Altura: " + height + " m.");
                System.out.print("Tipos: ");
                for (String type : typeList)
                    System.out.print(type + " ");
                System.out.println();

                //Evoluciones
                request = HttpRequest.newBuilder(URI.create("https://pokeapi.co/api/v2/pokemon-species/" + id))
                        .build();
                response = client.send(request, BodyHandlers.ofString());

                if (response.statusCode() == 200){
                    JsonObject specieData = JsonParser.parseString(response.body()).getAsJsonObject();
                    String evoChainURL = specieData.get("evolution_chain").getAsJsonObject().get("url").getAsString();

                    request = HttpRequest.newBuilder(URI.create(evoChainURL))
                            .build();
                    response = client.send(request, BodyHandlers.ofString());

                    if (response.statusCode() == 200){
                        JsonObject evolutionData = JsonParser.parseString(response.body()).getAsJsonObject();
                        JsonElement auxElement = evolutionData.get("chain");
                        List<String> evolutionList = new ArrayList<>();
                        String basePokemonName = auxElement.getAsJsonObject()
                                .get("species").getAsJsonObject()
                                .get("name").getAsString();
                        evolutionList.add(basePokemonName);
                        for(JsonElement evolution : auxElement.getAsJsonObject().get("evolves_to").getAsJsonArray()){
                            String aux = evolution.getAsJsonObject().get("species").getAsJsonObject().get("name").getAsString();
                            evolutionList.add(aux);
                            for (JsonElement evolution2 : evolution.getAsJsonObject().get("evolves_to").getAsJsonArray()){
                                aux = evolution2.getAsJsonObject().get("species").getAsJsonObject().get("name").getAsString();
                                evolutionList.add(aux);
                            }
                        }
                        System.out.println("Línea evolutiva: " + evolutionList);
                        //Juegos
                        List<String> gameList = new ArrayList<>();
                        for (JsonElement game : pokemonData.get("game_indices").getAsJsonArray())
                            gameList.add(game.getAsJsonObject()
                                    .get("version").getAsJsonObject()
                                    .get("name").getAsString());
                        System.out.print("Juegos: ");
                        for (String gameName : gameList)
                            System.out.print("[Pokémon " + gameName + "] ");
                        System.out.println();
                    }
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

    }
}
