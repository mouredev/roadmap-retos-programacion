//Operadores aritméticos en C#

//Operadores unarios

//Incremento
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


//Dificultad extra: Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55, pares, y qu eno son ni el 16 ni múltiplos de 3.

for (int i = 10; i < 56; i++)
{
    if (i % 3 != 0 && i % 2 == 0 && i != 16)
    {
        Console.WriteLine(i);

    }
}
