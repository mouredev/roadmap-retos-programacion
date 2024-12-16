import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().mostPopularBand();
    }

    final private String CLIENT_ID = "3e3909179f7041ebbf1d487900a18465";
    final private String CLIENT_SECRET = "5f1cbde87539487ea47baccc13aca4db";
    private String accessToken;

    public void mostPopularBand() {
        accessToken = getAccessToken();
        String idArtist1 = getArtistID("Oasis");
        String idArtist2 = getArtistID("Linkin Park");

        Map<String, String> artist1Data = getArtistData(idArtist1);
        Map<String, String> artist2Data = getArtistData(idArtist2);

        if (artist1Data == null || artist2Data == null){
            return;
        }

        String artist1Name = artist1Data.get("name");
        String artist2Name = artist2Data.get("name");
        Integer artist1Popularity = Integer.valueOf(artist1Data.get("popularity"));
        Integer artist2Popularity = Integer.valueOf(artist2Data.get("popularity"));

        System.out.println("Comparativa: " + artist1Data.get("name") + " vs " + artist2Data.get("name"));

        System.out.println("\nSeguidores");
        System.out.println(artist1Name + ": " + String.format("%,d", Long.valueOf(artist1Data.get("followers"))));
        System.out.println(artist2Name + ": " + String.format("%,d", Long.valueOf(artist2Data.get("followers"))));

        System.out.println("\nPopularidad (cuanto mas alto, mas popular)");
        System.out.println(artist1Name + ": " + artist1Popularity);
        System.out.println(artist2Name + ": " + artist2Popularity);

        System.out.println("\nCanción mas popular");
        System.out.println(artist1Data.get("most_popular_track_name") + " (" + artist1Name + "): "
                + artist1Data.get("most_popular_track_popularity") + " de popularidad");
        System.out.println(artist2Data.get("most_popular_track_name") + " (" + artist2Name + "): "
                + artist2Data.get("most_popular_track_popularity") + " de popularidad");

        System.out.println();
        if (artist1Popularity > artist2Popularity){
            System.out.println(artist1Name + " es mas popular que " + artist2Name);
        } else if (artist2Popularity > artist1Popularity) {
            System.out.println(artist2Name + " es mas popular que " + artist1Name);
        } else
            System.out.println(artist1Name + " y " + artist2Name + " son igual de populares");

    }

    private String getAccessToken() {
        String url = "https://accounts.spotify.com/api/token";
        String clientCredentials = CLIENT_ID + ":" + CLIENT_SECRET;
        String encodedCredentials = Base64.getEncoder().encodeToString(clientCredentials.getBytes(StandardCharsets.UTF_8));

        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder(URI.create(url))
                .header("Authorization", "Basic " + encodedCredentials)
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString("grant_type=client_credentials"))
                .build();

        String accessToken;
        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            if (response.statusCode() != 200) {
                System.out.println("Error al intentar obtener el token de autentificación");
                System.out.println("Respuesta: " + response.body());
                return null;
            }

            JsonObject data = JsonParser.parseString(response.body()).getAsJsonObject();
            accessToken = data.get("access_token").getAsString();
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

        return accessToken;
    }

    private String getArtistID(String artist) {
        String url = "https://api.spotify.com/v1/search?";
        url += "q=" + artist.replace(" ", "+");
        url += "&type=artist";
        url += "&limit=1";

        JsonObject data = getDataFromURL(url);
        String artistID = data.get("artists").getAsJsonObject()
                .get("items").getAsJsonArray()
                .get(0).getAsJsonObject()
                .get("id").getAsString();

        return artistID;
    }

    private Map<String, String> getArtistData(String artistID) {
        Map<String, String> artistData = new HashMap<>();

        String url = "https://api.spotify.com/v1/artists/";
        url += artistID;

        JsonObject data = getDataFromURL(url);
        if (data == null){
            System.out.println("Error al intentar obtener los datos del artista con ID: " + artistID);
            return null;
        }

        artistData.put("name", data.get("name").getAsString());
        artistData.put("popularity", data.get("popularity").getAsString());
        artistData.put("followers", data.get("followers").getAsJsonObject()
                .get("total").getAsString());

        JsonObject mostPopularTrackData = getMostPopularTrackFromArtist(artistID);
        if (mostPopularTrackData == null){
            System.out.println("Error al intentar obtener la canción mas popular del artista con ID: " + artistID);
            return null;
        }

        artistData.put("most_popular_track_name", mostPopularTrackData.get("name").getAsString());
        artistData.put("most_popular_track_popularity", mostPopularTrackData.get("popularity").getAsString());

        return artistData;
    }

    private JsonObject getMostPopularTrackFromArtist(String artistID){
        String url = "https://api.spotify.com/v1/artists/" + artistID + "/top-tracks";
        JsonObject topTracksData = getDataFromURL(url);
        if (topTracksData == null)
            return null;

        JsonObject mostPopularTrackData = null;
        Integer mostPopularTrackPopularity = 0;
        for (JsonElement trackData : topTracksData.get("tracks").getAsJsonArray()){
            String trackPopularity = trackData.getAsJsonObject()
                    .get("popularity").getAsString();
            if (mostPopularTrackData == null || Integer.valueOf(trackPopularity) > mostPopularTrackPopularity){
                mostPopularTrackData = trackData.getAsJsonObject();
                mostPopularTrackPopularity = Integer.valueOf(mostPopularTrackData.get("popularity").getAsString());
            }
        }

        return mostPopularTrackData;
    }

    private JsonObject getDataFromURL(String url){
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder(URI.create(url))
                .header("Authorization", "Bearer " + accessToken)
                .GET()
                .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            if (response.statusCode() != 200) {
                System.out.println("Ha ocurrido un error: " + response.statusCode());
                System.out.println("Url: " + url);
                System.out.println("Respuesta: " + response.body());
                return null;
            }

            return JsonParser.parseString(response.body()).getAsJsonObject();

        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
