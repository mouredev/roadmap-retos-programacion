package com.amsoft.roadmap.example37;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.Comparator;
import java.util.Objects;

record Artist(String name,int followers,int popularity){}
record Track(String name,int duration,int popularity){}

public class Example37 {
    public static void main(String[] args) {

        String token = getToken();
        var idArtist1 = searchArtist(token, "Oasis");
        var idArtist2 = searchArtist(token, "The Beatles");
        Artist artist1 = getArtistData(token, idArtist1);
        Artist artist2 = getArtistData(token, idArtist2);
        Track topTrack1 = getTopTrack(token, idArtist1);
        Track topTrack2 = getTopTrack(token, idArtist2);
        if(artist1 == null || artist2 == null || topTrack1 == null || topTrack2 == null){
            System.out.println("Error getting data");
            return;
        }

        String winnerPopularity = artist1.popularity() > artist2.popularity() ? artist1.name() : artist2.name();
        String winnerFollowers = artist1.followers() > artist2.followers() ? artist1.name() : artist2.name();
        String winnerTrack = topTrack1.popularity() > topTrack2.popularity() ? artist1.name() : artist2.name();

        System.out.println("----------------------Results----------------------");
        System.out.println("Variable\t | Artist1\t | Artist2 \t |winner");
        System.out.println("Name\t\t |" + artist1.name() + "\t\t |" + artist2.name() + "|");
        System.out.println("Followers\t |" + artist1.followers() + "\t |" + artist2.followers() + "\t |" + winnerPopularity);
        System.out.println("Popularity\t |" + artist1.popularity() + "\t\t |" + artist2.popularity() + "\t\t |" + winnerFollowers);
        System.out.println("Top Track\t |" + topTrack1.popularity() + "\t\t |" + topTrack2.popularity() + "\t\t |" + winnerTrack);
    }

    public static String getToken() {
        HttpClient client = HttpClient.newHttpClient();
        String grantType = "client_credentials";
        String clientId = System.getenv("SPOTIFY_CLIENT_ID");
        String clientSecret = System.getenv("SPOTIFY_CLIENT_SECRET");
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://accounts.spotify.com/api/token"))
                .headers("Content-Type", "application/x-www-form-urlencoded")
                .method("POST", HttpRequest.BodyPublishers.ofString("grant_type=" + grantType + "&client_id=" + clientId + "&client_secret=" + clientSecret))
                .build();
        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            JsonObject json = JsonParser.parseString(response.body()).getAsJsonObject();


            return json.get("access_token").getAsString();
        } catch (Exception e) {
            e.printStackTrace(System.out);
            return null;
        }
    }

    public static String searchArtist(String token, String artist) {
        String artistName = URLEncoder.encode(artist, StandardCharsets.UTF_8);
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://api.spotify.com/v1/search?q=" + artistName + "&type=artist&limit=1"))
                .headers("Authorization", "Bearer " + token)
                .build();
        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            var itemsFound = JsonParser.parseString(response.body()).getAsJsonObject().get("artists").getAsJsonObject().get("items").getAsJsonArray();
            if (itemsFound.size() <= 0){
                throw new Exception("No artist found");
            }
            return itemsFound.get(0).getAsJsonObject().get("id").getAsString();
        } catch (Exception e) {
            e.printStackTrace(System.out);
            return null;
        }
    }
    public static Artist getArtistData(String token, String artistId) {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://api.spotify.com/v1/artists/" + artistId))
                .headers("Authorization", "Bearer " + token)
                .build();
        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            if(response.statusCode() != 200){
                throw new Exception("Error getting artist data");
            }
            JsonObject artist = JsonParser.parseString(response.body()).getAsJsonObject();
            String name = artist.get("name").getAsString();
            int followers = artist.get("followers").getAsJsonObject().get("total").getAsInt();
            int popularity = artist.get("popularity").getAsInt();
            return new Artist(name,followers,popularity);
        } catch (Exception e) {
            e.printStackTrace(System.out);
            return null;
        }
    }

    public static Track getTopTrack(String token, String artistId) {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://api.spotify.com/v1/artists/" + artistId + "/top-tracks"))
                .headers("Authorization", "Bearer " + token)
                .build();
        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            if(response.statusCode() != 200){
                throw new Exception("Error getting top track");
            }
            var tracks = JsonParser.parseString(response.body()).getAsJsonObject().get("tracks").getAsJsonArray();
            if (tracks.size() <= 0){
                throw new Exception("No tracks found");
            }
            //order by popularity
            JsonObject topTrack = Objects.requireNonNull(tracks.asList().stream()
                    .max(Comparator.comparingInt(a -> a.getAsJsonObject().get("popularity").getAsInt()))
                    .orElseThrow()).getAsJsonObject();
            String name = topTrack.get("name").getAsString();
            int duration = topTrack.get("duration_ms").getAsInt();
            int popularity = topTrack.get("popularity").getAsInt();
            return new Track(name,duration,popularity);
        } catch (Exception e) {
            e.printStackTrace(System.out);
            return null;
        }
    }
}
