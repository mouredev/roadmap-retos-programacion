using System;

//Autor: Ariel Ventura

// 1. Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

    // Sitio oficial de C#: https://learn.microsoft.com/en-us/dotnet/csharp/

// 2. Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje(en una línea, varias...).

    // Esto es un comentario de un linea...

    /*
    * Es es un comentario
    * de Varias lineas.
    */

namespace ConsoleAppRoadMap001
{
    class Program
    {
        // 3. Crea una variable (y una constante si el lenguaje lo soporta).

        string MiVariable = "Hola";
        const string MiConst = "SinCambio";

        // 4.Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

        string MiVariable2 = "Esto es una cadena";
        int MiEntero = 17;
        bool Positivo = true;
        bool Negativo = false;
        

        static void Main(string[] args)
        {
            // 5.Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

            Console.WriteLine("Hola C#!");
        }
    }
}
