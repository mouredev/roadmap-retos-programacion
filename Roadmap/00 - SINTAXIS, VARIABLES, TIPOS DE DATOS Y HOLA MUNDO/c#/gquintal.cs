//https://dotnet.microsoft.com/es-es/languages/csharp

//comentario en una linea

/*
  Comentario en varias lineas
*/

//variables
int edad = 25;
string nombre = "Gustavo";
double altura = 1.75;

//constantes
const double PI = 3.1416;
const int Dias_Semana = 7;
const string Saludo = "Hola Mundo";

//datos primitivos
int myInt = 10;
long myLong = 20;
short myShort = 30;
byte myByte = 40;
float myFloat = 50.5f;
double myDouble = 60.6;
decimal myDecimal = 70.7m;
char myChar = 'A';
string myString = "Hola Mundo";
bool myBool = true;


Console.WriteLine("Hola Mundo"); //Imprimir en la consola

//Obtener el tipo de dato de una variable
Console.WriteLine($"El tipo de dato de la variable edad es: {edad.GetType()}"); //Imprimir en la consola
Console.WriteLine($"El tipo de dato de la variable nombre es: {nombre.GetType()}"); //Imprimir en la consola
Console.WriteLine($"El tipo de dato de la variable altura es: {altura.GetType()}"); //Imprimir en la consola