import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;
import org.json.JSONArray;
import org.json.JSONObject;

/**
 * Este programa demuestra el uso de peticiones HTTP en Java y la integración
 * con la PokéAPI.
 * 
 * Teoría sobre peticiones HTTP:
 * - HTTP (Hypertext Transfer Protocol) es un protocolo de comunicación que
 * permite
 * la transferencia de información en la World Wide Web.
 * - Los métodos HTTP más comunes son:
 * * GET: Solicita datos de un recurso específico
 * * POST: Envía datos para crear un nuevo recurso
 * * PUT: Actualiza un recurso existente
 * * DELETE: Elimina un recurso
 * 
 * En Java, podemos realizar peticiones HTTP utilizando la clase
 * HttpURLConnection,
 * que nos permite establecer una conexión con un servidor web y enviar/recibir
 * datos.
 */
public class EulogioEP {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Ejemplo básico de petición HTTP
        System.out.println("=== Ejemplo básico de petición HTTP ===");
        try {
            String content = makeHttpRequest("https://www.example.com");
            System.out.println("Contenido de example.com:");
            System.out.println(content);
        } catch (Exception e) {
            System.out.println("Error al realizar la petición HTTP: " + e.getMessage());
        }

        // Funcionalidad de la PokéAPI
        while (true) {
            System.out.println("\n=== Búsqueda de Pokémon ===");
            System.out.println("Ingrese el nombre o número del Pokémon (o 'salir' para terminar):");
            String input = scanner.nextLine().toLowerCase();

            if (input.equals("salir")) {
                break;
            }

            try {
                // Realizar petición a la PokéAPI
                String pokemonData = makeHttpRequest("https://pokeapi.co/api/v2/pokemon/" + input);
                JSONObject pokemon = new JSONObject(pokemonData);

                // Mostrar información básica del Pokémon
                System.out.println("\nInformación del Pokémon:");
                System.out.println("Nombre: " + pokemon.getString("name"));
                System.out.println("ID: " + pokemon.getInt("id"));
                System.out.println("Peso: " + pokemon.getInt("weight") / 10.0 + " kg");
                System.out.println("Altura: " + pokemon.getInt("height") / 10.0 + " m");

                // Mostrar tipos
                System.out.println("Tipos:");
                JSONArray types = pokemon.getJSONArray("types");
                for (int i = 0; i < types.length(); i++) {
                    System.out.println("- " + types.getJSONObject(i).getJSONObject("type").getString("name"));
                }

                // Obtener y mostrar cadena de evolución
                String speciesUrl = pokemon.getJSONObject("species").getString("url");
                String speciesData = makeHttpRequest(speciesUrl);
                JSONObject species = new JSONObject(speciesData);
                String evolutionChainUrl = species.getJSONObject("evolution_chain").getString("url");
                String evolutionData = makeHttpRequest(evolutionChainUrl);
                JSONObject evolution = new JSONObject(evolutionData);

                System.out.println("\nCadena de evolución:");
                printEvolutionChain(evolution.getJSONObject("chain"));

                // Mostrar juegos
                System.out.println("\nJuegos en los que aparece:");
                JSONArray games = pokemon.getJSONArray("game_indices");
                for (int i = 0; i < games.length(); i++) {
                    System.out.println("- " + games.getJSONObject(i).getJSONObject("version").getString("name"));
                }

            } catch (Exception e) {
                System.out.println(
                        "Error: No se pudo encontrar el Pokémon. Asegúrese de escribir el nombre o número correctamente.");
            }
        }

        scanner.close();
    }

    /**
     * Realiza una petición HTTP GET a la URL especificada.
     * 
     * @param urlString La URL a la que se realizará la petición
     * @return El contenido de la respuesta como String
     * @throws Exception Si ocurre un error durante la petición
     */
    private static String makeHttpRequest(String urlString) throws Exception {
        URL url = new URL(urlString);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");

        if (conn.getResponseCode() != 200) {
            throw new RuntimeException("HTTP error code : " + conn.getResponseCode());
        }

        BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));
        StringBuilder response = new StringBuilder();
        String output;
        while ((output = br.readLine()) != null) {
            response.append(output);
        }
        conn.disconnect();

        return response.toString();
    }

    /**
     * Imprime recursivamente la cadena de evolución de un Pokémon.
     * 
     * @param chain El objeto JSON que contiene la información de la cadena de
     *              evolución
     */
    private static void printEvolutionChain(JSONObject chain) {
        String pokemonName = chain.getJSONObject("species").getString("name");
        System.out.println("- " + pokemonName);

        JSONArray evolvesTo = chain.getJSONArray("evolves_to");
        for (int i = 0; i < evolvesTo.length(); i++) {
            printEvolutionChain(evolvesTo.getJSONObject(i));
        }
    }
}