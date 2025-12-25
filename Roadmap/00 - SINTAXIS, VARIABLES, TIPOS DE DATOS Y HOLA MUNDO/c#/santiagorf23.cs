// Santiago Ramirez Florez - santiagorf23
// Roadmap: SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
// https://learn.microsoft.com/es-es/dotnet/csharp/tour-of-csharp/overview

/*
    Comentario para varias lineas en C#
    Este es un ejemplo de comentario que abarca varias lineas.
*/

using System;
namespace Roadmap
{
    class Program
    {
        static void Main(string[] args)
        {
            int numero = 23;
            string nombre = "Santiago";
            float decimalFlotante = 23.08f;
            double altura = 1.84;
            bool esVerdadero = true;
            decimal precio = 23.08m;
            Console.WriteLine("Hola Mundo en C#.");
            const string saludo = "Hola, soy Santiago Ramirez Florez y este es mi primer programa en C#.";
            Console.WriteLine(saludo);
        }
    }
}