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

class Roadmap_01
{
    static void Main()
    {
        // Operadores Aritméticos
        Console.WriteLine("Operadores Aritméticos:");
        int a = 5;
        int b = 3;
        Console.WriteLine($"Suma: {a + b}");
        Console.WriteLine($"Resta: {a - b}");
        Console.WriteLine($"Multiplicación: {a * b}");
        Console.WriteLine($"División: {a / b}");
        Console.WriteLine($"Módulo: {a % b}");
        Console.WriteLine();

        // Operadores Lógicos
        Console.WriteLine("Operadores Lógicos:");
        bool p = true;
        bool q = false;
        Console.WriteLine($"AND lógico: {p && q}");
        Console.WriteLine($"OR lógico: {p || q}");
        Console.WriteLine($"NOT lógico: {!p}");
        Console.WriteLine();

        // Operadores de Comparación
        Console.WriteLine("Operadores de Comparación:");
        int x = 10;
        int y = 20;
        Console.WriteLine($"Igual: {x == y}");
        Console.WriteLine($"No igual: {x != y}");
        Console.WriteLine($"Mayor que: {x > y}");
        Console.WriteLine($"Menor que: {x < y}");
        Console.WriteLine($"Mayor o igual que: {x >= y}");
        Console.WriteLine($"Menor o igual que: {x <= y}");
        Console.WriteLine();

        // Operadores de Asignación
        Console.WriteLine("Operadores de Asignación:");
        int z = 7;
        Console.WriteLine($"Antes de la asignación: {z}");
        z += 3;
        Console.WriteLine($"Después de la asignación: {z}");
        Console.WriteLine();

        // Estructuras de Control
        Console.WriteLine("Estructuras de Control:");

        // Condicionales
        if (a > b)
        {
            Console.WriteLine("a es mayor que b");
        }
        else
        {
            Console.WriteLine("a no es mayor que b");
        }

        // Iterativas
        Console.WriteLine("Bucle for:");
        for (int i = 10; i <= 55; i++)
        {
            if (i % 2 == 0 && i != 16 && i % 3 != 0)
            {
                Console.WriteLine(i);
            }
        }

        // Excepciones
        Console.WriteLine("Manejo de excepciones:");
        try
        {
            // Simular una excepción (división por cero)
            int resultado = a / (b - 3);
            Console.WriteLine($"Resultado: {resultado}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Excepción: {ex.Message}");
        }
    }
}
