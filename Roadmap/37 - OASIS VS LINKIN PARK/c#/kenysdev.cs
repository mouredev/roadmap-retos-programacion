namespace exs37;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
OASIS VS LINKIN PARK
------------------------------------
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


using System.Linq;
using System.Threading.Tasks;

// https://www.nuget.org/packages/SpotifyAPI.Web/
// https://johnnycrazy.github.io/SpotifyAPI-NET/docs/introduction
using SpotifyAPI.Web;

// https://www.nuget.org/packages/DotNetEnv/
using DotNetEnv;

public class Spotify
{
    private readonly SpotifyClient _spotify;

    public Spotify()
    {
        Env.Load();
        var clientId = Environment.GetEnvironmentVariable("SPOTIFY_CLIENT_ID");
        var clientSecret = Environment.GetEnvironmentVariable("SPOTIFY_CLIENT_SECRET");

        if (string.IsNullOrEmpty(clientId) || string.IsNullOrEmpty(clientSecret))
        {
            throw new ArgumentException("Se debe proporcionar 'CLIENT_ID' y 'CLIENT_SECRET'.");
        }

        var config = SpotifyClientConfig
            .CreateDefault()
            .WithAuthenticator(new ClientCredentialsAuthenticator(clientId, clientSecret));

        _spotify = new SpotifyClient(config);
    }

    public async Task<SearchResponse> GetArtistsAsync(string name)
    {
        var searchRequest = new SearchRequest(SearchRequest.Types.Artist, name)
        {
            Limit = 3
        };
        return await _spotify.Search.Item(searchRequest);
    }

    public async Task<FullArtist?> GetMostPopularArtistAsync(string name)
    {
        var searchResult = await GetArtistsAsync(name);

        if (searchResult?.Artists?.Items == null || searchResult.Artists.Items.Count == 0)
        {
            return null;
        }

        var mostPopularArtist = searchResult.Artists.Items
            .OrderByDescending(artist => artist.Popularity)
            .FirstOrDefault();

        return mostPopularArtist;
    }

    public async Task<ArtistsTopTracksResponse> ArtistTopTracksAsync(string artistId)
    {
        return await _spotify.Artists.GetTopTracks(artistId, new ArtistsTopTracksRequest("US"));
    }

}

public class Versus(FullArtist artist1, FullArtist artist2, Spotify spotifyInstance)
{
    private readonly FullArtist _artist1 = artist1;
    private readonly FullArtist _artist2 = artist2;
    private readonly Spotify _spotify = spotifyInstance;
    private int _artist1Score = 0;
    private int _artist2Score = 0;

    private Task Popularity()
    {
        if (_artist1 == null || _artist2 == null)
        {
            Console.WriteLine("Uno o ambos artistas no están disponibles.");
            return Task.CompletedTask;
        }

        int a1Pop = _artist1.Popularity;
        int a2Pop = _artist2.Popularity;

        Console.WriteLine($"Popularidad: {a1Pop} vs {a2Pop}");
        if (a1Pop > a2Pop)
        {
            _artist1Score++;
        }
        else if (a2Pop > a1Pop)
        {
            _artist2Score++;
        }

        return Task.CompletedTask;
    }

    private Task Followers()
    {
        if (_artist1 == null || _artist2 == null)
        {
            Console.WriteLine("Uno o ambos artistas no están disponibles.");
            return Task.CompletedTask;
        }

        int a1Foll = _artist1.Followers.Total;
        int a2Foll = _artist2.Followers.Total;

        Console.WriteLine($"Seguidores: {a1Foll} vs {a2Foll}");
        if (a1Foll > a2Foll)
        {
            _artist1Score++;
        }
        else if (a2Foll > a1Foll)
        {
            _artist2Score++;
        }

        return Task.CompletedTask;
    }

    private async Task Top3TracksAsync()
    {
        if (_artist1 == null || _artist2 == null)
        {
            Console.WriteLine("Uno o ambos artistas no están disponibles.");
            return;
        }

        var a1Top = await _spotify.ArtistTopTracksAsync(_artist1.Id);
        var a2Top = await _spotify.ArtistTopTracksAsync(_artist2.Id);

        int a1Pop = a1Top.Tracks.Take(3).Sum(track => track.Popularity);
        int a2Pop = a2Top.Tracks.Take(3).Sum(track => track.Popularity);

        Console.WriteLine($"Popularidad Top 3 canciones: {a1Pop} vs {a2Pop}");
        if (a1Pop > a2Pop)
        {
            _artist1Score++;
        }
        else if (a2Pop > a1Pop)
        {
            _artist2Score++;
        }
    }

    private void FinalResult()
    {
        Console.WriteLine("\nRESULTADO FINAL:");
        Console.WriteLine($"{_artist1.Name}: {_artist1Score} puntos");
        Console.WriteLine($"{_artist2.Name}: {_artist2Score} puntos");

        if (_artist1Score > _artist2Score)
        {
            Console.WriteLine($"\n¡'{_artist1.Name}' gana el versus!");
        }
        else if (_artist2Score > _artist1Score)
        {
            Console.WriteLine($"\n¡'{_artist2.Name}' gana el versus!");
        }
        else
        {
            Console.WriteLine("\n¡Es un empate!");
        }
    }

    public async Task StartAsync()
    {
        Console.WriteLine($"{_artist1.Name} vs {_artist2.Name}");
        await Popularity();
        await Followers();
        await Top3TracksAsync();
        FinalResult();
    }
}

public class Program
{
    public static async Task Main()
    {
        Console.WriteLine("VERSUS");
        var spotify = new Spotify();

        var artist1 = await spotify.GetMostPopularArtistAsync("Oasis");
        var artist2 = await spotify.GetMostPopularArtistAsync("Linkin Park");

        if (artist1 == null || artist2 == null)
        {
            Console.WriteLine("Artistas no encontrados");
            return;
        }

        var versus = new Versus(artist1, artist2, spotify);
        await versus.StartAsync();
    }
}
