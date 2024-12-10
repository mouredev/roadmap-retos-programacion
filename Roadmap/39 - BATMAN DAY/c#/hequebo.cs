// Reto # 1
class BatmanAnniversary
{
    private int _anniversaryYear;
    private int _anniversary;
    private DateTime _anniversaryDate;

    public int AnniversaryYear { get { return _anniversaryYear; } }
    public int Anniversary { get { return _anniversary; } }
    public DateTime AnniversaryDate { get {  return _anniversaryDate; } }

    public BatmanAnniversary(int anniversaryYear, int anniversary, DateTime anniversaryDate)
    {
        _anniversaryYear = anniversaryYear;
        _anniversary = anniversary;
        _anniversaryDate = anniversaryDate;
    }
}
class Program
{
    static void Main(string[] args)
    {
        int yearOfCreation = 1939;
        int anniversaryYear = yearOfCreation + 85;

        var anniversaryList = new List<BatmanAnniversary>();
        while (anniversaryYear <= yearOfCreation + 100)
        {
            var september = new DateTime(anniversaryYear, 9, 1);
            if (september.DayOfWeek == DayOfWeek.Saturday)
            {
                september = september.AddDays(14);
                var anniversary = new BatmanAnniversary(anniversaryYear, anniversaryYear - yearOfCreation, september);
                anniversaryList.Add(anniversary);
            }
            else
            {
                int firstSaturday = september.Day + 6 - (int)september.DayOfWeek;
                september = new DateTime(anniversaryYear, 9, firstSaturday);

                september = september.AddDays(14);
                var anniversary = new BatmanAnniversary(anniversaryYear, anniversaryYear - yearOfCreation, september);
                anniversaryList.Add(anniversary);
            }
            anniversaryYear++;
        }

        Console.WriteLine("Próximos aniversarios de Batman hasta el No. 100");
        foreach (var anniversary in anniversaryList)
            Console.WriteLine($"Año: {anniversary.AnniversaryYear} Aniversario: {anniversary.Anniversary} " +
                $"Fecha: {anniversary.AnniversaryDate.ToShortDateString()}");

        // Reto #2

        List<(int, int, int)> sensors = new List<(int, int, int)>
        {
            (2, 3, 7),
            (4, 3, 8),
            (2, 2, 7),
            (10, 12, 8),
            (11, 11, 8),
            (10, 11, 8),
            (15, 18, 4)
        };

        var result = BatcaveSecuritySistem(sensors);
        Console.WriteLine($"Centro cuadrícula con más amenaza: {result.Item1.Item1}, {result.Item1.Item2}");
        Console.WriteLine($"Máximo nivel de alerta: {result.Item2}");
        Console.WriteLine($"Distancia a la Baticueva: {result.Item3}");
        Console.WriteLine($"Activar protocolo de emergencia: {(result.Item4 ? "Sí" : "No")}");
    }
    static int SumAlerts(List<(int, int, int)> sensors, int centerX, int centerY)
    {
        int total = 0;

        for (int i = centerX - 1; i <= centerX + 1; i++)
        {
            for (int j = centerY - 1; j <= centerY + 1; j++)
            {
                foreach(var sensor in sensors)
                {
                    if (sensor.Item1 == i && sensor.Item2 == j)
                        total += sensor.Item3;
                }
            }
        }
        return total;
    }
    static ((int, int), int, int, bool) BatcaveSecuritySistem(List<(int, int, int)> sensors)
    {
        int maxAlertLevel = 0;
        (int, int) maxAlertCoordinates = (0, 0);

        for (int i = 0; i <= 19;  i++)
        {
            for (int j = 0; j  <= 19; j++)
            {
                int alertLevel = SumAlerts(sensors, i, j);
                if (alertLevel > maxAlertLevel)
                {
                    maxAlertLevel = alertLevel;
                    maxAlertCoordinates = (i, j);
                }
            }
        }

        int distance = Math.Abs(maxAlertCoordinates.Item1) + Math.Abs(maxAlertCoordinates.Item2);
        bool activateProtocol = maxAlertLevel > 20;


        return (maxAlertCoordinates, maxAlertLevel, distance, activateProtocol);
    }
}