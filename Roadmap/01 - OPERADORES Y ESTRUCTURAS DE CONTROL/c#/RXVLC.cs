using System;
using System.Linq;

namespace R01___2024
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

            //aritméticos
            int a = 10;
            int b = 5;
            int suma = a + b;       // Suma
            int resta = a - b;      // Resta
            int multiplicacion = a * b;  // Multiplicación
            int division = a / b;        // División
            int modulo = a % b;          // Módulo

            //lógicos
            bool condicion1 = true;
            bool condicion2 = false;

            bool resultadoAnd = condicion1 && condicion2;  // AND lógico
            bool resultadoOr = condicion1 || condicion2;   // OR lógico
            bool resultadoNot = !condicion1;              // NOT lógico

            //de comparación
            int x = 5;
            int y = 10;

            bool igual = x == y;      // Igual a
            bool diferente = x != y;  // Diferente de
            bool mayorQue = x > y;    // Mayor que
            bool menorQue = x < y;    // Menor que
            bool mayorIgual = x >= y; // Mayor o igual que
            bool menorIgual = x <= y; // Menor o igual que

            //de asignación
            int num = 10;
            num += 5;   // num = num + 5;
            num -= 3;   // num = num - 3;
            num *= 2;   // num = num * 2;
            num /= 4;   // num = num / 4;
            num %= 2;   // num = num % 2;

            //de momento no controlo identidad

            //de pertenencia
            int[] array = { 1, 2, 3, 4, 5 };
            bool contiene = array.Contains(3);      // Verifica si el array contiene el valor 3
            bool noContiene = !array.Contains(6);   // Verifica si el array no contiene el valor 6

            //de momento no controlo de bits

            //estructuras de control:
            //if-else
            int numero = 10;

            if (numero > 0)
            {
                Console.WriteLine("El número es positivo.");
            }
            else if (numero == 0)
            {
                Console.WriteLine("El número es cero.");
            }
            else
            {
                Console.WriteLine("El número es negativo.");
            }
            Console.WriteLine();

            //for
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine($"Iteración número: {i}");
            }
            Console.WriteLine();

            //while
            int contador = 0;
            while (contador < 3)
            {
                Console.WriteLine($"Contador actual: {contador}");
                contador++;
            }
            Console.WriteLine();

            //dowhile
            int j = 0;
            do
            {
                Console.WriteLine($"El valor de j es: {j}");
                j++;
            } while (j < 2);
            Console.WriteLine();

            //de momento no controlo muy bien trycatch

            //Dificultad extra:
            bool primero = true;
            for (int i = 10; i<=55; i++)
            {
                if (i != 16 && i % 2 == 0 && i % 3 != 0)
                {
                    if (!primero)
                    {
                        Console.Write(", ");
                    }
                    Console.Write(i);
                    primero = false;
                }
            }

            Console.ReadKey();
        }
    }
}
