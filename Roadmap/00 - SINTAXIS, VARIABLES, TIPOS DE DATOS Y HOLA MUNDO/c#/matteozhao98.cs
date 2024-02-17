using System;

internal class matteozhao98
{
    //CREAR COMENTARIOS Y MOSTRAR LAS DISTINTAS FORMAS DE CREAR COMENTARIOS

    // Documentación oficial en: https://learn.microsoft.com/en-us/dotnet/csharp/

    /*
    * Esto es un comentario multilínea, para poder crear este tipo de comentarios,
    * es necesario iniciarlo con la secuencia de caracteres mostrados en la parte 
    * del principio y del final de este bloque
    * 
    * Se usan para aclarar información a nosotros mismos o a compañeros que puedan
    * estar trabajando con nosotros. Son líneas de texto que no se van a ejecutar.
    */

    static void Main(string[] args)
    {
        //CREAR UNA VARIABLE Y UNA CONSTANTE
        string saludo = "Hola mundo!";
        const double numPi = 3.1416;

        //CREA VARIABLES PRIMITIVAS DEL LENGUAJE
        int miEntero = 2;
        long miLong = 5;
        float miFloat = 3.14;
        double miDouble = 3.14;
        decimal miDecimal = 3.14;
        string miString = "C#";
        char miChar = 'a';
        bool miBool = true;

        Console.WriteLine($"Hola {miString}!");
    }
}
