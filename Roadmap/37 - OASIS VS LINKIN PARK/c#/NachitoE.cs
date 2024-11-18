using System;
using System.Diagnostics.Metrics;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;
using System.Text.Json.Serialization;

/*
 * EJERCICIO:
 * ¡Dos de las bandas más grandes de la historia están de vuelta!
 * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
 * Desarrolla un programa que se conecte al API de Spotify y los compare.
 * Requisitos:
 * 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
 * 2. Conéctate al API utilizando tu lenguaje de programación.
 * 3. Recupera datos de los endpoint que tú quieras.
 * Acciones:
 * 1. Accede a las estadísticas de las dos bandas.
 *    Por ejemplo: número total de seguidores, escuchas mensuales,
 *    canción con más reproducciones...
 * 2. Compara los resultados de, por lo menos, 3 endpoint.
 * 3. Muestra todos los resultados por consola para notificar al usuario.
 * 4. Desarrolla un criterio para seleccionar qué banda es más popular.
 */

public class Program
{
    static async Task Main()
    {
        string clientId = Environment.GetEnvironmentVariable("SPOTIFY_CLIENT_ID");
        string clientSecret = Environment.GetEnvironmentVariable("SPOTIFY_CLIENT_SECRET");
        SpotifyAPI api = new SpotifyAPI(clientId, clientSecret);
        List<String> bandsIDs = new List<string>();
        List<String> defaultbandIDs = ["2DaxqgrOhkeH0fpeiQq2f4", "6XyY86QOPPrYVGvF9ch6wz"];
        string token = await api.GetAuthToken();
        if (token == "")
        {
            Console.WriteLine("Invalid Token. Check if ClientID and ClientSecret are correctly written.");
            return;
        }

        Console.WriteLine("Write your desired band ID and press Enter.\nIf you don't want to add any more bands, just press Enter.\nNOTE : By default this program will compare Linkin Park against Oasis.");
        Console.Write("Write your band ID (or just Enter if you want to go with Linking Park and Oasis): ");
        string newBandId = Console.ReadLine();
        while (newBandId != "" || bandsIDs.Count < 2)
        {
            newBandId = newBandId.Trim();
            if (newBandId == "" && bandsIDs.Count == 0) //Going with Linkin Park and Oasis
            {
                bandsIDs = defaultbandIDs;
                break;
            }
            else if (newBandId == "" && bandsIDs.Count > 1) break; //User has written more than 1 band
            else if (newBandId == "" && bandsIDs.Count == 1) Console.WriteLine("Please enter at least one more band before proceeding");

            if (bandsIDs.Contains(newBandId))
            {
                Console.WriteLine("You've already added that band. Please add another one.");
            }
            else
            {
                string? json = await api.GetArtistInfo(newBandId, token);
                if (json != null) bandsIDs.Add(newBandId);
                else Console.WriteLine("Invalid band ID. Please check for typos.");
            }


            Console.Write("Write your band ID");
            //If user has written more than 1 band, inform him that he can continue
            if (bandsIDs.Count > 1) Console.Write(" (or just Enter to proceed)");
            Console.Write(": ");

            newBandId = Console.ReadLine();
        }

        //We'll be storing the artists data here
        List<ArtistData> artistsData = new List<ArtistData>();

        foreach (string bandId in bandsIDs)
        {
            int accumPopularity = 0;

            //Get artist's name and number of followers
            string artistJsonString = await api.GetArtistInfo(bandId, token);
            Artist artist = JsonSerializer.Deserialize<Artist>(artistJsonString);

            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine($"\n~~~~~BAND: {artist.Name}~~~~~");
            Console.ForegroundColor = ConsoleColor.White;

            Console.WriteLine($"\n{artist.Name} has {artist.Followers.TotalFollowers} followers.");
            accumPopularity += ((int)(artist.Followers.TotalFollowers * 0.00001));

            //Get top tracks
            string topTracksJsonString = await api.GetTopTracksInfo(bandId, token);

            TopTracks topTracks = JsonSerializer.Deserialize<TopTracks>(topTracksJsonString);
            //Get Popularity of the last 10 tracks
            Console.WriteLine($"\nWriting Top 10 Tracks for {artist.Name}");
            int i = 0;
            foreach (TrackObject track in topTracks.trackObjects)
            {
                Console.WriteLine($"The track called {track.Name} has {track.Popularity} popularity");
                accumPopularity += track.Popularity;
                i++;
                if (i >= 10) break;
            }

            //Get Albums
            string AlbumsJsonString = await api.GetAlbumsInfo(bandId, token);

            Albums simplifiedAlbums = JsonSerializer.Deserialize<Albums>(AlbumsJsonString);
            List<Album> albums = new List<Album>();


            foreach (SimplifiedAlbumObject sAlbum in simplifiedAlbums.AlbumObjects)
            {
                //Get Albums from SimplifiedAlbumObject, append them to an array
                string albumJsonString = await api.GetAlbumInfo(sAlbum.Id, token);
                Album album = JsonSerializer.Deserialize<Album>(albumJsonString);


                albums.Add(album);
            }
            List<Album> sortedAlbums = albums.OrderByDescending(x => x.Popularity).ToList();


            Album? mostFamousAlbum = null;
            Console.WriteLine($"\nWriting Top 10 Albums for {artist.Name}");
            i = 0;
            foreach (Album album in sortedAlbums)
            {
                if (mostFamousAlbum == null || album.Popularity > mostFamousAlbum.Popularity) mostFamousAlbum = album;
                Console.WriteLine($"The album called {album.Name} has {album.Popularity} popularity");
                accumPopularity += album.Popularity;
                i++;
                if (i >= 10) break;
            }

            ArtistData artistData = new ArtistData(bandId, artist.Name, artist.Followers.TotalFollowers, accumPopularity, mostFamousAlbum.Name);
            artistsData.Add(artistData);
        }

        //Sort by popularity, pick the most famous one
        List<ArtistData> sortedArtists = artistsData.OrderByDescending(x => x.Popularity).ToList();
        ArtistData mostFamousArtist = sortedArtists.First();

        Console.WriteLine($"\nThe most famous artist is {mostFamousArtist.Name}! (https://open.spotify.com/artist/{mostFamousArtist.Id})\nHe has the incredible amount of {mostFamousArtist.Followers} followers and his current most famous album is {mostFamousArtist.MostFamousAlbumName}");
    }
}

