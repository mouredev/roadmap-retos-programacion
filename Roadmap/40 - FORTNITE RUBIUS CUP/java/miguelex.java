import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.*;
import org.json.*;

public class miguelex {

    public static String obtenerTokenOAuth(String clientId, String clientSecret) throws IOException {
        String url = "https://id.twitch.tv/oauth2/token";
        String urlParameters = "client_id=" + clientId + "&client_secret=" + clientSecret + "&grant_type=client_credentials";

        byte[] postData = urlParameters.getBytes(StandardCharsets.UTF_8);
        int postDataLength = postData.length;

        URL obj = new URL(url);
        HttpURLConnection con = (HttpURLConnection) obj.openConnection();

        con.setDoOutput(true);
        con.setRequestMethod("POST");
        con.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        con.setRequestProperty("Content-Length", Integer.toString(postDataLength));

        try (DataOutputStream wr = new DataOutputStream(con.getOutputStream())) {
            wr.write(postData);
        }

        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        JSONObject jsonResponse = new JSONObject(response.toString());
        return jsonResponse.getString("access_token");
    }

    public static JSONObject obtenerInfoUsuarioTwitch(String accessToken, String clientId, String username) throws IOException {
        username = username.replaceAll("[^a-zA-Z0-9_]", "");
        String url = "https://api.twitch.tv/helix/users?login=" + URLEncoder.encode(username, "UTF-8");

        HttpURLConnection con = (HttpURLConnection) new URL(url).openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("Authorization", "Bearer " + accessToken);
        con.setRequestProperty("Client-ID", clientId);

        int responseCode = con.getResponseCode();
        if (responseCode != 200) {
            return null;
        }

        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        JSONObject jsonResponse = new JSONObject(response.toString());
        return jsonResponse.getJSONArray("data").isEmpty() ? null : jsonResponse.getJSONArray("data").getJSONObject(0);
    }

    public static int obtenerNumeroSeguidoresTwitch(String accessToken, String clientId, String userId) throws IOException {
        String url = "https://api.twitch.tv/helix/channels/followers?broadcaster_id=" + userId;

        HttpURLConnection con = (HttpURLConnection) new URL(url).openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("Authorization", "Bearer " + accessToken);
        con.setRequestProperty("Client-ID", clientId);

        int responseCode = con.getResponseCode();
        if (responseCode != 200) {
            return 0;
        }

        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuilder response = new StringBuilder();

        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        in.close();

        JSONObject jsonResponse = new JSONObject(response.toString());
        return jsonResponse.has("total") ? jsonResponse.getInt("total") : 0;
    }

    public static void main(String[] args) {
        String clientId = "TU_CLIENT_ID";
        String clientSecret = "TU_CLIENT_SECRET";

        String[] participantes = {
        "Abby", "Ache", "Adri Contreras", "Agustin", "Alexby", "Ampeter", "Ander", "Ari Gameplays",
        "Arigely", "Auronplay", "Axozer", "Beniju", "By Calitos", "Byviruzz", "Carrera", "Celopan",
        "Cheto", "CrystalMolly", "Dario Eme Hache", "Dheyo", "DjMariio", "Doble", "Elvisa", "Elyas360",
        "Folagor", "Grefg", "Guanyar", "Hika", "Hiper", "Ibai", "Ibelky", "Illojuan", "Imantado",
        "Irina Isasia", "JessKiu", "Jopa", "JordiWild", "Kenai Souza", "Keroro", "Kidd Keo", "Kiko Rivera",
        "Knekro", "Koko", "KronnoZomber", "Leviathan", "Lit Killah", "Lola Lolita", "Lolito", "Luh",
        "Luzu", "Mangel", "Mayichi", "Melo", "MissaSinfonia", "Mixwell", "Mr. Jagger", "Nate Gentile",
        "Nexxuz", "Nia", "Nil Ojeda", "NissaXter", "Ollie", "Orslok", "Outconsumer", "Papi Gavi",
        "Paracetamor", "Patica", "Paula Gonu", "Pausenpaii", "Perxitaa", "Plex", "Polispol", "Quackity",
        "RecueroDP", "Reven", "Rivers", "RobertPG", "Roier", "Rojuu", "Rubius", "Shadoune", "Silithur",
        "SpokSponha", "Spreen", "Spursito", "Staxx", "SuzyRoxx", "Vicens", "Vituber", "Werlyb", "Xavi",
        "Xcry", "Xokas", "Zarcort", "Zeling", "Zorman"
        };

        try {
            String accessToken = obtenerTokenOAuth(clientId, clientSecret);

            List<Map<String, Object>> infoUsuarios = new ArrayList<>();
            List<String> errores = new ArrayList<>();

            for (String participante : participantes) {
                JSONObject usuario = obtenerInfoUsuarioTwitch(accessToken, clientId, participante);

                if (usuario != null) {
                    int seguidores = obtenerNumeroSeguidoresTwitch(accessToken, clientId, usuario.getString("id"));

                    Map<String, Object> userInfo = new HashMap<>();
                    userInfo.put("username", usuario.getString("display_name"));
                    userInfo.put("followers", seguidores);
                    userInfo.put("creation_date", usuario.getString("created_at"));

                    infoUsuarios.add(userInfo);
                } else {
                    errores.add("El participante " + participante + " no tiene usuario en Twitch.");
                }
            }

            infoUsuarios.sort((a, b) -> Integer.compare((int) b.get("followers"), (int) a.get("followers")));

            System.out.println("Ranking por número de seguidores:");
            for (Map<String, Object> usuario : infoUsuarios) {
                System.out.println(usuario.get("username") + " - " + usuario.get("followers") + " seguidores");
            }

            infoUsuarios.sort((a, b) -> ((String) a.get("creation_date")).compareTo((String) b.get("creation_date")));

            System.out.println("\nRanking por antigüedad de la cuenta:");
            for (Map<String, Object> usuario : infoUsuarios) {
                System.out.println(usuario.get("username") + " - Cuenta creada el " + usuario.get("creation_date"));
            }

            if (!errores.isEmpty()) {
                System.out.println("\nErrores:");
                for (String error : errores) {
                    System.out.println(error);
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
