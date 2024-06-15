using System.Threading.Channels;

namespace _01_OPERADORES_Y_ESTRUCTURAS_DE_CONTROL
{
    internal class Program
    {
        static void Main(string[] args)
        {
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

            // Operadores aritméticos
            int a = 10;
            int b = 3;
            Console.WriteLine("Operadores aritméticos:");
            Console.WriteLine($"Suma: {a + b}");
            Console.WriteLine($"Resta: {a - b}");
            Console.WriteLine($"Multiplicación: {a * b}");
            Console.WriteLine($"División: {a / b}");
            Console.WriteLine($"Módulo: {a % b}");

            // Operadores lógicos
            bool verdad = true;
            bool falso = false;
            Console.WriteLine("\nOperadores lógicos:");
            Console.WriteLine($"AND: {verdad && falso}");
            Console.WriteLine($"OR: {verdad || falso}");
            Console.WriteLine($"NOT: {!verdad}");

            // Operadores de comparación
            Console.WriteLine("\nOperadores de comparación:");
            Console.WriteLine($"Igual a: {a == b}");
            Console.WriteLine($"Distinto de: {a != b}");
            Console.WriteLine($"Mayor que: {a > b}");
            Console.WriteLine($"Menor que: {a < b}");
            Console.WriteLine($"Mayor o igual que: {a >= b}");
            Console.WriteLine($"Menor o igual que: {a <= b}");

            // Operadores de asignación
            int c = 5;
            Console.WriteLine("\nOperadores de asignación:");
            c += 3;
            Console.WriteLine($"c += 3: {c}");
            c -= 2;
            Console.WriteLine($"c -= 2: {c}");
            c *= 2;
            Console.WriteLine($"c *= 2: {c}");
            c /= 4;
            Console.WriteLine($"c /= 4: {c}");
            c %= 3;
            Console.WriteLine($"c %= 3: {c}");

            // Operadores de identidad
            object x = new object();
            object y = x;
            object z = new object();
            Console.WriteLine("\nOperadores de identidad:");
            Console.WriteLine($"x es y: {ReferenceEquals(x, y)}");
            Console.WriteLine($"x es z: {ReferenceEquals(x, z)}");

            // Operadores de pertenencia
            int[] array = { 1, 2, 3, 4, 5 };
            Console.WriteLine("\nOperadores de pertenencia:");
            Console.WriteLine($"3 en array: {Array.Exists(array, element => element == 3)}");
            Console.WriteLine($"6 en array: {Array.Exists(array, element => element == 6)}");

            // Operadores de bits
            int bit1 = 6; // 110 en binario
            int bit2 = 3; // 011 en binario
            Console.WriteLine("\nOperadores de bits:");
            Console.WriteLine($"AND bit a bit: {bit1 & bit2}"); // 010
            Console.WriteLine($"OR bit a bit: {bit1 | bit2}");  // 111
            Console.WriteLine($"XOR bit a bit: {bit1 ^ bit2}"); // 101
            Console.WriteLine($"NOT bit a bit: {~bit1}");       // 001...1010
            Console.WriteLine($"Desplazamiento a la izquierda: {bit1 << 1}"); // 1100
            Console.WriteLine($"Desplazamiento a la derecha: {bit1 >> 1}");   // 11

            // Estructuras de control: Condicional
            Console.WriteLine("\nEstructuras de control: Condicional");
            if (a > b)
            {
                Console.WriteLine("a es mayor que b");
            }
            else
            {
                Console.WriteLine("a no es mayor que b");
            }

            // Estructuras de control: Iterativa (for)
            Console.WriteLine("\nEstructuras de control: Iterativa (for)");
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine($"Iteración for: {i}");
            }

            // Estructuras de control: Iterativa (while)
            Console.WriteLine("\nEstructuras de control: Iterativa (while)");
            int j = 0;
            while (j < 5)
            {
                Console.WriteLine($"Iteración while: {j}");
                j++;
            }

            // Estructuras de control: Iterativa (do-while)
            Console.WriteLine("\nEstructuras de control: Iterativa (do-while)");
            int k = 0;
            do
            {
                Console.WriteLine($"Iteración do-while: {k}");
                k++;
            } while (k < 5);

            // Estructuras de control: Manejo de excepciones
            Console.WriteLine("\nEstructuras de control: Manejo de excepciones");
            try
            {
                int divisionPorCero = a / 0;
            }
            catch (DivideByZeroException e)
            {
                Console.WriteLine($"Excepción atrapada: {e.Message}");
            }

            Console.WriteLine("\nCiclo FOR para dificultad extra");  // Ciclo for para pasar por una lista ENTRE 10 Y 55 (INCLUIDOS) con diferentes condiciones (PAR, DIFERENTE A 16 Y MULTIPLOS DE 3) 

            for(int i = 10; i <= 55; i++)
            {
                if(i % 2 == 0)
                {
                    if(i != 16)
                    {
                        if(i % 3 != 0)
                        {
                            Console.WriteLine(i);
                        }
                    }
                }
            }
        }
    }
}
