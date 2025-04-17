
/* EJERCICIO:
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
using System.Security.Cryptography;
class Retos 
 {
    static void Main () 
    {
        // Operadores Aritméticos 

        int suma = 12 + 5; 
        int resta = 25 - 3; 
        int multiplicacion = 5 * 5; 
        int division = 10 / 2; 
        int modulo = 30 % 3; 
        
        int incremento = 10; 
        incremento++; 

        int decremento = 3; 
        decremento--; 

        Console.WriteLine ("Suma: " + suma); 
        Console.WriteLine ("Resta: " + resta); 
        Console.WriteLine ("Multiplicación: " + multiplicacion); 
        Console.WriteLine ("division: " + division); 
        Console.WriteLine ("modulo: " + modulo);
        Console.WriteLine ("Incremento: " + incremento);
        Console.WriteLine ("Decremento: " + decremento);
        
        //Operadores Lógicos

        bool logico = 12 + 3 == 15 && 12 -3 == 9; //AND 
        Console.WriteLine (logico);

        bool logico2 = 10 + 3 == 13 || 10 + 5 == 25; //OR 
        Console.WriteLine (logico2);

        bool logico3 = 12 * 1 == 11; //NOT
        Console.WriteLine (logico3!);
    

        
    }
    }
 
 
 
 

 