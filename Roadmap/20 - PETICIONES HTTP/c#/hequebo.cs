using System.Text.Json;

class Program
{
    static async Task Main(string[] args)
    {
        #region Http
        // Peticiones Http
        Console.WriteLine("---Peticiones HTTP---");
        /*
         * En .Net existe la clase HttpClient la cual nos
         * permite crear peticiones http de manera asíncrona.
         * En su constructor podemos proporcionar la url a la 
         * cual queremos realizar la petición, cual usa la 
         * clase Uri y dentro del constructor la cadena de 
         * texto con la url
         */
        var httpClient = new HttpClient
        {
            BaseAddress = new Uri("https://jsonplaceholder.typicode.com/users"),
        };
        Console.WriteLine("Utilizamos el metodo GET en para la siguiente url:");
        Console.WriteLine(httpClient.BaseAddress);
        /*
         * Utilizamos el método GetAsync(requestUri) para realizar
         * la petición y guardamos el resultado en una variable de 
         * la clase HttpResponseMessage
         */
        var response = await httpClient.GetAsync(httpClient.BaseAddress);
        /*
         * Convertimos el resultado en un json
         */
        var jsonResponse = await response.Content.ReadAsStringAsync();
        Console.WriteLine("Nos devuelve la siguiente información:");
        Thread.Sleep(1000);
        Console.WriteLine(jsonResponse);
        httpClient.Dispose();
        #endregion

        Console.ReadLine();
        Console.Clear();

        // Ejercicio extra
        var httpClientPokemon = new HttpClient
        {
            BaseAddress = new Uri("https://pokeapi.co/api/v2/pokemon"),
        };
        bool salir = false;
        do
        {
            Menu();
            int option = 0;
            int.TryParse(Console.ReadLine(), out option);
            switch (option)
            {
                case 1:
                    await Search(httpClientPokemon);
                    break;
                case 2:
                    Console.Clear();
                    Console.WriteLine("Hasta la próxima...");
                    Thread.Sleep(1000);
                    salir = true;
                    break;
                default:
                    Console.WriteLine("Opción no válida...");
                    break;
            }

        } while (!salir);
    }
    static void Menu()
    {
        Console.WriteLine("---Pokedex---");
        Console.WriteLine("1.- Buscar por id o nombre");
        Console.WriteLine("2.- Salir");
        Console.WriteLine("Ingrese opción deseada...");
    }
    static async Task Search(HttpClient httpClient)
    {
        Console.Clear();
        Console.WriteLine("Ingresa id o nombre de pokemón a consultar");
        string search = Console.ReadLine();

        var response = await httpClient.GetAsync($"{httpClient.BaseAddress}/{search}");
        if (response.StatusCode != System.Net.HttpStatusCode.OK)
        {
            Console.WriteLine("Pokemon no encontrado...");
            return;
        }

        var body = await response.Content.ReadAsStringAsync();
        var options = new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true
        };
        /*
         * Con el metodo Deserialize podemos mapear el contenido
         * de la respuesta a una clase propia
         */
        var pokemon = JsonSerializer.Deserialize<Pokemon>(body, options);

        Console.WriteLine($"Id: {pokemon.Id}");
        Console.WriteLine($"Nombre: {pokemon.Name}");
        Console.WriteLine($"Peso: {pokemon.Weight}");
        Console.WriteLine($"Altura: {pokemon.Height}");
        Console.WriteLine("Tipos:");
        foreach (var type in  pokemon.Types)
            Console.WriteLine($"{type.Slot}: {type.Type.Name}");
        Console.WriteLine("Juegos:");
        foreach (var game in pokemon.Game_Indices)
            Console.WriteLine($"{game.Version.Name}");
        Console.WriteLine();

    }

}
class Pokemon
{
    public int Id { get; set; }
    public string Name { get; set; }
    public decimal Weight { get; set; }
    public decimal Height { get; set; }
    public List<TypeInfo> Types { get; set; }
    public List<GameInfo> Game_Indices { get; set; }
}
class TypeInfo
{
    public int Slot {  get; set; }
    public Type Type { get; set; }
}
class Type
{
    public string Name { get; set; }
}
class GameInfo
{
    public int Game_Index { get; set; }
    public Version Version { get; set; }
}
class Version
{
    public string Name { get; set; }
}
