using System;
class Ejercicio00
{
    static void Main(string[] args)
    {
        //**Pagina del lenguajes**
        //https://dotnet.microsoft.com/es-es/languages/csharp

        //**Sintaxis para crear comentarios
        //Soy un comentario de una linea.
        /*Soy un comnetario
        de varias lineas
        */

        //Variables y constante
        string variable;
        const string constante;

        //Datos primitivos
        string texto = "Hola";
        int entero = 20;
        double miDouble = 1.1;
        float miFloat = 1.1111f;
        decimal miDecimal = 1.111m;
        char miChart = 'k';
        bool miBool = true;
        bool miBool2 = false;
        byte miByte = 255;
        ushort miUShort = 82839;
        
        //Impresion por terminal
        Console.WriteLine("¡Hola, C#!");
    }
}