// EJERCICIO:
// - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
//   https://learn.microsoft.com/en-us/dotnet/csharp/

using System;

// El nombre de la clase "mysterio-wil" no es válido en C#. Se usará "MysterioWil".
public class MysterioWil
{
    public static void Main(string[] args)
    {
        // - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

        // Comentario de una línea

        /*
         Comentario
         de varias
         líneas
        */

        /// <summary>
        /// Comentario de documentación XML.
        /// </summary>

        // - Crea una variable (y una constante si el lenguaje lo soporta).
        string myVariable = "Mi variable";
        const string MY_CONSTANT = "Mi constante";

        // - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
        string myString = "Cadena de texto";
        int myInt = 10;
        float myFloat = 10.5f;
        double myDouble = 10.555;
        bool myBoolean = true;
        char myChar = 'a';

        // - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        Console.WriteLine("¡Hola, C#!");
    }
}
