import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.*;
import org.json.JSONObject;
import org.json.JSONArray;

public class MohamedElderkaoui {
    private static final String USER = "MohamedElderkaoui"; // GitHub user to generate the report for
    private static final String token ="";// System.getenv("your_GITHUB_TOKEN");

    public static void main(String[] args) throws IOException {
        if (token == null || token.isEmpty()) {
            System.out.println("Error: GitHub token is not set. Please set the GITHUB_TOKEN environment variable.");
            return;
        }

        GitHubClient client = GitHubClient.create(token);
        User user = client.getUser(USER);

        if (user == null) {
            System.out.println("User not found or data unavailable.");
            return;
        }

        // Generate user report
        StringBuilder report = new StringBuilder();
        report.append("User Information for ").append(USER).append(":\n").append("Most Used Language: ").append(user.getMostUsedLanguage()).append("\n").append("Number of Repositories: ").append(user.getPublicRepos()).append("\n").append("Followers: ").append(user.getFollowers()).append("\n").append("Following: ").append(user.getFollowing()).append("\n").append("Stars: ").append(user.getStars()).append("\n").append("Forks: ").append(user.getForks()).append("\n");

        System.out.println(report);
    }
}

class GitHubClient {
    private final String token;

    public GitHubClient(String token) {
        this.token = token;
    }

    public static GitHubClient create(String token) {
        return new GitHubClient(token);
    }

    public User getUser(String username) throws IOException {
        String apiUrl = "https://api.github.com/users/" + username;
        JSONObject userData = fetchJsonFromUrl(apiUrl);
        if (userData == null) return null;

        // Retrieve user stats from repositories
        JSONArray reposData = fetchJsonArrayFromUrl(apiUrl + "/repos");

        return new User(userData, reposData);
    }

    private JSONObject fetchJsonFromUrl(String apiUrl) throws IOException {
        HttpURLConnection connection = openConnection(apiUrl);
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            return new JSONObject(response.toString());
        } catch (Exception e) {
            System.out.println("Error fetching data: " + e.getMessage());
            return null;
        }
    }

    private JSONArray fetchJsonArrayFromUrl(String apiUrl) throws IOException {
        HttpURLConnection connection = openConnection(apiUrl);
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()))) {
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            return new JSONArray(response.toString());
        } catch (Exception e) {
            System.out.println("Error fetching data: " + e.getMessage());
            return null;
        }
    }

    private HttpURLConnection openConnection(String apiUrl) throws IOException {
        URL url = new URL(apiUrl);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.setRequestProperty("Authorization", "Bearer " + token);
        connection.setRequestProperty("Accept", "application/vnd.github.v3+json");
        return connection;
    }
}

 class User {
    private final String mostUsedLanguage;
    private final int publicRepos;
    private final int followers;
    private final int following;
    private final int stars;
    private final int forks;

    public User(JSONObject userData, JSONArray reposData) {
        this.publicRepos = userData.getInt("public_repos");
        this.followers = userData.getInt("followers");
        this.following = userData.getInt("following");

        int starCount = 0;
        int forkCount = 0;
        Map<String, Integer> languageCount = new HashMap<>();

        for (int i = 0; i < reposData.length(); i++) {
            JSONObject repo = reposData.getJSONObject(i);
            starCount += repo.getInt("stargazers_count");
            forkCount += repo.getInt("forks_count");

            // Only count non-null and non-empty language fields
            String language = repo.optString("language", null);
            if (language != null && !language.equals("null")) {
                languageCount.put(language, languageCount.getOrDefault(language, 0) + 1);
            }
        }

        this.stars = starCount;
        this.forks = forkCount;

        // Find the most used language
        this.mostUsedLanguage = languageCount.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .map(Map.Entry::getKey)
                .orElse("No predominant language");
    }

    public String getMostUsedLanguage() {
        return mostUsedLanguage;
    }

    public int getPublicRepos() {
        return publicRepos;
    }

    public int getFollowers() {
        return followers;
    }

    public int getFollowing() {
        return following;
    }

    public int getStars() {
        return stars;
    }

    public int getForks() {
        return forks;
    }
}
