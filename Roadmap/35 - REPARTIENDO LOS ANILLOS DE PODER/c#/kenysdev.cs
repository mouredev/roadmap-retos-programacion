namespace exs35;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
35 REPARTIENDO LOS ANILLOS DE PODER
------------------------------------
¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse!
¿Qué pasaría si tuvieras que encargarte de repartir los anillos
entre las razas de la Tierra Media?
Desarrolla un programa que se encargue de distribuirlos.
Requisitos:
1. Los Elfos recibirán un número impar.
2. Los Enanos un número primo.
3. Los Hombres un número par.
4. Sauron siempre uno.
Acciones:
1. Crea un programa que reciba el número total de anillos
   y busque una posible combinación para repartirlos.
2. Muestra el reparto final o el error al realizarlo.
*/

class Program
{
    static int GetTotalRings()
    {
        while (true)
        {
            Console.Write("Cantidad de anillos: ");
            if (int.TryParse(Console.ReadLine(), out int result) && result >= 1)
            {
                return result;
            }
            Console.WriteLine("Debe ser un valor entero '>= 1'.");
        }
    }

    static bool IsPrime(int n)
    {
        if (n < 2) return false;
        for (int i = 2; i <= Math.Sqrt(n); i++)
        {
            if (n % i == 0) return false;
        }
        return true;
    }

    static List<(int, int, int)> Distribute(int total)
    {
        var combinations = new List<(int, int, int)>();
        for (int elves = 1; elves < total; elves += 2)
        {
            for (int men = 2; men < total; men += 2)
            {
                int dwarves = total - (men + elves);
                if (dwarves > 0 && IsPrime(dwarves))
                {
                    combinations.Add((elves, men, dwarves));
                }
            }
        }
        return combinations;
    }

    static double StandardDeviation(Tuple<int, int, int> tup)
    {
        double[] values = [tup.Item1, tup.Item2, tup.Item3];
        double avg = values.Average();
        double sum = values.Sum(d => Math.Pow(d - avg, 2));
        return Math.Sqrt(sum / (values.Length - 1));
    }

    static (int, int, int) TheMostBalanced(List<(int, int, int)> combinations)
    {
        return combinations.OrderBy(c => StandardDeviation(Tuple.Create(c.Item1, c.Item2, c.Item3))).First();
    }

    static void PrintResult((int elves, int men, int dwarves) distribution, int sauron)
    {
        if (distribution == default)
        {
            Console.WriteLine("Error en la selección equitativa.");
            return;
        }

        Console.WriteLine("_________________________");
        Console.WriteLine($"Elfos   -> {distribution.elves} : # Impar");
        Console.WriteLine($"Enanos  -> {distribution.dwarves} : # Primo");
        Console.WriteLine($"Hombres -> {distribution.men} : # Par");
        Console.WriteLine($"Sauron  -> {sauron} : # Fijo");
        Console.WriteLine("-------------------------");
    }

    static void Main()
    {
        Console.WriteLine("REPARTIENDO LOS ANILLOS DE PODER");
        int total = GetTotalRings();
        int sauron = 1;
        total -= sauron;

        var combinations = Distribute(total);
        if (combinations.Count == 0)
        {
            Console.WriteLine("No existe una combinación posible.");
            return;
        }

        var distribution = TheMostBalanced(combinations);
        PrintResult(distribution, sauron);
    }
}
