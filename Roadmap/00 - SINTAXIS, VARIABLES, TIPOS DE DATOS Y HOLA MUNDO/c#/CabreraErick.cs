using System;
using Microsoft.VisualBasic;

namespace roadmap;

public class CabreraErick
{
    // ##00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

    //Lenguaje seleccioado: C# - C Sharp
    /*
        Url de lenguaje c#: https://learn.microsoft.com/en-us/dotnet/csharp/
    */

    //Comentario de una sola linea

    /*
        Comentario para una o 
        mas lineas, utlizado para 
        dar mas explicacion necesaria a codigo especifico
    */

    //VARIABLES DE TIPO PRIMITIVO

    //variable tipo byte
    byte numeroByte = 12;

    //Variable tipo int
    int numeroEntero = 29;

    //Varibale tipo double
    double numeroDecimal = 20.51;

    //Variable tipo flotante
    float numeeroFlotante = 3.5f;

    //Varibale tipo string
    string nombre = "Erick";

    //Variable tipo char
    char letra = 'a';

    //Variables tipo booleano
    bool falso = false;
    bool verdadero = true;

    //Constante tipo double
    const double pi = 3.1416;

    public static void Main(string[] args)
    {
        string nombreLenguajeProgramacion = "C# - C Sharp";
        Console.WriteLine("¡Hola, este es el lenguaje: " + nombreLenguajeProgramacion + "!");
    }

}