/*
   <dependencies>
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.10.1</version>
        </dependency>
    </dependencies>
*/

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public final static ArrayList<String> nameEvolves = new ArrayList<>();

    public static void getEvolve(JsonObject json){
        String nameEvolve = json.getAsJsonObject("species").get("name").getAsString();
        nameEvolves.add(nameEvolve);

        JsonArray evolves = json.getAsJsonArray("evolves_to");
        if(evolves.size() > 0){
            getEvolve(evolves.get(0).getAsJsonObject());
        }
    }

    public static void main(String[] args) {
        try {
            System.out.println("Primera petición HTTP");

            //Establecemos la conexón con la web
            URL url = new URL("https://holamundo.day/");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.connect();

            //Recuperamos el código de respuesta
            int code = connection.getResponseCode();
            System.out.println("Resultado: " + code);

            //Leo el contenido de la web y lo guardo en una variable
            Scanner scanner = new Scanner(connection.getInputStream());
            StringBuilder html = new StringBuilder("");
            while (scanner.hasNextLine()) {
                html.append(scanner.nextLine());
            }
            scanner.close();

            //Si la petición fue exitosa
            if (code == 200) {
                //Imprimo por consola el contenido de la web
                System.out.println("Contenido de la web: ");
                System.out.println(html);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        /*DIFICULTAD EXTRA*/
        try {
            System.out.println("Poke api: ");

            System.out.print("Introduce el nombre o id de un Pokemon: ");
            Scanner scanner = new Scanner(System.in);
            String nombre = scanner.nextLine();
            System.out.println();

            //Establecemos la conexón con la web
            URL url = new URL("https://pokeapi.co/api/v2/pokemon/" + nombre);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.connect();
            int code = connection.getResponseCode();

            //Leo el contenido y lo guardo en una variable
            scanner = new Scanner(connection.getInputStream());
            StringBuilder json = new StringBuilder("");
            while (scanner.hasNextLine()) {
                json.append(scanner.nextLine());
            }

            //Si la petición fue exitosa
            if (code == 200) {
                //Imprimo por consola el contenido
                Gson gson = new Gson();
                JsonObject data = gson.fromJson(json.toString(), JsonObject.class);

                String name = data.get("name").getAsString();
                int id = data.get("id").getAsInt();
                int weight = data.get("weight").getAsInt();
                int height = data.get("height").getAsInt();

                ArrayList<String> nameGames = new ArrayList<>();
                JsonArray games = data.getAsJsonArray("game_indices");
                for (int i = 0; i < games.size(); i++) {
                    JsonObject game = games.get(i).getAsJsonObject();
                    String nameGame = game.getAsJsonObject("version").get("name").getAsString();
                    nameGames.add(nameGame);
                }

                ArrayList<String> nameTypes = new ArrayList();
                JsonArray types = data.getAsJsonArray("types");
                for (JsonElement element : types) {
                    String nameType = element.getAsJsonObject().getAsJsonObject("type").get("name").getAsString();
                    nameTypes.add(nameType);
                }

                //Establecemos conexión para recuperar evoluciones
                url = new URL("https://pokeapi.co/api/v2/pokemon-species/"+id);
                connection = (HttpURLConnection) url.openConnection();
                connection.setRequestMethod("GET");
                connection.connect();
                code = connection.getResponseCode();

                //Leo el contenido y lo guardo en una variable
                scanner = new Scanner(connection.getInputStream());
                StringBuilder jsonSpecies = new StringBuilder("");
                while (scanner.hasNextLine()) {
                    jsonSpecies.append(scanner.nextLine());
                }

                //Si la petición fue exitosa
                if (code == 200) {
                    JsonObject dataSpecies = gson.fromJson(jsonSpecies.toString(), JsonObject.class);
                    url = new URL(dataSpecies.getAsJsonObject("evolution_chain").get("url").getAsString());
                    connection = (HttpURLConnection) url.openConnection();
                    connection.setRequestMethod("GET");
                    connection.connect();
                    code = connection.getResponseCode();

                    //Leo el contenido y lo guardo en una variable
                    scanner = new Scanner(connection.getInputStream());
                    StringBuilder jsonEvolves = new StringBuilder("");
                    while (scanner.hasNextLine()) {
                        jsonEvolves.append(scanner.nextLine());
                    }

                    //Si la petición fue exitosa
                    if (code == 200) {
                        JsonObject dataEvolves = gson.fromJson(jsonEvolves.toString(), JsonObject.class);
                        getEvolve(dataEvolves.getAsJsonObject("chain"));
                    }
                }

                //Mostramos todos los datos del pokemon
                System.out.println("Datos de la pokeApi: ");
                System.out.println("Name: " + name);
                System.out.println("Id: " + id);
                System.out.println("Weight: " + weight);
                System.out.println("Height: " + height);
                System.out.println("Types: " + nameTypes);
                System.out.println("Evolutions: " + nameEvolves);
                System.out.println("Games: " + nameGames);
            }

            //Cerramos los recursos
            scanner.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
