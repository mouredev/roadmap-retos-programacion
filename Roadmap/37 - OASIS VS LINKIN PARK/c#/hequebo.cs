using Newtonsoft.Json.Linq;
using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

class Artist
{
    public string? Id { get; set; }
    public string? Name { get; set; }
    public List<string>? Genres { get; set; }
    public int Popularity { get; set; }
    public int Followers { get; set; }
    public int Points {  get; set; }
    public TopTrack TopTrack { get; set; }
    public Artist()
    {
        Genres = new List<string>(); 
        Points = 0;
    }
}
class TopTrack
{
    public string Id { get; set; }
    public string Name { get; set; }
    public int Popularity { get; set; }
}

class Spotify
{
    private string? _clientId = Environment.GetEnvironmentVariable("CLIENT_ID");
    private string? _clientSecret = Environment.GetEnvironmentVariable("CLIENT_SECRET");
    public async Task<string> GetToken(HttpClient httpClient)
    {
        if (string.IsNullOrEmpty(_clientId) || string.IsNullOrEmpty(_clientSecret))
        {
            await Console.Out.WriteLineAsync("No se cuenta con las credenciales necesarias...");
            return "";
        }
        var content = new Dictionary<string, string>
        {
            { "grant_type", "client_credentials" }
        };
        httpClient.BaseAddress = new Uri("https://accounts.spotify.com/api");
        var authenticationString = Encoding.ASCII.GetBytes($"{_clientId}:{_clientSecret}");
        httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Basic", Convert.ToBase64String(authenticationString));

        var response = await httpClient.PostAsync($"{httpClient.BaseAddress}/token", new FormUrlEncodedContent(content));

        if (response.StatusCode != System.Net.HttpStatusCode.OK)
            return "";

        var jsonResponse = await response.Content.ReadAsStringAsync();
        string token = JObject.Parse(jsonResponse)["access_token"].ToString();

        return token;
    }

    public async Task<string> SearchArtist(HttpClient httpClient, string name, string token)
    {
        var url = $"https://api.spotify.com/v1/search?q={name}&type=artist&limit=1";

        httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

        var response = await httpClient.GetAsync(new Uri(url));
        if (response.StatusCode != System.Net.HttpStatusCode.OK)
        {
            return "";
        }

        var jsonResponse = await response.Content.ReadAsStringAsync();
        var resultObject = JObject.Parse(jsonResponse);
        var artist = resultObject["artists"];
        var item = artist["items"][0];
        return item["id"].ToString();
    }

    public async Task<Artist> GetArtist(string id, HttpClient httpClient, string token)
    {
        var url = $"https://api.spotify.com/v1/artists/{id}";

        httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

        var response = await httpClient.GetAsync(new Uri(url));
        if (response.StatusCode != System.Net.HttpStatusCode.OK)
        {
            return null;
        }
        var jsonResponse = await response.Content.ReadAsStringAsync();
        var resultObject = JObject.Parse(jsonResponse);

        var artist = new Artist();
        artist.Id = id;
        artist.Name = resultObject["name"].ToString();
        foreach (string genre in resultObject["genres"])
            artist.Genres.Add(genre);
        artist.Popularity = (int)resultObject["popularity"];
        artist.Followers = (int)resultObject["followers"]["total"];

        return artist;
    }

