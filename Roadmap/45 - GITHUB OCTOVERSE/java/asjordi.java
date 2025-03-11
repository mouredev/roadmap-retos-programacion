import com.google.gson.Gson;
import com.google.gson.JsonArray;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.*;

public class Main {

    /*
    * CLI to fetch the recent activity of a GitHub user and display it in the terminal.
    * https://github.com/ASJordi/gh-user-activity-cli
    */

    public static void main(String[] args) {
        Main m = new Main("asjordi");

        int gist = m.getNumGists();
        int stars = m.getNumStars();
        int followers = m.getNumFollowers();
        int following = m.getNumFollowing();
        int repos = m.getInfoRepos();

        System.out.println("Stats for user: " + m.getUsuario());
        System.out.println("Repos: " + repos);
        System.out.println("Gists: " + gist);
        System.out.println("Stars: " + stars);
        System.out.println("Followers: " + followers);
        System.out.println("Following: " + following);
    }

    private final String usuario;
    private Gson gson = new Gson();
    private HttpClient httpClient = HttpClient.newHttpClient();
    private HttpRequest request = null;

    public Main(String usuario) {
        this.usuario = usuario;
    }

    public int getInfoRepos() {
        String url = "https://api.github.com/users/" + this.usuario + "/repos?per_page=100";
        Map<String, Integer> map = new HashMap<>();

        HttpResponse<String> response = sendRequest(url);
        int statusCode = response.statusCode();

        if (statusCode != 200) return -1;
        String responseBody = response.body();
        JsonArray repos = gson.fromJson(responseBody, JsonArray.class);

        return repos.size();
    }

    public int getNumFollowing() {
        String url = "https://api.github.com/users/" + this.usuario + "/following?per_page=100";

        HttpResponse<String> response = sendRequest(url);
        int statusCode = response.statusCode();

        if (statusCode != 200) return -1;
        String responseBody = response.body();
        JsonArray following = gson.fromJson(responseBody, JsonArray.class);

        return following.size();
    }

    public int getNumFollowers() {
        String url = "https://api.github.com/users/" + this.usuario + "/followers?per_page=100";

        HttpResponse<String> response = sendRequest(url);
        int statusCode = response.statusCode();

        if (statusCode != 200) return -1;
        String responseBody = response.body();
        JsonArray followers = gson.fromJson(responseBody, JsonArray.class);

        return followers.size();
    }

    public int getNumGists() {
        String url = "https://api.github.com/users/" + this.usuario + "/gists?per_page=100";

        HttpResponse<String> response = sendRequest(url);
        int statusCode = response.statusCode();

        if (statusCode != 200) return -1;
        String responseBody = response.body();
        JsonArray gists = gson.fromJson(responseBody, JsonArray.class);

        return gists.size();
    }

    public int getNumStars() {
        String url = "https://api.github.com/users/" + this.usuario + "/starred?per_page=100";

        HttpResponse<String> response = sendRequest(url);
        int statusCode = response.statusCode();

        if (statusCode != 200) return -1;
        String responseBody = response.body();
        JsonArray stars = gson.fromJson(responseBody, JsonArray.class);

        return stars.size();
    }

    private HttpResponse<String> sendRequest(String url) {
        HttpResponse<String> response = null;
        try {
            this.request = HttpRequest.newBuilder()
                    .uri(new URI(url))
                    .GET()
                    .build();

            response = this.httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        } catch (URISyntaxException | IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }

        return response;
    }

    public String getUsuario() {
        return this.usuario;
    }

}
