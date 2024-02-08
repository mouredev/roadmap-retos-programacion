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

class Program 
{
    static void Main() 
    {
        Console.WriteLine("Printing numbers");
        Solution.PrintingNumbers(100);
        Console.WriteLine("");
        Console.WriteLine("Factorial");
        Console.WriteLine(Solution.Factorial(10));
        Console.WriteLine("");
        Console.WriteLine("Fibonacci");
        Console.WriteLine(Solution.Fibonacci(15));
        Console.Read();

    }
}


public static class Solution
{ 
    //Method to print numbers from a given number to 0
    public static void PrintingNumbers(int num) 
    {

        if (num >= 0)
        {
            Console.Write(num+" ");
            PrintingNumbers(num - 1);
        }
    }

    public static BigInteger Factorial(int num) 
    {
        if (num == 0 || num == 1) 
        {
            return 1;
        }
        return BigInteger.Multiply(num,Factorial(num-1));
    }

    //Using unsigned types
    public static ulong Fibonacci(uint num) 
    {
        if (num == 1 || num == 2)
        {
            return 1;
        }

        return Fibonacci(num - 1) + Fibonacci(num - 2);

    }
}