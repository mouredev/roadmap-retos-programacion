/*
--------------------------------------------------------------------------------------------------------
Instrucciones:

    1. Crea ejemplos de funciones básicas que representen las diferentes
       posibilidades del lenguaje:
       Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
    2. Comprueba si puedes crear funciones dentro de funciones.
    3. Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
    4. Pon a prueba el concepto de variable LOCAL y GLOBAL.
    5. Debes hacer print por consola del resultado de todos los ejemplos.
       (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

Dificultad Extra:
    Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
        La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
            - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
            - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
            - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
            - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
--------------------------------------------------------------------------------------------------------
*/

#region 1.

using System.Reflection.Metadata.Ecma335;

Console.WriteLine("1.\n");

void SinParametrosNiRetorno() => Console.WriteLine("     Sin parametros ni retorno");
void ConParametrosSinRetorno(string a) => Console.WriteLine($"     Con parametros sin retorno | {a}");
string SinParametrosConRetorno() => "Hola";
string ConParametrosYRetorno(string text) => text;
void ConParametrosRef(ref string text) => text = "Hola";

SinParametrosNiRetorno();
ConParametrosSinRetorno("Txt");
Console.WriteLine($"     Sin parametros con retorno | {SinParametrosConRetorno()}");
Console.WriteLine($"     Con parametros y retorno | {ConParametrosYRetorno("Hola!")}");
string text = null!;
ConParametrosRef(ref text);
Console.WriteLine($"     Con parametros ref | {text}");

#endregion

#region 2.

AñadirDivision();
Console.WriteLine("2.\n");

Padre();

void Padre()
{
    Console.WriteLine("     Funcion padre");
    Hijo();
    void Hijo()
    { 
        Console.WriteLine("     Funcion hijo");
    }
}

#endregion

#region 3.

AñadirDivision();
Console.WriteLine("3.\n");

bool EsNullo = string.IsNullOrEmpty(text);
Console.WriteLine($"     Funcion integrada con el lenguaje (string.IsNullOrEmpty) | {EsNullo}");

#endregion

#region 4.

AñadirDivision();
Console.WriteLine("4.\n");

Variables();

void Variables()
{
    text = "Hola"; // text es una variable global
    Console.WriteLine($"     Variable global: {text}");
    string text2 = "Chao"; // text2 es una variable local
    Console.WriteLine($"     Variable local: {text2}");
}
//text2 = "Hola"; // No se encuentra por que es local en Variables()

#endregion

#region Extra

AñadirDivision();
Console.WriteLine("Extra:\n");

/*Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
        La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
            - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
            - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
            - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
            - La función retorna el número de veces que se ha impreso el número en lugar de los textos.*/

Console.WriteLine($"\n     {Extra("Hola", "Mundo")} impresiones.");

int Extra(string text1, string text2)
{
    int[] Numeros = Enumerable.Range(1, 100).ToArray();
    int impresiones = 0;
    foreach (int i in Numeros)
    {
        if ((i % 3) == 0 && (i % 5) == 0)
        {
            Console.WriteLine($"     {text1}, {text2}");
        }
        else if ((i % 3) == 0)
        {
            Console.WriteLine($"     {text1}");
        }
        else if ((i % 5) == 0)
        {
            Console.WriteLine($"     {text2}");
        }
        else
        {
            Console.WriteLine($"     {i}");
            impresiones++;
        }
    }
    return impresiones;
}

#endregion

#region Funciones

void AñadirDivision() => Console.WriteLine("\n" + new string('-', 75) + "\n");

#endregion