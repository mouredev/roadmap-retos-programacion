public class albmartinez {

    private static final String CLIENT_ID = "";
    private static final String CLIENT_SECRET = "";
    private static final String TOKEN_URL = "https://id.twitch.tv/oauth2/token";
    private static final String TWITCH_API_URL_USERS = "https://api.twitch.tv/helix/users";
    private static final String TWITCH_API_URL_FOLLOWERS = "https://api.twitch.tv/helix/channels/followers";

    private static String accessToken = "";
    private static final HttpClient httpClient = HttpClient.newHttpClient();
    private static final DateTimeFormatter creationDateFormat = DateTimeFormatter.ofPattern("yyyy-MM-dd'T'HH:mm:ss'Z'");
    private static final DateTimeFormatter outputDateFormat = DateTimeFormatter.ofPattern("dd-MM-yyyy");

    public static void main(String[] args) {
        try {
            List<String> participants = getListParticipants();
            accessToken = getAccessToken();
            List<TwitchUser> userWithFollowers = new ArrayList<>();
            List<String> userWithoutAccount = new ArrayList<>();

            for (String username : participants) {
                Optional<TwitchUser> optionalUser = getTwitchUserInfo(username);
                optionalUser.ifPresentOrElse(userWithFollowers::add,
                        () -> userWithoutAccount.add(username));
            }

            printRanking(userWithFollowers, userWithoutAccount);

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

    }

    private static List<String> getListParticipants() {
        return Arrays.asList(
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
    }

    private static String getAccessToken() throws IOException, InterruptedException {
        // Crear el cuerpo de la solicitud
        String body = "client_id=" + CLIENT_ID
                + "&client_secret=" + CLIENT_SECRET
                + "&grant_type=client_credentials";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(TOKEN_URL))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(body))
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() != 200) {
            throw new IOException("Error en la solicitud del token: " + response.body());
        }

        JSONObject jsonResponse = new JSONObject(response.body());
        if (!jsonResponse.has("access_token")) {
            throw new JSONException("Token de acceso no encontrado en la respuesta: " + response.body());
        }

        return jsonResponse.getString("access_token");
    }

    private static Optional<TwitchUser> getTwitchUserInfo(String username) {
        try {
            String encodedUsername = URLEncoder.encode(username, StandardCharsets.UTF_8);
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(TWITCH_API_URL_USERS + "?login=" + encodedUsername))
                    .GET()
                    .header("Authorization", "Bearer " + accessToken)
                    .header("Client-ID", CLIENT_ID)
                    .build();

            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
            if (response.statusCode() != 200) {
                return Optional.empty();
            }

            JSONObject json = new JSONObject(response.body());
            JSONArray data = json.optJSONArray("data");
            if (data != null && data.length() > 0) {
                JSONObject userData = data.getJSONObject(0);
                long followers = getFollowersCount(userData.getString("id"));
                return Optional.of(new TwitchUser(userData.getString("id"),
                        userData.getString("display_name"), followers, userData.getString("created_at")));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return Optional.empty();
    }

    private static long getFollowersCount(String userId) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(TWITCH_API_URL_FOLLOWERS + "?broadcaster_id=" + userId))
                .GET()
                .header("Authorization", "Bearer " + accessToken)
                .header("Client-ID", CLIENT_ID)
                .build();

        HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
        if (response.statusCode() != 200) {
            throw new IOException("Error obteniendo el número de seguidores: " + response.body());
        }

        JSONObject json = new JSONObject(response.body());
        return json.getLong("total");
    }

    private static void printRanking(List<TwitchUser> usersWithFollowers, List<String> usersWithoutAccount) {
        System.out.println("\nRanking por número de seguidores");
        usersWithFollowers.sort(Comparator.comparingLong(TwitchUser::getFollowers).reversed());
        usersWithFollowers.forEach(user ->
                System.out.println(user.getDisplayName() + ": " + user.getFollowers() + " seguidores"));

        System.out.println("\nRanking por antigüedad de la cuenta:");
        usersWithFollowers.sort(Comparator.comparing(TwitchUser::getCreationDate));
        usersWithFollowers.forEach(user ->
                System.out.println(user.getDisplayName() + ": " + user.getCreationDataString()));

        if (!usersWithoutAccount.isEmpty()) {
            System.out.println("\nUsuarios sin cuenta en Twitch:");
            System.out.println(String.join(", ", usersWithoutAccount));
        } else {
            System.out.println("\nTodos los participantes tienen cuenta en Twitch");
        }
    }

    static class TwitchUser {
        private String id;
        private String displayName;
        private long followers;
        private LocalDateTime creationDate;

        public TwitchUser(String id, String displayName, long followers, String creationDate) {
            this.id = id;
            this.displayName = displayName;
            this.followers = followers;
            this.creationDate = (creationDate != null) ? parseCreationDate(creationDate) : null;
        }

        private LocalDateTime parseCreationDate(String creationDateString) {
            return LocalDateTime.parse(creationDateString, creationDateFormat)
                    .atOffset(ZoneOffset.UTC).toLocalDateTime();
        }

        public String getDisplayName() {
            return displayName;
        }

        public long getFollowers() {
            return followers;
        }

        public LocalDateTime getCreationDate() {
            return creationDate;
        }

        public String getCreationDataString() {
            return (creationDate != null) ? creationDate.format(outputDateFormat) : "Fecha no disponible";
        }
    }

}
