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

using System;
class Recursion
{

    static void PrintNumbers(int n = 100)
    {
        if (n >= 0)
        {
            Console.Write($"{n} -> llamo a PrintNumbers({n - 1})\n");
            PrintNumbers(n - 1);
        }
        else
        {
            Console.WriteLine("Fin de la recursión :D");
        }
    }

    static int Factorial(int n)
    {
        if (n == 0)
        {
            return 1;
        }
        else
        {
            return n * Factorial(n - 1);
        }
    }

    static int Fibonacci(int n)
    {
        if (n == 0)
        {
            return 0;
        }
        else if (n == 1)
        {
            return 1;
        }
        else
        {
            return Fibonacci(n - 1) + Fibonacci(n - 2);
        }
    }

    static void Extra()
    {
        Console.WriteLine("Factorial de 5: " + Factorial(5));
        Console.WriteLine("Número 11 de la sucesión de Fibonacci: " + Fibonacci(11));
    }

    static void Main()
    {
        Console.WriteLine("========================================");
        Console.WriteLine("============== RECURSIVIDAD ============");
        Console.WriteLine("========================================\n");
        PrintNumbers();
        Console.WriteLine("\n========================================\n");
        Console.WriteLine("============ EJERCICIO EXTRA ===========");
        Console.WriteLine("========================================\n");
        Extra();
    }
}
