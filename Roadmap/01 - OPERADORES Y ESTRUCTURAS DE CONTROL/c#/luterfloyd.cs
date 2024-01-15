using System.Drawing;

// OPERADORES ARITMETICOS, COMPARACION, LOGICOS E IGUALDAD, BIT
Console.WriteLine("* Operadores aritmeticos:++,--,+,-,*,/,%");
int miEntero = 5;
int miEntero2 = 2;
int miLong = 10;
double miDoble = 10.5;
bool miBooleano = true;
bool miBooleano2 = false;

const int MICONSTANTE = 5; // las constantes son inalterables y se declaran con const
const string MICONSTANTE2 = "Hola Mundo";

Console.WriteLine(miEntero++);
Console.WriteLine(miEntero+miDoble);
Console.WriteLine(++miDoble);

Console.WriteLine(miEntero--);
Console.WriteLine(miEntero+miDoble);
Console.WriteLine(--miDoble);
Console.WriteLine(miEntero*miDoble);
Console.WriteLine(10/2);
Console.WriteLine(10%2);

Console.WriteLine("* Operadores de comparacion: >,<,>=,<=,==,!=");
Console.WriteLine(miEntero>miDoble);
Console.WriteLine(miEntero<miDoble);
Console.WriteLine(miEntero>=miDoble);
Console.WriteLine(miEntero<=miDoble);
Console.WriteLine(miEntero==miDoble);
Console.WriteLine(miEntero!=miDoble);

Console.WriteLine("* Operadores logicos: !,&,|,^  &&,||");
Console.WriteLine(!miBooleano); // NOT
Console.WriteLine(miBooleano&miBooleano2); // AND LOGICO
Console.WriteLine(miBooleano|miBooleano2); // OR LOGICO
Console.WriteLine(miBooleano^miBooleano2); // XOR LOGICO
Console.WriteLine(miBooleano&&miBooleano2); // AND CONDICIONAL
Console.WriteLine(miBooleano||miBooleano2); // OR CONDICIONAL

Console.WriteLine("Operadores bit a bit:~");
Console.WriteLine(~miEntero); // 
Console.WriteLine(miEntero<<miEntero2); // 
Console.WriteLine(miEntero>>miEntero2); // 
Console.WriteLine(miEntero>>>miEntero2); // 

// CICLOS Y ESTRUCTURAS DE CONTROL
Console.WriteLine("* Ciclos: for, foreach");
for (int indice=0; indice<10;indice++) // se repite mientras se cumpla la condicion
{
    Console.WriteLine(indice);
}

var miArray = new string[] {"rojo","blanco","verde"}; // recorre un iterable
foreach (var color in miArray)
{
    Console.WriteLine(color);
}

miEntero = 15;
Console.WriteLine("* Estructuras de control de flujo: if-else if-else");
if (miEntero < 15) // ejecuta un codigo si se cumple una condicion
{
    Console.WriteLine("mi entero es menor que 15");
}
else if (miEntero>15)
{
    Console.WriteLine($"mi entero es mayor que 15");
}
else
{
    Console.WriteLine("mi entero es igual a 15");
}

switch(miEntero) // evalua varias condicionales de una misma expresion o variable
{
    case < 5:
        Console.WriteLine("menor que 5");
        break;
    case 5:
        Console.WriteLine("igual a 5");
        break;
    case > 5:
        Console.WriteLine("mayor que 5");
        break;
}
    miEntero = 0;
    Console.WriteLine($"ciclo while: {miEntero}");
    while (miEntero<10) // se ejecuta mientras se cumpla la condicion
    {
        Console.WriteLine(miEntero);
        miEntero++;
    }

do // se ejecuta mientras se cumpla la condicion pero entra al bloque de codigo al menos una vez
{
    Console.WriteLine($"ciclo do-while: {miEntero}");
    miEntero--;
} while (miEntero>10);