using System;

namespace Alfarog507
{
    class Program
    {
        static void Main(string[] args)
        {
            /*EJERCICIO:
            * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
            *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
            *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
            * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
            *   que representen todos los tipos de estructuras de control que existan
            *   en tu lenguaje:
            *   Condicionales, iterativas, excepciones...
            * - Debes hacer print por consola del resultado de todos los ejemplos.
            *
            * DIFICULTAD EXTRA (opcional):
            * Crea un programa que imprima por consola todos los números comprendidos
            * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
            *
            * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.*/

            //Operadores aritméticos
            int a = 5;
            int b = 3;
            Console.WriteLine("Operadores aritméticos");
            Console.WriteLine("Suma: " + (a + b));
            Console.WriteLine("Resta: " + (a - b));
            Console.WriteLine("Multiplicación: " + (a * b));
            Console.WriteLine("División: " + (a / b));
            Console.WriteLine("Módulo: " + (a % b));

            //Operadores lógicos
            bool c = true;
            bool d = false;
            Console.WriteLine("\nOperadores lógicos");
            Console.WriteLine("AND: " + (c && d));
            Console.WriteLine("OR: " + (c || d));
            Console.WriteLine("NOT: " + (!c));

            //Operadores de comparación
            Console.WriteLine("\nOperadores de comparación");
            Console.WriteLine("Igualdad: " + (a == b));
            Console.WriteLine("Desigualdad: " + (a != b));
            Console.WriteLine("Mayor que: " + (a > b));
            Console.WriteLine("Menor que: " + (a < b));
            Console.WriteLine("Mayor o igual que: " + (a >= b));
            Console.WriteLine("Menor o igual que: " + (a <= b));

            //Operadores de asignación
            Console.WriteLine("\nOperadores de asignación");
            Console.WriteLine("Asignación: " + (a = b));
            Console.WriteLine("Suma y asignación: " + (a += b));
            Console.WriteLine("Resta y asignación: " + (a -= b));
            Console.WriteLine("Multiplicación y asignación: " + (a *= b));
            Console.WriteLine("División y asignación: " + (a /= b));
            Console.WriteLine("Módulo y asignación: " + (a %= b));

            //Operadores de identidad
            Console.WriteLine("\nOperadores de identidad");
            Console.WriteLine("Igualdad: " + (a == b));
            Console.WriteLine("Desigualdad: " + (a != b));

            //Operadores de pertenencia
            Console.WriteLine("\nOperadores de pertenencia");
            int[] array = { 1, 2, 3, 4, 5 };
            Console.WriteLine("Pertenece: " + (Array.IndexOf(array, 3) != -1));
            Console.WriteLine("No pertenece: " + (Array.IndexOf(array, 6) == -1));

            //Operadores de bits
            Console.WriteLine("\nOperadores de bits");
            Console.WriteLine("AND: " + (a & b));
            Console.WriteLine("OR: " + (a | b));
            Console.WriteLine("XOR: " + (a ^ b));
            Console.WriteLine("Desplazamiento a la izquierda: " + (a << 1));
            Console.WriteLine("Desplazamiento a la derecha: " + (a >> 1));

            //Estructuras de control
            Console.WriteLine("\nEstructuras de control");
            //Condicionales
            if (a == b)
            {
                Console.WriteLine("a es igual a b");
            }
            else if (a > b)
            {
                Console.WriteLine("a es mayor que b");
            }
            else
            {
                Console.WriteLine("a es menor que b");
            }

            //Iterativas
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine("Iteración " + i);
            }

            //Excepciones
            try
            {
                int zero = 0;
                int division = 5 / zero;
            }
            catch (DivideByZeroException e)
            {
                Console.WriteLine("Error: " + e.Message);
            }

            //Dificultad extra
            Console.WriteLine("\nDificultad extra");
            for (int i = 10; i <= 55; i++)
            {
                if (i % 2 == 0 && i != 16 && i % 3 != 0)
                {
                    Console.WriteLine(i);
                }
            }

            Console.ReadKey();


        }
    }
}