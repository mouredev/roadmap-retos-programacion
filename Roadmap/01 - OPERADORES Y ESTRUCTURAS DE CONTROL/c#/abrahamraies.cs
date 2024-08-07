// Author: Abraham Raies https://github.com/abrahamraies

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

// Ejercicio 1:

internal class Program
{
    // Variable global
    static int globalVariable = 70;

    private static void Main(string[] args)
    {
        // Operadores aritméticos
        int a = 20;
        int b = 4;
        Console.WriteLine("Operadores aritméticos:");
        Console.WriteLine($"a + b = {a + b}"); // Suma
        Console.WriteLine($"a - b = {a - b}"); // Resta
        Console.WriteLine($"a * b = {a * b}"); // Multiplicación
        Console.WriteLine($"a / b = {(double)a / b}"); // División
        Console.WriteLine($"a % b = {a % b}"); // Módulo

        // Operadores lógicos
        bool x;
        bool y = false;
        Console.WriteLine("\nOperadores lógicos:");
        Console.WriteLine($"x && y: {x && y}"); // AND
        Console.WriteLine($"x || y: {x || y}"); // OR
        Console.WriteLine($"!x: {!x}"); // NOT

        // Operadores de comparación
        Console.WriteLine("\nOperadores de comparación:");
        Console.WriteLine($"a == b: {a == b}"); // Igual a
        Console.WriteLine($"a != b: {a != b}"); // Diferente de
        Console.WriteLine($"a > b: {a > b}"); // Mayor que
        Console.WriteLine($"a < b: {a < b}"); // Menor que
        Console.WriteLine($"a >= b: {a >= b}"); // Mayor o igual que
        Console.WriteLine($"a <= b: {a <= b}"); // Menor o igual que

        // Operadores de asignación
        Console.WriteLine("\nOperadores de asignación:");
        int c = 10;
        Console.WriteLine($"c = {c}");
        c += 2; // Equivalente a c = c + 2
        Console.WriteLine($"c += 3: {c}");
        c -= 3; // Equivalente a c = c - 3
        Console.WriteLine($"c -= 2: {c}");
        c *= 4; // Equivalente a c = c * 4
        Console.WriteLine($"c *= 2: {c}");
        c /= 5; // Equivalente a c = c / 5
        Console.WriteLine($"c /= 4: {c}");
        c %= 6; // Equivalente a c = c % 6
        Console.WriteLine($"c %= 3: {c}");

        // Operadores de identidad (Referencia y valor)
        Console.WriteLine("\nOperadores de identidad:");
        string s1 = "Mate";
        string s2 = "Mate";
        Console.WriteLine($"s1 == s2: {s1 == s2}"); // Comparación de valor
        Console.WriteLine($"object.ReferenceEquals(s1, s2): {object.ReferenceEquals(s1, s2)}"); // Comparación de referencia

        // Estructuras de control
        Console.WriteLine("\nEstructuras de control:");

        // Condicionales
        if (a > b)
        {
            Console.WriteLine("a es mayor que b");
        }
        else
        {
            Console.WriteLine("a no es mayor que b");
        }

        // Switch
        switch (a)
        {
            case 20:
                Console.WriteLine("a es 20");
                break;
            case 5:
                Console.WrteLine("a es 5");
                break;
            default:
                Console.WriteLine("a no es 20");
                break;
        }

        // Bucles
        Console.WriteLine("\nBucle for:");
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine(i);
        }

        Console.WriteLine("\nBucle while:");
        int j = 0;
        while (j < 5)
        {
            Console.WriteLine(j);
            j++;
        }

        Console.WriteLine("\nBucle do-while:");
        int k = 0;
        do
        {
            Console.WriteLine(k);
            k++;
        } while (k < 5);

        Console.WriteLine("\nBucle foreach:");
        int[] numeros = { 1, 2, 3, 4, 5, 6, 7 };
        foreach (var num in numeros)
        {
            Console.WriteLine($"Este es el bluche ForEach {num}");
        }

        // Excepciones
        Console.WriteLine("\nExcepciones:");

        try
        {
            int x = 3;
            int y = 0;
            Console.WriteLine(x / y);
        }
        catch (Exception e)
        {
            Console.WriteLine("Error: " + e.Message);
        }
        finally
        {
            Console.WriteLine("Finally");
        }

        // Ejercicio Extra:
        Console.WriteLine("\nEjercicio Extra");
        ImprimirNumeros();
    }

    static void ImprimirNumeros()
    {
        for (int i = 10; i <= 55; i++)
        {
            if (i % 2 == 0 && i != 16 && !(i % 3 == 0))
            {
                Console.WriteLine(i);
            }
        }
    }
}