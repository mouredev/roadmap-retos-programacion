using System;
namespace LionnyRdguez
{
    class Program
    {
        static void Main(string[] args)
        {
            Ejercicio_00.Saludar();
        }
    }

   public class Ejercicio_00
    {
        //https://dotnet.microsoft.com/es-es/languages/csharp

        //Comentario en una linea
        /* Comentario
        en
        varias 
        lineas
        */
        public int UnaVariableCualquiera;
        public const float UnaConstanteCualquiera = 3.14f;
        public bool UnaVariableBooleana = true;
        public int UnaVariableEntera = 10;
        public byte UnaVariableByte = 255;
        public char UnaVariableCaracter = 'A';
        public string UnaVariableCadena = "Hola Mundo";
        public short UnaVariableCorta = 32767;
        public long UnaVariableLarga = 9223372036854775807;
        public double UnaVariableDoble = 3.14159265358979323846;
        public decimal UnaVariableDecimal = 79228162514264337593543950335m;
        
        public static void Saludar()
        {
            Console.WriteLine("¡Hola, C#!");
        }
    }
}
