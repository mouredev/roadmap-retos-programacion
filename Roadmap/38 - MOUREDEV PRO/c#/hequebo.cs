class Participant
{
    public int Id { get; set; }
    public string Email { get; set; }
    public string Status { get; set; }

    public Participant(int id, string email, string status) 
    {
        Id = id;
        Email = email;
        Status = status;
    }

}
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("---Ganadores de Sortea MoureDevPro---");

        using (var reader =  new StreamReader("participantes.csv"))
        {
            List<Participant> list = new List<Participant>();

            reader.ReadLine(); // Saltar primera linea con nombre de columnas

            while (!reader.EndOfStream)
            {
                var line = reader.ReadLine();
                var values = line.Split(",");

                list.Add(new Participant(int.Parse(values[0]), values[1].Trim(), values[2].Trim()));
            }

            if (list.Count < 3)
            {
                Console.WriteLine("Error.- Deben de existir por lo menos tres participantes...");
                return;
            }
            List<Participant> activeList = list.Where(p => p.Status.ToLower() == "activo").ToList();
            if (activeList.Count() < 3)
            {
                Console.WriteLine("Error.- Deben de existir por lo menos tres participantes " +
                    "con el campo Status en 'Activo'...");
                return;
            }
            Console.WriteLine("Participantes Activos en el sorteo");
            foreach (var participant in activeList)
                Console.WriteLine($"{participant.Id}.- {participant.Email}");

            Random random = new Random();
            int winnerIndex = random.Next(0, activeList.Count - 1);

            var winner = activeList[winnerIndex];
            activeList.RemoveAt(winnerIndex);

            Console.WriteLine($"¡{winner.Email} ha ganado una suscripción!");

            winnerIndex = random.Next(0, activeList.Count - 1);
            winner = activeList[winnerIndex];
            activeList.RemoveAt(winnerIndex);

            Console.WriteLine($"¡{winner.Email} ha ganado un descuento del 30% en la suscripción anual!");

            winnerIndex = random.Next(0, activeList.Count - 1);
            winner = activeList[winnerIndex];
            activeList.RemoveAt(winnerIndex);

            Console.WriteLine($"¡{winner.Email} ha ganado el libro de progrmación!");

            Console.WriteLine("Felicidades a los ganadores y suerte en el próximo sorteo a:");
            foreach (var participant in activeList)
                Console.WriteLine($"{participant.Id}.- {participant.Email}");
            Console.WriteLine("¡Hasta la próxima!");
        }

    }
}