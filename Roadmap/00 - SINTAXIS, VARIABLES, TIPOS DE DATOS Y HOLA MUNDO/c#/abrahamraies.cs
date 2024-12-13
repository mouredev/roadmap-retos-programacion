// Author: Abraham Raies https://github.com/abrahamraies

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

// Sitio oficial de C#: https://dotnet.microsoft.com/en-us/languages/csharp

// Ejercicio 2:

// Comentario de una sola linea en C#

/*
Comentario
de
varias
lineas
*/

/// Comentario utilizado para describir un metodo
/// se pueden agregar variables para describir su funcion
/// el retorno del metodo
/// y los posibles errores.


// Ejercicio 3:

var variable = 2;

const constante = 10;

// Ejercicio 4:

// Enteros(int)

int intNumber = 20;

// Numero de punto flotante(float)

// 32 bits
float floatNumber32Bits = 5.14f;

// 64 bits
double doubleNumber = 3.14;

long longNumber = 3.2342;

// Decimal
decimal decimalNumber = 10.3;

// Cadena de texto (String)

string stringText = "Esto es un String";

// Caracter

char charText = 'C';

// Booleanos (bool)

bool booleanTrue = true;
bool booleanFalse = false;

// Ejercicio 5:

class abrahamraies
{
	static void Main(string[] args)
	{
		string lenguaje = "C#";
		Console.WriteLine($"¡Hola, {lenguaje}!");
	}
}