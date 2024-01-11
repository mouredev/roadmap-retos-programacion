/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 */
// https://learn.microsoft.com/es-es/dotnet/csharp/

using System;

/*
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 */

// Comentario de una sola línea

/*
 * Comentario
 * de varias
 * líneas
 */

/// <summary>
/// Comentario de documentación
/// </summary>
/// <remarks>
/// Crea documentación de las funciones, variables, ...
/// a partir de comentarios,
/// con una sintaxis más específica
/// </remarks>

/*
* - Crea una variable (y una constante si el lenguaje lo soporta).
*/

int miVariable = 1;
const int MI_CONSTANTE = 1;


/*
* - Crea variables representando todos los tipos de datos primitivos
*   del lenguaje (cadenas de texto, enteros, booleanos...).
*/

string variableTexto = "Cadena de texto";
char variableCaracter = 'Ñ';
//Rune variableEscalarUnicode = 0x10FFFF;

int variableEntero = -25;
uint varaibleEnteroPositivo = 3500;
long variableEnteroGrande = -3500;
ulong varibleEnteroPositivoGrande = 987654321;
short variableEnteroPequeño = -700;
ushort variableEnteroPsitivoPequeño = 800;
byte variableByte = 128;

float variableNumeroFlotante = 2.5f;
double variableNumeroFlotantePrecisionDoble = 2.5D;
decimal variableNumeroDecimal = 2.5m;

bool variableBooleano = true;


/*
* - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

Console.WriteLine("¡Hola, C#!");
