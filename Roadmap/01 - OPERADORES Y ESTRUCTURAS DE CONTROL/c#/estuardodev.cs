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

class Program
{
    // Operadores aritméticos
    private static int asignacion = 0;
    private static int suma = 4 + 2;
    private static int resta = 5 - 2;
    private static int multiplicacion = 5 * 2;
    private static int division = 0;
    private static int residuo = 5 % 2;

    public static void Main(string[] args)
    {
        Console.WriteLine("Resta: " + resta);
        Console.WriteLine("Residuo: " + residuo);

        if (suma == 6)
        {
            Console.WriteLine("Suma es 6");
        } else
        {
            Console.WriteLine("Suma no es 6 :(");
        }

        while(asignacion < multiplicacion)
        {
            Console.WriteLine(asignacion);
            asignacion++;
        }

        try
        {
            division = 150 / 120;
        } catch (Exception e)
        {
            Console.WriteLine("No se puede dividir por: " + e);
        }

        int contador_extra = 10;
        Console.WriteLine("------ DIFICULTAD EXTRA -------");
        while (contador_extra <= 55)
        {
            if(contador_extra != 16 && contador_extra % 3 != 0)
            {
                Console.WriteLine(contador_extra);
            }

            contador_extra++;
        }
    }
}
