using System;

class miguelex
{
    static bool EsPrimo(int num)
    {
        if (num <= 1) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;

        for (int i = 3; i <= Math.Sqrt(num); i += 2)
        {
            if (num % i == 0) return false;
        }
        return true;
    }

    static string RepartirAnillos(int totalAnillos)
    {
        if (totalAnillos < 4)
        {
            return "Error: No hay suficientes anillos para cumplir con los requisitos.";
        }

        int anillosSauron = 1;
        totalAnillos -= 1;

        int mejorDiferencia = int.MaxValue;
        int[] mejorReparto = null;

        for (int anillosElfos = 1; anillosElfos <= totalAnillos; anillosElfos += 2)
        {
            for (int anillosEnanos = 2; anillosEnanos <= totalAnillos; anillosEnanos++)
            {
                if (EsPrimo(anillosEnanos))
                {
                    int anillosHombres = totalAnillos - anillosElfos - anillosEnanos;

                    if (anillosHombres > 0 && anillosHombres % 2 == 0)
                    {
                        int diferencia = Math.Max(anillosElfos, Math.Max(anillosEnanos, anillosHombres)) -
                                         Math.Min(anillosElfos, Math.Min(anillosEnanos, anillosHombres));

                        if (diferencia < mejorDiferencia)
                        {
                            mejorDiferencia = diferencia;
                            mejorReparto = new int[] { anillosElfos, anillosEnanos, anillosHombres, anillosSauron };
                        }
                    }
                }
            }
        }

        if (mejorReparto != null)
        {
            return $"Reparto exitoso: Elfos = {mejorReparto[0]}, Enanos = {mejorReparto[1]}, Hombres = {mejorReparto[2]}, Sauron = {mejorReparto[3]}";
        }
        else
        {
            return "Error: No se encontró una combinación válida para repartir los anillos.";
        }
    }

    static void Main(string[] args)
    {
        Console.Write("Ingresa el número total de anillos: ");
        int totalAnillos = int.Parse(Console.ReadLine());

        string resultado = RepartirAnillos(totalAnillos);
        Console.WriteLine(resultado);
    }
}
