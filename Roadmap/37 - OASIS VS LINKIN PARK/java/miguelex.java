import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Base64;
import java.util.Scanner;
import org.json.JSONArray;
import org.json.JSONObject;

public class SpotifyComparison {

    private static final String CLIENT_ID = "YOUR_CLIENT_ID";
    private static final String CLIENT_SECRET = "YOUR_CLIENT_SECRET";

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Introduce el nombre del primer grupo: ");
        String band1 = scanner.nextLine();
        System.out.print("Introduce el nombre del segundo grupo: ");
        String band2 = scanner.nextLine();

        String token = getAccessToken();

        JSONObject band1Data = getArtistData(token, band1);
        JSONObject band2Data = getArtistData(token, band2);

        JSONObject band1Stats = getArtistStats(band1Data.getString("id"), token);
        JSONObject band2Stats = getArtistStats(band2Data.getString("id"), token);

        JSONObject band1TopTrack = getArtistTopTrack(band1Data.getString("id"), token);
        JSONObject band2TopTrack = getArtistTopTrack(band2Data.getString("id"), token);

        System.out.println("\n" + band1 + " Stats: " + band1Stats);
        System.out.println("Canción más popular de " + band1 + ": " + band1TopTrack);

        System.out.println("\n" + band2 + " Stats: " + band2Stats);
        System.out.println("Canción más popular de " + band2 + ": " + band2TopTrack);

        String moreFollowers = band1Stats.getInt("followers") > band2Stats.getInt("followers") ? band1 : band2;
        String morePopularTrack = band1TopTrack.getInt("playCount") > band2TopTrack.getInt("playCount") ? band1 : band2;

        System.out.println("\nLa banda con más seguidores es: " + moreFollowers);
        System.out.println("La banda con la canción más popular es: " + morePopularTrack);
    }

    private static String getAccessToken() throws Exception {
        String auth = CLIENT_ID + ":" + CLIENT_SECRET;
        String encodedAuth = Base64.getEncoder().encodeToString(auth.getBytes());

        URL url = new URL("https://accounts.spotify.com/api/token");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Authorization", "Basic " + encodedAuth);
        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        conn.setDoOutput(true);

        String data = "grant_type=client_credentials";
        conn.getOutputStream().write(data.getBytes());

        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        JSONObject json = new JSONObject(response.toString());
        return json.getString("access_token");
    }

    private static JSONObject getArtistData(String token, String artistName) throws Exception {
        URL url = new URL("https://api.spotify.com/v1/search?q=" + artistName + "&type=artist");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setRequestProperty("Authorization", "Bearer " + token);

        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        JSONObject json = new JSONObject(response.toString());
        JSONArray items = json.getJSONObject("artists").getJSONArray("items");
        return items.getJSONObject(0);
    }

    private static JSONObject getArtistStats(String artistId, String token) throws Exception {
        URL url = new URL("https://api.spotify.com/v1/artists/" + artistId);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setRequestProperty("Authorization", "Bearer " + token);

        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        return new JSONObject(response.toString());
    }

    private static JSONObject getArtistTopTrack(String artistId, String token) throws Exception {
        URL url = new URL("https://api.spotify.com/v1/artists/" + artistId + "/top-tracks?market=US");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setRequestProperty("Authorization", "Bearer " + token);

        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        JSONObject json = new JSONObject(response.toString());
        JSONArray tracks = json.getJSONArray("tracks");
        return tracks.getJSONObject(0);
    }
}
