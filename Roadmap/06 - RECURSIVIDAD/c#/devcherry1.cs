using System;

class Program
{
    static void Main()
    {
        contador(100);
        Console.WriteLine("Indique la posicion en la serie Fibonacci: ");
        int serie;
        int.TryParse(Console.ReadLine(), out serie);
        Console.WriteLine(Extra.Fibonacci(serie));
        int factor;
        int.TryParse(Console.ReadLine(), out factor);
        Console.WriteLine(Extra.Factorial(factor));
    }
    static void contador(int limite)
    {
        if (limite == 0)
        {
            Console.WriteLine(limite);
            return;
        }
        Console.WriteLine(limite);
        contador(limite - 1);
    }
}
class Extra
{
    public static int Fibonacci(int posicion)
    {
        // Casos base
        if (posicion == 0) return 0;
        if (posicion == 1) return 1;

        // Caso recursivo
        return Fibonacci(posicion - 1) + Fibonacci(posicion - 2);
    }
    public static int Factorial(int numero)
    {
        if (numero == 0) return 1;

        return numero * Factorial(numero - 1);
    }
}
