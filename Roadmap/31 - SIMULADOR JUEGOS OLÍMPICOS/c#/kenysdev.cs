namespace exs31;
/*
╔══════════════════════════════════════╗
║ Autor:  Kenys Alvarado               ║
║ GitHub: https://github.com/Kenysdev  ║
║ 2024 -  C#                           ║
╚══════════════════════════════════════╝
-----------------------------------------------------
* SIMULADOR JUEGOS OLÍMPICOS
-----------------------------------------------------

* EJERCICIO:
* ¡Los JJOO de París 2024 han comenzado!
* Crea un programa que simule la celebración de los juegos.
* El programa debe permitir al usuario registrar eventos y participantes,
* realizar la simulación de los eventos asignando posiciones de manera aleatoria
* y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
*/

// NOTA IMPORTANTE:  Esto es un intento de aplicar los principios SOLID. Claramente, 
// el reto se podría realizar con unas pocas líneas de código 'hardcoded'.

// ________________________________________________
public static class GlobalConstants
{
    public const string Menu = """
    SIMULADOR JUEGOS OLÍMPICOS:
    --------------------------------------------------
    | 1. Registrar evento        | 4. Crear informes |  
    | 2. Registrar participante  | 5. Salir          |
    | 3. Simulación de eventos   |                   |
    --------------------------------------------------
    """;

    public static readonly string[] Medals = ["Oro", "Plata", "Bronce"];

}

// ________________________________________________
// Interfaces
/// <summary>
/// Contrato sobre los métodos requeridos para cada tabla creada.
/// </summary>
public interface IDataTable<T>
{
    void Add(T item);

    /// <returns>El número de elementos.</returns>
    int Count();

    /// <returns>Una lista de los elementos.</returns>
    List<T> GetList();
}

/// <summary>
/// Contrato para implementar en diferentes formas de almacenamiento.
/// </summary>
public interface IData
{
    IDataTable<string> EventsTable { get; }
    IDataTable<(string Name, string Country)> ParticipantsTable { get; }
    IDataTable<List<(string EventName, List<(string Name, string Country, int Score, string Medal)> Results)>> SimulationTable { get; }
}

/// <summary>
/// Contrato sobre la entra de datos.
/// </summary>
public interface IInput
{
    /// <returns>Una cadena no vacía</returns>
    string Get(string msg);
}

// ________________________________________________
/// CONTRATOS sobre la comunicación entre la interacción del usuario y la capa de datos.
public interface IEvents{ void Add(); }

public interface IParticipants{ void Add(); }

public interface ISimulations{ void Start(); }

public interface IReports{ void Generate(); }

// ________________________________________________
// IMPLEMENTAR CONTRATOS
public class EventsTable : IDataTable<string>
{
    private readonly List<string> dt = [];

    public void Add(string sport)
    {
        dt.Add(sport);
    }

    public int Count()
    {
        return dt.Count;
    }

    public List<string> GetList()
    {
        return new List<string>(dt);
    }
}

public class ParticipantsTable : IDataTable<(string Name, string Country)>
{
    private readonly List<(string Name, string Country)> dt = [];

    public void Add((string Name, string Country) participant)
    {
        dt.Add(participant);
    }

    public int Count()
    {
        return dt.Count;
    }

    public List<(string Name, string Country)> GetList()
    {
        return new List<(string Name, string Country)>(dt);
    }
}

public class SimulationTable : IDataTable<List<(string EventName, List<(string Name, string Country, int Score, string Medal)> Results)>>
{
    private readonly List<List<(string EventName, List<(string Name, string Country, int Score, string Medal)> Results)>> dt = [];

    public void Add(List<(string EventName, List<(string Name, string Country, int Score, string Medal)> Results)> simulation)
    {
        dt.Add(simulation);
    }

    public int Count()
    {
        return dt.Count;
    }

    public List<List<(string EventName, List<(string Name, string Country, int Score, string Medal)> Results)>> GetList()
    {
        return new List<List<(string EventName, List<(string Name, string Country, int Score, string Medal)> Results)>>(dt);
    }
}

