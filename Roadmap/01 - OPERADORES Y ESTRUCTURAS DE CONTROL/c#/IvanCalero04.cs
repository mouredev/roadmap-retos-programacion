// Ejercicio #01 Operadores y Estructuras de control.

int myAge = 42;
int myAge1 = 21;

// Operadores aritmeticos:
var sumaEnteros = myAge + myAge1;
var restaEnteros = myAge - myAge1;
var multiplicacionEnteros = myAge * myAge1;
var divisionEnteros = myAge / myAge1;
var moduloEnteros = myAge % myAge1;

Console.WriteLine($"Esto es una suma de dos varaibles: {sumaEnteros}");
Console.WriteLine($"Esto es una resta de dos varaibles: {restaEnteros}");
Console.WriteLine($"Esto es una multiplicación de dos varaibles: {multiplicacionEnteros}");
Console.WriteLine($"Esto es una division entre dos varaibles: {divisionEnteros}");
Console.WriteLine($"Esto es el resto de dos varaibles: {moduloEnteros}");



// Condicionales y estructura de control:
            if (myAge < myAge1)
            {
                Console.WriteLine($"La edad {myAge1} es mayor.");
            }
            else if (myAge > myAge1)
                {
                    Console.WriteLine($"La edad {myAge} es mayor.");
                }
            else if (myAge <= 0 && myAge > 100 && myAge1 <= 0 && myAge1 > 100)
                {
                    Console.WriteLine($"La edad debe de ser mayor que 0 y menor que 100.");
                }
            else
            {
                Console.WriteLine("Las variables (age) deben de tener contenido INT");
            }

string myName = "Iván";
string myLastname = "Calero Moreno";

if (myName == "Iván" || myLastname == "Calero Moreno")
{
    Console.WriteLine("Hola Ivan!");
}
else if (myName != "Iván" && myLastname != "Calero Moreno")
{
    Console.WriteLine($"Hola {myName} {myLastname} que tengas un buen dia.");
}
else if (myName == "" && myLastname == "")
{
    Console.WriteLine($"Las variables deben de tener algun valor.");
}


// Imprimir por pantalla los numeros comprendidos entre 10 y el 55 que sean pares y que no son ni el 16 ni multiplos de 3

for (int index = 10; index >= 10 && index <= 55; index++)
{
    if (index % 2 == 0 && index != 16 && index % 3 != 0)
    {
        Console.WriteLine(index);
    }
}
