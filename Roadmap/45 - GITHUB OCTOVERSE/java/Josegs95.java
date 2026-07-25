import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().GitHubOctoverse();
    }

    private String user = "mouredev";
    final private String ACCESS_TOKEN = System.getenv("ACCESS_TOKEN");

    public void GitHubOctoverse(){
        Map<String, String> userData = new HashMap<>();
        userData.put("name", user);

        try{
            String url = "https://api.github.com/users/" + user;
            JsonElement data = makeGETRequest(url);
            if (data == null){
                throw new Exception();
            }
            JsonObject userJSONData = data.getAsJsonObject();
            int publicRepositories = Integer.valueOf(userJSONData.get("public_repos").getAsString());

            userData.put("followers", userJSONData.get("followers").getAsString());
            userData.put("following", userJSONData.get("following").getAsString());
            userData.put("public_repos", String.valueOf(publicRepositories));

            JsonArray repositories = new JsonArray();
            int pageCount = 1;
            do{
                url = userJSONData.get("repos_url").getAsString().concat("?per_page=30&page=" + pageCount);
                data = makeGETRequest(url);
                if (data == null){
                    throw new Exception();
                }

                repositories.addAll(data.getAsJsonArray());
                pageCount++;
                publicRepositories -= 30;
            }while(publicRepositories > 0);

            userData.putAll(analyzeRepositories(repositories));
        } catch (Exception e) {}

        printUserData(userData);
    }

    private Map<String, String> analyzeRepositories(JsonArray repositories){
        JsonObject mostPopularRepository = null;
        Map<String, Integer> languageUse = new HashMap<>();
        Map<String, String> data = new HashMap<>();

        for ( JsonElement repository : repositories){
            JsonObject repo = repository.getAsJsonObject();
            JsonElement langElement = repo.get("language");
            if (!langElement.isJsonNull()){
                String language = langElement.getAsString();
                if (languageUse.containsKey(language))
                    languageUse.replace(language, languageUse.get(language) + 1);
                else
                    languageUse.put(language, 1);
            }

            if (mostPopularRepository == null) {
                mostPopularRepository = repo;
                continue;
            }

            int stars = Integer.valueOf(repo.get("stargazers_count").getAsString());
            if (stars > Integer.valueOf(mostPopularRepository.get("stargazers_count").getAsString())){
                mostPopularRepository = repo;
            }
        }

        List<Map.Entry<String, Integer>> aux = new ArrayList<>(languageUse.entrySet());
        aux.sort(Collections.reverseOrder(Map.Entry.comparingByValue()));

        data.put("most_popular_repository", mostPopularRepository.get("name").getAsString());
        data.put("most_popular_repository_stars", mostPopularRepository.get("stargazers_count").getAsString());
        data.put("most_used_language", aux.get(0).getKey());
        data.put("most_used_language_count", aux.get(0).getValue().toString());

        return data;
    }

    private void printUserData(Map<String, String> data){
        System.out.println("Nombre del usuario: " + data.get("name"));
        System.out.println("Seguidores: " + data.get("followers") + ", Siguiendo: " + data.get("following"));
        System.out.println("Repositorios públicos: " + data.get("public_repos"));
        System.out.println("Repositorio mas popular: '" + data.get("most_popular_repository")
                + "' con " + data.get("most_popular_repository_stars") + " estrellas");
        System.out.println("Lenguaje mas utilizado: " + data.get("most_used_language") + " en "
                + data.get("most_used_language_count") + "/" +  data.get("public_repos") + " repositorios");
    }

    private JsonElement makeGETRequest(String url){
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder(URI.create(url))
                .header("Accept", "application/vnd.github+json")
                .header("Authorization", "Bearer " + ACCESS_TOKEN)
                .GET()
                .build();
        try{
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            if (response.statusCode() != 200){
                System.out.println("Ha ocurrido un error al intentar hacer una petición a la API");
                System.out.println("Respuesta: " + response.body() + "\n");
                return null;
            }

            return JsonParser.parseString(response.body());
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}