public class SpotifyAPI
{
    const string APIURL = "https://accounts.spotify.com/api/token";
    private string _clientId;
    private string _clientSecret;
    HttpClient httpClient;

    public SpotifyAPI(string clientId, string clientSecret)
    {
        httpClient = new HttpClient();
        _clientId = clientId;
        _clientSecret = clientSecret;
    }

    public async Task<string?> GetArtistInfo(string artistId, string token)
    {
        //Create url
        var url = $"https://api.spotify.com/v1/artists/{artistId}";
        var rString = await GetJSONStringFromGETRequest(url, token);

        return rString;
    }

    public async Task<string?> GetTopTracksInfo(string artistId, string token)
    {
        var url = $"https://api.spotify.com/v1/artists/{artistId}/top-tracks";
        var rString = await GetJSONStringFromGETRequest(url, token);

        return rString;
    }
    public async Task<string?> GetAlbumsInfo(string artistId, string token)
    {
        var url = $"https://api.spotify.com/v1/artists/{artistId}/albums";
        var rString = await GetJSONStringFromGETRequest(url, token);

        return rString;
    }

    public async Task<string?> GetAlbumInfo(string artistId, string token)
    {
        var url = $"https://api.spotify.com/v1/albums/{artistId}";
        var rString = await GetJSONStringFromGETRequest(url, token);

        return rString;
    }

    public async Task<string?> GetJSONStringFromGETRequest(string url, string token)
    {
        //send GET request
        var r = await CreateGETRequestAtUrl(url, token);
        if (r == null) return null;

        //Make response "r" a String
        string responseStr = await r.Content.ReadAsStringAsync();
        return responseStr;
    }

    public async Task<HttpResponseMessage?> CreateGETRequestAtUrl(string url, string token)
    {
        //Set Headers
        httpClient.DefaultRequestHeaders.Clear();
        httpClient.DefaultRequestHeaders.Add("Authorization", $"Bearer {token}");
        HttpResponseMessage response = await httpClient.GetAsync(url);
        if (response.IsSuccessStatusCode)
        {
            return response;
        }
        return null;
    }

    public async Task<string> GetAuthToken()
    {
        //Format to Base64, grant_type to client_credentials
        string authHeader = Convert.ToBase64String(Encoding.UTF8.GetBytes($"{_clientId}:{_clientSecret}"));
        var requestKey = new List<KeyValuePair<string, string>>
    {
        new KeyValuePair<string, string>("grant_type", "client_credentials")
    };

        httpClient.DefaultRequestHeaders.Clear();
        httpClient.DefaultRequestHeaders.Add("Authorization", $"Basic {authHeader}");

        //Encode requestKey
        FormUrlEncodedContent content = new FormUrlEncodedContent(requestKey);

        HttpResponseMessage response = await httpClient.PostAsync(APIURL, content);
        if (response.IsSuccessStatusCode)
        {
            string responseStr = await response.Content.ReadAsStringAsync();
            Console.WriteLine(response.StatusCode);

            //Deserialize to dict
            var responseDict = JsonSerializer.Deserialize<Dictionary<string, object>>(responseStr);
            return responseDict["access_token"].ToString();
        }

        Console.WriteLine($"Error: {response.StatusCode}");
        return "";
    }
}


public class Artist
{
    [JsonPropertyName("name")]
    public string Name { get; set; }
    [JsonPropertyName("followers")]
    public Followers Followers { get; set; }
}

public class Followers
{
    [JsonPropertyName("total")]
    public int TotalFollowers { get; set; }
}

public class TopTracks
{
    [JsonPropertyName("tracks")]
    public TrackObject[] trackObjects { get; set; }
}

public class TrackObject
{
    [JsonPropertyName("name")]
    public string Name { get; set; }
    [JsonPropertyName("popularity")]
    public int Popularity { get; set; }
}

public class Albums
{
    [JsonPropertyName("items")]
    public SimplifiedAlbumObject[] AlbumObjects { get; set; }
}

public class SimplifiedAlbumObject
{
    [JsonPropertyName("id")]
    public string Id { get; set; }
}

public class Album
{
    [JsonPropertyName("name")]
    public string Name { get; set; }
    [JsonPropertyName("popularity")]
    public int Popularity { get; set; }
}

public class ArtistData
{
    public string Id;
    public string Name;
    public int Followers;
    public int Popularity;
    public string MostFamousAlbumName;

    public ArtistData(string id, string name, int followers, int popularity, string mostFamousAlbumName)
    {
        Id = id;
        Name = name;
        Followers = followers;
        Popularity = popularity;
        MostFamousAlbumName = mostFamousAlbumName;
    }
}