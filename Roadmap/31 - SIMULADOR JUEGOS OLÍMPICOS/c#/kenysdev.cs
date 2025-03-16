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

// NOTA: Esto es un intento de aplicar los principios SOLID.

// ________________________________________________
// Interfaces
/// <summary>Contrato sobre las constantes globales.</summary>
public interface IConstants
{
    string GetMenu();
    string[] GetMedals();
}

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
    IDataTable<(string Name, string Country, int EventId)> ParticipantsTable { get; }
    IDataTable<List<(string EventName, List<(string Name, string Country, int EventId, int Score, string Medal)> Results)>> SimulationTable { get; }
}

/// <summary>
/// Contrato sobre la entra de datos.
/// </summary>
public interface IInput
{
    /// <returns>Una cadena no vacía</returns>
    string GetStr(string msg);
    /// <returns>Un entero</returns>
    int GetInt(string msg);
}

// ________________________________________________
/// CONTRATOS sobre la comunicación entre la interacción del usuario y la capa de datos.
public interface IEvents { void Add(); }

public interface IParticipants { void Add(); }

public interface ISimulations { void Start(); }

public interface IReports { void Generate(); }

// ________________________________________________
// IMPLEMENTAR CONTRATOS
// ________________________________________________
public class Constants : IConstants
{
    private const string Menu = """
    
    SIMULADOR JUEGOS OLÍMPICOS:
    --------------------------------------------------
    | 1. Registrar evento        | 4. Crear informes |  
    | 2. Registrar participante  | 5. Salir          |
    | 3. Simulación de eventos   |                   |
    --------------------------------------------------
    """;

    private static readonly string[] Medals = ["🥇 Oro", "🥈 Plata", "🥉 Bronce"];
    public string GetMenu() { return Menu; }
    public string[] GetMedals() { return Medals; }
}

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

public class ParticipantsTable : IDataTable<(string Name, string Country, int EventId)>
{
    private readonly List<(string Name, string Country, int EventId)> dt = [];

    public void Add((string Name, string Country, int EventId) participant)
    {
        dt.Add(participant);
    }

    public int Count()
    {
        return dt.Count;
    }

    public List<(string Name, string Country, int EventId)> GetList()
    {
        return new List<(string Name, string Country, int EventId)>(dt);
    }
}

public class SimulationTable : IDataTable<List<(string EventName, List<(string Name, string Country, int EventId, int Score, string Medal)> Results)>>
{
    private readonly List<List<(string EventName, List<(string Name, string Country, int EventId, int Score, string Medal)> Results)>> dt = [];

    public void Add(List<(string EventName, List<(string Name, string Country, int EventId, int Score, string Medal)> Results)> simulation)
    {
        dt.Add(simulation);
    }

    public int Count()
    {
        return dt.Count;
    }

    public List<List<(string EventName, List<(string Name, string Country, int EventId, int Score, string Medal)> Results)>> GetList()
    {
        return new List<List<(string EventName, List<(string Name, string Country, int EventId, int Score, string Medal)> Results)>>(dt);
    }
}

/// <summary>
/// Datos en memoria aplicando el patrón Singleton.
/// </summary>
public class DataInMemory : IData
{
    private static DataInMemory? _instance;
    public IDataTable<string> EventsTable { get; private set; }
    public IDataTable<(string Name, string Country, int EventId)> ParticipantsTable { get; private set; }
    public IDataTable<List<(string EventName, List<(string Name, string Country, int EventId, int Score, string Medal)> Results)>> SimulationTable { get; private set; }

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
    public string GetStr(string msg)
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

