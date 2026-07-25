import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.net.HttpURLConnection;
import java.net.URL;

//Imports que no se pueden usar a no ser que se tengan en un archivo pom.xml
import javax.json.Json;
import javax.json.JsonArray;
import javax.json.JsonObject;
import javax.json.JsonReader;

/* Dependencias necesarias para que funcione el codigo
<dependency>
        <groupId>javax.json</groupId>
        <artifactId>javax.json-api</artifactId>
        <version>1.1.4</version>
    </dependency>
    <dependency>
        <groupId>org.glassfish</groupId>
        <artifactId>javax.json</artifactId>
        <version>1.1.4</version>
    </dependency>*/

public class simonguzman {
    public static void main(String[] args) throws IOException{
        makeHttpRequest("https://www.google.com/");
        getPokemonApi("bulbasaur");
    }

    public static void makeHttpRequest(String url) throws IOException{
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();
        
        con.setRequestMethod("GET");

        int responseCode = con.getResponseCode();
        if (responseCode == 200) {
            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();

            while ((inputLine = in.readLine()) != null) { 
                response.append(inputLine);
            }
            in.close();

            System.out.println(response.toString());
        }else{
            System.out.println("ERROR: "+responseCode);
        }
    }

    public static void getPokemonInfo(String pokemonName) throws IOException {
        String url = "https://pokeapi.co/api/v2/pokemon/" + pokemonName;
        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();

        con.setRequestMethod("GET");
        con.setRequestProperty("User-Agent", "MyPokemonApp");

        int responseCode = con.getResponseCode();
        if (responseCode == 200) {
            BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            JsonReader jsonReader = Json.createReader(new StringReader(response.toString()));
            JsonObject jsonObject = jsonReader.readObject();

            System.out.println("Nombre: " + jsonObject.getString("name"));
            System.out.println("ID: " + jsonObject.getInt("id"));
            System.out.println("Peso: " + jsonObject.getJsonNumber("weight").doubleValue());
            System.out.println("Altura: " + jsonObject.getJsonNumber("height").doubleValue());
            System.out.println("Tipos: " + jsonObject.getJsonArray("types"));

            JsonObject speciesObject = jsonObject.getJsonObject("species");
            String speciesUrl = speciesObject.getString("url");
            URL speciesObj = new URL(speciesUrl);
            HttpURLConnection speciesCon = (HttpURLConnection) speciesObj.openConnection();

            speciesCon.setRequestMethod("GET");
            speciesCon.setRequestProperty("User-Agent", "MyPokemonApp");

            int speciesResponseCode = speciesCon.getResponseCode();
            if (speciesResponseCode == 200) {
                BufferedReader speciesIn = new BufferedReader(new InputStreamReader(speciesCon.getInputStream()));
                String speciesInputLine;
                StringBuffer speciesResponse = new StringBuffer();

                while ((speciesInputLine = speciesIn.readLine()) != null) {
                    speciesResponse.append(speciesInputLine);
                }
                speciesIn.close();

                JsonReader speciesJsonReader = Json.createReader(new StringReader(speciesResponse.toString()));
                JsonObject speciesJsonObject = speciesJsonReader.readObject();

                String evolutionChainUrl = speciesJsonObject.getJsonObject("evolution_chain").getString("url");
                System.out.println("Cadena de evoluciones: " + evolutionChainUrl);
            } else {
                System.out.println("Error: " + speciesResponseCode);
            }

            JsonArray games = jsonObject.getJsonArray("game_indices");
            System.out.println("Juegos: ");
            for (int i = 0; i < games.size(); i++) {
                JsonObject gameIndexObject = games.getJsonObject(i);
                JsonObject versionObject = gameIndexObject.getJsonObject("version");
                System.out.println("  - " + versionObject.getString("name"));
            }
        } else {
            System.out.println("Error: " + responseCode);
        }
    }
}
