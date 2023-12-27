/* Crea un comentario en el código y coloca la URL del sitio web oficial del
 *  lenguaje de programación que has seleccionado.*/

// Web oficial C# -->     https://dotnet.microsoft.com/es-es/languages/csharp

/* - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.*/
// Este es un comentario en una línea

/*
    Este es un comentario con varias líneas
*/

/// <summary>
///  Este es un comentario para generar documentacion XML desde el compilador.
/// </summary>

/* - Crea una variable (y una constante si el lenguaje lo soporta).*/
int i;
const int J = 2;

/* - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).*/
int integer;
long bigInt;
float puntoFlotante;
double puntoFlotanteDoble;
decimal monetario;
string cadena;
char caracter;
bool booleano;


/* - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"*/
string lang = "C#";
Console.WriteLine($"¡Hola, {lang}!");