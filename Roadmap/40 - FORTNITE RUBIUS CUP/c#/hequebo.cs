using Newtonsoft.Json.Linq;
using System.Net.Http.Headers;

class Streamer
{
    public string? Id { get; set; }
    public string? Login { get; set; }
    public string? DisplayName { get; set; }
    public DateTime CreatedAt { get; set; }
    public int Followers {  get; set; }
}
class Twitch
{
    private string? _clientId;
    private string? _clientSecret;
    private HttpClient _httpClient = new HttpClient();

    public Twitch()
    {
        _clientId = Environment.GetEnvironmentVariable("CLIENT_ID");
        _clientSecret = Environment.GetEnvironmentVariable("CLIENT_SECRET");
        _httpClient.DefaultRequestHeaders.Add("client-id", _clientId);
    }

    public async Task<bool> GetToken()
    {
        if (string.IsNullOrWhiteSpace(_clientId) || string.IsNullOrEmpty(_clientSecret))
        {
            Console.WriteLine("No se cuenta con las credenciales necesarias...");
            return false;
        }
        string url = "https://id.twitch.tv/oauth2/token";

        var content = new Dictionary<string, string>
        {
            {"grant_type", "client_credentials"},
            {"client_id", _clientId},
            {"client_secret", _clientSecret}
        };


        var response = await _httpClient.PostAsync(url, new FormUrlEncodedContent(content));
        if (response.StatusCode != System.Net.HttpStatusCode.OK)
            return false;

        var jsonResponse = await response.Content.ReadAsStringAsync();
        string token = JObject.Parse(jsonResponse)["access_token"].ToString();

        _httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
        
        return true;
    }

    public async Task<Streamer?> GetUserInfo(string user)
    {
        string url = $"https://api.twitch.tv/helix/users?login={user}";

        var response = await _httpClient.GetAsync(url);
        if (response.StatusCode != System.Net.HttpStatusCode.OK)
            return null;

        var jsonResponse = await response.Content.ReadAsStringAsync();

        var objectResponse = JObject.Parse(jsonResponse);
        if (objectResponse["data"].Count() == 0)
            return null;
        var streamer = new Streamer();
        streamer.Id = objectResponse["data"][0]["id"].ToString();
        streamer.Login = objectResponse["data"][0]["login"].ToString();
        streamer.DisplayName = objectResponse["data"][0]["display_name"].ToString();
        streamer.CreatedAt = (DateTime)objectResponse["data"][0]["created_at"];

        return streamer;
    }
    public async Task<int> GetFollowers(string id)
    {
        string url = $"https://api.twitch.tv/helix/channels/followers?broadcaster_id={id}";

        var response = await _httpClient.GetAsync(url);
        if (response.StatusCode != System.Net.HttpStatusCode.OK)
            return 0;

        var jsonResponse = await response.Content.ReadAsStringAsync();

        var objectResponse = JObject.Parse(jsonResponse);

        int followers = (int)objectResponse["total"];

        return followers;
    }
}
class Program
{
    static async Task Main(string[] args)
    {

        Twitch twitch = new Twitch();
        
        bool authorized = await twitch.GetToken();
        if (!authorized)
        {
            Console.WriteLine("No ha sido posible obtener autorización...");
            return;
        }

        var users = new List<string>
        {
            "littleragergirl", "ache", "adricontreras4", "agustin51", "alexby11", "ampeterby7", "tvander",
            "arigameplays", "arigeli_", "auronplay", "axozer", "beniju03", "bycalitos",
            "byviruzz", "carreraaa", "celopan", "srcheeto", "crystalmolly", "darioemehache",
            "dheylo", "djmariio", "doble", "elvisayomastercard", "elyas360", "folagorlives", "thegrefg",
            "guanyar", "hika", "hiperop", "ibai", "ibelky_", "illojuan", "imantado",
            "irinaissaia", "jesskiu", "jopa", "jordiwild", "kenaivsouza", "mrkeroro10",
            "thekiddkeo95", "kikorivera", "knekro", "kokoop", "kronnozomberoficial", "leviathan",
            "litkillah", "lolalolita", "lolitofdez", "luh", "luzu", "mangel", "mayichi",
            "melo", "missasinfonia", "mixwell", "jaggerprincesa", "nategentile7", "nexxuz",
            "lakshartnia", "nilojeda", "nissaxter", "olliegamerz", "orslok", "outconsumer", "papigavitv",
            "paracetamor", "patica1999", "paulagonu", "pausenpaii", "perxitaa", "nosoyplex",
            "polispol1", "quackity", "recuerd0p", "reventxz", "rivers_gg", "robertpg", "roier",
            "ceuvebrokenheart", "rubius", "shadoune666", "silithur", "spok_sponha", "elspreen", "spursito",
            "bystaxx", "suzyroxx", "vicens", "vitu", "werlyb", "xavi", "xcry", "elxokas",
            "thezarcort", "zeling", "zormanworld", "mouredev"
        };
        var userDataList = new List<Streamer>();
        var notFoundList = new List<string>();
        foreach (var user in users)
        {
            var streamer = await twitch.GetUserInfo(user);
            if (streamer == null)
                notFoundList.Add(user);
            else
            {
                streamer.Followers = await twitch.GetFollowers(streamer.Id);
                userDataList.Add(streamer);
            }
        }

        var followersSortedList = userDataList.OrderByDescending(u => u.Followers).ToList();
        var dateSortedList = userDataList.OrderBy(u => u.CreatedAt).ToList();

        Console.WriteLine("----Ranking por número de seguidores----");
        foreach (var (user, id) in followersSortedList.Select((item, index) => (item, index)))
            Console.WriteLine($"{id + 1} {user.DisplayName} Seguidores: {user.Followers}");

        Console.WriteLine("----Ranking por antigüedad----");
        foreach (var (user, id) in dateSortedList.Select((item, index) => (item, index)))
            Console.WriteLine($"{id + 1} {user.DisplayName} Creado el {user.CreatedAt.ToShortDateString()}");

        if (notFoundList.Count > 0)
        {
            Console.WriteLine("----Usuarios no encontrados----");
            foreach (var user in notFoundList)
                Console.WriteLine(user);
        }
    }
}