// #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
/* 
    Sitio web oficial de C#
    https://dotnet.microsoft.com/es-es/languages/csharp
*/

using System;
using System.Threading.Tasks;

class estuardodev
{
    private static string _Greeting = "Hola";
    private const string _Lenguage = "C#";
    private static int _Year = 2024;
    private static char _Comma = ',';
    private static long _EarthYears = 45400000;
    private static double _PiMedium = 3.14159265359;
    private static float _PiShort = 3.14f;
    private static bool _Susbscribed = true;

    public static void Main(string[] args)
    {
        Console.WriteLine($"¡{_Greeting}{_Comma} {_Lenguage} en Retos de Programación {_Year}!");
        }
}
