// Ejercicio 01

// El sitio de referencia utilizado es https://learn.microsoft.com/en-us/dotnet/csharp/

/*
    Tipos de commentarios
    ---------------------
    - Comentarios de una sola línea
    - Comentarios multilinea
    - Comentarios de Documentación XML (https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/documentation-comments)
*/

/* Ejemplos */

// Este es un comentario de una sola línea.

/*  Esto podría ser un resumen de todos los códigos.
    Puede agregar varios párrafos o enlaces a páginas como https://learn.microsoft.com/dotnet/csharp.

    Incluso podrías incluir emojis. Un ejemplo es 🔥
    Luego, cuando hayas terminado, cierra con
*/

/// <summary>
/// Este es un comentario de Documentación XML
/// </summary>

// Variables
int indice;
indice = 0;
indice = 3;

// Constantes
// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/const
const int meses = 12;

// Tipos Primitivos

// Tipo booleano
// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool
bool dosEsPar = true;

// Tipos numéricos enteros
// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types
byte  totalDiasSemana = 7; 

sbyte velocidad = 120;

short lineasCodigo = 30000;

int maxInt = 2147483647;

uint maxUInt = 4294967295;

long minLong = -9223372036854775808;

ulong maxULong =  18446744073709551615;

nint tamanio = -1302;

nuint altura = 1302;

// Tipos numéricos de punto flotante
// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types
double d = 4d;

float f = 3_000.5F;

decimal dec = 400.75M;

// Tipo carácter
// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/char
char inicial = 'r';

// Tipo secuencia de caracteres
// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/reference-types#the-string-type
string sistemaOperativo = "Windows";

Console.WriteLine("¡Hola, C#!");