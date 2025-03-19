// Operadores Aritmeticos

int num1 = 5;
int num2 = 2;

int suma = num1 + num2; //Operacion de suma
int resta = num1 - num2; // Operacion de resta
int mutiplicacion = num1 * num2; // Operacion de multiplicacion
int division = num1 / num2; // Operacion de division
int modulo = num1 % num2; // Operacion de residuo de una division
double potencia = Math.Pow(num1, num2); // Potenciación

Console.WriteLine(suma);
Console.WriteLine(resta);
Console.WriteLine(mutiplicacion);
Console.WriteLine(division);
Console.WriteLine(modulo);
Console.WriteLine(potencia);

Console.WriteLine("\n");

//Operadores de comparacion 

bool igual = num1 == num2; // Valor A igual que valor B
bool diferente = num1 != num2; // Valor A diferente de valor B
bool mayor = num1 > num2; // Valor A mayor que valor B
bool menor = num1 < num2; // Valor A menor que valor B
bool mayorIgual = num1 >= num2; // Valor A mayor o igual que valor B
bool menorIgual = num1 <= num2; // Valor A menor o igual que valor B


Console.WriteLine(igual);
Console.WriteLine(diferente);
Console.WriteLine(mayor);
Console.WriteLine(menor);
Console.WriteLine(mayorIgual);
Console.WriteLine(menorIgual);

Console.WriteLine("\n");

// Operadores logicos

bool and = (num1 == num2) && (num1 > num2); // Operador Y (Se tienen que cumplir las dos condiciones para que el valor sea true)
bool or = (num1 == num2) || (num1 > num2); // Operador O (Se tiene una de las dos condiciones para que el valor sea true)
bool not = !(num1 == num2); // Operador NO (El valor es el contrario al que realmente es)


Console.WriteLine(and);
Console.WriteLine(or);
Console.WriteLine(not);

// Operadores de asignacion

int x = 10;

int s = x += 3; // El valor de x se suma con 3
int r = x -= 3; // El valor de x se resta con 3
int m = x *= 3; // El valor de x se multiplica con 3
int d = x /= 3; // El valor de x se divide con 3
int re = x %= 3; // El valor dado es el residuo de la division de x entre 3
int y = x &= 3; // Las dos condiciones se cumplen
int o = x |= 3; // Una de las dos condiciones se cumple

Console.WriteLine("\n");
Console.WriteLine(s);
Console.WriteLine(r);
Console.WriteLine(m);
Console.WriteLine(d);
Console.WriteLine(re);
Console.WriteLine(y);
Console.WriteLine(o);

Console.WriteLine("\n");

// Estructuras condicionales


if (num1 == num2)
{
    Console.WriteLine($"{num1} es igual que {num2}");
}
else if (num1 > num2)
{
    Console.WriteLine($"{num1} es mayor que {num2}");
}
else if (num1 < num2)
{
    Console.WriteLine($"{num1} es menor que {num2}");
}
else if (num1 != num2)
{
    Console.WriteLine($"{num1} es diferente de {num2}");
}

Console.WriteLine("\n");

// Estructuras iterativas (Bucles)


while (num1 > num2)
{
    Console.WriteLine($"num2 a subido su valor en 1. Ahora es {num2 + 1}");
    num2 += 1;
}
Console.WriteLine("\n");

int contador = 11;
do
{
    Console.WriteLine("Codigo que se ejecuta al menos una vez");
    contador++;

} while (contador < 10);


Console.WriteLine("\n");

for (int i = 0; i <= num1; i++)
{
    Console.WriteLine($"El valor de num1 es: {num1 + i}");
}

Console.WriteLine("\n");

// Control de excepciones

try
{
    Console.WriteLine(65 + "Cadena");
}
catch
{
    Console.WriteLine("Se ha producido un error");
}
finally
{
    Console.WriteLine("El control de excepciones a finalizado");

}

Console.WriteLine("\n");

//============================================== EJERCICIO EXTRA =======================================================

for (int i = 10; i <= 55; i++)
{
    if (i != 16 && i % 2 == 0 && i % 3 != 0)
    {
        Console.WriteLine(i);
    }
    
}





