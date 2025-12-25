using System;
namespace retoProgramacion2025
{
    internal class reto00
    {
        static void Main(string[] args)
        {
            // https://learn.microsoft.com/es-es/dotnet/csharp/tour-of-csharp/overview
            // Comentario de una linea

            /* Comentario de 
             * varias
             * lineas
             */

            //Crear variable y constante
            int entero = 1;
            const int constanteEntero = 2;

            // Tipos primitivos
            sbyte mySbyte = 1;
            Console.WriteLine(mySbyte);
            byte myByte = 1;
            Console.WriteLine(myByte);
            short myShort = 1;
            Console.WriteLine(myShort);
            ushort myUShort = 1;
            Console.WriteLine(myUShort);
            int myInt = 1;
            Console.WriteLine(myInt);
            uint myUInt = 1;
            Console.WriteLine(myUInt);
            long myLong = 1;
            Console.WriteLine(myLong);
            ulong myULong = 1;
            Console.WriteLine(myULong);
            float myFloat = 5.9998f;
            Console.WriteLine(myFloat);
            double myDouble = 5.99;
            Console.WriteLine(myDouble);
            decimal myDecimal = 10.0m;
            Console.WriteLine(myDecimal);
            char myChar = 'A';
            Console.WriteLine(myChar);
            bool myBoolean = false;
            Console.WriteLine(myBoolean);
            Console.WriteLine("");
            Console.WriteLine("¡Hola, C#!");
        }
    }
}