    public int GetInt(string msg)
    {
        while (true)
        {
            Console.Write(msg);
            string? txt = Console.ReadLine();
            if (int.TryParse(txt, out int input))
            {
                return input;
            }
            else
            {
                Console.WriteLine("Ingresa un número entero.");
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
        string sport = input.GetStr("Deporte: ");
        data.EventsTable.Add(sport);
        Console.WriteLine($"{sport} fue agregado");
        //Console.WriteLine(constants.Menu);
    }
}

// ________________________________________________
/// <summary>
/// 2. Registrar participantes por nombre y país.
/// </summary>
public class Participants(IConstants constants, IData data, IInput input) : IParticipants
{
    private int GetEventId()
    {
        Console.WriteLine("Seleccionar el evento donde participará:");
        var events = data.EventsTable.GetList();
        for (int i = 0; i < events.Count; i++)
        {
            Console.WriteLine($"{i}. {events[i]}");
        }

        while (true)
        {
            int index = input.GetInt("Id de evento: ");
            if (index < 0 || index >= events.Count)
            {
                Console.WriteLine("\nId no encontrada.");
            }
            else
            {
                return index;
            }
        }
    }

    public void Add()
    {
        Console.WriteLine("AGREGAR PARTICIPANTE:");
        var events = data.EventsTable.GetList();
        if (!(events.Count > 0))
        {
            Console.WriteLine("No existe evento en cuál participar.");
            return;
        }

        int eventId = GetEventId();
        string name = input.GetStr("Nombre: ");
        string country = input.GetStr("país: ");
        data.ParticipantsTable.Add((name, country, eventId));
        Console.WriteLine($"{eventId} fue agregado");
        Console.WriteLine(constants.GetMenu());
    }
}

// ________________________________________________
/// <summary>
/// 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
/// 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
/// </summary>
public class Simulation(IConstants constants, IData data) : ISimulations
{
    private static readonly Random _random = new();

    /// <returns>Una lista con los 3 ganadores del éxito, junto con su puntaje y su medalla. </returns>
    private List<List<object>> QualifyParticipants(int eventId)
    {
        var participants = data.ParticipantsTable.GetList();
        var ParticipantsOfEvent = participants.Where(p => p.EventId == eventId).ToList();

        var qualifiedParticipants = ParticipantsOfEvent.Select(p =>
        {
            var list = new List<object>
            {
            p.Name,
            p.Country,
            p.EventId,
            _random.Next(1, 101)
            };
            return list;
        }).ToList();

        qualifiedParticipants = [.. qualifiedParticipants.OrderByDescending(p => (int)p[3])];

        var top3Participants = qualifiedParticipants.Take(3).ToList();

        string[] medals = constants.GetMedals();
        for (int i = 0; i < top3Participants.Count; i++)
        {
            top3Participants[i].Add(medals[i]);
        }

        return top3Participants;
    }

    private void AddResultEvents()
    {
        var events = data.EventsTable.GetList();
        var simulation = new List<(
            string EventName, List<(string Name, string Country, 
            int EventId, int Score, string Medal)> Results)>();

        for (int id = 0; id < events.Count; id++)
        {
            var qualifiedParticipants = QualifyParticipants(id);
            var eventResult = qualifiedParticipants.Select(p =>
                (
                    Name: p[0]?.ToString() ?? string.Empty,
                    Country: p[1]?.ToString() ?? string.Empty,
                    eventId: Convert.ToInt32(p[2]),
                    Score: Convert.ToInt32(p[3]),
                    Medal: p[4]?.ToString() ?? string.Empty
                )
            ).ToList();

            simulation.Add((EventName: events[id], Results: eventResult));
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
public class Reports(IConstants constants, IData data) : IReports
{
    private readonly Dictionary<string, (int Medals, int CurrentScore)> rankingCountries = [];

    private void GenerateTopCountries()
    {
        var sortedRank = rankingCountries.OrderByDescending(item => item.Value);

        int i = 1;
        foreach (var (name, total) in sortedRank)
        {
            Console.WriteLine($"'{i}' - {name} -> Medallas: {total.Medals} | Puntaje: {total.CurrentScore}");
            i++;
        }
    }

    private void IterateParticipants(IEnumerable<(
        string Name, string Country, int EventId, int Score, string Medal)> participants)
    {
        int i = 1;
        foreach (var (name, country, eventid, score, medal) in participants)
        {
            Console.WriteLine($"'{i}' - {name} - {country} -> Score: {score}, Medal: {medal}");

            // Registrar para generar ranking de países por número de medallas
            if (rankingCountries.TryGetValue(country, out var value))
            {
                int medals = value.Medals;
                int currentScore = value.CurrentScore;
                rankingCountries[country] = (medals + 1, currentScore + score);
            }
            else
            {
                rankingCountries[country] = (1, score);
            }

            i++;
        }
    }

    private void IterateEvents(List<(
        string EventName, List<(string Name, string Country, int EventId, int Score, string Medal)> Results)> simulation)
    {
        foreach (var (eventName, results) in simulation)
        {
            Console.WriteLine($"\nEvent: {eventName}:");
             if (results.Count < 3)
             {
                Console.WriteLine("Evento cancelado por falta de participantes.");
                continue;
             }

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

            Console.WriteLine("\nRanking de países, según el número de medallas y puntaje:");
            GenerateTopCountries();
            rankingCountries.Clear();

            i++;
        }

        Console.WriteLine(constants.GetMenu());
    }
}

// ________________________________________________
public class Features
{
    public required IConstants Constants { get; set; }
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
        Console.WriteLine(Ft.Constants.GetMenu());
        while (true)
        {
            string option = Ft.Input.GetStr("\nOpción: ");
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
        IConstants constants = new Constants();
        IData data = DataInMemory.Instance;
        IInput input = new Input();

        Features Features_ = new()
        {
            Constants = constants,
            Data = data,
            Input = input,
            Events = new Events(data, input),
            Participants = new Participants(constants, data, input),
            Simulation = new Simulation(constants, data),
            Reports = new Reports(constants, data)
        };

        Program program = new(Features_);
        program.Run();
    }
}

// NOTA: Esto es un intento de aplicar los principios SOLID.

