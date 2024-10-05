import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.http.HttpResponse.BodyHandlers;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Comparator;
import java.util.List;
import java.util.TimeZone;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MohamedElderkaoui {

    private static final String CLIENT_ID =""; // Replace with your Client ID
    private static final String CLIENT_SECRET = "";  // Replace with your Client Secret
    private static final String TOKEN_URL = "https://id.twitch.tv/oauth2/token";
    private static final String TWITCH_API_URL = "https://api.twitch.tv/helix/users";
    private static final String FOLLOWERS_API_URL = "https://api.twitch.tv/helix/users/follows";
    private static String accessToken = "";

    public static void main(String[] args) {
        try {
            // List of participants from the Twitter post
            List<String> participants = Arrays.asList(
                    "ABBY", "ACHE", "ADRI CONTRERAS", "AGUSTIN", "ALEXBY", "AMPETER", "ANDER", "ARI GAMEPLAYS",
                    "ARIGELI", "AURONPLAY", "AXOZER", "BENIJU", "BY CALITOS", "BYVIRUZZ", "CARRERA", "CELOPAN",
                    "CHEETO", "CRYSTALMOLLY", "DARIO EMEHACHE", "DHEYLO", "DJMARIO", "DOBLE", "ELVISA", "ELYAS360",
                    "FOLAGOR", "GREFG", "GUANYAR", "HIKA", "HIPER", "IBAI", "IBELKY", "ILLOJUAN", "IMANTADO",
                    "IRINA ISSAIA", "JESSKIU", "JOPA", "JORDIWILD", "KENAI SOUZA", "KERORO", "KIDD KEO", "KIKO RIVERA",
                    "KNEKRO", "KOKO", "KRONNOZOMBER", "LEVIATHAN", "LIT KILLAH", "LOLA LOLITA", "LOLITO", "LUH", "LUZU",
                    "MANGEL", "MAYICHI", "MELO", "MISSASINOFIA", "MIXWELL", "MR.JAGGER", "NATE GENTILE", "NEXXUZ",
                    "NIA", "NIL OJEDA", "NISSAXTER", "OLLIE", "ORSLOK", "OUTCONSUMER", "PAPI GAVI", "PARCETAMOR",
                    "PATICA", "PAULA GONU", "PAUSENPAII", "PERXITAA", "PLEX", "POLISPOL", "QUACKITY", "RECUERDOP",
                    "REVEN", "RIVERS", "ROBERTPG", "ROIER", "ROJUU", "RUBIUS", "SHADOUNE", "SILITHUR", "SPOKSPONHA",
                    "SPREEN", "SPURSITO", "STAXX", "SUZYROXX", "VICENS", "VITUBER", "WERLYB", "XAVI", "XCRY", "XOKAS",
                    "ZARCORT", "ZELING", "ZORMAN"
            );

            // Get access token
            accessToken = getAccessToken();

            // Get Twitch user information
            List<TwitchUser> users = getTwitchUsers(participants);

            // Filter out users that were not found
            List<TwitchUser> foundUsers = new ArrayList<>();
            List<String> notFoundUsers = new ArrayList<>();

            for (TwitchUser user : users) {
                if (user != null) {
                    foundUsers.add(user);
                } else {
                    notFoundUsers.add("Unknown User"); // Placeholder for unknown users
                }
            }

            // Sort by number of followers
            foundUsers.sort(Comparator.comparingLong(TwitchUser::getFollowers).reversed());

            // Print ranking by number of followers
            System.out.println("Ranking por número de seguidores:");
            for (TwitchUser user : foundUsers) {
                System.out.println(user.getDisplayName() + ": " + user.getFollowers() + " seguidores");
            }

            // Sort by account creation date (seniority)
            foundUsers.sort(Comparator.comparing(TwitchUser::getCreationDate));

            // Print ranking by account creation date
            System.out.println("\nRanking por antigüedad de la cuenta:");
            for (TwitchUser user : foundUsers) {
                System.out.println(user.getDisplayName() + ": " + user.getCreationDateStr());
            }

            // Print unknown users
            System.out.println("\nUsuarios no encontrados:");
            for (String notFound : notFoundUsers) {
                System.out.println(notFound);
            }

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    private static String getAccessToken() throws IOException, InterruptedException {
        // Create the body for the request to obtain the access token
        String body = "client_id=" + CLIENT_ID
                    + "&client_secret=" + CLIENT_SECRET
                    + "&grant_type=client_credentials";

        // Make the HTTP POST request to get the access token
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(TOKEN_URL))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(body))
                .build();

        HttpClient client = HttpClient.newHttpClient();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        // Check if the response is successful (status code 200)
        if (response.statusCode() != 200) {
            throw new IOException("Error en la solicitud de token: " + response.body());
        }

        // Parse the response to get the access token
        JSONObject jsonResponse = new JSONObject(response.body());
        if (!jsonResponse.has("access_token")) {
            throw new JSONException("Token de acceso no encontrado en la respuesta: " + response.body());
        }

        return jsonResponse.getString("access_token");
    }

    // Method to get Twitch users
    private static List<TwitchUser> getTwitchUsers(List<String> usernames) throws IOException, InterruptedException {
        List<TwitchUser> users = new ArrayList<>();
        HttpClient client = HttpClient.newHttpClient();

        for (String username : usernames) {
            try {
                // URL encode the username to handle spaces and special characters
                String encodedUsername = URLEncoder.encode(username, "UTF-8");
                HttpRequest request = HttpRequest.newBuilder()
                        .uri(URI.create(TWITCH_API_URL + "?login=" + encodedUsername))
                        .GET()
                        .header("Authorization", "Bearer " + accessToken)
                        .header("Client-Id", CLIENT_ID)
                        .build();

                HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
                JSONObject json = new JSONObject(response.body());
                JSONArray data = json.optJSONArray("data");

                if (data != null && data.length() > 0) {
                    JSONObject userData = data.getJSONObject(0);
                    long followersCount = getFollowersCount(userData.getString("id")); // Get follower count
                    TwitchUser user = new TwitchUser(
                            userData.getString("id"),
                            userData.getString("display_name"),
                            followersCount,
                            userData.getString("created_at")
                    );
                    users.add(user);
                } else {
                    users.add(null); // User not found
                }
            } catch (UnsupportedEncodingException e) {
                e.printStackTrace(); // Handle URL encoding exceptions
                users.add(null); // If encoding fails, consider the user as not found
            }
        }

        return users;
    }

    private static long getFollowersCount(String userId) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(FOLLOWERS_API_URL + "?to_id=" + userId))
                .GET()
                .header("Authorization", "Bearer " + accessToken)
                .header("Client-Id", CLIENT_ID)
                .build();

        HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
        JSONObject json = new JSONObject(response.body());
        JSONArray data = json.optJSONArray("data");

        // Return the count of followers
        return data != null ? data.length() : 0; // Return 0 if no followers
    }
}

// Class to model Twitch users
class TwitchUser {
    private String id;
    private String displayName;
    private long followers;
    private Calendar creationDate;

    public TwitchUser(String id, String displayName, long followers, String creationDate) {
        this.id = id;
        this.displayName = displayName;
        this.followers = followers;
        this.creationDate = parseCreationDate(creationDate);
    }

    private Calendar parseCreationDate(String creationDateString) {
        Calendar calendar = Calendar.getInstance();
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'");
        sdf.setTimeZone(TimeZone.getTimeZone("UTC"));
        try {
            calendar.setTime(sdf.parse(creationDateString));
        } catch (Exception e) {
            e.printStackTrace();
        }
        return calendar;
    }

    public String getId() {
        return id;
    }

    public String getDisplayName() {
        return displayName;
    }

    public long getFollowers() {
        return followers;
    }

    public Calendar getCreationDate() {
        return creationDate;
    }

    public String getCreationDateStr() {
        SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-yyyy");
        return sdf.format(creationDate.getTime());
    }
}
