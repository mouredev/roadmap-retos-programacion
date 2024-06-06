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
namespace estuardodev
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            countdown(100);
            Console.WriteLine("Factorial: " + factorial(5));
            Console.WriteLine("Número fibonacci en valor concreto: " + fibonacci(5));
        }

        // Ejercicio
        static void countdown(int contador)
        {
            if (contador >= 0) 
            {
                Console.WriteLine(contador);
                countdown(contador - 1);
            }
        }

        // Extra
        static int factorial(int numero)
        {
            if (numero < 0)
            {
                return 0;
            } else if (numero == 0) 
            {
                return 1;
            }
            
            return numero * factorial(numero - 1);
        }

        static int fibonacci(int numero)
        {
            if (numero <= 0)
            {
                return 0;
            } else if (numero == 1)
            {
                return 0;
            } else if (numero == 2)
            {
                return 1;
            }
            else
            {
                 return fibonacci(numero - 1) + fibonacci(numero - 2);
            }
        }

    }
}