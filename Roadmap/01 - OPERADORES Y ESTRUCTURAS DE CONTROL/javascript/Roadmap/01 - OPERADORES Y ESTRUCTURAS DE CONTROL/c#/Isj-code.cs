// Operadores
// Operadores matemáticos

int num1 = 5;
int num2 = 8;

// Suma
var suma = num1 + num2;
// Resta
var resta = num1 - num2;
// Multiplicación
var mult = num1 * num2;
// Division
var division = num1 / num2;
// Resto
var resto = num1 & num2;

// Comparación
var igualQue = num1 == num2;
var distinto = num1 != num2;
var mayorQue = num1 > num2;
var mayorIgualQue = num1 >= num2;
var menorQue = num1 < num2;
var menorIgualQue = num1 <= num2;
var yAdemas = num1 <= num2 && num1 != 0;
var oEsto = num1 <= num2 || num1 != 0;

// Asignación, suma y resta del número original mas asignación;

num1 = num2;
num1 += num2;
num1 -= num2;

// Incremento y decremento
num1++;
++num1;
num2--;
--num2;


Console.WriteLine("--------------------------------");
Console.WriteLine("Condicionales");
// Estructura de control y pertenencia;
// If, else if, else
if (num1 < num2)
{
    Console.WriteLine($"El num1: {num1} es menor que el num2: {num2}");
} else if (num1 == num2)
{
    Console.WriteLine("Los números son iguales");
}
else
{
    Console.WriteLine($"El num1: {num1} es mayor que el num2: {num2}");
}

// While
int xWhile = 0;

while (xWhile < 3)
{
    Console.WriteLine($"Estoy dentro del While mientras no valga 3, ahora valgo {xWhile}");
    xWhile++;
}

// Do While
do
{
    Console.WriteLine($"Ya valgo 3 pero me ejecuto una vez en do..while");
} while (xWhile < 3);


// Switch

Console.WriteLine("Ingresa entre a, b, c para probar el switch");
string resp = Console.ReadLine().ToUpper();
switch (resp)
{
    case "A":
        Console.WriteLine("Elegiste a/A");
        break;
    case "B":
        Console.WriteLine("Elegiste b/B");
        break;
    case "C":
        Console.WriteLine("Elegiste c/C");
        break;
    default:
        Console.WriteLine("Elegiste otra letra!!!!");
        break;
}
Console.WriteLine("--------------------------------");
Console.WriteLine("Iteraciones");
// Iterativas
var num3 = 4;
List<int> nums = [1,2,3,4,5,6,7,8,9,10];

Console.WriteLine($"El valor de num3 es: {num3} ");
for (int i = 0; i < nums.Count; i++)
{
    Console.WriteLine($"Posición de la lista {i} con valor {nums[i]}");
    if (nums[i] == num3)
    {
        Console.WriteLine("Soy igual que num3!!!!");
    }
    else
    {
        Console.WriteLine("Soy distinto a num3");
    }
}

foreach (var item in nums)
{
    Console.WriteLine($"Tengo el valor {item}");
}
Console.WriteLine("--------------------------------");
Console.WriteLine("Excepciones");
// Excepciones
try
{
    if (num1 * num2 > 10_000)
    {
        Console.WriteLine("Soy verdadero");  
    }
    else
    {
        Console.WriteLine("Soy falso");
    }
    
}
catch (Exception e)
{
    Console.WriteLine($"En caso de fallar en el try te hablo yo, te puedo dar mas motivos con e: {e}");
    throw;
}

// Opcional, uso del continue
Console.WriteLine("--------------------------------");
Console.WriteLine("Ejercicio Opcional");
for (int i = 10; i <= 55; i++)
{
    if (i % 3 == 0 || i == 16)
    {
        continue;
    }
    Console.WriteLine($"No soy ni múltiplo de 3 ni el 16, soy el número {i}");
}

