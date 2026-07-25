/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */


var int numero = 50;

//operadores aritmeticos
int a = 10;
int b = 3;
Console.WriteLine$"a + b = {a + b}"; // Suma
Console.WriteLine$"a - b = {a - b}"; // Resta
Console.WriteLine$"a * b = {a * b}"; // Multiplicación
Console.WriteLine$"a / b = {a / b}"; // División
Console.WriteLine$"a % b = {a % b}"; // Módulo

// Operadores de comparación 
Console.WriteLine("\nOperadores de Comparación:");
Console.WriteLine($"a == b : {a == b}"); // Igual
Console.WriteLine($"a != b : {a != b}"); // Diferente
Console.WriteLine($"a > b : {a > b}"); // Mayor
Console.WriteLine($"a < b : {a < b}"); // Menor
Console.WriteLine($"a >= b : {a >= b}"); // Mayor o igual
Console.WriteLine($"a <= b : {a <= b}"); // Menor o igual

// Operadores logicos
bool x = true;
bool y = false;
Console.WriteLine("\nOperadores lógicos");
Console.WriteLine($"x && y: {x && y}"); // AND
Console.WriteLine($"x || y: {x || y}"); // OR
Console.WriteLine($"!x: {!x}"); // NOT

// Operadores de asignación
Console.WriteLine("\Operadores de asignación");
int c = 6;
Console.WriteLine($"c = {c}");
c += 4; // equivalente a c = c + 4
Console.WriteLine($"c += 4; {c}");
c -= 2; // equivalente a c = c - 2
Console.WriteLine($"c -= 2 {c}");
c *= 2; // equivalente a c = c * 2
Console.WriteLine($"c *= 2: {c}");
c /= 4; // equivalente a c = c / 4
Console.WriteLine($"c /= 4: {c}");
c %= 3; // equivalente a c = c % 3
Console.WriteLine($"c %= 3: {c}");


// Operadores de bits
Console.WriteLine("\nOperadores de bits:");
int d = 6; // 110 en binario
int e = 3; // 011 en binario
Console.WriteLine($"d & e: {d & e}"); // AND bit a bit
Console.WriteLine($"d | e: {d | e}"); // OR bit a bit
Console.WriteLine($"d ^ e: {d ^ e}"); // XOR bit a bit
Console.WriteLine($"~d: {~d}"); // NOT bit a bit
Console.WriteLine($"d << 1: {d << 1}"); // Desplazamiento a la izquierda
Console.WriteLine($"d >> 1: {d >> 1}"); // Desplazamiento a la derecha

 // Operadores de identidad (Referencia y valor)
Console.WriteLine("\nOperadores de identidad:");
string msg1 = "Hola";
string msg2 = "Hola";
Console.WriteLine($"msg1 == msg2: {msg1 == msg2); // Comparación de valor
Console.WriteLine($"object.ReferenceEquals(msg1, msg2): {object.ReferenceEquals(msg1, msg2)}"); // Comparación de referencia

// Operadores de pertenencia (usualmente usando listas o colecciones)
Console.WriteLine("\nOperadores de pertenencia");
int[] array = {1, 2, 3, 4, 5};
Console.WriteLine($"array contiene 3: {Array.Exists(array, element => element == 3)}"); // Usando un método de Array para verificar pertenencia
 
// Estructuras de control 
Console.WriteLine("\nOperadores de control");

// Condicionales
if (a > b)
{
    Console.WriteLine("a es mayor que b");
}
else 
{
    Console.WriteLine("a no es mayor que b");
}

switch (a)
{
    case 10:
        Console.WriteLine("a es 10");
        break;
    default:
        Console.WriteLine("a no es 10");
        break;
}

// Bucles
Console.WriteLine("\Bucles");
for (int i = 0; i < 10; i++)
{
    Console.WriteLine(i);
}

Console.WriteLine("\nBucle while: ");
int j = 0;
while (j < 10)
{
    Console.WriteLine(j);
    j++;
}

Console.WriteLine("\nBucle do-while:");
int k = 0;
    do
    {
        Console.WriteLine(k);
        k++;
    } while (k < 5);

// Excepciones
Console.WriteLine("\nExcepciones");
try
{
    int result = a / 0;
}
catch (DivideByZeroException e)
{
    
     Console.WriteLine("Excepción: División por cero.");
}

// Uso de funciones
Saludar();
int suma = Sumar(5, 7);
Console.WriteLine($"La suma de 5 y 7 es : {suma}");

//funciones

// Función sin parámetros ni retorno
static void Saludar()
{
    Console.WriteLine("¡Hola desde la función Saludar!");
}

// Función con parámetros y retorno
static int Sumar(int a, int b)
{
     return a + b;
}

// Dificultad extra
Console.WriteLine(\nDifultad extra);
for (int i = 10; i <= 55; i++)
{
    if (i % 2 == 0 && i != 16 && i % 3 != 0)
    {
        Console.WriteLine(i);
    }
}