    public async Task<TopTrack> GetTopTrack(string id, HttpClient httpClient, string token)
    {
        var url = $"https://api.spotify.com/v1/artists/{id}/top-tracks";
        httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

        var response = await httpClient.GetAsync(new Uri(url));
        if (response.StatusCode != System.Net.HttpStatusCode.OK)
        {
            return null;
        }
        var jsonResponse = await response.Content.ReadAsStringAsync();

        var resultObject = JObject.Parse(jsonResponse);
        var tracks = new List<TopTrack>();

        foreach(var item in resultObject["tracks"])
        {
            var track = new TopTrack();
            track.Id = item["id"].ToString();
            track.Name = item["name"].ToString();
            track.Popularity = (int)item["popularity"];
            tracks.Add(track);
        }
        var maxPoularity = tracks.Max(track => track.Popularity);
        var topTrack = tracks.Where(t => t.Popularity == maxPoularity).FirstOrDefault();

        return topTrack;
    }

}
class Program
{
    private static HttpClient _httpClient = new HttpClient();
    static async Task Main(string[] args)
    {
        var spotify = new Spotify();
        string token = await spotify.GetToken(_httpClient);
        Console.WriteLine("---Enfrentamiento de Artistas---");
        Console.WriteLine("Ingresa el nombre del primera artista");
        string artist1Name = Console.ReadLine();


        string artist1Id = await spotify.SearchArtist(_httpClient, artist1Name, token);

        if (artist1Id == "")
        {
            Console.WriteLine($"No se ha encontrado información del artista {artist1Name}...");
            return;
        }
        
        var artist1 = await spotify.GetArtist(artist1Id, _httpClient, token);

        Console.WriteLine("Ingresa el nombre del segundo artista");
        string artist2Name = Console.ReadLine();


        string artist2Id = await spotify.SearchArtist(_httpClient, artist2Name, token);

        if (artist2Id == "")
        {
            Console.WriteLine($"No se ha encontrado información del artista {artist2Name}...");
            return;
        }

        var artist2 = await spotify.GetArtist(artist2Id, _httpClient, token);

        Console.WriteLine($"{artist1.Name} VS {artist2.Name}");
        Console.WriteLine("---Seguidores---");
        Console.WriteLine($"{artist1.Name}: {artist1.Followers}\t{artist2.Name}:{artist2.Followers}");
        if (artist1.Followers > artist2.Followers)
        {
            Console.WriteLine($"{artist1.Name} supera a {artist2.Name} en seguidores con un total de " +
                $"{artist1.Followers} seguidores en Spotify...");
            artist1.Points++;
        }
        else if (artist1.Followers == artist2.Followers)
        {
            Console.WriteLine($"{artist1.Name} y {artist2.Name} empatan este round con " +
                $"{artist1.Followers} cada uno");
        }
        else
        {
            Console.WriteLine($"{artist2.Name} gana este round con un total de {artist2.Followers}");
            artist2.Points++;
        }
        Console.WriteLine("---Popularidad---");
        Console.WriteLine($"{artist1.Name}: {artist1.Popularity}\t{artist2.Name}: {artist2.Popularity}");
        if (artist1.Popularity > artist2.Popularity)
        {
            Console.WriteLine($"{artist1.Name} gana el round de popularidad");
            artist1.Points++;
        }
        else if (artist1.Popularity == artist2.Popularity)
        {
            Console.WriteLine($"{artist1.Name} y {artist2.Name} empatan este round");
            artist1.Points++;
            artist2.Points++;
        }
        else
        {
            Console.WriteLine($"{artist2.Name} supera a {artist1.Name} en popularidad");
            artist2.Points++;
        }

        artist1.TopTrack = await spotify.GetTopTrack(artist1.Id, _httpClient, token);
        artist2.TopTrack = await spotify.GetTopTrack(artist2.Id, _httpClient, token);

        Console.WriteLine("---Canciones más populares---");
        Console.WriteLine($"{artist1.Name}.- {artist1.TopTrack.Name}: {artist1.TopTrack.Popularity}");
        Console.WriteLine($"{artist2.Name}.- {artist2.TopTrack.Name}: {artist2.TopTrack.Popularity}");
        
        if (artist1.TopTrack.Popularity > artist2.TopTrack.Popularity)
        {
            Console.WriteLine($"{artist1.Name} gana este round con {artist1.TopTrack.Name}");
            artist1.Points++;
        }
        else if (artist1.TopTrack.Popularity  == artist2.TopTrack.Popularity)
        {
            Console.WriteLine($"Las canciones {artist1.TopTrack.Name} y {artist2.TopTrack.Name} " +
                $"están empatadas en cuanto popularidad");
            artist1.Points++;
            artist2.Points++;
        }
        else
        {
            Console.WriteLine($"{artist2.Name} supera a {artist1.Name} con {artist2.TopTrack.Name}");
            artist2.Points++;
        }

        Console.WriteLine("---RESULTADOS---");
        if (artist1.Points > artist2.Points)
            Console.WriteLine($"{artist1.Name} es el ganador de esta batalla");
        else if (artist1.Points == artist2.Points)
            Console.WriteLine($"{artist1.Name} y {artist2.Name} han empatado");
        else
            Console.WriteLine($"{artist2.Name} se lleva la victoria");
    }

}
