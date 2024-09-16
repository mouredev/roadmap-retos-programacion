import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.entity.StringEntity;
import org.apache.http.util.EntityUtils;
import org.apache.http.impl.client.HttpClientBuilder;
import org.json.JSONObject;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
public class MohamedElderkaoui {

 private static final String CLIENT_ID = System.getenv("SPOTIFY_CLIENT_ID");
private static final String CLIENT_SECRET = System.getenv("SPOTIFY_CLIENT_SECRET");
    private static final String TOKEN_URL = "https://accounts.spotify.com/api/token";
    private static final String ARTIST_OASIS_ID = "2DaxqgrOhkeH0fpeiQq2f4"; // ID de Spotify para Oasis
    private static final String ARTIST_LP_ID = "6XyY86QOPPrYVGvF9ch6wz"; // ID de Spotify para Linkin Park
    
    public static void main(String[] args) throws IOException {
        String accessToken = getSpotifyAccessToken();
        
        JSONObject oasisData = getArtistData(accessToken, ARTIST_OASIS_ID);
        JSONObject lpData = getArtistData(accessToken, ARTIST_LP_ID);
        
        compareBands(oasisData, lpData);
    }
    
    private static String getSpotifyAccessToken() throws IOException {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpPost post = new HttpPost(TOKEN_URL);

        String auth = CLIENT_ID + ":" + CLIENT_SECRET;
        String encodedAuth = Base64.getEncoder().encodeToString(auth.getBytes(StandardCharsets.UTF_8));

        post.setHeader("Authorization", "Basic " + encodedAuth);
        post.setHeader("Content-Type", "application/x-www-form-urlencoded");
        post.setEntity(new StringEntity("grant_type=client_credentials"));

        CloseableHttpResponse response = httpClient.execute(post);
        String jsonResponse = EntityUtils.toString(response.getEntity());
        JSONObject jsonObject = new JSONObject(jsonResponse);

        return jsonObject.getString("access_token");
    }

    private static JSONObject getArtistData(String accessToken, String artistId) throws IOException {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        String url = "https://api.spotify.com/v1/artists/" + artistId;

        HttpGet get = new HttpGet(url);
        get.setHeader("Authorization", "Bearer " + accessToken);

        CloseableHttpResponse response = httpClient.execute(get);
        String jsonResponse = EntityUtils.toString(response.getEntity());
        return new JSONObject(jsonResponse);
    }

    private static void compareBands(JSONObject oasisData, JSONObject lpData) {
        System.out.println("Comparación entre Oasis y Linkin Park:");

        int oasisFollowers = oasisData.getJSONObject("followers").getInt("total");
        int lpFollowers = lpData.getJSONObject("followers").getInt("total");

        int oasisPopularity = oasisData.getInt("popularity");
        int lpPopularity = lpData.getInt("popularity");

        System.out.println("Oasis - Seguidores: " + oasisFollowers);
        System.out.println("Linkin Park - Seguidores: " + lpFollowers);

        System.out.println("Oasis - Popularidad: " + oasisPopularity);
        System.out.println("Linkin Park - Popularidad: " + lpPopularity);

        if (oasisFollowers > lpFollowers) {
            System.out.println("Oasis tiene más seguidores que Linkin Park.");
        } else {
            System.out.println("Linkin Park tiene más seguidores que Oasis.");
        }

        if (oasisPopularity > lpPopularity) {
            System.out.println("Oasis es más popular según la popularidad en Spotify.");
        } else {
            System.out.println("Linkin Park es más popular según la popularidad en Spotify.");
        }
    }
}