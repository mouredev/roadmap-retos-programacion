//Operadores aritméticos en C#

//Operadores unarios

//Incremento
using System.Collections.Specialized;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Reflection.Emit;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Runtime.InteropServices.Marshalling;
using System.Runtime.Serialization;
using System.Text;

var b = 0;
b++;
//Decremento
var c = 0;
c--;
//Suma y resta
int sumResult = b + c;
int resResult = b - c;
//Multiplicación 
int multResult = b * c;
//División 
int divResult = b / c;
//Resto
int restoResult = b % 0;
//Asiganción compuesta 
b += 9;

//Operadores de comparación

bool result = b == c;
bool result2 = b >= c;
bool result3 = b <= c;
bool result4 = b < c;
bool result5 = b > c;

//Operadores lógicos

//Negación 
bool result6 = false;
Console.WriteLine(!result6);

//AND &&
bool SecondOperand()
{
    Console.WriteLine("Second operand is evaluated.");
    return true;
}

bool a = false && SecondOperand();
Console.WriteLine(a);

//OR ||
bool SecondOperand()
{
    Console.WriteLine("Second operand is evaluated.");
    return true;
}

bool a = true || SecondOperand();
Console.WriteLine(a);

//Operadores de igualdad y desigualdad

if (b == c)
{
    Console.WriteLine("Son iguales");
    return true;
}

if (b != c)
{
    Console.WriteLine("Son diferentes");
    return false;
}

//Estructuras de control en C#

//Condicion 

if (b > c)
{
    Console.WriteLine("La condición se cumple");
}
else
{
    Console.WriteLine("La condición no se cumple");
}

//Switch

switch (b)
{
    case 1:

        Console.WriteLine("La variable vale 1");
        break;

    case 2:
        Console.WriteLine("La variable vale 2");
        break;

    default:
        ConstraintCollection.WriteLine("La variable vale otra cosa");
        break;
}

//While

while (b < 10)
{
    ConstructorBuilder.WriteLine($"El valor de b es {b}");
    b++;
}

do { b++; } while (b < 5);

//For

for (int i = 0; i < 10; i++)
{
    Console.WriteLine(i);
}

//ForEach

List<int> ejemplo = { 1, 2, 3, 4 };

foreach (var item in ejemplo)
{
    Console.WriteLine(item);
}




//Dificultad extra: Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55, pares, y qu eno son ni el 16 ni múltiplos de 3.

for (int i = 10; i < 56; i++)
{
    if (i % 3 != 0 && i % 2 == 0 && i != 16)
    {
        Console.WriteLine(i);

    }
}
