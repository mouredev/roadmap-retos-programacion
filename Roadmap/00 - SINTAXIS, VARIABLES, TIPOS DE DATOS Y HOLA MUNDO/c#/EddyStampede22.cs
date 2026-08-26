namespace DefaultNamespace;
using System;

public class EddyStampede22
{
    // https://dotnet.microsoft.com/es-es/languages/csharp
    
    /*
     Esto es otro tipo de comentario en C#
     */

    public static void Main()
    {
        // variable
        string name = "Eddy";

        // constante
        const int numero = 2;
        
        
        // Tipos Númericos

        sbyte numero8bits = -127;
        byte numero8bitspositivos = 127;
        short numero16bits = 32767;
        ushort numero16bitspositivos = 32767;
        int numero32bits = -32768;
        uint numero32bitspositivos = 32768;
        long numero64bits = -64768;
        ulong numero64bitspositivos = 64768;
        
        // Decimales
        float numeroprecisosimple = 5.10f;
        double numeroprecisodoble = 5.10D;
        decimal numeroprecisoalta = 5.10M;
        
        // Lógicos
        bool estado = false;
        char caracter = 'a';
        
        // Dato clave: En C#, la palabra clave string no es un tipo primitivo como en otros lenguajes;
        // es un tipo de referencia que se usa para almacenar cadenas de texto
        // Lo que suele omitirse es que es inmutable, y esa característica hace
        // que su comportamiento se parezca en ocasiones al de un tipo valor.
        
        
        // Saludo
        Console.WriteLine("Hola C#! C:");
    }
}