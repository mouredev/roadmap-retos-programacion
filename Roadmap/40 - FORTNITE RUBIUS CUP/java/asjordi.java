import com.github.philippheuer.credentialmanager.domain.OAuth2Credential;
import com.github.twitch4j.ITwitchClient;
import com.github.twitch4j.TwitchClientBuilder;
import com.github.twitch4j.helix.domain.UserList;

import java.time.LocalDate;
import java.time.ZoneId;
import java.util.*;

public class asjordi {

    static String clientId = "";
    static String accessToken = "";

    static ITwitchClient twitchClient = TwitchClientBuilder.builder()
            .withDefaultAuthToken(new OAuth2Credential(clientId, accessToken))
            .withEnableHelix(true)
            .build();

    public static void main(String[] args) {
        List<Streamer> streamers = getStreamers();

        streamers.forEach(streamer -> streamer.setFollowers(getTotalFollowers(String.valueOf(streamer.getId()))));

        // sort by followers
        streamers.sort(Comparator.comparing(Streamer::getFollowers).reversed());
        System.out.println("Ranking by followers:");
        streamers.forEach(streamer -> System.out.println(streamer.getDisplayName() + " has " + streamer.getFollowers() + " followers"));

        // sort by joined date
        streamers.sort(Comparator.comparing(Streamer::getJoined));
        System.out.println("Ranking by joined date:");
        streamers.forEach(streamer -> System.out.println(streamer.getDisplayName() + " joined on " + streamer.getJoined()));
    }

    public static List<Streamer> getStreamers() {
        List<String> streamerNames = Arrays.asList(
                "littleragergirl", "ache", "adricontreras4", "agustin51", "alexby11", "ampeterby7", "tvander", "arigameplays", "arigeli_", "auronplay",
                "axozer", "beniju03", "bycalitos", "byviruzz", "carreraaa", "celopan", "srcheeto", "crystalmolly", "darioemehache", "dheylo",
                "djmariio", "doble", "elvisayomastercard", "elyas360", "folagorlives", "thegrefg", "guanyar", "hika", "hiperop", "ibai",
                "ibelky_", "illojuan", "imantado", "irinaisasia", "jesskiu", "jopa", "jordiwild", "kenaivsouza", "mrkeroro10", "thekiddkeo95",
                "kikorivera", "knekro", "a_big_koko", "kronnozomberoficial", "leviathan", "litkillah", "lolalolita", "lolitofdez", "luh", "luzu",
                "mangel", "mayichi", "melo", "missasinfonia", "mixwell", "jaggerprincesa", "nategentile7", "nexxuz", "lakshartnia", "nilojeda",
                "nissaxter", "olliegamerz", "orslok", "outconsumer", "papigavitv", "paracetamor", "patica1999", "paulagonu", "pausenpaii", "perxitaa",
                "nosoyplex", "polispol1", "quackity", "recuerd0p", "reventxz", "rivers_gg", "robertpg", "roier", "rojuu", "rubius",
                "shadoune666", "silithur", "spok_sponha", "elspreen", "spursito", "bystaxx", "suzyroxx", "vicens", "vitu", "werlyb",
                "xavi", "xcry", "elxokas", "thezarcort", "zeling", "zormanworld"
        );

        List<Streamer> streamers = new LinkedList<>();

        UserList resultList = twitchClient.getHelix().getUsers(null, null, streamerNames).execute();
        resultList.getUsers().forEach(user -> streamers.add(new Streamer(Long.parseLong(user.getId()), user.getLogin(), user.getDisplayName(), user.getCreatedAt().atZone(ZoneId.systemDefault()).toLocalDate())));

        return streamers;
    }

    public static int getTotalFollowers(String id) {
        var followers = twitchClient.getHelix().getChannelFollowers(accessToken, id, null, 100, null).execute();
        return followers.getTotal();
    }

    static class Streamer {
        private long id;
        private String login;
        private String displayName;
        private int followers;
        private LocalDate joined;

        public Streamer(long id, String login, String displayName, LocalDate joined) {
            this.id = id;
            this.login = login;
            this.displayName = displayName;
            this.joined = joined;
        }

        public long getId() {
            return id;
        }

        public String getLogin() {
            return login;
        }

        public String getDisplayName() {
            return displayName;
        }

        public int getFollowers() {
            return followers;
        }

        public LocalDate getJoined() {
            return joined;
        }

        public void setFollowers(int followers) {
            this.followers = followers;
        }

        @Override
        public String toString() {
            return new StringJoiner(", ", Streamer.class.getSimpleName() + "[", "]")
                    .add("id=" + id)
                    .add("login='" + login + "'")
                    .add("displayName='" + displayName + "'")
                    .add("followers=" + followers)
                    .add("joined=" + joined)
                    .toString();
        }
    }
}