/// <summary>
/// Datos en memoria aplicando el patrón Singleton.
/// </summary>
public class DataInMemory : IData
{
    private static DataInMemory? _instance;
    public IDataTable<string> EventsTable { get; private set; }
    public IDataTable<(string Name, string Country)> ParticipantsTable { get; private set; }
    public IDataTable<List<(string EventName, List<(string Name, string Country, int Score, string Medal)> Results)>> SimulationTable { get; private set; }

    private DataInMemory()
    {
        EventsTable = new EventsTable();
        ParticipantsTable = new ParticipantsTable();
        SimulationTable = new SimulationTable();
    }

    public static DataInMemory Instance
    {
        get
        {
            _instance ??= new DataInMemory();
            return _instance;
        }
    }
}

// ________________________________________________
/// <summary>
/// Muestra un mensaje al usuario y devuelve su entrada.
/// </summary>
public class Input : IInput
{
    public string Get(string msg)
    {
        while (true)
        {
            Console.Write(msg);
            string? txt = Console.ReadLine();
            if (!string.IsNullOrEmpty(txt))
            {
                return txt;
            }
        }
    }
}

// ________________________________________________
/// <summary>
/// 1. Registrar eventos deportivos.
/// </summary>
public class Events(IData data, IInput input) : IEvents
{
    public void Add()
    {
        Console.WriteLine("AGREGAR EVENTO DEPORTIVO:");
        string sport = input.Get("Deporte: ");
        data.EventsTable.Add(sport);
        Console.WriteLine($"{sport} fue agregado");
        //Console.WriteLine(GlobalConstants.Menu);
    }
}

// ________________________________________________
/// <summary>
/// 2. Registrar participantes por nombre y país.
/// </summary>
public class Participants(IData data, IInput input) : IParticipants
{
    public void Add()
    {
        Console.WriteLine("AGREGAR PARTICIPANTE:");
        string name = input.Get("Nombre: ");
        string country = input.Get("país: ");
        data.ParticipantsTable.Add((name, country));
        Console.WriteLine($"{name} fue agregado");
        //Console.WriteLine(GlobalConstants.Menu);
    }
}

// ________________________________________________
/// <summary>
/// 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
/// 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
/// </summary>
public class Simulation(IData data) : ISimulations
{
    private static readonly Random _random = new();

    /// <returns>Una lista con los 3 ganadores del éxito, junto con su puntaje y su medalla. </returns>
    private List<List<object>> QualifyParticipants()
    {
        var participants = data.ParticipantsTable.GetList();

        var qualifiedParticipants = participants.Select(p =>
        {
            var list = new List<object>
            {
            p.Name,
            p.Country,
            _random.Next(1, 101)
            };
            return list;
        }).ToList();

        qualifiedParticipants = [.. qualifiedParticipants.OrderByDescending(p => (int)p[2])];

        var top3Participants = qualifiedParticipants.Take(3).ToList();

        var medals = GlobalConstants.Medals;
        for (int i = 0; i < top3Participants.Count; i++)
        {
            top3Participants[i].Add(medals[i]);
        }

        return top3Participants;
    }

    private void AddResultEvents()
    {
        var events = data.EventsTable.GetList();
        var simulation = new List<(string EventName, List<(string Name, string Country, int Score, string Medal)> Results)>();

        foreach (var e in events)
        {
            var qualifiedParticipants = QualifyParticipants();
            var eventResult = qualifiedParticipants.Select(p =>
                (
                    Name: p[0]?.ToString() ?? string.Empty,
                    Country: p[1]?.ToString() ?? string.Empty,
                    Score: Convert.ToInt32(p[2]),
                    Medal: p[3]?.ToString() ?? string.Empty
                )
            ).ToList();

            simulation.Add((EventName: e, Results: eventResult));
        }

        data.SimulationTable.Add(simulation);
    }

