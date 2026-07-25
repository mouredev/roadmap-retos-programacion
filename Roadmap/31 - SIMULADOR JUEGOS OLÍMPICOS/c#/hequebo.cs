class Program
{
    static void Main(string[] args)
    {
        EventService eventService = new EventService();
        ParticipantService participantService = new ParticipantService();
        ResultService resultService = new ResultService();
        CountryResultService countryResultService = new CountryResultService();
        Olympics olympics = new Olympics(eventService, participantService, resultService,countryResultService);

        bool salir = false;

        do
        {
            Menu();
            int option = 0;
            int.TryParse(Console.ReadLine(), out option);

            switch (option)
            {
                case 1:
                    olympics.AddEvent();
                    break;
                case 2:
                    olympics.AddParticipant();
                    break;
                case 3:
                    olympics.SimulateEvent();
                    break;
                case 4:
                    olympics.ShowResults();
                    break;
                case 5:
                    salir = true;
                    Console.Clear();
                    Console.WriteLine("Hasta la próxima...");
                    Thread.Sleep(1000);
                    break;
                default:
                    Console.WriteLine("Opción no válida...");
                    break;
            }
        }
        while (!salir);
    }

    static void Menu()
    {
        Console.WriteLine("---Simulador JJOO París 2024---");
        Console.WriteLine("1.- Registrar Evento.");
        Console.WriteLine("2.- Registrar Participante.");
        Console.WriteLine("3.- Simular Evento.");
        Console.WriteLine("4.- Consultar Ranking.");
        Console.WriteLine("5.- Salir.");
        Console.WriteLine("Seleccione una opción...");
    }
}
class Event
{
    private int _id;
    private string _name;

    public string Name { get { return _name; } }
    public int Id { get { return _id; } } 

    public Event(int id, string name)
    {
        _id = id;
        _name = name;
    }
}
class EventService
{
    public int id = 1;
    private List<Event> _events;

    public EventService()
    {
        _events = new List<Event>();
    }
    public int SearchEvent(string name) => _events.Where(e => e.Name == name).Count();
    public string Search(int id)
    {
        if (_events.Where(e => e.Id == id).Count() == 0)
        {
            Console.WriteLine($"El evento con id {id} no existe...");
            return "";
        }
        var @event = _events.Where(e => e.Id == id).FirstOrDefault();
        return @event.Name;
    }
    public void AddEvent(Event @event)
    {
        _events.Add(@event);
        id++;
    }

    public bool GetEvents()
    {
        if (_events.Count == 0)
        {
            Console.WriteLine("No hay eventos registrados...");
            return false;
        }
        foreach (var @event in _events)
            Console.WriteLine($"{@event.Id}.- {@event.Name}");
        return true;
    }
}
class Participant
{
    private string _name;
    private string _country;
    private int _idEvent;

    public string Name { get { return _name; } }
    public string Country { get { return _country; } }
    public int IdEvent { get { return _idEvent; } }

    public Participant(string name, string country, int idEvent)
    {
        _name = name;
        _country = country;
        _idEvent = idEvent;
    }
}
class ParticipantService
{
    private List<Participant> _participants;

    public ParticipantService()
    {
        _participants = new List<Participant>();
    }
    public int SearchParticipant(string name, string country) =>
        _participants.Where(p => p.Name == name && p.Country == country).Count();
    public List<Participant>? GetEventParticipants(int id)
    {
        var  participants = _participants.Where(p => p.IdEvent == id).ToList();

        if (participants.Count() == 0)
        {
            Console.WriteLine("No hay participantes registrados en este evento...");
            return null;
        }
        if (participants.Count() < 3)
        {
            Console.WriteLine("Se necesitan al menos 3 participantes para simular el evento" +
                $"actalmente solo hay {participants} participante(s) registrado(s)...");
            return null;
        }
        Console.Clear();
        foreach (var participant in participants)
            Console.WriteLine($"Nombre: {participant.Name}, País: {participant.Country}");
        return participants;
    }

    public void AddParticipant(Participant participant) => _participants.Add(participant);
}
class Result
{
    private string _event;
    private string _gold;
    private string _silver;
    private string _bronze;

    public string Event { get { return _event; } }
    public string Gold { get { return _gold; } }
    public string Silver { get { return _silver; } }
    public string Bronze { get { return _bronze; } }

    public Result(string @event, string gold, string silver, string bronze)
    {
        _event = @event;
        _gold = gold;
        _silver = silver;
        _bronze = bronze;
    }
}
class ResultService
{
    private List<Result> _results;

    public ResultService()
    {
        _results = new List<Result>();
    }

    public void AddResult(Result result) => _results.Add(result);
    public void ShowResults()
    {
        foreach (var result in _results)
            Console.WriteLine($"Evento: {result.Event}, Oro: {result.Gold}, " +
                $"Plata: {result.Silver}, Bronce: {result.Bronze}");
    }
}
class CountryResult 
{
    private string _country;
    private int _gold;
    private int _silver;
    private int _bronze;

    public string Country 
    {
        get
        {
            return _country;
        }
        set
        {
            _country = value;
        }
    }
    public int Gold
    {
        get
        {
            return _gold;
        }
        set
        {
            _gold = value;
        }
    }

    public int Silver
    {
        get
        {
            return _silver;
        }
        set
        {
            _silver = value;
        }
    }
    public int Bronze
    {
        get
        {
            return _bronze;
        }
        set
        {
            _bronze = value;
        }
    }

