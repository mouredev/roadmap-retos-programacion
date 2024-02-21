using System;
using System.Runtime.InteropServices.Marshalling;

class Hello
{

    //Comentario de una sola linea
    /* Comentario
     * de
     * multiples lineas */

    //https://learn.microsoft.com/es-es/dotnet/csharp

    static void Main()
    {
        //Variables primitivas

        string nombre; //Declaracion de una variable
        string saludo = "Hola!"; //Declaracion y asignacion de una variable
        const int edadMaxima = 100; //Declaracion y asignacion de una constante

        sbyte bytee= -128;
        byte byteePositivos= 255;

        short enteroDe16bits = -32768;
        ushort enteroDe16bitsPositivos = 65535;

        int enteroDe32bits = -2147483648;
        uint enteroDe32bitsPositivos = 4294967295;

        long enteroDe64bits = -9223372036854775808;
        ulong enteroDe64bitsPositivos = 18446744073709551615;
        
        double floatDouble = 13.5;
        float flotante = 13.5f;

        string buendia = "Como estas?";
        char caracter = 'a';

        Console.WriteLine("Hola C#!");
    }
}