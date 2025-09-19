import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;
import org.json.*;

public class AnaLauDB {
    // Realiza una petición HTTP GET y devuelve el contenido como String
    public static String httpGet(String urlStr) throws Exception {
        URL url = new URL(urlStr);
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        int status = con.getResponseCode();
        if (status != 200) {
            throw new Exception("Error en la petición. Código: " + status);
        }
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuilder content = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            content.append(inputLine);
        }
        in.close();
        con.disconnect();
        return content.toString();
    }

    public static void main(String[] args) {
        // Ejemplo simple: petición a una web
        try {
            String contenido = httpGet("https://pokeapi.co/api/v2/pokemon/ditto");
            System.out.println("Petición exitosa. Contenido de la web:");
            System.out.println(contenido.substring(0, Math.min(500, contenido.length())) + "...");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }

        // DIFICULTAD EXTRA: Consulta a la PokéAPI
        Scanner sc = new Scanner(System.in);
        System.out.print("\nIntroduce el nombre o número de un Pokémon: ");
        String poke = sc.nextLine().trim().toLowerCase();

        try {
            // 1. Datos básicos del Pokémon
            String pokeJson = httpGet("https://pokeapi.co/api/v2/pokemon/" + poke);
            JSONObject pokeObj = new JSONObject(pokeJson);

            String nombre = pokeObj.getString("name");
            int id = pokeObj.getInt("id");
            int peso = pokeObj.getInt("weight");
            int altura = pokeObj.getInt("height");

            // Tipos
            JSONArray tiposArr = pokeObj.getJSONArray("types");
            StringBuilder tipos = new StringBuilder();
            for (int i = 0; i < tiposArr.length(); i++) {
                tipos.append(tiposArr.getJSONObject(i).getJSONObject("type").getString("name"));
                if (i < tiposArr.length() - 1)
                    tipos.append(", ");
            }

            // Juegos
            JSONArray juegosArr = pokeObj.getJSONArray("game_indices");
            StringBuilder juegos = new StringBuilder();
            for (int i = 0; i < juegosArr.length(); i++) {
                String juego = juegosArr.getJSONObject(i).getJSONObject("version").getString("name");
                if (juegos.indexOf(juego) == -1) { // Evitar duplicados
                    juegos.append(juego);
                    if (i < juegosArr.length() - 1)
                        juegos.append(", ");
                }
            }

            // Cadena de evolución
            String especieUrl = pokeObj.getJSONObject("species").getString("url");
            String especieJson = httpGet(especieUrl);
            JSONObject especieObj = new JSONObject(especieJson);
            String evoUrl = especieObj.getJSONObject("evolution_chain").getString("url");
            String evoJson = httpGet(evoUrl);
            JSONObject evoObj = new JSONObject(evoJson);

            // Obtener nombres de la cadena de evolución
            StringBuilder cadenaEvo = new StringBuilder();
            JSONObject chain = evoObj.getJSONObject("chain");
            while (chain != null) {
                cadenaEvo.append(chain.getJSONObject("species").getString("name"));
                JSONArray evoluciones = chain.getJSONArray("evolves_to");
                if (evoluciones.length() > 0) {
                    cadenaEvo.append(" -> ");
                    chain = evoluciones.getJSONObject(0);
                } else {
                    break;
                }
            }

            // Mostrar resultados
            System.out.println("\n--- Información de Pokémon ---");
            System.out.println("Nombre: " + nombre);
            System.out.println("ID: " + id);
            System.out.println("Peso: " + peso);
            System.out.println("Altura: " + altura);
            System.out.println("Tipo(s): " + tipos);
            System.out.println("Cadena de evolución: " + cadenaEvo);
            System.out.println("Juegos: " + juegos);

        } catch (Exception e) {
            System.out.println("No se pudo obtener información del Pokémon. " + e.getMessage());
        }
        sc.close();
    }
}
