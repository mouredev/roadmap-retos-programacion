using System;

// Documentación oficial de C#: https://docs.microsoft.com/es-es/dotnet/csharp/
/*
* Operadores y expresiones de C#
* https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/operators/
*/
class OperatorsAndControlStructures
{

    // https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/operators/arithmetic-operators
    static void arithmeticOperators()
    {
        Console.WriteLine("1. Operadores aritméticos");

        Console.WriteLine("1.1 Operador de incremento");


        Console.WriteLine("1.1.1 Postfijo");

        int a = 10;
        Console.WriteLine("a → a++ → a");
        Console.WriteLine($"{a} → {a++} → {a}");

        Console.WriteLine("1.1.2 Prefijo");

        Console.WriteLine("a → ++a → a");
        Console.WriteLine($"{a} → {++a} → {a}");

        Console.WriteLine("1.2 Operador de decremento");


        Console.WriteLine("1.2.1 Postfijo");

        Console.WriteLine("a → a-- → a");
        Console.WriteLine($"{a} → {a--} → {a}");

        Console.WriteLine("1.2.2 Prefijo");
        Console.WriteLine("a → --a → a");

        Console.WriteLine("1.3 Operadores unarios más y menos");

        Console.WriteLine($"+4 → {+4}");     // output: 4

        Console.WriteLine($"-4 → {-4}");     // output: -4
        Console.WriteLine($"-(-4) → {-(-4)}");  // output: 4

        uint x = 5;
        var b = -x;
        Console.WriteLine("uint x = 5; var b = -x; Console.WriteLine(b);");
        Console.WriteLine(b);            // output: -5
        Console.Write("b.GetType(): ");  // output: System.Int32
        Console.WriteLine(b.GetType());  // output: System.Int64

        Console.Write("-double.NaN: ");  // output: NaN
        Console.WriteLine(-double.NaN);  // output: NaN

        Console.Write("-double.PositiveInfinity: ");  // output: -Infinity
        Console.WriteLine(-double.PositiveInfinity);  // output: -Infinity

        Console.Write("-double.NegativeInfinity: ");  // output: Infinity
        Console.WriteLine(-double.NegativeInfinity);  // output: Infinity

        Console.WriteLine("1.4 Operadores de multiplicación, división y resto");

        Console.WriteLine("1.4.1 Operador de multiplicación");

        Console.WriteLine("2 * 3 → {0}", 2 * 3);  // output: 6

        Console.WriteLine("1.4.2 Operador de división");

        Console.WriteLine("1.4.2.1 División entera");

        Console.WriteLine("10 / 3 → {0}", 10 / 3);  // output: 3

        Console.WriteLine("1.4.2.2 División real");

        Console.WriteLine("10.0 / 3.0 → {0}", 10.0 / 3.0);  // output: 3.33333333333333

        Console.WriteLine("1.4.3 Operador de resto");

        Console.WriteLine("10 % 3 → {0}", 10 % 3);  // output: 1

        Console.WriteLine("1.5 Operadores de suma y resta");

        Console.WriteLine("1.5.1 Operador de suma");

        Console.WriteLine("2 + 3 → {0}", 2 + 3);  // output: 5

        Console.WriteLine("1.5.2 Operador de resta");

        Console.WriteLine("2 - 3 → {0}", 2 - 3);  // output: -1

        Console.WriteLine("1.6 Asignación compuesta");

        Console.WriteLine("1.6.1 Operador de asignación de suma");

        Console.WriteLine("a += 1 → {0}", a += 1);  // output: 6

        Console.WriteLine("1.6.2 Operador de asignación de resta");

        Console.WriteLine("a -= 1 → {0}", a -= 1);  // output: 5

        Console.WriteLine("1.6.3 Operador de asignación de multiplicación");

        Console.WriteLine("a *= 2 → {0}", a *= 2);  // output: 10

        Console.WriteLine("1.6.4 Operador de asignación de división");

        Console.WriteLine("a /= 2 → {0}", a /= 2);  // output: 5

        Console.WriteLine("1.6.5 Operador de asignación de resto");

        Console.WriteLine("a %= 2 → {0}", a %= 2);  // output: 1

    }

    // https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/operators/comparison-operators
    static void comparisonOperators()
    {
        Console.WriteLine("\n2. Operadores de comparación");

        Console.WriteLine("2.1 Operador mayor que");

        Console.WriteLine("2 > 2 → {0}", 2 > 2);  // output: False

        Console.WriteLine("2.2 Operador menor que");

        Console.WriteLine("2 < 2 → {0}", 2 < 2);  // output: False

        Console.WriteLine("2.3 Operador mayor o igual que");

        Console.WriteLine("2 >= 2 → {0}", 2 >= 2);  // output: True

        Console.WriteLine("2.4 Operador menor o igual que");

        Console.WriteLine("2 <= 2 → {0}", 2 <= 2);  // output: True
    }

