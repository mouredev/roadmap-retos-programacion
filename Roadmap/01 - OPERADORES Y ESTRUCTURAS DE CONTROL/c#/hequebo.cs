// Operadores Aritméticos
Console.WriteLine("-----------ARITMETICOS-----------");
Console.WriteLine($"Suma: 1 + 5 = {1 + 5}");
Console.WriteLine($"Resta: 1 - 5 = {1 - 5}");
Console.WriteLine($"Multiplicación: 1 * 5 = {1 * 5}");
Console.WriteLine($"División: 1 / 5 = {1 / 5.0}");
Console.WriteLine($"Módulo: 1 % 5 = {1 % 5}");

// Operadores de Comparación
Console.WriteLine("-----------COMPARACION-----------");
Console.WriteLine($"Igualdad: 10 == 5 es {10 == 5}");
Console.WriteLine($"Desigualdad: 10 != 5 es {10 != 5}");
Console.WriteLine($"Menor que: 10 < 5 es {10 < 5}");
Console.WriteLine($"Mayor que: 10 > 5 es {10 >= 5}");
Console.WriteLine($"Menor o igual que: 10 <= 5 es {10 <= 5}");
Console.WriteLine($"Mayor o igual que: 10 >= 5 es {10 >= 5}");

// Operadores Lógicos
Console.WriteLine("-----------LOGICOS-----------");
Console.WriteLine($"AND &&: 10 > 3 && 2 < 3 es {10 > 3 && 2 < 3}");
Console.WriteLine($"OR ||: 10 > 3 || 2 > 3 es {10 > 3 ||2 > 3}");
Console.WriteLine($"NOT !: !(10 > 3) es {!(10 > 3)}");
Console.WriteLine($"XOR &&: 10 > 3 ^ 2 < 3 es {10 > 3 ^ 2 < 3}");

// Operadores de Asignación
Console.WriteLine("-----------ASIGNACION-----------");
int myNum = 1;
int myNum2 = 15;
myNum = myNum2; //Asignación
Console.WriteLine(myNum);
myNum++; // Suma y asignación
Console.WriteLine(myNum);
myNum--; // Resta y asignación
Console.WriteLine(myNum);
myNum *= 2; // Multiplicación y asignación
Console.WriteLine(myNum);
myNum /= 2; // División y asignación;
Console.WriteLine(myNum);
myNum %= 2; // Modulo y asignación
Console.WriteLine(myNum);

// Estructuras de Control
// Condicional
int dayOfTheWeek = (int)DateTime.Today.DayOfWeek;
if (dayOfTheWeek == (int)DayOfWeek.Monday)
    Console.WriteLine("I hate mondays");
else if (dayOfTheWeek == (int)DayOfWeek.Friday)
    Console.WriteLine("Thank God is friday");
else
    Console.WriteLine($"Today is {DateTime.Today.DayOfWeek}");

// Bucles
// Bucle for
for (int i = 0; i < 10; i++)
    Console.WriteLine($"Esta es la iteración {i + 1}");

// Bucle foreach

string[] personas = ["Emilio", "Aldo", "Luis", "Samantha", "Ale"];

foreach (string persona in personas)
    Console.WriteLine($"Hola, {persona}");

// Bucle while

bool salir = false;
while (!salir)
{
    Console.WriteLine("Estás dentro de un bucle while");
    Console.WriteLine("Para salir presiona la tecla 'X'");
    char tecla = (char)Console.ReadLine()[0];
    if (tecla == 'x' || tecla == 'X')
        salir = true;
}

// Excepciones

Console.WriteLine("Bienvenido al sistema de divisiones");
try
{
    Console.WriteLine("Ingresa numero a dividir");
    int num1 = int.Parse(Console.ReadLine());
    Console.WriteLine("Ingresa número por el cual dividir");
    int num2 = int.Parse(Console.ReadLine());
    decimal res = (decimal)num1 / num2;
    Console.WriteLine($"El resultado de la división es: {res}");
} 
catch (Exception ex)
{
    Console.WriteLine("Ocurrió un error");
    Console.WriteLine(ex.Message);
}
finally
{
    Console.WriteLine("Este es el final del sistema de divisiones");
}

/*
 Ejercicio extra: Imprimpir por consola
 todos los números comprendidos entre el
 10 y 55 (incluidos), pares y que no sean
 el 16 ni múltiplos de 3
 */
for (int i = 10; i < 55; i++)
{
    if (i % 2 == 0 && i != 16 && i % 3 != 0)
        Console.WriteLine(i);
}