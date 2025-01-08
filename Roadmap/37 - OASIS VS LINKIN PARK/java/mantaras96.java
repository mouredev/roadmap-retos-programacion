package org.example;

import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.utils.URIBuilder;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.apache.http.entity.StringEntity;
import org.json.JSONObject;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class Main {

    private static final String CLIENT_ID = "";
    private static final String CLIENT_SECRET = "";
    private static final String TOKEN_URL = "https://accounts.spotify.com/api/token";
    private static final String SEARCH_URL = "https://api.spotify.com/v1/search";
    private static final String ARTIST_URL = "https://api.spotify.com/v1/artists";

    private static final String ARTIST_NAME_1 = "Oasis";
    private static final String ARTIST_NAME_2 = "Linkin Park";

    private static String getSpotifyAccessToken() throws IOException {
        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpPost post = new HttpPost(TOKEN_URL);

        // Encode credentials
        String auth = CLIENT_ID + ":" + CLIENT_SECRET;
        String encodedAuth = Base64.getEncoder().encodeToString(auth.getBytes(StandardCharsets.UTF_8));

        // Set headers
        post.setHeader("Authorization", "Basic " + encodedAuth);
        post.setHeader("Content-Type", "application/x-www-form-urlencoded");

        // Set entity
        StringEntity entity = new StringEntity("grant_type=client_credentials");
        post.setEntity(entity);

        // Execute request
        try (CloseableHttpResponse response = httpClient.execute(post)) {
            String jsonResponse = EntityUtils.toString(response.getEntity());
            JSONObject jsonObject = new JSONObject(jsonResponse);
            return jsonObject.getString("access_token");
        } finally {
            httpClient.close();
        }
    }

    private static String getArtistId(String accessToken, String artistName) throws IOException, URISyntaxException {
        CloseableHttpClient httpClient = HttpClients.createDefault();

        // Build URL with encoded artist name
        URIBuilder uriBuilder = new URIBuilder(SEARCH_URL);
        uriBuilder.addParameter("q", artistName);
        uriBuilder.addParameter("type", "artist");
        String requestUrl = uriBuilder.toString();

        HttpGet get = new HttpGet(requestUrl);

        // Set headers
        get.setHeader("Authorization", "Bearer " + accessToken);

        // Execute request
        try (CloseableHttpResponse response = httpClient.execute(get)) {
            String jsonResponse = EntityUtils.toString(response.getEntity());
            JSONObject jsonObject = new JSONObject(jsonResponse);
            // Get the artist ID from the first result
            JSONObject artist = jsonObject.getJSONObject("artists").getJSONArray("items").getJSONObject(0);
            return artist.getString("id");
        } finally {
            httpClient.close();
        }
    }

    private static JSONObject getArtistInformation(String accessToken, String artistId) throws IOException, URISyntaxException {
        CloseableHttpClient httpClient = HttpClients.createDefault();

        // Build URL with encoded artist name
        URIBuilder uriBuilder = new URIBuilder(ARTIST_URL + "/" + artistId);
        String requestUrl = uriBuilder.toString();

        HttpGet get = new HttpGet(requestUrl);

        // Set headers
        get.setHeader("Authorization", "Bearer " + accessToken);

        // Execute request
        try (CloseableHttpResponse response = httpClient.execute(get)) {
            String jsonResponse = EntityUtils.toString(response.getEntity());
            JSONObject jsonObject = new JSONObject(jsonResponse);
            System.out.println(jsonObject);
            //Integer popularity = jsonObject.getInt("popularity");
            //System.out.println("Popularity:" + jsonObject.getJSONObject("followers").getInt("total"));
            return jsonObject;
        } finally {
            httpClient.close();
        }
    }


    public static void main(String[] args) throws Exception {
        try {
            String accessToken = getSpotifyAccessToken();

            System.out.println("Access Token: " + accessToken);
            String artistID = getArtistId(accessToken, ARTIST_NAME_1);
            String artistID2 = getArtistId(accessToken, ARTIST_NAME_2);


            JSONObject jsonObjectArtist1 = getArtistInformation(accessToken, artistID);
            JSONObject jsonObjectArtist2 = getArtistInformation(accessToken, artistID2);

            if (jsonObjectArtist1.getInt("popularity") > jsonObjectArtist2.getInt("popularity")){
                System.out.println("El grupo mas popular es " + ARTIST_NAME_1);
            } else {
                System.out.println("El grupo mas popular es " + ARTIST_NAME_2);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
