/*
--------------------------------------------------------------------------------------------------
    Instrucciones:

    1. Crea un comentario en el código y coloca la URL del sitio web oficial del
       lenguaje de programación que has seleccionado.
    2. Representa las diferentes sintaxis que existen de crear comentarios
       en el lenguaje (en una línea, varias...).
    3. Crea una variable (y una constante si el lenguaje lo soporta).
    4. Crea variables representando todos los tipos de datos primitivos
       del lenguaje (cadenas de texto, enteros, booleanos...).
    5. Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
--------------------------------------------------------------------------------------------------
*/

// 1.
// Sitio Oficial: https://dotnet.microsoft.com/es-es/languages/csharp

//2.
// En una linea
/*
Varias
Lineas
*/
string comentario = /*"Entre " +*/ "Medio";

//3.
string variable;
const string constante = null!;

//4.
string cadena;
int entero;
float flotante;
double doble;
long largo;
bool booleano;

//5.
const string lenguaje = "C#";
Console.WriteLine($"¡Hola, {lenguaje}!");