import org.apache.hc.core5.http.ParseException;
import se.michaelthelin.spotify.SpotifyApi;
import se.michaelthelin.spotify.exceptions.SpotifyWebApiException;
import se.michaelthelin.spotify.model_objects.credentials.ClientCredentials;
import se.michaelthelin.spotify.model_objects.specification.Artist;
import se.michaelthelin.spotify.requests.authorization.client_credentials.ClientCredentialsRequest;
import se.michaelthelin.spotify.requests.data.artists.GetArtistRequest;

import java.io.IOException;
import java.util.Arrays;

public class Main {

    private final String clientId = System.getenv("SPOTIFY_CLIENT_ID");
    private final String clientSecret = System.getenv("SPOTIFY_CLIENT_SECRET");
    private String clientToken;
    private SpotifyApi spotifyApi = new SpotifyApi.Builder()
            .setClientId(clientId)
            .setClientSecret(clientSecret)
            .build();
    private final ClientCredentialsRequest clientCredentialsRequest = spotifyApi.clientCredentials()
            .build();

    public static void main(String[] args) {
        Main m = new Main();
        m.getClientToken();
        ArtistInfo oasis = m.getArtistInfo("2DaxqgrOhkeH0fpeiQq2f4");
        ArtistInfo lp = m.getArtistInfo("6XyY86QOPPrYVGvF9ch6wz");

        System.out.println(oasis);
        System.out.println(lp);

        System.out.println("Who is more popular?");
        System.out.println(oasis.popularity() > lp.popularity() ? "Oasis" : "Linkin Park");
    }

    public ArtistInfo getArtistInfo(String id) {
        GetArtistRequest getArtistRequest = spotifyApi.getArtist(id).build();
        try {
            Artist artist = getArtistRequest.execute();
            return new ArtistInfo(artist.getName(), artist.getPopularity(), artist.getFollowers().getTotal(), artist.getGenres());
        } catch (IOException | SpotifyWebApiException | ParseException e) {
            System.out.println("Error: " + e.getMessage());
        }
        return null;
    }

    private void getClientToken() {
        try {
            final ClientCredentials clientCredentials = clientCredentialsRequest.execute();
            this.clientToken = clientCredentials.getAccessToken();
            spotifyApi.setAccessToken(clientCredentials.getAccessToken());
        } catch (IOException | SpotifyWebApiException | ParseException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    record ArtistInfo(String name, int popularity, int followers, String[] genres) {
        @Override
        public String toString() {
            return "ArtistInfo{" +
                    "name='" + name + '\'' +
                    ", popularity=" + popularity +
                    ", followers=" + followers +
                    ", genres=" + Arrays.toString(genres) +
                    '}';
        }
    }

}

// https://github.com/spotify-web-api-java/spotify-web-api-java
