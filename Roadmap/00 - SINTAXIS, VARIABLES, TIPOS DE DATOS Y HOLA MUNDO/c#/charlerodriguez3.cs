
/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
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

// Url C# : https://dotnet.microsoft.com/es-es/languages/csharp

// Single line comment -> //

/*
This is a comment of two or more lines
asdasdasd */


//numeros

//integer ordered from the lowest to the largest ocuppation of memory
sbyte edad = 120;
short number1 = 10500;
int number2 = 2;
long trillion = 15004040404; // Not an actual trillion


//float It's necessary to put F in upper so the interpreter doesn't makea problem with the number
//of double type (less precision)
float numberFloat = 2.5555F;

//double (more precision than the float one)
double numberDouble = 3.04;

//decimal It's necessary to put M in upper 
//so the interpreter doesn't make a problem with the number of double type (More precision Required for Contable or Financial Use)
decimal numberDecimal = 5.23M;


//boolean
bool isItComplicated=false;

//char Only one character from keyboard: It goes between single quotation marks
char letter = 'a';

//string two or more characters: It goes between double quotation marks
string style = "Cool";

//Print a string
Console.WriteLine("¡Hola, C#!");