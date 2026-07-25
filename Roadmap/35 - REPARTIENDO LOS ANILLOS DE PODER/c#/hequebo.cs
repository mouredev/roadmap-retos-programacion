class Distribution
{
    private int _sauron;
    private int _elves;
    private int _dwarves;
    private int _men;

    public int Sauron { get { return _sauron; } }
    public int Elves { get { return _elves; } }
    public int Dwarves {  get { return _dwarves; } }
    public int Men { get { return _men; } }

    public Distribution(int sauron, int elves, int dwarves, int men)
    {
        _sauron = sauron;
        _elves = elves;
        _dwarves = dwarves;
        _men = men;
    }
}
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("---DISTRIBUCIÓN DE ANILLOS---");
        Console.WriteLine("Ingresa un número entero de anillos a distribuir");
        int rings = 0;
        int.TryParse(Console.ReadLine(), out rings);
        if (rings == 0)
        {
            Console.WriteLine("El número de anillos no es válido...");
            return;
        }
        var distributions = DistributeRings(rings);
        if (distributions.Count() == 0)
        {
            Console.WriteLine("No se pudo distribuir los anillos correctamente...");
            return;
        }
        Console.WriteLine("---Posibles Distribuciones de los anillos---");
        foreach (var distribution in distributions)
        {
            Console.WriteLine($"Elfos: {distribution.Elves}, Enanos: {distribution.Dwarves} " +
                $"Hombres: {distribution.Men}, Sauron: {distribution.Sauron}");
        }
        Console.WriteLine("Distribucion media:");
        var mean = distributions[(int) distributions.Count() / 2];
        Console.WriteLine($"Elfos: {mean.Elves}, Enanos: {mean.Dwarves} " +
                $"Hombres: {mean.Men}, Sauron: {mean.Sauron}");
    }
    /*
     * 1. Los Elfos recibirán un número impar.
     * 2. Los Enanos un número primo.
     * 3. Los Hombres un número par.
     * 4. Sauron siempre uno.
     */
    static List<Distribution> DistributeRings(int rings)
    {
        var distributions = new List<Distribution>();
        int sauron = 1;
        rings -= sauron;

        for (int elves = 1; elves < rings; elves += 2) 
        {
            for (int men = 2; men < rings; men += 2) 
            {
                int dwarves = rings - elves - men;
                if (dwarves > 0 && IsPrime(dwarves)) 
                {
                    var distribution = new Distribution(sauron, elves, dwarves, men);
                    distributions.Add(distribution);
                }
            }
        }
        return distributions;
    }
    static bool IsPrime(int number)
    {
        if (number <= 1)
            return false;
        if (number == 2)
            return true;
        if (number % 2 == 0)
            return false;
        int limit = (int)Math.Sqrt(number);
        for (int i = 3; i < limit; i += 2)
        {
            if (number % i == 0)
                return false;

        }
        return true;
    }

}