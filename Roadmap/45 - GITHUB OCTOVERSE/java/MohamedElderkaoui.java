import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.*;
import org.json.*;

public class MohamedElderkaoui {
    private static final String USER = "MohamedElderkaoui"; // GitHub user to generate the report for
    private static final String TOKEN = System.getenv("GITHUB_TOKEN");

    public static void main(String[] args) throws IOException {
        if (TOKEN == null || TOKEN.isEmpty()) {
            System.out.println("Error: GitHub token is not set. Please set the GITHUB_TOKEN environment variable.");
            return;
        }

        GitHubClient client = GitHubClient.create(TOKEN);
        User user = client.getUser(USER);

        if (user == null) {
            System.out.println("User not found or data unavailable.");
            return;
        }

        // Generate user report
        StringBuilder report = new StringBuilder();
        report.append("GitHub User Report for ").append(USER).append(":\n")
                .append("Name: ").append(user.getName()).append("\n")
                .append("Location: ").append(user.getLocation()).append("\n")
                .append("Bio: ").append(user.getBio()).append("\n")
                .append("Public Repositories: ").append(user.getPublicRepos()).append("\n")
                .append("Followers: ").append(user.getFollowers()).append("\n")
                .append("Following: ").append(user.getFollowing()).append("\n")
                .append("Most Used Language: ").append(user.getMostUsedLanguage()).append("\n")
                .append("Total Stars: ").append(user.getStars()).append("\n")
                .append("Total Forks: ").append(user.getForks()).append("\n");

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

        if (userData == null) {
            return null;
        }

        // Fetch user's repositories
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
    private final String name;
    private final String location;
    private final String bio;
    private final int followers;
    private final int following;
    private final int publicRepos;
    private final int stars;
    private final int forks;
    private final String mostUsedLanguage;

    public User(JSONObject userData, JSONArray reposData) {
        this.name = userData.optString("name", "N/A");
        this.location = userData.optString("location", "N/A");
        this.bio = userData.optString("bio", "N/A");
        this.followers = userData.optInt("followers", 0);
        this.following = userData.optInt("following", 0);
        this.publicRepos = userData.optInt("public_repos", 0);

        Map<String, Integer> languageCount = new HashMap<>();
        int starsSum = 0;
        int forksSum = 0;

        if (reposData != null && reposData.length() > 0) {
            for (int i = 0; i < reposData.length(); i++) {
                JSONObject repo = reposData.getJSONObject(i);
                starsSum += repo.optInt("stargazers_count", 0);
                forksSum += repo.optInt("forks_count", 0);

                String language = repo.optString("language", "Unknown");
                if (!language.equals("Unknown")) {
                    languageCount.put(language, languageCount.getOrDefault(language, 0) + 1);
                }
            }
        }

        this.stars = starsSum;
        this.forks = forksSum;

        this.mostUsedLanguage = languageCount.isEmpty()
                ? "No languages found"
                : languageCount.entrySet()
                        .stream()
                        .max(Map.Entry.comparingByValue())
                        .map(Map.Entry::getKey)
                        .orElse("Unknown");
    }

    public String getName() {
        return name;
    }

    public String getLocation() {
        return location;
    }

    public String getBio() {
        return bio;
    }

    public int getFollowers() {
        return followers;
    }

    public int getFollowing() {
        return following;
    }

    public int getPublicRepos() {
        return publicRepos;
    }

    public int getStars() {
        return stars;
    }

    public int getForks() {
        return forks;
    }

    public String getMostUsedLanguage() {
        return mostUsedLanguage;
    }
}