import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class Josegs95 {
    public static void main(String[] args) {
        new Josegs95().forniteCup();
    }

    private final String CLIENT_ID = System.getenv("Client_ID");
    private final String CLIENT_SECRET = System.getenv("Client_Secret");
    private String AUTH_TOKEN;

    private void forniteCup(){
        getAuthToken();

        String[] participants = getUsersList();
        List<Map<String, String>> userDataList = new ArrayList<>();
        List<String> notFoundUserList = new ArrayList<>();

        for (String participant : participants) {
            Map userData = getUserInfo(participant);
            if (userData == null) {
                notFoundUserList.add(participant);
                continue;
            }
            userDataList.add(userData);
        }

        List<Map<String, String>> sortedListByFollowers = userDataList.stream()
                .sorted((x, y) -> {
                    int followers1 = Integer.valueOf(x.get("followers"));
                    int followers2 = Integer.valueOf(y.get("followers"));
                    return (followers1 - followers2) * -1;
                }).toList();

        List<Map<String, String>> sortedListByDateTime = userDataList.stream()
                .sorted((x, y) -> {
                    LocalDateTime date1 = LocalDateTime.parse(x.get("creation_date"));
                    LocalDateTime date2 = LocalDateTime.parse(y.get("creation_date"));
                    return date1.compareTo(date2);
                }).toList();

        System.out.println("Usuarios encontrados (ordenados por seguidores):");
        int counter = 0;
        for (Map<String, String> userData : sortedListByFollowers){
            System.out.println(++counter + ". " + userData.get("name") + ": "
                    + String.format("%,d", Long.valueOf(userData.get("followers"))) + " seguidores");
        }
        System.out.println("Usuarios encontrados (ordenados por antigüedad):");
        counter = 0;
        for (Map<String, String> userData : sortedListByDateTime){
            System.out.println(++counter + ". " + userData.get("name") + ": "
                    + LocalDateTime.parse(userData.get("creation_date")).format(DateTimeFormatter.ofPattern("dd'/'MM'/'yyyy")));
        }

        if (!notFoundUserList.isEmpty()){
            System.out.println("Lista de usuarios que no se ha podido encontrar información:");
            for (String userName : notFoundUserList)
                System.out.println(userName);
        }
    }

    private void getAuthToken(){
        String url = "https://id.twitch.tv/oauth2/token";
        String body = "client_id=" + CLIENT_ID + "&client_secret=" + CLIENT_SECRET
                + "&grant_type=client_credentials";

        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder(URI.create(url))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(body))
                .build();

        try{
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            if (response.statusCode() != 200){
                System.out.println("Error al intentar obtener el token de autorización");
                System.out.println("Código: " + response.statusCode());
                System.out.println("Respuesta: " + response.body());
            }

            JsonObject data = JsonParser.parseString(response.body()).getAsJsonObject();
            AUTH_TOKEN = data.get("access_token").getAsString();
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }

    private Map<String, String> getUserInfo(String userName){
        Map<String, String> userData = new HashMap<>();

        String url = "https://api.twitch.tv/helix/users";
        url += "?login=" + userName.replace(" ", "");
        JsonObject data = getDataFromGETRequest(url);
        if (data == null)
            return null;

        JsonArray userArray = data.get("data").getAsJsonArray();
        if (userArray.isEmpty()){
            System.out.println("No se ha podido encontrar información de: " + userName);
            return null;
        }
        JsonObject userJson = userArray.get(0).getAsJsonObject();

        userData.put("name", userJson.get("display_name").getAsString());
        LocalDateTime date = LocalDateTime.parse(userJson.get("created_at").getAsString(),
                DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss'Z'"));
        userData.put("creation_date", date.toString());

        String userID = userJson.get("id").getAsString();
        url = "https://api.twitch.tv/helix/channels/followers";
        url += "?broadcaster_id=" + userID;
        JsonObject followerInfo = getDataFromGETRequest(url);
        if (followerInfo == null)
            return null;

        userData.put("followers", followerInfo.get("total").getAsString());

        return userData;
    }

    private JsonObject getDataFromGETRequest(String url){
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder(URI.create(url))
                .header("Authorization", "Bearer " + AUTH_TOKEN)
                .header("Client-Id", CLIENT_ID)
                .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            if (response.statusCode() != 200) {
                System.out.println("Error al intentar obtener información del usuario");
                System.out.println("Código: " + response.statusCode() + " URL: " + url);
                System.out.println("Respuesta: " + response.body());
            }

            return JsonParser.parseString(response.body()).getAsJsonObject();

        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
    }

    //Quedan muchos nombres, pero el ejercicio lo doy por terminado
    private String[] getUsersList(){
        return new String[] {
                "ibai", "elxokas", "auronplay", "rubius", "thegrefg",
                "rivers_gg", "djmariio", "alexby11", "ampeterby7", "mayichi",
                "mrkeroro10", "quackity", "elspreen", "litkillah", "illojuan",
                "werlyb", "zeling", "paracetamor", "paulagonu", "celopan",
                "elmariana", "littleragergirl", "zormanworld", "silithur", "luzu",
                "outconsumer", "FolagorLives", "bysTaXx", "suzyroxx", "spok_sponha",
                "LOLITOFDEZ", "jaggerprincesa", "nexxuz", "ElvisaYomastercard", "ReventXz"
        };

    }

}
