namespace exs40;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
40 FORTNITE RUBIUS CUP
------------------------------------

* EJERCICIO:
* ¡Rubius tiene su propia skin en Fortnite!
* Y va a organizar una competición para celebrarlo.
* Esta es la lista de participantes:
* https://x.com/Rubiu5/status/1840161450154692876
*
* Desarrolla un programa que obtenga el número de seguidores en
* Twitch de cada participante, la fecha de creación de la cuenta 
* y ordene los resultados en dos listados.
* - Usa el API de Twitch: https://dev.twitch.tv/docs/api/reference
*   (NO subas las credenciales de autenticación)
* - Crea un ranking por número de seguidores y por antigüedad.
* - Si algún participante no tiene usuario en Twitch, debe reflejarlo.
*/

using System.Net.Http;
using System.Text.Json;
// https://www.nuget.org/packages/DotNetEnv/
using DotNetEnv;

public class Twitch(string clientId, string clientSecret)
{
    private readonly string clientId = clientId;
    private readonly string clientSecret = clientSecret;
    private string? accessToken;

    public class UserData
    {
        public required string Username { get; set; }
        public DateTime CreatedAt { get; set; }
        public int Followers { get; set; }
    }

    private async Task EnsureAccessTokenAsync()
    {
        if (string.IsNullOrEmpty(accessToken))
        {
            using var client = new HttpClient();
            var tokenContent = new FormUrlEncodedContent(new Dictionary<string, string>
            {
                { "client_id", clientId },
                { "client_secret", clientSecret },
                { "grant_type", "client_credentials" }
            });

            var tokenResponse = await client.PostAsync("https://id.twitch.tv/oauth2/token", tokenContent);

            if (!tokenResponse.IsSuccessStatusCode)
            {
                throw new Exception($"Error al obtener el token: {tokenResponse.StatusCode}");
            }

            var tokenJson = await tokenResponse.Content.ReadAsStringAsync();
            var tokenData = JsonSerializer.Deserialize<JsonElement>(tokenJson);
            accessToken = tokenData.GetProperty("access_token").GetString();
        }
    }

    private static async Task<int> GetFollowers(HttpClient client, string? idUser)
    {
        var response = await client.GetAsync($"https://api.twitch.tv/helix/channels/followers?broadcaster_id={idUser}");
        var json = await response.Content.ReadAsStringAsync();
        var data = JsonSerializer.Deserialize<JsonElement>(json);
        var total = data.GetProperty("total").GetInt32();
        return total;
    }

    private async Task<UserData?> GetUserData(string userName)
    {
        await EnsureAccessTokenAsync();

        using var client = new HttpClient();
        client.DefaultRequestHeaders.Add("Client-Id", clientId);
        client.DefaultRequestHeaders.Add("Authorization", $"Bearer {accessToken}");

        var response = await client.GetAsync($"https://api.twitch.tv/helix/users?login={userName}");
        var json = await response.Content.ReadAsStringAsync();
        var data = JsonSerializer.Deserialize<JsonElement>(json);
        if (data.GetProperty("data").EnumerateArray().Any())
        {
            var dt = data.GetProperty("data")[0];
            var idUser = dt.GetProperty("id").GetString();
            var createdAtString = dt.GetProperty("created_at").GetString();

            if (createdAtString != null)
            {
                var createdAt = DateTime.Parse(createdAtString);
                var totalFolowers = await GetFollowers(client, idUser);

                return new UserData
                {
                    Username = userName,
                    CreatedAt = createdAt,
                    Followers = totalFolowers
                };
            }
        }
        return null;
    }

    public class Program
    {
        private static void PrintRankings(List<UserData> usersData)
        {
            var byFollowers = usersData.OrderByDescending(x => x.Followers).ToList();
            var byDate = usersData.OrderBy(x => x.CreatedAt).ToList();

            Console.WriteLine("\nRanking por número de seguidores:");
            for (int i = 0; i < byFollowers.Count; i++)
            {
                Console.WriteLine($"{i + 1} - {byFollowers[i].Username}: {byFollowers[i].Followers:N0} seguidores");
            }

            Console.WriteLine("\nRanking por antigüedad:");
            for (int i = 0; i < byDate.Count; i++)
            {
                Console.WriteLine($"{i + 1} - {byDate[i].Username}: Creado el {byDate[i].CreatedAt:dd/MM/yyyy}");
            }
        }

        public static async Task ProcessUsers(List<string> users, Twitch Tw)
        {

            var usersData = new List<UserData>();
            var notFoundUsers = new List<string>();

            Console.WriteLine("Obteniendo datos...");

            foreach (var name in users)
            {
                var userData = await Tw.GetUserData(name);
                if (userData != null)
                {
                    usersData.Add(userData);
                }
                else
                {
                    notFoundUsers.Add(name);
                }
            }

            PrintRankings(usersData);

            if (notFoundUsers.Count != 0)
            {
                Console.WriteLine("\nUsuarios no encontrados:");
                foreach (var user in notFoundUsers)
                {
                    Console.WriteLine(user);
                }
            }
        }
    }

    public static async Task Main()
    {
        Env.Load();
        string clientId = Environment.GetEnvironmentVariable("TWITCH_CLIENT_ID") ?? "defaultClientId";
        string clientSecret = Environment.GetEnvironmentVariable("TWITCH_CLIENT_SECRET") ?? "defaultClientSecret";
        var Tw = new Twitch(clientId, clientSecret);

        var users = new List<string>
        {
            "abby", "ache", "adricontreras", "agustin", "alexby", "ampeter", "ander", "arigameplays",
            "arigeli", "auronplay", "axozer", "beniju", "bycalitos", "byviruzz", "carrera", "celopan",
            "cheeto", "crystalmolly", "darioemehache", "dheyo",
            "djmario", "doble", "elvisa", "elyas360", "folagor", "grefg", "guanyar", "hika",
            "hiper", "ibai", "ibelky", "illojuan", "imantado", "irinaisasia", "jesskiu", "jopa",
            "jordiwild", "kenaisouza", "keroro", "kiddkeo",
            "kikorivera", "knekro", "koko", "kronnozomber", "leviathan", "litkillah", "lolalolita", "lolito",
            "luh", "luzu", "mangel", "mayichi", "melo", "missasinonia", "mixwell", "mrjagger",
            "nategentile", "nexxuz", "nia", "nilojeda",
            "nissaxter", "ollie", "orslok", "outconsumer", "papigavi", "paracetamor", "patica", "paulagonu",
            "pausenpaii", "perxitaa", "plex", "polispol", "quackity", "recuerdop", "reven", "rivers",
            "robertpg", "roier", "rojuu", "rubius",
            "shadoune", "silithur", "spoksponha", "spreen", "spursito", "staxx", "suzyroxx", "vicens",
            "vituber", "werlyb", "xavi", "xcry", "xokas", "zarcort", "zeling", "zorman"
        };

        await Program.ProcessUsers(users, Tw);
    }
}