    public void Start()
    {
        if (data.EventsTable.Count() >= 1 && data.ParticipantsTable.Count() >= 3)
        {
            AddResultEvents();
            var totalSimulation = data.SimulationTable.Count();
            Console.WriteLine($"Simulación '#{totalSimulation}' creada.");
            Console.WriteLine("Puedes ver el resultado con opción: '4. Crear informes.'");
        }
        else
        {
            Console.WriteLine("Debe haber al menos un evento y al menos 'tres' participantes.");
        }
    }
}

// ________________________________________________
/// <summary>
/// 5. Mostrar los ganadores por cada evento.
/// 6. Mostrar el ranking de países según el número de medallas.
/// </summary>
public class Reports(IData data) : IReports
{
    private readonly Dictionary<string, int> rankingCountries = [];

    private void GenerateTopCountries()
    {
        var sortedRank = rankingCountries.OrderByDescending(item => item.Value);

        int i = 1;
        foreach (var (name, total) in sortedRank)
        {
            Console.WriteLine($"'{i}' - {name} -> Medallas: {total}");
            i++;
        }
    }

    private void IterateParticipants(IEnumerable<(string Name, string Country, int Score, string Medal)> participants)
    {
        int i = 1;
        foreach (var (name, country, score, medal) in participants)
        {
            Console.WriteLine($"'{i}' - {name} - {country} -> Score: {score}, Medal: {medal}");

            // Registrar para generar ranking de países por número de medallas
            if (rankingCountries.TryGetValue(country, out int value))
            {
                rankingCountries[country] = ++value;
            }
            else
            {
                rankingCountries[country] = 1;
            }

            i++;
        }
    }

    private void IterateEvents(List<(string EventName, List<(string Name, string Country, int Score, string Medal)> Results)> simulation)
    {
        foreach (var (eventName, results) in simulation)
        {
            Console.WriteLine($"\nEvent: {eventName}:");
            IterateParticipants(results);
        }
    }

    public void Generate()
    {
        var simulations = data.SimulationTable.GetList();
        if (simulations.Count == 0)
        {
            Console.WriteLine("Aún no hay simulaciones creadas.");
            return;
        }

        int i = 1;
        foreach (var simulation in simulations)
        {
            Console.WriteLine($"\n______________\nSimulation {i}");
            IterateEvents(simulation);

            Console.WriteLine("\nRanking de países, según el número de medallas:");
            GenerateTopCountries();
            rankingCountries.Clear();

            i++;
        }

        //Console.WriteLine(GlobalConstants.Menu);
    }
}

// ________________________________________________
public class Features
{
    public required IData Data { get; set; }
    public required IInput Input { get; set; }
    public required IEvents Events { get; set; }
    public required IParticipants Participants { get; set; }
    public required ISimulations Simulation { get; set; }
    public required IReports Reports { get; set; }
}

/// <summary>
/// Recibimos instancias con las características del programa que dependen de las interfaces.
/// </summary>
public class Program(Features Ft)
{
    public void Run()
    {
        Console.WriteLine(GlobalConstants.Menu);
        while (true)
        {
            string option = Ft.Input.Get("\nOpción: ");
            switch (option)
            {
                case "1": Ft.Events.Add(); break;
                case "2": Ft.Participants.Add(); break;
                case "3": Ft.Simulation.Start(); break;
                case "4": Ft.Reports.Generate(); break;
                case "5": Console.WriteLine("Adios"); return;
                default: Console.WriteLine("Seleccionar de '1 a 5'"); break;
            }
        }
    }

    public static void Main()
    {
        IData data = DataInMemory.Instance;
        IInput input = new Input();

        Features Features_ = new()
        {
            Data = data,
            Input = input,
            Events = new Events(data, input),
            Participants = new Participants(data, input),
            Simulation = new Simulation(data),
            Reports = new Reports(data)
        };

        Program program = new(Features_);
        program.Run();
    }
}

// NOTA IMPORTANTE:  Esto es un intento de aplicar los principios SOLID. Claramente, 
// el reto se podría realizar con unas pocas líneas de código 'hardcoded'.
