/*
 * EJERCICIO:
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
 */

namespace Roadmap
{
    internal class Reto17
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 10;  i++)
                Console.WriteLine(i.ToString());

            Console.WriteLine();

            int counter = 1;
            while (counter <= 10)
            {
                Console.WriteLine(counter.ToString());
                counter++;
            }

            Console.WriteLine();

            counter = 1;
            do
            {
                Console.WriteLine(counter.ToString());
                counter++;
            } while (counter <= 10);

            Console.WriteLine();

            // Reto extra
            int[] numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            foreach (int number in numbers)
                Console.WriteLine(number.ToString());

            Console.WriteLine();

            Iterar1al10(1);
        }

        static void Iterar1al10(int number)
        {
            if (number <= 10)
            {
                Console.WriteLine(number.ToString());
                Iterar1al10(++number);
            }
        }
    }
}
