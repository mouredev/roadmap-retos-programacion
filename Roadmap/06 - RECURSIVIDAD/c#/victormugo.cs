using System.Xml.Linq;

namespace _06_recursividad
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * EJERCICIO:
             * Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.
             *
             * DIFICULTAD EXTRA (opcional):
             * Utiliza el concepto de recursividad para:
             * - Calcular el factorial de un número concreto (la función recibe ese número).
             * - Calcular el valor de un elemento concreto (según su posición) en la 
             *   sucesión de Fibonacci (la función recibe la posición).
             */

            // Entiende el concepto de recursividad creando una función recursiva que imprima números del 100 al 0.
            _RecusiveFunction(100);


            // ---------------------------------------------------------------------------------
            // ---------------------------------------------------------------------------------


            // Utiliza el concepto de recursividad para:
            //      Calcular el factorial de un número concreto(la función recibe ese número).
            int result = 0;
            int factorial = 12;
            result = _RecursiveFactorial(factorial);
            Console.WriteLine($"Factorial de {factorial} es: {result}");

            //      Calcular el valor de un elemento concreto(según su posición) en la sucesión de Fibonacci(la función recibe la posición).
            int position = 10;
            result = _RecursiveFibonacci(position);
            Console.WriteLine($"Posición en la serie de Fibonacci es: {result}");
        }

        private static void _RecusiveFunction(int value)
        {
            Console.WriteLine(value);
            if (value == 0) return;

            value--;

            _RecusiveFunction(value);
        }

        private static int _RecursiveFactorial(int factorial)
        {
            if (factorial <= 1) return 1;
            return factorial * _RecursiveFactorial(factorial-1);
        }

        private static int _RecursiveFibonacci(int position)
        {
            // 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

            if (position == 0)
            {
                return 0;
            }
            else if (position == 1)
            {
                return 1;
            }

            return _RecursiveFibonacci(position - 1) + _RecursiveFibonacci(position - 2);

        }

    }
}
