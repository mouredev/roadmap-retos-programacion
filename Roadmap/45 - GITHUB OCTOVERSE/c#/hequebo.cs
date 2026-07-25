using Newtonsoft.Json.Linq;
using System.Text.Json;

class User
{
    public string? Login { get; set; }
    private string? _company;
    public int Public_Repos { get; set; }
    public int Followers { get; set; }
    public int Following { get; set; }
    public string? Repos_Url { get; set; }
    public DateTime Created_At { get; set; }
    public List<Repository> Repos { get; set; }

    public string Company
    {
        get
        {
            return _company ?? "Ninguna";
        }
        set
        {
            _company = value;
        }
    }
}
class Repository
{
    public string Full_Name { get; set; }
    private string _language;
    public string Language
    {
        get
        {
            return _language ?? "Ninguno";
        }
        set
        {
            _language = value;
        }
    }
    public int Stargazers_Count {  get; set; }
    public int Forks_Count {  get; set; }
}
class GitHub
{
    private static HttpClient _httpClient = new HttpClient();
    public static async Task GenerateReport(string? username)
    {
        if (string.IsNullOrEmpty(username))
        {
            Console.WriteLine("No se ha ingresado ningún usuario...");
            return;
        }
        string url = $"https://api.github.com/users/{username}";
        _httpClient.DefaultRequestHeaders.UserAgent.TryParseAdd("request");
        var response = await _httpClient.GetAsync(url);
        if (!response.IsSuccessStatusCode)
        {
            Console.WriteLine($"El usuario {username} no ha sido encontrado...");
            return;
        }
        var jsonResponse = await response.Content.ReadAsStringAsync();
        JsonSerializerOptions options = new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true,
        };
        var user = JsonSerializer.Deserialize<User>(jsonResponse, options);

        Console.WriteLine($"------Reporte de usuario {username}------");
        Console.WriteLine($"Usuario: {user?.Login}");
        Console.WriteLine($"Compañia: {user?.Company}");
        Console.WriteLine($"Repositorios públicos: {user?.Public_Repos}");
        Console.WriteLine($"Seguidores: {user?.Followers}");
        Console.WriteLine($"Seguidos: {user.Following}");
        Console.WriteLine($"Fecha de creación: {user.Created_At.ToShortDateString()}");

        if (user.Public_Repos == 0)
            return;
        response = await _httpClient.GetAsync(user.Repos_Url);
        jsonResponse = await response.Content.ReadAsStringAsync();
        user.Repos = JsonSerializer.Deserialize<List<Repository>>(jsonResponse, options);

        var languages = new Dictionary<string, int>();
        Console.WriteLine($"------Repositorios de {user.Login}------");
        Console.WriteLine("-----------------------------------------");
        foreach (var repo in user.Repos)
        {
            Console.WriteLine($"Nombre del Repositorio: {repo.Full_Name}");
            Console.WriteLine($"Lenguaje: {repo.Language}");
            Console.WriteLine($"Estrellas: {repo.Stargazers_Count}");
            Console.WriteLine($"Forks: {repo.Forks_Count}");
            Console.WriteLine();
            Console.WriteLine("-----------------------------------------");

            if (!languages.ContainsKey(repo.Language) && repo.Language != "Ninguno")
                languages.Add(repo.Language, 1);
            else if (repo.Language != "Ninguno")
                languages[repo.Language] += 1;
        }

        int maxCount = languages.Max(l => l.Value);
        var mostUsedLanguages = languages.Where(l => l.Value == maxCount).Select(l => l.Key).ToList();
        
        if (mostUsedLanguages.Count > 1)
        {
            Console.WriteLine($"Los lenguajes más utilizados por {user.Login} son:");
            foreach(var language in mostUsedLanguages)
            {
                Console.WriteLine(language);
            }
        }
        else
        {
            Console.WriteLine($"El lenguaje más utilizado por {user.Login} es: {mostUsedLanguages[0]}");
        }
    }
}

class Program
{
    static async Task Main(string[] args)
    {
        Console.WriteLine("------Reporte de Usuario de Github------");
        Console.WriteLine("Ingresa el nombre del usuario que quieres consultar");
        string? userName = Console.ReadLine();
        await GitHub.GenerateReport(userName);
    }
}