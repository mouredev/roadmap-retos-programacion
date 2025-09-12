//La pagina web oficial es: https://learn.microsoft.com/es-es/dotnet/csharp/

//Tipos de Comentarios
//--------------------
//Comentario de una Linea

/*Comentario de
  bloque
*/

///<summary>
///Comentario XML
/// </summary>

int variable = 6;
const int constante = 100;

byte numeroByteMin = 0;
byte numeroByteMax = 255;

sbyte numeroSbyteMin = -128;
sbyte numeroSbyteMax = 127;

short numeroShortMin = -32768;
short numeroShortMax = 32767;

ushort numeroUshortMin = 0;
ushort numeroUshortMax = 65535;

int numeroIntMin = -2147483648;
int numeroIntMax = 2147483647;

uint numeroUintMin = 0;
uint numeroUintMax = 4294967295;

long numeroLongMin = -9223372036854775808;
long numeroLongMax = 9223372036854775807;

ulong numeroUlongMin = 0;
ulong numeroUlongMax = 18446744073709551615;

float numeroFloat = 3.14f;

double numeroDouble = 3.14;

decimal numeroDecimal = 3.14m;

char caracter = 'C';

bool verdaderoFalso = true;

string cadena = "Cadena de Texto";

Console.WriteLine("¡Hola, C#!");
