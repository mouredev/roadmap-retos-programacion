// Link al lenguaje https://dotnet.microsoft.com/es-es/languages/csharp

// Comentario de una línea

/*
 * Comentario en bloque
 */
 
// Variable inferida 
var numeroReto = 00;

// Constante
const string lenguaje = "C#";

// Tipos de datos primitivos

// Numeros de menos a mayor uso de memoria
byte numByte = 1;
int numInt = 1;
long numLong = 1;
float numFloat = 1.1f;
double numDouble = 1.1;
decimal numDecimal = 1.1m;

// Cadenas de texto
char letra = 'a';
string frase = "El char anterior debe de ir entre comillas simples";

// Booleano
bool respuesta = true;

// Object y dynamic
dynamic dinamico = "Hola Caracola, no voy a poder usar Lenght";
object nombre = "Hola soy object y no sabre inferirte hasta que me ejecutes";

// Hola Mundo!!!!!! El System no haría falta ya que está importado, pero por si acaso.
System.Console.WriteLine($"¡Hola, {lenguaje}!");