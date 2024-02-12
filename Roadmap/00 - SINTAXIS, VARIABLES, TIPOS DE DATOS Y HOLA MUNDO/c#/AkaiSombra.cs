
// Author: Nicolas Romero https://github.com/AkaiSombra

/*
 * EJERCICIO:
 * 1. Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * 2. Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * 3. Crea una variable (y una constante si el lenguaje lo soporta).
 * 4. Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * 5. Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

using System;

// Ejercicio 1:

// Sitio oficial de C#: https://learn.microsoft.com/en-us/dotnet/csharp/

// Ejercicio 2:

// Comentario de una sola linea en C#

/*
Comentario de varias lineas
en C#, igual que en JS
*/

// Ejercicio 3:

var Variable = 2;

const int Constante = 10;

// Ejercicio 4:

// Enteros(int)

int IntNumber = 20;

// Numero de punto flotante(float)

// 32 bits
float FloatNumber32Bits = 5.14f;

// 64 bits
double FloatNumber = 3.14;

// Cadena de texto (String)

string StringText = "Esto es un String";

// Booleanos (bool)

bool BooleanTrue = true;
bool BooleanFalse = false;

// Ejercicio 5:

class AkaiSombra
{
    static void Main(string[] args)
    {
        string lenguaje = "C#";
        Console.WriteLine($"¡Hola, {lenguaje}!");
    }
}