import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Comparator;
import java.util.Map;

import static java.net.http.HttpClient.newHttpClient;

/**
 * #37 OASIS VS LINKIN PARK
 * <dependency>
 * <groupId>com.google.code.gson</groupId>
 * <artifactId>gson</artifactId>
 * <version>2.10.1</version>
 * </dependency>
 *
 * @author martinbohorquez
 */

public class SpotifyTest {
    private static final String CLIENT_ID = System.getenv("CLIENT_ID");
    private static final String CLIENT_SECRET = System.getenv("CLIENT_SECRET");
    private static final String TOKEN_URL = "https://accounts.spotify.com/api/token";

    public static void main(String[] args) throws Exception {
        int artistCounter1 = 0;
        int artistCounter2 = 0;

        // 1. Token
        String token = getToken();

        // 2. IDs
        String artistId1 = searchArtist(token, "Linkin Park");
        String artistId2 = searchArtist(token, "Green Day");

        // 3. Data
        Map<String, String> artistData1 = getArtistData(token, artistId1);
        Map<String, String> artistData2 = getArtistData(token, artistId2);
        System.out.println(artistData1);
        System.out.println(artistData2);
        // 3.1. Seguidores
        System.out.println("Banda con más seguidores:");
        if (Integer.parseInt(artistData1.get("followers")) > Integer.parseInt(artistData2.get("followers"))) {
            System.out.printf("%s es más popular en número de seguidores!%n", artistData1.get("name"));
            artistCounter1++;
        } else {
            System.out.printf("%s es más popular en número de seguidores!%n", artistData2.get("name"));
            artistCounter2++;
        }
        // 3.2. Popularidad
        System.out.println("Banda con más popularidad:");
        if (Integer.parseInt(artistData1.get("popularity")) > Integer.parseInt(artistData2.get("popularity"))) {
            System.out.printf("%s es más popular a nivel general!%n", artistData1.get("name"));
            artistCounter1++;
        } else {
            System.out.printf("%s es más popular a nivel general!%n", artistData2.get("name"));
            artistCounter2++;
        }

        // 4. Canción más popular
        Map<String, String> artistTopTrack1 = getArtistTopTrack(token, artistId1);
        Map<String, String> artistTopTrack2 = getArtistTopTrack(token, artistId2);
        System.out.printf("%s: %s%n", artistData1.get("name"), artistTopTrack1);
        System.out.printf("%s: %s%n", artistData2.get("name"), artistTopTrack2);

        System.out.println("Canción con más popularidad:");
        if (Integer.parseInt(artistTopTrack1.get("popularity")) > Integer.parseInt(artistTopTrack2.get("popularity"))) {
            System.out.printf("La canción %s de %s es más popular!%n", artistTopTrack1.get("name"), artistData1.get("name"));
            artistCounter1++;
        } else {
            System.out.printf("La canción %s de %s es más popular!%n", artistTopTrack2.get("name"), artistData2.get("name"));
            artistCounter2++;
        }

        // 5. Resultados
        System.out.println("Resultado final:");
        System.out.printf("%s es más popular!", artistCounter1 > artistCounter2 ? artistData1.get("name") : artistData2.get("name"));

    }

    private static String getToken() {
        String auth = CLIENT_ID + ":" + CLIENT_SECRET;
        String encodedAuth = Base64.getEncoder().encodeToString(auth.getBytes(StandardCharsets.UTF_8));
        JsonObject jsonObject = responseJsonPost(TOKEN_URL, encodedAuth);
        return jsonObject.get("access_token").getAsString();
    }

    private static String searchArtist(String token, String artist) throws Exception {
        String encodedArtist = URLEncoder.encode(artist, StandardCharsets.UTF_8);
        String url = "https://api.spotify.com/v1/search?q=" + encodedArtist + "&type=artist&limit=1";
        JsonObject responseJson = responseJsonGet(token, url);

        JsonArray artistsList = responseJson.getAsJsonObject("artists").getAsJsonArray("items");
        if (artistsList.isEmpty()) {
            throw new Exception("El artista" + artist + "no se ha encontrado!");
        }
        return artistsList.get(0).getAsJsonObject()
                .get("id").getAsString();
    }

    private static Map<String, String> getArtistData(String token, String id) {
        String url = "https://api.spotify.com/v1/artists/" + id;
        JsonObject responseJson = responseJsonGet(token, url);

        return Map.of("name", responseJson.get("name").getAsString(),
                "followers", responseJson.getAsJsonObject("followers").get("total").getAsString(),
                "popularity", responseJson.get("popularity").getAsString());
    }

    private static Map<String, String> getArtistTopTrack(String token, String id) {
        String url = "https://api.spotify.com/v1/artists/" + id + "/top-tracks";
        JsonObject responseJson = responseJsonGet(token, url);

        JsonObject topTrack = responseJson.getAsJsonArray("tracks").asList().stream()
                .max(Comparator.comparing(t -> t.getAsJsonObject().get("popularity").getAsInt()))
                .orElseThrow().getAsJsonObject();

        return Map.of("name", topTrack.get("name").getAsString(),
                "popularity", topTrack.get("popularity").getAsString());
    }

    private static JsonObject responseJsonGet(String token, String url) {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Authorization", "Bearer " + token) // Authorization header if needed
                .build();
        HttpResponse<String> response;

        try (HttpClient client = newHttpClient()) {
            response = client.send(request, HttpResponse.BodyHandlers.ofString());
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }

        String responseBody = response.body();
        return JsonParser.parseString(responseBody).getAsJsonObject();
    }

    private static JsonObject responseJsonPost(String url, String encodedAuth) {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Content-Type", "application/x-www-form-urlencoded") // Add headers
                .header("Authorization", "Basic " + encodedAuth) // Authorization header if needed
                .POST(HttpRequest.BodyPublishers.ofString("grant_type=client_credentials"))
                .build();
        HttpResponse<String> response;

        try (HttpClient client = newHttpClient()) {
            response = client.send(request, HttpResponse.BodyHandlers.ofString());
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
        String responseBody = response.body();

        return JsonParser.parseString(responseBody).getAsJsonObject();
    }
}
