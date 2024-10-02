import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class MohamedElderkaoui {

    private static final String CLIENT_ID = System.getenv("TWITCH_CLIENT_ID"); // Reemplaza con tu Client ID
    private static final String CLIENT_SECRET = System.getenv("TWITCH_CLIENT_SECRET");  // Reemplaza con tu Client Secret
    private static final String TOKEN_URL = "https://id.twitch.tv/oauth2/token";
    private static final String TWITCH_API_URL = "https://api.twitch.tv/helix/users";
    private static String accessToken = "";

    public static void main(String[] args) throws IOException, InterruptedException {
        // Lista de participantes
        List<String> participants = Arrays.asList(
                "ABBY", "ACHE", "ADRI CONTRERAS", "AGUSTIN", "ALEXBY", "AMPETER", "ANDER", "ARI GAMEPLAYS",
                "ARIGELI", "AURONPLAY", "AXOZER", "BENIJU", "BY CALITOS", "BYVIRUZZ", "CARRERA", "CELOPAN",
                "CHEETO", "CRYSTALMOLLY", "DARIO EMEHACHE", "DHEYLO", "DJMARIO", "DOBLE", "ELVISA", "ELYAS360",
                "FOLAGOR", "GREFG", "GUANYAR", "HIKA", "HIPER", "IBAI", "IBELKY", "ILLOJUAN", "IMANTADO",
                "IRINA ISSAIA", "JESSKIU", "JOPA", "JORDIWILD", "KENAI SOUZA", "KERORO", "KIDD KEO", "KIKO RIVERA",
                "KNEKRO", "KOKO", "KRONNOZOMBER", "LEVIATHAN", "LIT KILLAH", "LOLA LOLITA", "LOLITO", "LUH", "LUZU",
                "MANGEL", "MAYICHI", "MELO", "MISSASINOFIA", "MIXWELL", "MR.JAGGER", "NATE GENTILE", "NEXXUZ", 
                "NIA", "NIL OJEDA", "NISSAXTER", "OLLIE", "ORSLOK", "OUTCONSUMER", "PAPI GAVI", "PARCETAMOR", 
                "PATICA", "PAULA GONU", "PAUSENPAII", "PERXITAA", "PLEX", "POLISPOL", "QUACKITY", "RECUERDOP", 
                "REVEN", "RIVERS", "ROBERTPG", "ROIER", "ROJUU", "RUBIUS", "SHADOUNE", "SILITHUR", "SPOKSPONHA", 
                "SPREEN", "SPURSITO", "STAXX", "SUZYROXX", "VICENS", "VITUBER", "WERLYB", "XAVI", "XCRY", "XOKAS", 
                "ZARCORT", "ZELING", "ZORMAN"
        );

        // Obtener el token de acceso
        obtainAccessToken();

        List<TwitchUser> users = new ArrayList<>();

        for (String username : participants) {
            TwitchUser user = fetchTwitchUserInfo(username);
            if (user != null) {
                users.add(user);
            } else {
                System.out.println("El usuario " + username + " no tiene cuenta en Twitch.");
            }
        }

        // Ordenar por número de seguidores
        users.sort(Comparator.comparingInt(TwitchUser::getFollowers).reversed());
        System.out.println("Ranking por número de seguidores:");
        users.forEach(System.out::println);

        // Ordenar por antigüedad (fecha de creación)
        users.sort(Comparator.comparing(TwitchUser::getCreatedAt));
        System.out.println("\nRanking por antigüedad:");
        users.forEach(System.out::println);
    }

    // Obtener el token de acceso para la API de Twitch
    private static void obtainAccessToken() throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(TOKEN_URL + "?client_id=" + CLIENT_ID + "&client_secret=" + CLIENT_SECRET + "&grant_type=client_credentials"))
                .POST(HttpRequest.BodyPublishers.noBody())
                .header("Content-Type", "application/x-www-form-urlencoded")
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        ObjectMapper mapper = new ObjectMapper();
        JsonNode jsonResponse = mapper.readTree(response.body());
        accessToken = jsonResponse.get("access_token").asText();
    }

    // Obtener información del usuario de Twitch
    private static TwitchUser fetchTwitchUserInfo(String username) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(TWITCH_API_URL + "?login=" + username))
                .header("Authorization", "Bearer " + accessToken)
                .header("Client-Id", CLIENT_ID)
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() == 200) {
            ObjectMapper mapper = new ObjectMapper();
            JsonNode jsonResponse = mapper.readTree(response.body());
            JsonNode userData = jsonResponse.get("data").get(0);

            if (userData != null) {
                String displayName = userData.get("display_name").asText();
                int followers = fetchFollowersCount(userData.get("id").asText());
                String createdAt = userData.get("created_at").asText();

                return new TwitchUser(displayName, followers, createdAt);
            }
        }
        return null; // Usuario no encontrado
    }

    // Obtener número de seguidores del usuario
    private static int fetchFollowersCount(String userId) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(TWITCH_API_URL + "/follows?to_id=" + userId))
                .header("Authorization", "Bearer " + accessToken)
                .header("Client-Id", CLIENT_ID)
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() == 200) {
            ObjectMapper mapper = new ObjectMapper();
            JsonNode jsonResponse = mapper.readTree(response.body());
            return jsonResponse.get("total").asInt();
        }
        return 0;
    }
}

// Clase que representa a un usuario de Twitch
class TwitchUser {
    private String username;
    private int followers;
    private String createdAt;

    public TwitchUser(String username, int followers, String createdAt) {
        this.username = username;
        this.followers = followers;
        this.createdAt = createdAt;
    }

    public String getUsername() {
        return username;
    }

    public int getFollowers() {
        return followers;
    }

    public String getCreatedAt() {
        return createdAt;
    }

    @Override
    public String toString() {
        return "Usuario: " + username + ", Seguidores: " + followers + ", Fecha de creación: " + createdAt;
    }
}
