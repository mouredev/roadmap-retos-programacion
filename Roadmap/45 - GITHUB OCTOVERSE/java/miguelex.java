import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.*;

public class miguelex {
    private String username;
    private final String baseApiUrl = "https://api.github.com";
    private final Map<String, String> headers = Map.of(
        "User-Agent", "GitHub-Report-App",
        "Accept", "application/vnd.github.v3+json"
    );

    public miguelex(String username) {
        this.username = username;
    }

    private String apiRequest(String endpoint) throws Exception {
        String urlString = baseApiUrl + endpoint;
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();

        connection.setRequestMethod("GET");
        headers.forEach(connection::setRequestProperty);

        int responseCode = connection.getResponseCode();

        if (responseCode != 200) {
            throw new Exception("Error al conectar con la API de GitHub (HTTP " + responseCode + "). Verifica el nombre de usuario.");
        }

        BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        StringBuilder response = new StringBuilder();
        String line;
        while ((line = in.readLine()) != null) {
            response.append(line);
        }
        in.close();

        return response.toString();
    }

    private Map<String, Object> parseJson(String jsonString) {
        Map<String, Object> map = new HashMap<>();
        jsonString = jsonString.replace("{", "").replace("}", "").trim();
        String[] pairs = jsonString.split(",");
        for (String pair : pairs) {
            String[] keyValue = pair.split(":", 2);
            if (keyValue.length == 2) {
                String key = keyValue[0].trim().replace("\"", "");
                String value = keyValue[1].trim().replace("\"", "");
                map.put(key, value);
            }
        }
        return map;
    }

    public void generateReport() {
        try {
            String userInfoResponse = apiRequest("/users/" + username);
            Map<String, Object> userInfo = parseJson(userInfoResponse);

            String reposResponse = apiRequest("/users/" + username + "/repos");
            String[] repos = reposResponse.replace("[", "").replace("]", "").split("},\\{");

            int totalRepos = repos.length;
            int followers = Integer.parseInt(userInfo.getOrDefault("followers", "0").toString());
            int following = Integer.parseInt(userInfo.getOrDefault("following", "0").toString());

            Map<String, Integer> languageCounts = new HashMap<>();
            int totalStars = 0;
            int totalForks = 0;

            for (String repo : repos) {
                Map<String, Object> repoData = parseJson(repo);

                String language = repoData.getOrDefault("language", null).toString();
                if (language != null && !language.isEmpty()) {
                    languageCounts.put(language, languageCounts.getOrDefault(language, 0) + 1);
                }

                totalStars += Integer.parseInt(repoData.getOrDefault("stargazers_count", "0").toString());
                totalForks += Integer.parseInt(repoData.getOrDefault("forks_count", "0").toString());
            }

            String topLanguage = languageCounts.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .map(Map.Entry::getKey)
                .orElse("N/A");

            System.out.println("=== Informe de GitHub para el usuario: " + username + " ===");
            System.out.println("Nombre: " + userInfo.getOrDefault("name", "N/A"));
            System.out.println("Bio: " + userInfo.getOrDefault("bio", "N/A"));
            System.out.println("Ubicación: " + userInfo.getOrDefault("location", "N/A"));
            System.out.println("Total de repositorios: " + totalRepos);
            System.out.println("Seguidores: " + followers);
            System.out.println("Seguidos: " + following);
            System.out.println("Lenguaje más utilizado: " + topLanguage);
            System.out.println("Total de estrellas: " + totalStars);
            System.out.println("Total de forks: " + totalForks);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el nombre de usuario de GitHub: ");
        String username = scanner.nextLine().trim();

        if (username.isEmpty()) {
            System.err.println("Debe ingresar un nombre de usuario.");
            return;
        }

        miguelex report = new miguelex(username);
        report.generateReport();
    }
}
