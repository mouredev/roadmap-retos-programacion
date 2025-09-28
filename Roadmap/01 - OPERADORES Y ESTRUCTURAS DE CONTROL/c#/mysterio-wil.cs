/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

using System;

public class MysterioWil {
    public static void Main(string[] args) {
        Console.WriteLine("### OPERADORES ###");

        // Operadores Aritméticos
        Console.WriteLine("\n--- Aritméticos ---");
        int a = 10, b = 3;
        Console.WriteLine($"Suma: 10 + 3 = {a + b}");
        Console.WriteLine($"Resta: 10 - 3 = {a - b}");
        Console.WriteLine($"Multiplicación: 10 * 3 = {a * b}");
        Console.WriteLine($"División: 10 / 3 = {a / b}");
        Console.WriteLine($"Módulo: 10 % 3 = {a % b}");

        // Operadores Lógicos
        Console.WriteLine("\n--- Lógicos ---");
        Console.WriteLine($"AND (true && false): {true && false}");
        Console.WriteLine($"OR (true || false): {true || false}");
        Console.WriteLine($"NOT (!true): {!true}");

        // Operadores de Comparación
        Console.WriteLine("\n--- Comparación ---");
        Console.WriteLine($"Igualdad (10 == 3): {10 == 3}");
        Console.WriteLine($"Desigualdad (10 != 3): {10 != 3}");

        // Operadores de Asignación
        Console.WriteLine("\n--- Asignación ---");
        int x = 5;
        x += 2;
        Console.WriteLine($"Suma y asignación: x += 2 -> x = {x}");

        // Operadores de Bits
        Console.WriteLine("\n--- Bits ---");
        int p = 10; // 1010
        int q = 3;  // 0011
        Console.WriteLine($"AND a nivel de bits (10 & 3): {p & q}");
        Console.WriteLine($"OR a nivel de bits (10 | 3): {p | q}");

        /*
         * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
         *   que representen todos los tipos de estructuras de control que existan
         *   en tu lenguaje:
         *   Condicionales, iterativas, excepciones...
         */

        Console.WriteLine("\n### ESTRUCTURAS DE CONTROL ###");

        // Condicionales
        Console.WriteLine("\n--- Condicionales (if, else) ---");
        int edad = 18;
        if (edad < 18) {
            Console.WriteLine("Eres menor de edad.");
        } else {
            Console.WriteLine("Eres mayor de edad.");
        }

        // Iterativas
        Console.WriteLine("\n--- Iterativas (for) ---");
        for (int i = 1; i <= 3; i++) {
            Console.WriteLine(i);
        }

        Console.WriteLine("\n--- Iterativas (while) ---");
        int contador = 3;
        while (contador > 0) {
            Console.WriteLine(contador);
            contador--;
        }

        // Excepciones
        Console.WriteLine("\n--- Excepciones (try, catch) ---");
        try {
            int div = 10 / int.Parse("0");
        } catch (DivideByZeroException e) {
            Console.WriteLine($"Se capturó una excepción: {e.Message}");
        }

        /*
         * DIFICULTAD EXTRA (opcional):
         * Crea un programa que imprima por consola todos los números comprendidos
         * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
         */

        Console.WriteLine("\n### DIFICULTAD EXTRA ###");
        for (int numero = 10; numero <= 55; numero++) {
            if (numero % 2 == 0 && numero != 16 && numero % 3 != 0) {
                Console.WriteLine(numero);
            }
        }
    }
}