    static void logicalOperators()
    {
        Console.WriteLine("\n3. Operadores lógicos booleanos");

        Console.WriteLine("3.1 Operador AND lógico booleano");

        Console.WriteLine("true && true → {0}", true && true);  // output: True

        Console.WriteLine("3.2 Operador OR lógico booleano");

        Console.WriteLine("true || false → {0}", true || false);  // output: True

        Console.WriteLine("3.3 Operador NOT lógico booleano");

        Console.WriteLine("!true → {0}", !true);  // output: False

        Console.WriteLine("3.4 Operador IR exclusivo lógico booleano");

        Console.WriteLine("true ^ false → {0}", true ^ false);  // output: True
        Console.WriteLine("false ^ false → {0}", false ^ false);  // output: False
    }

    // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators
    static void BitToBitOperators()
    {
        Console.WriteLine("\n4. Operadores bit a bit y de desplazamiento");

        Console.WriteLine("4.1 Operador de complemento bit a bit ~");

        Console.WriteLine("~0b00000001 → {0}", ~0b00000001);  // output: -2

        Console.WriteLine("4.2 Operador de desplazamiento izquierdo <<");

        Console.WriteLine("0b00000001 << 2 → {0}", 0b00000001 << 2);  // output: 4

        Console.WriteLine("4.3 Operador de desplazamiento derecho >>");

        Console.WriteLine("0b00000100 >> 2 → {0}", 0b00000100 >> 2);  // output: 1

        Console.WriteLine("4.4 Operador de desplazamiento a la derecha sin signo >>>");

        Console.WriteLine("0b10000000 >>> 2 → {0}", 0b10000000 >> 2);  // output: 32

        Console.WriteLine("4.5 Operador AND bit a bit &");

        Console.WriteLine("0b00000001 & 0b00000010 → {0}", 0b00000001 & 0b00000010);  // output: 0

        Console.WriteLine("4.6 Operador OR bit a bit |");

        Console.WriteLine("0b00000001 | 0b00000010 → {0}", 0b00000001 | 0b00000010);  // output: 3

        Console.WriteLine("4.7 Operador XOR bit a bit ^");

        Console.WriteLine("0b00000001 ^ 0b00000010 → {0}", 0b00000001 ^ 0b00000010);  // output: 3

        Console.WriteLine("Estos operadores también se pueden utilizar con asignación compuesta");
    }

    // https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/operators/equality-operators
    static void equalityOperators()
    {
        Console.WriteLine("\n5. Operadores de igualdad");

        Console.WriteLine("5.1 Operador de igualdad");

        Console.WriteLine("2 == 2 → {0}", 2 == 2);  // output: True

        Console.WriteLine("5.2 Operador de desigualdad");

        Console.WriteLine("2 != 2 → {0}", 2 != 2);  // output: False
    }

    static void extraExercise()
    {
        Console.WriteLine("\nEjercicio extra");
        Console.WriteLine("Números pares entre 10 y 55 que no sean múltiplos de 3 ni 16:");

        for (int i = 10; i <= 55; ++i)
        {
            if (i % 2 == 0 && i % 3 != 0 && i != 16)
                Console.WriteLine($"{i}");
        }
    }

    static void Main()
    {
        /*
        C# proporciona una serie de operadores. Muchos de ellos son compatibles
        con los tipos integrados y permiten realizar operaciones básicas con
        valores de esos tipos. Entre estos operadores se incluyen los siguientes
        grupos:
        */

        // Operadores aritméticos
        // Realizan operaciones aritméticas con operandos numéricos.
        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/operators/arithmetic-operators
        // +, -, *, /, %, ++, --, <<, >>, &, |, ^, ~, !, +=, -=, *=, /=, %=, <<=, >>=, &=, |=, ^=
        arithmeticOperators();

        // Operadores de comparación
        // Comparan operandos numéricos.
        // https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/operators/comparison-operators
        // ==, !=, >, <, >=, <=
        comparisonOperators();

        // Operadores lógicos booleanos
        // Realizan operaciones lógicas con operandos bool.
        // https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/operators/boolean-logical-operators
        // &&, ||, !, ^
        logicalOperators();

        // Operadores bit a bit y de desplazamiento
        // Realizan operaciones bit a bit o de desplazamiento con operandos de tipos enteros.
        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators
        // <<, >>, &, |, ^, ~, >>>
        BitToBitOperators();

        // Operadores de igualdad
        // Comprueban si sus operandos son iguales o no.
        // https://learn.microsoft.com/es-es/dotnet/csharp/language-reference/operators/equality-operators
        // ==, !=
        equalityOperators();

        // Ejercicio extra
        extraExercise();
    }
}
