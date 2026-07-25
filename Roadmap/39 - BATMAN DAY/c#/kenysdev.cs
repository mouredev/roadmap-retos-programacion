namespace exs39;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
BATMAN DAY
------------------------------------

* RETO 1:
* Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
* su 100 aniversario.
*/

public class BatmanDay
{
    private static string ThirdSaturdayOfSeptember(int year)
    {
        var date = new DateTime(year, 9, 15);
        int daysToAdd = ((int)DayOfWeek.Saturday - (int)date.DayOfWeek + 7) % 7;
        date = date.AddDays(daysToAdd);
        return date.ToString("dd-MM-yyyy");
    }

    public static void CalculateAnniversaryDates(int totalAnniversaries)
    {
        Console.WriteLine("Batman Day");
        const int batmanDayStart = 2014;
        int currentYear = DateTime.Today.Year;

        if (currentYear < batmanDayStart)
        {
            Console.WriteLine("xd");
            return;
        }

        int pastAnniversaries = currentYear - batmanDayStart;
        Console.WriteLine($"Aniversarios que ya han pasado: {pastAnniversaries}");

        for (int i = 0; i < totalAnniversaries - pastAnniversaries; i++)
        {
            int num = pastAnniversaries + i + 1;
            string theDate = ThirdSaturdayOfSeptember(currentYear);
            Console.WriteLine($"- Aniversario #{num}: {theDate}");
            currentYear++;
        }
    }

    /*
     * RETO 2:
     * Crea un programa que implemente el sistema de seguridad de la Batcueva. 
     * Este sistema está diseñado para monitorear múltiples sensores distribuidos
     * por Gotham, detectar intrusos y activar respuestas automatizadas. 
     * Cada sensor reporta su estado en tiempo real, y Batman necesita un programa 
     * que procese estos datos para tomar decisiones estratégicas.
     * Requisitos:
     * - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
     * - Cada sensor se identifica con una coordenada (x, y) y un nivel
     *   de amenaza entre 0 a 10 (número entero).
     * - Batman debe concentrar recursos en el área más crítica de Gotham.
     * - El programa recibe un listado de tuplas representando coordenadas de los 
     *   sensores y su nivel de amenaza. El umbral de activación del protocolo de
     *   seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
     * Acciones: 
     * - Identifica el área con mayor concentración de amenazas
     *   (sumatorio de amenazas en una cuadrícula 3x3).
     * - Si el sumatorio de amenazas es mayor al umbral, activa el 
     *   protocolo de seguridad.
     * - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
     *   la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
     * - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
     *   sus amenazas, la distancia a la Batcueva y si se debe activar el
     *   protocolo de seguridad.
    */

    static string[,] CreateMap((int, int) size, (int, int) batcave, List<(int, int, int)> sensors, List<(int, int)> threats)
    {
        var gotham = new string[size.Item1, size.Item2];
        for (int i = 0; i < size.Item1; i++)
            for (int j = 0; j < size.Item2; j++)
                gotham[i,j] = "| ";
        
        gotham[batcave.Item1, batcave.Item2] = "|B";
        
        foreach (var s in sensors)
            gotham[s.Item1, s.Item2] = "|S";
        
        foreach (var t in threats)
            gotham[t.Item1, t.Item2] = "|T";
        
        return gotham;
    }

    static void PrintMap(string[,] gotham, (int, int) size)
    {
        Console.WriteLine("\nMapa de Gotham:");
        for (int i = 0; i < size.Item1; i++)
        {
            for (int j = 0; j < size.Item2; j++)
                Console.Write(gotham[i,j]);
            Console.WriteLine();
        }
    }

    static void ScanMap(string[,] gotham, List<(int, int, int)> sensors, (int, int) size)
    {
        var dangerList = new List<(int, int)>();

        for (int c = 0; c < sensors.Count; c++)
        {
            var s = sensors[c];
            int dangerCounter = 0;

            for (int i = s.Item1 - 1; i <= s.Item1 + 1; i++)
                for (int j = s.Item2 - 1; j <= s.Item2 + 1; j++)
                    if (i >= 0 && i < size.Item1 && j >= 0 && j < size.Item2 && gotham[i,j] == "|T")
                        dangerCounter += s.Item3;

            dangerList.Add((c, dangerCounter));
        }

        var maxDanger = dangerList.MaxBy(x => x.Item2);
        var location = sensors[maxDanger.Item1];

        Console.WriteLine("\nInforme:");
        Console.WriteLine($"Cuadrícula más amenazada: '{location.Item1}, {location.Item2}'");
        Console.WriteLine($"Máximo nivel de alerta: '{maxDanger.Item2}'");

        if (maxDanger.Item2 >= 20)
        {
            Console.WriteLine("Protocolo de seguridad activado.");
            Console.WriteLine($"Distancia: '{location.Item1 + location.Item2}'");
        }
        else
            Console.WriteLine("No hay amenazas relevantes.");
    }

    public static void Main()
    {
        CalculateAnniversaryDates(100);

        // exs #2
        var size = (20, 20);
        var batcave = (0, 0);
        var sensors = new List<(int, int, int)> { (2, 2, 10), (6, 8, 9), (10, 12, 8), (17, 15, 7) };
        var threats = new List<(int, int)> { (2, 3), (2, 1), (6, 9), (17, 16), (15, 4) };

        var gotham = CreateMap(size, batcave, sensors, threats);
        PrintMap(gotham, size);
        ScanMap(gotham, sensors, size);
    }
}
