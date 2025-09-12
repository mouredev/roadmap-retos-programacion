/* ╔══════════════════════════════════════╗
   ║ Autor:  Amador Q                     ║
   ║ Web  : https://amsoft.dev            ║
   ║ 2024                                 ║
   ╚══════════════════════════════════════╝
*/


/*
<dependency>
	<groupId>com.google.code.gson</groupId>
	<artifactId>gson</artifactId>
	<version>2.10.1</version>
</dependency>
*/

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import javax.net.ssl.HttpsURLConnection;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Roadmap {

    public static void main(String[] args) {
        //EJERCICIO
        try {
            getWeb("https://amsoft.dev");
        }catch (IOException e){
            System.out.println(e.getMessage());
        }
        //EXTRA
        Scanner sc = new Scanner(System.in);
        System.out.println("====CONSULTA DE POKEMON====");
        System.out.print("Ingresa el id o nombre del pokemon :");
        String idPokemon = sc.nextLine();
        try {
            getPokemon(idPokemon);
        } catch (Exception e) {
            System.out.println(e.getMessage());;
        }
        sc.close();
    }

    public static void getWeb(String web) throws IOException {
        URL url = new URL(web);
        HttpsURLConnection con = (HttpsURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        int status = con.getResponseCode();
        if (status == 200) {
            try (BufferedReader in = new BufferedReader(
                    new InputStreamReader(con.getInputStream()))) {
                String inputLine;
                StringBuffer content = new StringBuffer();
                while ((inputLine = in.readLine()) != null) {
                    content.append(inputLine);
                }
                System.out.println("====CONTENIDO DE LA WEB=====");
                System.out.println(content);
            }
        }
        con.disconnect();
    }

    public static void getPokemon(String idPokemon) throws Exception {
        String urlPoke = String.format("https://pokeapi.co/api/v2/pokemon/%s", idPokemon);
        URL url = new URL(urlPoke);
        HttpsURLConnection con = (HttpsURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        Gson gson = new Gson();
        try (BufferedReader in = new BufferedReader(
                new InputStreamReader(con.getInputStream()))) {
            String inputLine;
            StringBuilder content = new StringBuilder();
            while ((inputLine = in.readLine()) != null) {
                content.append(inputLine);
            }
            JsonObject data = gson.fromJson(content.toString(), JsonObject.class);

            String id = data.get("id").getAsString();
            String name = data.get("name").getAsString();
            String weight = data.get("weight").getAsString();
            String height = data.get("height").getAsString();

            var types = data.getAsJsonArray("types");
            var games = data.getAsJsonArray("game_indices");
            System.out.println("Datos del pokemon");

            System.out.println("id :" + id);
            System.out.println("name :" + name);
            System.out.println("weight :" + weight);
            System.out.println("height :" + height);
            System.out.print("Tipos : ");
            List<String> typesPrint = new ArrayList<>();
            types.forEach(
                    p -> typesPrint.add(p.getAsJsonObject().get("type").getAsJsonObject().get("name").getAsString())
            );
            System.out.println(typesPrint);
            System.out.print("Juegos : ");
            List<String> gamesPrint = new ArrayList<>();
            games.forEach(
                    g -> gamesPrint.add(g.getAsJsonObject().get("version").getAsJsonObject().get("name").getAsString())
            );
            System.out.println(gamesPrint);

            String evolutions = getEvolutionChains(idPokemon);
            System.out.print("Evoluciones : ");
            System.out.println(evolutions);


        }

    }



    public static String getEvolutionChains(String idPokemon) throws Exception {
        String urlEvolutionChain = getUrlEvolutionChain(idPokemon);
        URL url = new URL(urlEvolutionChain);
        HttpsURLConnection con = (HttpsURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        int status = con.getResponseCode();
        if(status==200){
            Gson gson = new Gson();
            BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String input = br.readLine();
            JsonObject data = gson.fromJson(input, JsonObject.class);
            var chain = data.getAsJsonObject("chain");
            StringBuilder evolutionNames = new StringBuilder();
            String chainName = chain.getAsJsonObject("species").get("name").getAsString();
            evolutionNames.append(chainName);
            return chainFormat(chain,evolutionNames).toString();
        }else {
            throw new Exception("Respuesta diferente de OK");
        }
    }

    public static String getUrlEvolutionChain(String idPokemon) throws IOException, Exception{
        String urlSpecies = String.format("https://pokeapi.co/api/v2/pokemon-species/%s",idPokemon);
        URL url = new URL(urlSpecies);
        HttpsURLConnection con = (HttpsURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        int status = con.getResponseCode();
        if (status==200){
            Gson gson = new Gson();
            BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream()));
            String input = br.readLine();
            JsonObject data = gson.fromJson(input, JsonObject.class);
            String evolutionChainUrl = data.getAsJsonObject("evolution_chain").get("url").getAsString();
            br.close();
            return  evolutionChainUrl;
        }else {
            throw new Exception("Respuesta diferente de OK");
        }
    }

    public static StringBuilder chainFormat(JsonObject chain, StringBuilder evolutionNames) {
        evolutionNames.append("-> ");
        JsonArray evolvesToArray = chain.get("evolves_to").getAsJsonArray();
        for (int i = 0; i < evolvesToArray.size(); i++) {
            JsonObject evolution = evolvesToArray.get(i).getAsJsonObject();
            evolutionNames.append(evolution.get("species").getAsJsonObject().get("name").getAsString());

            if (i < evolvesToArray.size() - 1) {
                evolutionNames.append(", ");
            }

            if (!evolution.get("evolves_to").getAsJsonArray().isEmpty()) {
                chainFormat(evolution, evolutionNames);
            }
        }
        return evolutionNames;
    }

}
