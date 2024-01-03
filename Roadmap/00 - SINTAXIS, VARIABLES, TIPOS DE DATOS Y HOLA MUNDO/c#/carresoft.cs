// - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
// https://learn.microsoft.com/es-es/dotnet/csharp/

// - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
// Una sola línea de comentario
int numero = 1; // Comentario final de una línea
int suma = numero /* Comentario entre código */ + 1;
/*
 Comentarios de varias
 líneas
*/

// - Crea una variable (y una constante si el lenguaje lo soporta).
int numero1 = 1;
const double pi = 3.1415926535;

// - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
byte var1 = 255;
sbyte var2 = 127;
short var3 = 32767;
ushort var4 = 65535;
int var5 = 2147483647;
uint var6 = 4294967295;
long var7 = 9223372036854775807;
ulong var8 = 18446744073709551615;
char var9 = 'A';
bool var10 = true;
float var11 = 3.402823e38f;
double var12 = 1.79769313486232e38;
decimal var13 = 7.9e28M;

// - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
string lenguaje = "C#";
Console.WriteLine($"¡Hola, {lenguaje}!");