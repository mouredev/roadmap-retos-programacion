using System;

class Program
{
    static void Main()
    {    
        // Sitio web oficial de C#: https://docs.microsoft.com/en-us/dotnet/csharp/

        // Este es un comentario de una línea

        /*
        Este es un comentario
        de varias líneas
        */

        // Crea una variable
        public void MyGenericMethod<T>(T genericVariable)
        {
            Console.WriteLine(genericVariable);
        }

        // Llamada al método con un valor específico
        MyGenericMethod<int>(10);

        // Declaración de una constante
        const int MyConstant = 10;

        // Crea una variable (y una constante si el lenguaje lo soporta)
        int myInt = 10;
        double myDouble = 9.99;
        char myChar = 'A';
        bool myBool = true;
        float myFloat = 19.99F;
        byte myByte = 255;
        short myShort = 32767;
        long myLong = 9223372036854775807;
        sbyte mySbyte = 127;
        ushort myUshort = 65535;
        uint myUint = 4294967295;
        ulong myUlong = 18446744073709551615;
        decimal myDecimal = 79228162514264337593543950335M;

        //Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
        Console.WriteLine("¡Hola C#!");
    }
}