class AdventCalendar
{
    private bool[] _days = new bool[24];

    public AdventCalendar() 
    {
        for (int i = 0; i < 24; i++)
        {
            _days[i] = false;
        }
    }
    public void Display()
    {
        string line = string.Join("\t", Enumerable.Repeat("****", 6));
        for (int i = 0; i < 4;i++)
        {
            Console.Write($"{line}\n");
            for (int j = i * 6; j < (i * 6) + 6; j++)
                Console.Write($"*{(!_days[j] ? (j < 9 ? $"0{j + 1}" : j +1 ) : "**")}*\t");
            
            Console.Write($"\n{line}\n\n");
        }
    }
    public void SelectDay(int day)
    {
        if (day <= 0 || day > 24)
        {
            Console.WriteLine("El día debe estar entre 1 y 24...");
            return;
        }
        if (_days[day - 1])
        {
            Console.WriteLine($"El día {day} ya ha sido revelado");
            return;
        }
        _days[day - 1] = true;
        Console.WriteLine($"Has abierto el día {day}");
    }

}
class Program
{
    static void Main(string[] args)
    {
        var calendar = new AdventCalendar();
        bool exit = false;
        do
        {
            Console.WriteLine("-----------CALENDARIO DE ADVIENTO-----------");
            calendar.Display();
            Console.WriteLine("Selecciona el día que quieras descubir o escribe 'salir' para finalizar");

            string? input = Console.ReadLine();
            Console.Clear();
            if (input.ToLower() == "salir")
            {
                exit = true;
                Console.WriteLine("Hasta la próxima...");
            }
            else
            {
                int.TryParse(input, out int option);
                calendar.SelectDay(option);
            }
        } while (!exit);

    }
}