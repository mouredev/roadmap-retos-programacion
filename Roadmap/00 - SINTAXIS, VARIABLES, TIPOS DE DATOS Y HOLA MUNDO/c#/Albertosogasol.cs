// URL oficial del lenguaje C#: https://learn.microsoft.com/en-us/dotnet/csharp/

using System;

class Program
{
    static void Main()
    {
        // Esto es un comentario de una sola línea

        /*
         * Esto es un comentario
         * de múltiples líneas
         */

        /// <summary>
        /// También se puede usar esta sintaxis para comentarios de documentación XML.
        /// Se suelen usar para describir métodos, clases, etc.
        /// </summary>

        // Variable
        string nombre = "C#";

        // Constante
        const double PI = 3.14159;

        // Tipos de datos primitivos
        string texto = "Esto es una cadena de texto";
        char caracter = 'A';
        int entero = 42;
        long enteroLargo = 1234567890L;
        float flotante = 3.14f;
        double doble = 2.71828;
        bool booleano = true;
        decimal numeroDecimal = 19.99m;

        // Imprimir mensaje por consola
        Console.WriteLine("¡Hola, " + nombre + "!");
    }
}
