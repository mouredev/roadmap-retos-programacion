using System;

// Documentación oficial de C#: https://docs.microsoft.com/es-es/dotnet/csharp/

// Comentario de una sola línea
/*
    Comentario
    de
    varias
    líneas
*/

class RoadMap
{
    static void Main()
    {
        // Variables
        var variable = "Hola mundo";
        // Constantes
        const string constante = "Hola mundo";
        // constante = "Adiós mundo"; <- Error

        // Tipos de datos
        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/built-in-types
        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/keywords/value-types

        // Tipos de datos primitivos
        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types
        float flotante = 1.5f;
        double doble = 1.5;
        decimal _decimal = 1.5m;

        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/integral-numeric-types
        byte _byte = 1;
        sbyte _sbyte = 1;
        short _short = 1;
        ushort _ushort = 1;
        int entero = 1;
        uint uinteger = 1;
        long longo = 1;
        ulong ulongo = 1;

        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/bool
        bool booleano = true;

        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/char
        char caracter = 'a';

        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/string
        string cadena = "Hola mundo";

        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/object
        object objeto = new object();

        /*
            Tipos de datos no primitivos
        */

        /*
            Arrays
        */
        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/pointer-types
        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/keywords/unsafe
        unsafe
        {
            int entero = 1;
            int* puntero = &entero;
            Console.WriteLine(*puntero);
        }

        /*
            Nullable value types
        */
        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/nullable-value-types
        int? enteroNulo = null;
        Console.WriteLine($"El valor de enteroNulo es {enteroNulo}");

        /*
            Valor vacío
        */
        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/void
        unsafe
        {
            void* vacio = null;
        }

        /*
            * Stackalloc
        */
        // https://docs.microsoft.com/es-es/dotnet/csharp/language-reference/builtin-types/stackalloc
        unsafe
        {
            int* puntero2 = stackalloc int[10];
            Console.WriteLine(*puntero2);
        }

        Console.WriteLine("Hola C#!");

    }
}
