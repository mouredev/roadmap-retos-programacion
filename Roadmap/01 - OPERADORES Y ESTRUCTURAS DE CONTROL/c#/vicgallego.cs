/*
 * EJERCICIO:
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
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Roadmap_01
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int a = 4; int b = 9;
           

            Console.WriteLine(a + b);
            Console.WriteLine(a - b);
            Console.WriteLine(a * b);   
            Console.WriteLine(a / b);
            Console.WriteLine(a % b);
            Console.WriteLine("\n");


            // Lógicos
            bool x = true;
            bool y = false;

         bool resultado_and = x && y;
         bool resultado_or = x || y;         
         bool resultado_not = !x;

            Console.WriteLine(resultado_not);
            Console.WriteLine(resultado_or);
            Console.WriteLine(resultado_and);

            Console.WriteLine("\n");

            // Asignación
            int c = 5;

            c += 2;  // Equivalente a: a = a + 2
            Console.WriteLine(c);

            c -= 3;  // Equivalente a: a = a - 3
            Console.WriteLine(c);

            c *= 4;  // Equivalente a: a = a * 4
            Console.WriteLine(c);

            c /= 2;  // Equivalente a: a = a / 2
            Console.WriteLine(c);

            Console.WriteLine("\n");

            int num1 =10 ; int num2 = 55;

            for(int i = 10; i <= num2 ; i++)
            {
                if (i % 2 == 0 && i != 16 && i % 3 != 0)
                {
                    Console.WriteLine(i);
                }
            }
        }
    }
}