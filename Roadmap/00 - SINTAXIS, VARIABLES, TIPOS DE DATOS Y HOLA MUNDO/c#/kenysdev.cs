// ╔══════════════════════════════════════╗
// ║ Autor: Kenys Alvarado                ║
// ║ GitHub: https://github.com/Kenysdev  ║
// ║ 2024 - C# - CSharp                   ║
// ╚══════════════════════════════════════╝

// 1. Sitio web oficial:
// *********************
// https://dotnet.microsoft.com/es-es/languages/csharp

// 2. Sintaxis para comentarios:
// *****************************
int edad = 21; //comentario inline

//Comentarios Block

/*
  comentario para
  múltiples líneas.
*/

[Obsolete("Obsolete comment or Deprecated comment")]

// TODO: Futuras modificaciones o escritura.
// HACK: Solución temporal, revisar y mejorar.
// BUG: Corregir

#pragma warning disable IDE0018 //desactivar temporalmente una advertencia.
// codigo ...
#pragma warning restore IDE0018 //restaurarla después

/// <summary>
/// comentarios XML, para generadores de documentación
/// </summary>
/// <param name="parametro">Descripción del parámetro.</param>
/// <returns>Descripción del valor de retorno.</returns>

#if DEBUG
    // Comentarios condicionales
    // Este código se compila solo en configuraciones de depuración
#endif

// 3. Variable y constante.
// ************************
int variable_edad = 21;
const double Constante = 3.14;

// 4. Variables para datos primitivos.
// ***********************************
// Enteros:
int entero = 42;         // Entero de 32 bits
byte byteEntero = 255;   // Entero sin signo de 8 bits
short corto = 10000;     // Entero de 16 bits
long largo = 123456789L; // Entero de 64 bits
// uint, ushort, ulong -> No soportan numeros negativos

// Decimales:
float flotante = 3.14f;          // Número de punto flotante de 32 bits
double doble = 3.14159;          // Número de punto flotante de 64 bits
decimal decimalValor = 123.456m; // Número decimal de 128 bits

// Caracteres y Cadenas:
char caracter = 'A';    // Carácter Unicode
string cadena = "Hola"; // Cadena de caracteres

// Booleanos:
bool esVerdadero = true; // Valor booleano verdadero
bool esFalso = false;    // Valor booleano falso

// 5. Imprime: hola, lenguaje:
// **************************
Console.WriteLine("¡Hola, c#!");