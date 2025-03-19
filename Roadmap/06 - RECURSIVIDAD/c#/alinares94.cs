/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */

using System.Numerics;
Console.WriteLine("#####################################");
Console.WriteLine("######### 01 - Print n to 0 #########");
Console.WriteLine("#####################################");
Console.WriteLine();
Console.WriteLine("Example for n=100");
PrintNumbers(100);
Console.WriteLine();
Console.WriteLine();

Console.WriteLine("#####################################");
Console.WriteLine("######### 02 - Factorial n! #########");
Console.WriteLine("#####################################");
Console.WriteLine();
Console.WriteLine("Example for n=5");
Console.WriteLine(Factorial(5));
Console.WriteLine("Example for n=50");
Console.WriteLine(Factorial(50).ToString("E"));
Console.WriteLine();

Console.WriteLine("#####################################");
Console.WriteLine("#### 03 - Fibonacci starting at 1 ###");
Console.WriteLine("#####################################");
Console.WriteLine();
Console.WriteLine("Example for n=5");
Console.WriteLine(Fibonacci(5));
Console.WriteLine("Example for n=15");
Console.WriteLine(Fibonacci(15));
Console.WriteLine();

// Print n to 0
static void PrintNumbers(int n)
{
    if (n < 0)
        return;
    Console.Write($"{n} ");
    PrintNumbers(n-1);
}

// Calculate n!
static BigInteger Factorial(uint n)
{
    if (n.Equals(0) || n.Equals(1))
        return 1;

    return BigInteger.Multiply(n, Factorial(n-1));
}

// Print n-item in fibonacci sequence starting at 1
static ulong Fibonacci(uint n)
{
    if (n.Equals(0))
        throw new ArgumentOutOfRangeException(nameof(n), "Input should be greather than 0");
    if (n.Equals(1) || n.Equals(2))
        return 1;

    return Fibonacci(n-1)+Fibonacci(n-2);
}