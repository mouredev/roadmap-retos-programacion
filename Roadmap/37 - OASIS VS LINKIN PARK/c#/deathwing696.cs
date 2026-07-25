using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json.Linq;
using System.Configuration;

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

namespace Reto_37
{
    internal class deathwing696
    {
        public class Spotify
        {
            private string urlAPI = "https://api.spotify.com/v1/";
            private string urlApiToken = "https://accounts.spotify.com/api/token";
            private static string clientId = ConfigurationManager.AppSettings["SpotifyClientId"];
            private static string clientSecret = ConfigurationManager.AppSettings["SpotifyClientSecret"];
            private string artist1;
            private string artist2;
            private int artist1Points = 0;
            private int artist2Points = 0;

            public Spotify(string artist1, string artist2)
            {
                this.artist1 = artist1;
                this.artist2 = artist2;
            }

            internal async Task<string> GetSpotifyAccessToken()
            {
                using (var client = new HttpClient())
                {
                    var request = new HttpRequestMessage(HttpMethod.Post, urlApiToken);
                    var clientCredentials = Convert.ToBase64String(Encoding.UTF8.GetBytes($"{clientId}:{clientSecret}"));

                    request.Headers.Authorization = new AuthenticationHeaderValue("Basic", clientCredentials);
                    request.Content = new StringContent("grant_type=client_credentials", Encoding.UTF8, "application/x-www-form-urlencoded");

                    var response = await client.SendAsync(request);
                    response.EnsureSuccessStatusCode();

                    var responseBody = await response.Content.ReadAsStringAsync();
                    var json = JObject.Parse(responseBody);

                    return json["access_token"].ToString();
                }
            }

            internal async Task CompareArtists(string token)
            {
                var artist1Data = await GetArtistData(token, artist1);
                var artist2Data = await GetArtistData(token, artist2);

                Console.WriteLine($"Artista: {artist1Data.Name}");
                Console.WriteLine($"Seguidores: {artist1Data.Followers}");
                Console.WriteLine($"Popularidad: {artist1Data.Popularity}");
                Console.WriteLine($"Canción más popular: {artist1Data.TopTrack} con {artist1Data.TopTrackPopularity} de popularidad");
                Console.WriteLine();

                Console.WriteLine($"Artista: {artist2Data.Name}");
                Console.WriteLine($"Seguidores: {artist2Data.Followers}");
                Console.WriteLine($"Popularidad: {artist2Data.Popularity}");
                Console.WriteLine($"Canción más popular: {artist2Data.TopTrack} con {artist2Data.TopTrackPopularity} de popularidad");
                Console.WriteLine();

                // Comparación
                Console.WriteLine("Comparación:");
                string moreFollowers;

                if (artist1Data.Followers > artist2Data.Followers)
                {
                    moreFollowers = artist1Data.Name;
                    artist1Points++;
                }
                else 
                {
                    moreFollowers = artist2Data.Name;
                    artist2Points++;
                }
                Console.WriteLine($"Artista con más seguidores: {moreFollowers}");

                string morePopular;
                if (artist1Data.Popularity > artist2Data.Popularity)
                {
                    morePopular = artist1Data.Name;
                    artist1Points++;
                }
                else
                {
                    morePopular = artist2Data.Name;
                    artist2Points++;
                }
                Console.WriteLine($"Artista más popular: {morePopular}");

                string topTrack, artistTopTrack;
                if (artist1Data.TopTrackPopularity > artist2Data.TopTrackPopularity)
                {
                    topTrack = artist1Data.TopTrack;
                    artistTopTrack = artist1Data.Name;
                    artist1Points++;
                }
                else
                {
                    topTrack = artist2Data.TopTrack;
                    artistTopTrack = artist2Data.Name;
                    artist2Points++;
                }
                Console.WriteLine($"Canción con más popularidad: {topTrack} de {artistTopTrack}");

                Console.WriteLine("PUNTUACIÓN FINAL:");
                
                if (artist1Points > artist2Points)
                {
                    Console.WriteLine($"El ganador de este duelo es {artist1Data.Name} con {artist1Points} puntos");
                }
                else if (artist2Points > artist1Points)
                {
                    Console.WriteLine($"El ganador de este duelo es {artist2Data.Name} con {artist2Points} puntos");
                }
                else
                {
                    Console.WriteLine($"Ha habido un empate en el duelo entre {artist1Data.Name} y {artist2Data.Name} con {artist1Points} puntos");
                }
            }

            private async Task<(string Name, int Followers, int Popularity, string TopTrack, int TopTrackPopularity)> GetArtistData(string token, string artistName)
            {
                using (var client = new HttpClient())
                {
                    client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);

                    // Buscar al artista
                    var searchResponse = await client.GetAsync($"{urlAPI}search?q={Uri.EscapeDataString(artistName)}&type=artist");
                    searchResponse.EnsureSuccessStatusCode();
                    var searchResult = JObject.Parse(await searchResponse.Content.ReadAsStringAsync());

                    var artist = searchResult["artists"]["items"].First;
                    string artistId = artist["id"].ToString();
                    string name = artist["name"].ToString();
                    int followers = (int)artist["followers"]["total"];
                    int popularity = (int)artist["popularity"];

                    // Obtener las canciones más populares
                    var tracksResponse = await client.GetAsync($"{urlAPI}artists/{artistId}/top-tracks?market=US");
                    tracksResponse.EnsureSuccessStatusCode();
                    var tracksResult = JObject.Parse(await tracksResponse.Content.ReadAsStringAsync());

                    var topTrack = tracksResult["tracks"].First;
                    string topTrackName = topTrack["name"].ToString();
                    int topTrackPopularity = (int)topTrack["popularity"];

                    return (name, followers, popularity, topTrackName, topTrackPopularity);
                }
            }
        }

        static async Task Main(string[] args)
        {
            Spotify spotify = new Spotify("Oasis", "Linkin Park");

            string token = await spotify.GetSpotifyAccessToken();

            await spotify.CompareArtists(token);            

            Console.ReadKey();
        }
    }
}
