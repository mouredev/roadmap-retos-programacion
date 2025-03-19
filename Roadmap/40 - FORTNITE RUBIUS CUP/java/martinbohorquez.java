import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.io.IOException;
import java.net.*;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

import static java.net.http.HttpClient.newHttpClient;

/**
 * #40 FORTNITE RUBIUS CUP
 * <dependency>
 * <groupId>com.google.code.gson</groupId>
 * <artifactId>gson</artifactId>
 * <version>2.10.1</version>
 * </dependency>
 *
 * @author martinbohorquez
 */


public class martinbohorquez {
    private static final String TWITCH_ID = System.getenv("TWITCH_ID");
    private static final String TWITCH_SECRET = System.getenv("TWITCH_SECRET");
    private static final String TOKEN_URL = "https://id.twitch.tv/oauth2/token";
    private static final String USER_URL = "https://api.twitch.tv/helix/users?login=";
    private static final String FOLLOWERS_URL = "https://api.twitch.tv/helix/channels/followers?broadcaster_id=";

    public static void main(String[] args) throws Exception {
        // 1. Token
        String token = getToken();

        // 2. IDs
        List<Map<String, String>> usersData = new ArrayList<>();
        List<String> usersNoData = new ArrayList<>();
        List<String> users = List.of(
                "littleragergirl", "ache", "adricontreras4", "agustin51", "alexby11", "ampeterby7", "tvander",
                "arigameplays", "arigeli_", "auronplay", "axozer", "beniju03", "bycalitos",
                "byviruzz", "carreraaa", "celopan", "srcheeto", "crystalmolly", "darioemehache",
                "dheylo", "djmariio", "doble", "elvisayomastercard", "elyas360", "folagorlives", "thegrefg",
                "guanyar", "hika", "hiperop", "ibai", "ibelky_", "illojuan", "imantado",
                "irinaissaia", "jesskiu", "jopa", "jordiwild", "kenaivsouza", "mrkeroro10",
                "thekiddkeo95", "kikorivera", "knekro", "kokoop", "kronnozomberoficial", "leviathan",
                "litkillah", "lolalolita", "lolitofdez", "luh", "luzu", "mangel", "mayichi",
                "melo", "missasinfonia", "mixwell", "jaggerprincesa", "nategentile7", "nexxuz",
                "lakshartnia", "nilojeda", "nissaxter", "olliegamerz", "orslok", "outconsumer", "papigavitv",
                "paracetamor", "patica1999", "paulagonu", "pausenpaii", "perxitaa", "nosoyplex",
                "polispol1", "quackity", "recuerd0p", "reventxz", "rivers_gg", "robertpg", "roier",
                "ceuvebrokenheart", "rubius", "shadoune666", "silithur", "spok_sponha", "elspreen", "spursito",
                "bystaxx", "suzyroxx", "vicens", "vitu", "werlyb", "xavi", "xcry", "elxokas",
                "thezarcort", "zeling", "zormanworld", "mouredev"
        );
        for (String username: users) {
            JsonObject user = getUserInfo(token, username);
            if (user == null) usersNoData.add(username);
            else {
                Map<String, String> userMap = new HashMap<>();
                userMap.put("username", username);
                userMap.put("created_at", user.get("created_at").getAsString());
                int followers = getTotalFollowers(token, user.get("id").getAsString());
                userMap.put("followers", Integer.toString(followers));
                usersData.add(userMap);
            }
        }
        System.out.println("Lista de usuarios que no tienen cuenta de Twitch:");
        usersNoData.forEach(user -> System.out.printf("- %s%n", user));

        System.out.println("Lista de usuarios que tienen cuenta de Twitch:");

        System.out.println("Ordenado por followers de forma descendente");
        usersData.sort(Comparator.comparing(u -> u.get("followers")));
        AtomicInteger i = new AtomicInteger(1);
        usersData.reversed().forEach(user -> System.out.printf("%d.- %s%n", i.getAndIncrement(),
                user.get("username") + ": " + user.get("followers") + " followers"));

        System.out.println("Ordenado por fecha de creación de forma ascendente");
        usersData.sort(Comparator.comparing(u -> u.get("created_at")));
        AtomicInteger j = new AtomicInteger(1);
        usersData.forEach(user -> System.out.printf("%d.- %s%n", j.getAndIncrement(),
                user.get("username") + ": " + user.get("created_at")));

    }

    private static String getToken() {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(TOKEN_URL))
                .header("Content-Type", "application/x-www-form-urlencoded") // Add headers
                .POST(HttpRequest.BodyPublishers.ofString(
                        "client_id=" + TWITCH_ID + "&client_secret=" + TWITCH_SECRET + "&grant_type=client_credentials"))
                .build();
        JsonObject jsonObject = getJsonObject(request);
        return jsonObject.get("access_token").getAsString();
    }

    private static JsonObject getUserInfo(String token, String user) {
        String encodedUser = URLEncoder.encode(user, StandardCharsets.UTF_8);
        JsonObject json = getJson(token, USER_URL + encodedUser);
        JsonArray userList = json.getAsJsonArray("data");
        if (userList == null) return null;
        if (userList.isEmpty()) return null;
        return userList.get(0).getAsJsonObject();
    }

    private static int getTotalFollowers(String token, String id) {
        JsonObject json = getJson(token, FOLLOWERS_URL + id);
        return json.get("total").getAsInt();
    }

    private static JsonObject getJson(String token, String url) {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("Authorization", "Bearer " + token) // Authorization header if needed
                .header("Client-Id", TWITCH_ID)
                .build();
        return getJsonObject(request);
    }

    private static JsonObject getJsonObject(HttpRequest request) {
        HttpResponse<String> response;
        try (HttpClient client = newHttpClient()) {
            response = client.send(request, HttpResponse.BodyHandlers.ofString());
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
        String responseBody = response.body();
        return JsonParser.parseString(responseBody).getAsJsonObject();
    }
}
