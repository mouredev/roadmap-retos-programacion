/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

// Ejercicio #00.1
// https://dotnet.microsoft.com/es-es/languages/csharp

// Ejercicio #00.2: Comentario en una línea
/*
    Comentario
    múltiples
    líneas
*/
int x = /*comentario en linea de codigo*/ 1;

// Ejercicio #00.3
int y = 0; // Declaracion de variable (tipo int)
const double pi = 3.14159265; //Declaracion de constante (tipo double)

// Ejercicio #00.4
    //********Tipos enteros************
sbyte sb = 0; //Variable tipo sbyte (8 bits con signo)
byte b = 0; //Variable tipo byte (8 bits sin signo)
short s = 0; //Variable tipo short (16 bits con signo)
ushort us = 0; //Variable tipo ushort (16 bits sin signo)
int i = 0; //Variable tipo int (32 bits con signo)
uint ui = 0; //Variable tipo uint (32 bits sin signo)
long L = 0; //Variable tipo long (64 bits con signo)
ulong uL = 0; //Variable tipo ulong (64 bits sin signo)
//********Tipos punto flotante************
float f = 0.0f; //Variable tipo float (decimales)(4 bytes)(presicion 6 a 9 digitos aprox.)
double d = 0.0; //Variable tipo double (decimales)(8 bytes)(presicion 15 a 17 digitos aprox.)
decimal m = 0.0m; //Variable tipo decimal (decimales)(16 bytes)(presicion 28 a 29 digitos aprox.)
//********Tipo bool************
bool b1 = true; //Representacion true en bool
bool b2 = false; //Representacion false en bool
//********Tipo caracteres************
char c = 'a'; //Variable tipo char (16 bits)
string cadena = "Variable para cadena de texto"; //Variable tipo string (coleccion secuencial solo lectura objetos char)
//*******Asignacion implicita********
var z = 1; //Asigna como int
var w = 'b'; //Asigna como char
var p = "Hola"; //Asigna como string

// Ejercicio #00.5: 
Console.WriteLine("Hola C#");
    

 