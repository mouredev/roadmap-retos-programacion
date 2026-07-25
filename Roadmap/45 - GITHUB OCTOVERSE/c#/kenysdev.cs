namespace exs44;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
45 GITHUB OCTOVERSE
------------------------------------

 * EJERCICIO:
 * GitHub ha publicado el Octoverse 2024, el informe
 * anual del estado de la plataforma:
 * https://octoverse.github.com
 *
 * Utilizando el API de GitHub, crea un informe asociado
 * a un usuario concreto.
 * 
 * - Se debe poder definir el nombre del usuario
 *   sobre el que se va a generar el informe.
 *   
 * - Crea un informe de usuario basándote en las 5 métricas
 *   que tú quieras, utilizando la informración que te
 *   proporciona GitHub. Por ejemplo:
 *   - Lenguaje más utilizado
 *   - Cantidad de repositorios
 *   - Seguidores/Seguidos
 *   - Stars/forks
 *   - Contribuciones
 *   (lo que se te ocurra)
*/
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.Json;
using System.Linq;
using System.Threading.Tasks;

public class GitHubApi
{
    private readonly HttpClient _client = new();
    private readonly Dictionary<string, JsonElement> _userData;

    public GitHubApi(string userName)
    {
        _userData = GetUserDataAsync(userName).Result;
    }

    private async Task<Dictionary<string, JsonElement>> GetUserDataAsync(string userName)
    {
        try
        {
            _client.DefaultRequestHeaders.Add("User-Agent", "Mozilla/5.0");
            var response = await _client.GetStringAsync($"https://api.github.com/users/{userName}");
            
            var Json = JsonSerializer.Deserialize<Dictionary<string, JsonElement>>(response);
            if (Json == null)
            {
                Console.WriteLine("Response: null");
                return [];
            }
            return Json;
        }
        catch (HttpRequestException ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
            return [];
        }
    }

    private bool VerifyStatus()
    {
        if (_userData.TryGetValue("status", out var status) && status.GetString() == "404")
        {
            Console.WriteLine($"Usuario no encontrado.");
            return false;
        }
        return true;
    }

    private static string GetRepoInfo(JsonElement repo)
    {
        return $"""
        Lang: {(repo.TryGetProperty("full_name", out var name) ? name.GetString() : "Desconocido")}
        Repo: {(repo.TryGetProperty("language", out var lang) ? lang.GetString() : "Desconocido")}
        Stars: {(repo.TryGetProperty("stargazers_count", out var stars) ? stars.GetInt32() : 0)}
        Forks: {(repo.TryGetProperty("forks_count", out var forks) ? forks.GetInt32() : 0)}
        """;
    }

    public void PrintBasicInfo()
    {
        if (!VerifyStatus()) return;

        Console.WriteLine($"""
        -------------------------------------------
        Nombre: {(_userData.TryGetValue("name", out var name) ? name.GetString() : "Desconocido")}
        Creación: {(_userData.TryGetValue("created_at", out var created) ? created.GetString() : "Desconocido")}
        Repos: {(_userData.TryGetValue("public_repos", out var repos) ? repos.GetInt32() : 0)}
        Gists: {(_userData.TryGetValue("public_gists", out var gists) ? gists.GetInt32() : 0)}
        Seguidores: {(_userData.TryGetValue("followers", out var followers) ? followers.GetInt32() : 0)}
        Seguidos: {(_userData.TryGetValue("following", out var following) ? following.GetInt32() : 0)}
        -------------------------------------------
        """);
    }

    public async Task PrintReposInfoAsync()
    {
        if (!VerifyStatus()) return;

        if (_userData.TryGetValue("repos_url", out var reposUrl))
        {
            var reposResponse = await _client.GetStringAsync(reposUrl.GetString());
            var repos = JsonSerializer.Deserialize<List<JsonElement>>(reposResponse);
            var languages = new Dictionary<string, int>();
            Console.WriteLine("Repositorios publicos:");

            if (repos == null)
            {
                Console.WriteLine("Sin repositorios");
                return;
            }

            foreach (var repo in repos)
            {
                Console.WriteLine("\n" + GetRepoInfo(repo));

                if (repo.TryGetProperty("language", out var language))
                {
                    var lang = language.GetString();
                    if (!string.IsNullOrEmpty(lang))
                    {
                        languages[lang] = languages.TryGetValue(lang, out int value) ? value + 1 : 1;
                    }
                }
            }

            var mostUsedLang = languages.OrderByDescending(x => x.Value).FirstOrDefault();
            Console.WriteLine($"________\nTotal de repositorios: '{repos.Count}'");
            Console.WriteLine($"El lenguaje más utilizado: '{mostUsedLang.Key}'({mostUsedLang.Value})");
        }
    }

    public static async Task Main()
    {
        Console.WriteLine("Informe sobre los datos del usuario en GitHub");
        Console.Write("Usuario: ");
        string? userName = Console.ReadLine();

        if (userName != null)
        {
            var github = new GitHubApi(userName);
            await github.PrintReposInfoAsync();
            github.PrintBasicInfo();
        }
    }
}
