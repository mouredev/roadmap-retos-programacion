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

namespace RetosProgramacion2024
{
    internal class Reto6
    {
        static void Main(string[] args)
        {
            ImprimirNumero(100);
            Console.WriteLine("\nFactorial");
            Console.WriteLine(Factorial(10));
            Console.WriteLine("\nFibonacci");
            Console.WriteLine(Fibonacci(10));
        }

        private static void ImprimirNumero(int numero)
        {
            Console.WriteLine(numero--);
            if (numero >= 1)
                ImprimirNumero(numero);
        }

        private static int Factorial(int numero)
        {
            if (numero == 1)
                return 1;

            return numero *= Factorial(--numero);
        }

        private static int Fibonacci(int pos)
        {
            if (pos < 2)
                return pos;
            else
                return Fibonacci(pos - 1) + Fibonacci(pos - 2);
  
        }
    }
}
