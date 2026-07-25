// #31 SIMULADOR JUEGOS OLÍMPICOS - SisaRoot

using System;
using System.Collections.Generic;
using System.Linq;

class Participant
{
    public string Name { get; set; }
    public string Country { get; set; }
    public Participant(string name, string country) { Name = name; Country = country; }
}

class OlympicEvent
{
    public string Name { get; set; }
    public List<Participant> Participants { get; set; } = new();
    public OlympicEvent(string name) => Name = name;
}

class CountryMedals
{
    public string Country { get; set; }
    public int Gold { get; set; }
    public int Silver { get; set; }
    public int Bronze { get; set; }
    public int Total => Gold + Silver + Bronze;
    public CountryMedals(string country) => Country = country;
}

class SisaRoot
{
    static readonly List<OlympicEvent> events = new();
    static readonly Dictionary<string, CountryMedals> medalTable = new();
    static readonly Random rng = new();

    static void RegisterEvent()
    {
        Console.Write("Nombre del evento: ");
        string name = Console.ReadLine()?.Trim() ?? "";
        if (string.IsNullOrEmpty(name)) { Console.WriteLine("Nombre inválido."); return; }
        if (events.Any(e => e.Name.Equals(name, StringComparison.OrdinalIgnoreCase)))
        { Console.WriteLine($"El evento '{name}' ya existe."); return; }
        events.Add(new OlympicEvent(name));
        Console.WriteLine($"Evento '{name}' registrado.");
    }

    static void RegisterParticipant()
    {
        if (events.Count == 0) { Console.WriteLine("No hay eventos registrados."); return; }
        Console.WriteLine("Eventos disponibles:");
        for (int i = 0; i < events.Count; i++)
            Console.WriteLine($"  {i + 1}. {events[i].Name}");
        Console.Write("Selecciona el número del evento: ");
        if (!int.TryParse(Console.ReadLine(), out int idx) || idx < 1 || idx > events.Count)
        { Console.WriteLine("Selección inválida."); return; }
        var ev = events[idx - 1];
        Console.Write("Nombre del participante: ");
        string pname = Console.ReadLine()?.Trim() ?? "";
        Console.Write("País del participante: ");
        string country = Console.ReadLine()?.Trim() ?? "";
        if (string.IsNullOrEmpty(pname) || string.IsNullOrEmpty(country))
        { Console.WriteLine("Datos inválidos."); return; }
        ev.Participants.Add(new Participant(pname, country));
        Console.WriteLine($"Participante '{pname} ({country})' añadido a '{ev.Name}'.");
    }

    static void AddMedal(string country, string type)
    {
        if (!medalTable.TryGetValue(country, out var cm))
        { cm = new CountryMedals(country); medalTable[country] = cm; }
        if (type == "gold") cm.Gold++;
        else if (type == "silver") cm.Silver++;
        else cm.Bronze++;
    }

    static void SimulateEvents()
    {
        if (events.Count == 0) { Console.WriteLine("No hay eventos para simular."); return; }
        foreach (var ev in events)
        {
            Console.WriteLine($"\n=== Simulando: {ev.Name} ===");
            if (ev.Participants.Count < 3)
            { Console.WriteLine($"  Necesita >=3 participantes (tiene {ev.Participants.Count}). Saltando."); continue; }
            var shuffled = ev.Participants.OrderBy(_ => rng.Next()).ToList();
            var gold = shuffled[0]; var silver = shuffled[1]; var bronze = shuffled[2];
            Console.WriteLine($"  🥇 Oro:    {gold.Name} ({gold.Country})");
            Console.WriteLine($"  🥈 Plata:  {silver.Name} ({silver.Country})");
            Console.WriteLine($"  🥉 Bronce: {bronze.Name} ({bronze.Country})");
            AddMedal(gold.Country, "gold"); AddMedal(silver.Country, "silver"); AddMedal(bronze.Country, "bronze");
        }
    }

    static void ShowReport()
    {
        Console.WriteLine("\n==============================");
        Console.WriteLine("   INFORME FINAL - JJOO 2024  ");
        Console.WriteLine("==============================");
        if (medalTable.Count == 0) { Console.WriteLine("No se han simulado eventos aún."); return; }
        var ranking = medalTable.Values
            .OrderByDescending(c => c.Gold).ThenByDescending(c => c.Silver).ThenByDescending(c => c.Bronze).ToList();
        Console.WriteLine($"{"Pos.",-5} {"País",-25} {"Oro",-6} {"Plata",-6} {"Bronce",-6} {"Total",-6}");
        Console.WriteLine(new string('-', 60));
        for (int i = 0; i < ranking.Count; i++)
        {
            var c = ranking[i];
            Console.WriteLine($"{i + 1 + ".",-5} {c.Country,-25} {c.Gold,-6} {c.Silver,-6} {c.Bronze,-6} {c.Total,-6}");
        }
    }

    static void Main()
    {
        while (true)
        {
            Console.WriteLine("\n====== SIMULADOR JJOO PARÍS 2024 ======");
            Console.WriteLine("1. Registrar evento\n2. Registrar participante\n3. Simular eventos\n4. Ver informe\n5. Salir");
            Console.Write("Selecciona una opción: ");
            switch (Console.ReadLine()?.Trim())
            {
                case "1": RegisterEvent(); break;
                case "2": RegisterParticipant(); break;
                case "3": SimulateEvents(); break;
                case "4": ShowReport(); break;
                case "5": Console.WriteLine("¡Hasta luego!"); return;
                default: Console.WriteLine("Opción no válida."); break;
            }
        }
    }
}
