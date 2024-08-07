using System;

// Funciones y Alcance
class FunctionsAndScope
{

    // Funciones sin parámetros ni valor de retorno
    static void SayHello()
    {
        Console.WriteLine("Hello World!");
    }

    // Funciones sin parámetros pero con valor de retorno
    static string GiveHello()
    {
        return "Hello World!";
    }

    // Funciones con parámetros pero sin valor de retorno
    static void SayHello(string name) // Se puede sobrecargar!
    {
        Console.WriteLine($"Hello {name}!");
    }

    // Funciones con parámetros y valor de retorno
    static string SayHello(string name, bool isFormal) // Tantas como quieras!
    {
        if (isFormal)
        {
            return $"Hello Mr. {name}!";
        }
        else
        {
            return $"Hello {name}!";
        }
    }

    // Funciones dentro de funciones
    static void SayHello(string name, bool isFormal, bool isSpanish)
    {
        void SayHelloInSpanish()
        {
            if (isFormal)
            {
                Console.WriteLine($"Hola Sr. {name}!");
            }
            else
            {
                Console.WriteLine($"Hola {name}!");
            }
        }
        void SayHelloInEnglish()
        {
            if (isFormal)
            {
                Console.WriteLine($"Hello Mr. {name}!");
            }
            else
            {
                Console.WriteLine($"Hello {name}!");
            }
        }
        if (isSpanish)
        {
            SayHelloInSpanish();
        }
        else
        {
            SayHelloInEnglish();
        }
    }

    // Variables locales
    static void LocalVariables()
    {
        int a = 1;
        int b = 2;
        int c = 3;
        Console.WriteLine("int a = 1; int b = 2; int c = 3;");
        Console.WriteLine($"a: {a}, b: {b}, c: {c}");
    }

    // Variables globales
    static readonly string a = "global";
    static void GlobalVariables()
    {
        Console.WriteLine("C# no maneja un concepto de variables globales");
        Console.WriteLine("como tal, se pueden declarar variables `globales`");
        Console.WriteLine("dentro de una clase, y estas serán accesibles ");
        Console.WriteLine("desde cualquier función de la misma.");
        Console.Write("static readonly string a = \"global\";");
        Console.WriteLine(" // <- declarada en la clase");
        Console.WriteLine($"a: {a}");
    }

    static int OptionalExercise(string cadenaA, string cadenaB)
    {
        int count = 0;
        for (int i = 1; i <= 100; ++i)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                Console.WriteLine($"{cadenaA}{cadenaB}");
            }
            else if (i % 3 == 0)
            {
                Console.WriteLine(cadenaA);
            }
            else if (i % 5 == 0)
            {
                Console.WriteLine(cadenaB);
            }
            else
            {
                Console.WriteLine(i);
                ++count;
            }
        }
        return count;
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Funciones y Alcance");
        Console.WriteLine("\n1. Funciones");
        Console.WriteLine("\n1.1 Funciones sin parámetros ni valor de retorno");
        Console.WriteLine("static void SayHello()");
        SayHello();
        Console.WriteLine("\n1.2 Funciones sin parámetros pero con valor de retorno");
        Console.WriteLine("static string GiveHello()");
        Console.WriteLine(GiveHello());
        Console.WriteLine("\n1.3 Funciones con parámetros pero sin valor de retorno");
        Console.WriteLine("static void SayHello(string name)");
        SayHello("Javier");
        Console.WriteLine("\n1.4 Funciones con parámetros y valor de retorno");
        Console.WriteLine("static string SayHello(string name, bool isFormal)");
        Console.WriteLine(SayHello("Javier", true));
        Console.WriteLine("1.5 Funciones dentro de funciones");
        Console.WriteLine("static void SayHello(string name, bool isFormal, bool isSpanish)");
        SayHello("Javier", false, true);
        Console.WriteLine("\n\n2. Variables locales");
        LocalVariables();
        Console.WriteLine("\n\n3. Variables globales");
        GlobalVariables();
        Console.WriteLine("\n\n4. Ejercicio opcional");
        Console.WriteLine("static int OptionalExercise(string cadenaA, string cadenaB)");
        Console.WriteLine("OptionalExercise(\"Moure\", \"Dev\")");
        Console.WriteLine($"\nNúmeros no múltiplos de 3 ni 5: {OptionalExercise("Moure", "Dev")}");
    }
}
