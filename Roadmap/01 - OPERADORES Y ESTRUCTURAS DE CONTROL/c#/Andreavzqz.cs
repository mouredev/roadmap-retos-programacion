using System;

class Program
{
    // Variable global para demostración
    static int globalVariable = 100;

    static void Main(string[] args)
    {
        // Operadores aritméticos
        int a = 10;
        int b = 3;
        Console.WriteLine("Operadores aritméticos:");
        Console.WriteLine($"a + b = {a + b}"); // Suma
        Console.WriteLine($"a - b = {a - b}"); // Resta
        Console.WriteLine($"a * b = {a * b}"); // Multiplicación
        Console.WriteLine($"a / b = {(double)a / b}"); // División
        Console.WriteLine($"a % b = {a % b}"); // Módulo

        // Operadores de comparación
        Console.WriteLine("\nOperadores de comparación:");
        Console.WriteLine($"a == b: {a == b}"); // Igual a
        Console.WriteLine($"a != b: {a != b}"); // Diferente de
        Console.WriteLine($"a > b: {a > b}"); // Mayor que
        Console.WriteLine($"a < b: {a < b}"); // Menor que
        Console.WriteLine($"a >= b: {a >= b}"); // Mayor o igual que
        Console.WriteLine($"a <= b: {a <= b}"); // Menor o igual que

        // Operadores lógicos
        bool x = true;
        bool y = false;
        Console.WriteLine("\nOperadores lógicos:");
        Console.WriteLine($"x && y: {x && y}"); // AND
        Console.WriteLine($"x || y: {x || y}"); // OR
        Console.WriteLine($"!x: {!x}"); // NOT

        // Operadores de asignación
        Console.WriteLine("\nOperadores de asignación:");
        int c = 5;
        Console.WriteLine($"c = {c}");
        c += 3; // Equivalente a c = c + 3
        Console.WriteLine($"c += 3: {c}");
        c -= 2; // Equivalente a c = c - 2
        Console.WriteLine($"c -= 2: {c}");
        c *= 2; // Equivalente a c = c * 2
        Console.WriteLine($"c *= 2: {c}");
        c /= 4; // Equivalente a c = c / 4
        Console.WriteLine($"c /= 4: {c}");
        c %= 3; // Equivalente a c = c % 3
        Console.WriteLine($"c %= 3: {c}");

        // Operadores de bits
        Console.WriteLine("\nOperadores de bits:");
        int d = 6; // 110 en binario
        int e = 3; // 011 en binario
        Console.WriteLine($"d & e: {d & e}"); // AND bit a bit
        Console.WriteLine($"d | e: {d | e}"); // OR bit a bit
        Console.WriteLine($"d ^ e: {d ^ e}"); // XOR bit a bit
        Console.WriteLine($"~d: {~d}"); // NOT bit a bit
        Console.WriteLine($"d << 1: {d << 1}"); // Desplazamiento a la izquierda
        Console.WriteLine($"d >> 1: {d >> 1}"); // Desplazamiento a la derecha

        // Operadores de identidad (Referencia y valor)
        Console.WriteLine("\nOperadores de identidad:");
        string s1 = "Hola";
        string s2 = "Hola";
        Console.WriteLine($"s1 == s2: {s1 == s2}"); // Comparación de valor
        Console.WriteLine($"object.ReferenceEquals(s1, s2): {object.ReferenceEquals(s1, s2)}"); // Comparación de referencia

        // Operadores de pertenencia (usualmente usando listas o colecciones)
        Console.WriteLine("\nOperadores de pertenencia:");
        int[] array = { 1, 2, 3, 4, 5 };
        Console.WriteLine($"array contiene 3: {Array.Exists(array, element => element == 3)}"); // Usando un método de Array para verificar pertenencia

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
            case 10:
                Console.WriteLine("a es 10");
                break;
            default:
                Console.WriteLine("a no es 10");
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

        // Excepciones
        Console.WriteLine("\nExcepciones:");
        try
        {
            int result = a / 0;
        }
        catch (DivideByZeroException e)
        {
            Console.WriteLine("Excepción: División por cero.");
        }

        // Uso de funciones 
        Saludar();
        int suma = Sumar(5, 7);
        Console.WriteLine($"La suma de 5 y 7 es: {suma}");

        // Variables globales y locales
        Console.WriteLine("\nVariables globales y locales:");
        Console.WriteLine($"Variable global: {globalVariable}");
        int localVariable = 50;
        Console.WriteLine($"Variable local: {localVariable}");

        // Dificultad extra: función FizzBuzz
        int vecesImpreso = ImprimirNumeros("Fizz", "Buzz");
        Console.WriteLine($"La función ImprimirNumeros se ejecutó {vecesImpreso} veces.");
    }

    // Función sin parámetros ni retorno
    static void Saludar()
    {
        Console.WriteLine("¡Hola desde la función Saludar!");
    }

    // Función con parámetros y retorno
    static int Sumar(int a, int b)
    {
        return a + b;
    }

    // Función FizzBuzz
    static int ImprimirNumeros(string texto1, string texto2)
    {
        int vecesImpreso = 0;
        for (int i = 1; i <= 100; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                Console.WriteLine(texto1 + texto2);
                vecesImpreso++;
            }
            else if (i % 3 == 0)
            {
                Console.WriteLine(texto1);
                vecesImpreso++;
            }
            else if (i % 5 == 0)
            {
                Console.WriteLine(texto2);
                vecesImpreso++;
            }
            else
            {
                Console.WriteLine(i);
            }
        }
        return vecesImpreso;
    }
}


/*
Explicación

Operadores:

Aritméticos: Suma, resta, multiplicación, división, módulo.
Comparación: Igual a, diferente de, mayor que, menor que, mayor o igual que, menor o igual que.
Lógicos: AND (&&), OR (||), NOT (!).
Asignación: Asignación simple (=), y combinada (+=, -=, *=, /=, %=).
Bits: AND (&), OR (|), XOR (^), NOT (~), desplazamiento a la izquierda (<<), desplazamiento a la derecha (>>).
Identidad: Comparación de valor (==) y de referencia (ReferenceEquals).
Pertenencia: Usando métodos de colecciones, como Array.Exists.

Estructuras de control:

Condicionales: if, else, switch.
Iterativas: for, while, do-while.
Excepciones: try, catch.

Funciones:

Sin parámetros ni retorno (Saludar).
Con parámetros y retorno (Sumar).
FizzBuzz (ImprimirNumeros).

Variables globales y locales:

Global: globalVariable.
Local: localVariable dentro de Main.

*/