    public CountryResult(string country, int gold, int silver, int bronze)
    {
        _country = country;
        _gold = gold;
        _silver = silver;
        _bronze = bronze;
    }
}
class CountryResultService
{
    private List<CountryResult> _countryResults;

    public CountryResultService()
    {
        _countryResults = new List<CountryResult>();
    }

    public void AddResult(CountryResult countryResult)
    {
        if (_countryResults.Where(c => c.Country == countryResult.Country).Count() > 0)
        {
            var country = _countryResults.Where(c => c.Country == countryResult.Country).FirstOrDefault();
            country.Gold += countryResult.Gold;
            country.Silver += countryResult.Silver;
            country.Bronze += countryResult.Bronze;
        }
        else
        {
            _countryResults.Add(countryResult);
        }
    }
    public void ShowResults()
    {
        var results = _countryResults.OrderByDescending(c => c.Gold).ThenByDescending(c => c.Silver)
            .ThenByDescending(c => c.Bronze).ToList();

        foreach(var result in results)
            Console.WriteLine($"País: {result.Country}, Oro: {result.Gold}, " +
                $"Plata: {result.Silver}, Bronce: {result.Bronze}");
    }
}

class Olympics
{
    private EventService _eventService;
    private ParticipantService _participantService;
    private ResultService _resultService;
    private CountryResultService _countryResultService;

    public Olympics(EventService eventService, ParticipantService participantService, 
        ResultService resultService, CountryResultService countrResultService)
    {
        _participantService = participantService;
        _eventService = eventService;
        _resultService = resultService;
        _countryResultService = countrResultService;
    }

    public void AddEvent()
    {
        Console.Clear();
        Console.WriteLine("Ingresa el nombre del evento:");
        string? name = Console.ReadLine();
        if(string.IsNullOrEmpty(name))
        {
            Console.WriteLine("No se ha ingresado ningún nombre...");
            return;
        }
        if (_eventService.SearchEvent(name) > 0)
        {
            Console.WriteLine($"El evento {name} ya ha sido registrado...");
            return;
        }
        Event @event = new Event(_eventService.id, name);
        _eventService.AddEvent(@event);
        Console.Clear();
        Console.WriteLine($"El evento {name} se ha registrado correctamente...");
    }
    public void AddParticipant()
    {
        Console.Clear();
        Console.WriteLine("Ingresa nombre del participante");
        string? name = Console.ReadLine();
        Console.WriteLine("Ingresa país del participante");
        string? country = Console.ReadLine();
        if(string.IsNullOrEmpty(name) || string.IsNullOrEmpty(country))
        {
            Console.WriteLine("No se ingresaron los datos correctamente...");
            return;
        }
        if (_participantService.SearchParticipant(name, country) > 0)
        {
            Console.WriteLine("Este participante ya se encuentra registrado");
            return;
        }
        if (!_eventService.GetEvents())
            return;
        Console.WriteLine("Selecciona evento en el cual se participará");
        int idEvento  = 0;
        int.TryParse(Console.ReadLine(), out idEvento);
        string eventName = _eventService.Search(idEvento);
        if (eventName == "")
            return;

        Participant participant = new Participant(name, country, idEvento);
        _participantService.AddParticipant(participant);
        Console.Clear();
        Console.WriteLine("El participante se ha registrado correctamente...");
        Console.WriteLine($"Nombre: {participant.Name}, País: {participant.Country}, Evento: {eventName}");
    }
    public void SimulateEvent()
    {
        Console.Clear();
        if (!_eventService.GetEvents())
            return;
        Console.WriteLine("Seleccione evento a simular");
        int idEvent = 0;
        int.TryParse(Console.ReadLine(), out idEvent);

        string eventName = _eventService.Search(idEvent);
        if (eventName == "")
            return;

        var participants = _participantService.GetEventParticipants(idEvent);
        if (participants == null)
            return;

        List<Participant> winnersList = new List<Participant>();
        Random random = new Random();
        
        // Medalla de Oro
        int index = random.Next(0, participants.Count);
        winnersList.Add(participants[index]);
        participants.RemoveAt(index);

        // Medalla de Plata
        index = random.Next(0, participants.Count);
        winnersList.Add(participants.ElementAt(index));
        participants.RemoveAt(index);

        // Medalla de Bronce
        index = random.Next(0, participants.Count);
        winnersList.Add(participants.ElementAt(index));


        Console.WriteLine("---Resultados---");
        Console.WriteLine($"Medalla de Oro: {winnersList[0].Name}, {winnersList[0].Country}");
        Console.WriteLine($"Medalla de Plata: {winnersList[1].Name}, {winnersList[1].Country}");
        Console.WriteLine($"Medalla de Bronce: {winnersList[2].Name}, {winnersList[2].Country}");

        Result result = new Result(eventName, winnersList[0].Country, winnersList[1].Country, winnersList[2].Country);
        _resultService.AddResult(result);

        var gold = new CountryResult(winnersList[0].Country, 1, 0, 0);
        var silver = new CountryResult(winnersList[1].Country, 0, 1, 0);
        var bronze = new CountryResult(winnersList[2].Country, 0, 0, 1);
        _countryResultService.AddResult(gold);
        _countryResultService.AddResult(silver);
        _countryResultService.AddResult(bronze);
        

        Console.ReadLine();
        Console.Clear();
    }
    public void ShowResults()
    {
        Console.Clear();
        _resultService.ShowResults();
        _countryResultService.ShowResults();
        Console.ReadLine();
    }
}
