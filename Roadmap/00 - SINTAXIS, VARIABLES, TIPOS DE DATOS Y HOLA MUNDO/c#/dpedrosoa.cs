//Reto #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

// Web oficial del leguaje de programación C#: https://learn.microsoft.com/en-us/dotnet/csharp/

// Esto es un comentario de una sola línea

/*
 * Esto es 
 * un comentario 
 * de varias líneas
 */

// -----------------------------
// Tipos de números enteros: (tipo de valor)
// -----------------------------

// sbyte: tipo entero con signo de 8 bits (-128 .. 127)
sbyte signedByte = -30;

// byte: tipo entero sin signo de 8 bits (0 .. 255)
byte unsignedByte = 30;

// short: tipo entero con signo de 16 bits (-32,768 .. 32,767)
short signedShort = -30000;

// ushort: tipo entero sin signo de 16 bits (0 .. 65,535)
ushort unsignedShort = 30111;

// int: tipo entero con signo de 32 bits (-2,147,483,648 .. 2,147,483,647)
int signedInt = -2_111_222_333;

// uint: tipo entero sin signo de 32 bits (0 .. 4,294,967,295)
uint unsignedInt = 4111222333;

// long: tipo entero con signo de 64 bits (-9,223,372,036,854,775,808 .. 9,223,372,036,854,775,807)
long signedLong = -9_111_222_333_444_555_666;

// ulong: tipo entero sin signo de 64 bits (0 .. 18,446,744,073,709,551,615)
ulong unsignedLong = 18111222333444555666;


// -----------------------------
// Tipos de números de punto flotante: (tipo de valor)
// -----------------------------

// float: tipo de punto flotante de 32 bits = 4 bytes (±1.5 x 10^−45 a ±3.4 x 10^38, con una precisión de 6-9 dígitos)
float floatValue = -123_456_789.75f;
floatValue = 5.4f;

// double: tipo de punto flotante de 64 bits = 8 bytes (±5.0 × 10^−324 a ±1.7 × 10^308, con una precisión de 15-16 dígitos)
double doubleValue = 123_456_789.75d;
doubleValue = 4.25D;
doubleValue = 3.1;

// decimal: tipo de punto flotante de 128 bits = 16 bytes (±1.0 x 10^-28 a ±7.9 x 10^28, con una precisión de 28-29 dígitos)
decimal decimalValue = 123_456_789.75m;
decimalValue = 3.75M;

// -----------------------
// Tipo Booleano: (tipo de valor)
// Representa valores de verdad (true o false)
// -----------------------

bool isProgrammer = true;

// -----------------------
// Tipo Character: (tipo de valor)
// Representa un solo carácter Unicode (16 bits)
// -----------------------

char inicial = 'J';

// -----------------------
// Tipo String: (tipo de referencia)
// Representa una cadena de texto
// -----------------------

string nombre = "Juan"; // variable tipo 

// ------------------------
// Tipo Constant: (tipo de valor)
// Son inmutables, no pueden cambiar su valor una vez asignados. Deben ser inicializadas en el momento de su declaración.
const double PI = 3.14159;

// ------------------------
// Tipo Var: (implicita) El compilador deduce el tipo de dato a partir del valor asignado.
// No se puede cambiar el tipo de dato después de la declaración.
// Solo se puede usar para variables locales dentro de métodos.
// -------------------------
var numero = 42;
var texto = "¡Hola, mundo!";

// ------------------------
// Tipo Object: (tipo de referencia) Es el tipo base de todos los tipos en C#.
// Puede almacenar cualquier tipo de dato, pero se necesita un proceso de conversión (casting) para recuperar el valor original.
// ------------------------
object obj = 123;
int number = (int)obj; // Casting explícito para recuperar el valor entero

object obj2 = "Variable objeto";
object obj3 = 'A';
object obj4 = true;
object obj5 = 3.14;
object obj6 = 5;

Console.WriteLine("¡Hola, C#!");