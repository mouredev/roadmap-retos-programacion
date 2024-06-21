/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

using System;

namespace Roadmap17
{
    class Iterations
    {
        // Primera forma: ciclo for
        static void ForLoop()
        {
            for (int i = 1; i <= 10; i++)
            {
                Console.WriteLine(i);
            }
        }

        // Segunda forma: ciclo while
        static void WhileLoop()
        {
            int i = 1;
            while (i <= 10)
            {
                Console.WriteLine(i);
                i++;
            }
        }

        // Tercera forma: ciclo do-while
        static void DoWhileLoop()
        {
            int i = 1;
            do
            {
                Console.WriteLine(i);
                i++;
            } while (i <= 10);
        }

        // Cuarta forma: ciclo foreach
        static void ForEachLoop()
        {
            int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            foreach (int number in numbers)
            {
                Console.WriteLine(number);
            }
        }

        // Quinta forma: ciclo foreach con rangos
        static void ForEachRangeLoop()
        {
            foreach (int number in Enumerable.Range(1, 10))
            {
                Console.WriteLine(number);
            }
        }

        static void Main(string[] args)
        {
            Console.WriteLine("For Loop:");
            ForLoop();

            Console.WriteLine("\nWhile Loop:");
            WhileLoop();

            Console.WriteLine("\nDo-While Loop:");
            DoWhileLoop();
        }
    }
}
