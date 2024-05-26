using System;

namespace RetosDeProgramacion
{
    //URL oficial de C#: https://learn.microsoft.com/es-es/collections/yz26f8y64n7k07
    //comentario de una sola linea
    /*
     * comentario de multiples lineas
     */

    internal class Program
    {
        //creando variable global

        int edad = 30;

        //Creando variable tipo constante

        const int numero = 1;
        static void Main(string[] args)
        {
            byte myByte = 100;
            Console.WriteLine($"esto es un byte {myByte}");
            sbyte myByte2 = -10;
            Console.WriteLine($"esto es un sbyte {myByte2}");
            short myShort = 20000;
            Console.WriteLine($"esto es un short {myShort}");
            ushort myUShort = 60000;
            Console.WriteLine($"esto es un Ushort {myUShort}");
            int myInt = -2000000000;
            Console.WriteLine($"esto es un Int {myInt}");
            uint myUint = 2000000000;
            Console.WriteLine($"esto es un Uint {myUint}");
            long myLong = -1000000000000000000;
            Console.WriteLine($"esto es un Long {myLong}");
            ulong myULong = 1000000000000000000;
            Console.WriteLine($"esto es un ULong {myULong}");
            float myFloat = 1.3f;
            Console.WriteLine($"esto es un float {myFloat}");
            double myDouble = 10.2;
            Console.WriteLine($"esto es un double {myDouble}");
            String myString = "Ejemplo de String";
            Console.WriteLine($"esto es un String {myString}");
            bool myBool = false;
            Console.WriteLine($"esto es un boolean {myBool}");

            Console.WriteLine("Hola, C#!");
            Console.ReadKey();
        }
    }
}
