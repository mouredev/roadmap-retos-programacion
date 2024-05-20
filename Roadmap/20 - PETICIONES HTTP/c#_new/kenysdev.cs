/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
------------------------------------------
* PETICIONES HTTP
------------------------------------------
*/

using System.Text.Json;

#pragma warning disable CA1050
class Program {
    /*
    * EJERCICIO:
    * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
    * una petición a la web que tú quieras, verifica que dicha petición
    * fue exitosa y muestra por consola el contenido de la web.
    */
    static readonly HttpClient client = new();

    static async Task<Dictionary<string, object>> GetUser(int userId) {
        try {
            string url = $"https://jsonplaceholder.typicode.com/users/{userId}";
            HttpResponseMessage response = await client.GetAsync(url);
            
            if (response.IsSuccessStatusCode) {
                string json = await response.Content.ReadAsStringAsync();
                return JsonSerializer.Deserialize<Dictionary<string, object>>(json);
            } else {
                Console.WriteLine($"Id: {userId} No encontrado");
                Console.WriteLine(response.StatusCode);
                return [];
            }
        }
        catch (HttpRequestException) {
            Console.WriteLine("Error de conexión");
            return [];
        }
    }

    static void PrintUser(Dictionary<string, object> userData) {
        if (userData.Count > 0) {
            Console.WriteLine(
                $"Usuario con id: '{userData["id"]}':\n" +
                $"Nombre:  {userData["name"]}\n" +
                $"Usuario: {userData["username"]}\n" +
                $"Email:   {userData["email"]}\n" +
                $"Teléfono: {userData["phone"]}\n"
            );
        }
    }

    static async Task Main() {
        Console.WriteLine("\nEJERCICIO #1:\n");

        var u1 = await GetUser(1);
        PrintUser(u1);

        var u2 = await GetUser(2);
        PrintUser(u2);

        var u3 = await GetUser(777); // no existente
        PrintUser(u3);

        client.Dispose();
    }

}
