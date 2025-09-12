// Documentación oficial: https://learn.microsoft.com/es-es/dotnet/csharp/
/*
Esto es un comentario de múltiples líneas.
*/
// Esto es un comentario de una sola línea


int numeroEntero = 42;
long numeroLargo = 1234567890123456789L;
float numeroFlotante = 3.14f;
double numeroDoble = 2.71828;
decimal numeroDecimal = 123.456m;

bool esVerdadero = true;
bool esFalso = false;

char caracter = 'A';

string texto = "Hola, mundo!";

DateTime fechaHoraActual = DateTime.Now;

List<int> listaEnteros = new List<int>() { 1, 2, 3 };
Dictionary<string, int> diccionario = new Dictionary<string, int>();

object objetoGenerico = 42;
dynamic variableDinamica = "Hola, dinámico!";

Console.WriteLine("Número Entero: " + numeroEntero);
Console.WriteLine("Número Largo: " + numeroLargo);
Console.WriteLine("Número Flotante: " + numeroFlotante);
Console.WriteLine("Número Doble: " + numeroDoble);
Console.WriteLine("Número Decimal: " + numeroDecimal);
Console.WriteLine("Es Verdadero: " + esVerdadero);
Console.WriteLine("Carácter: " + caracter);
Console.WriteLine("Cadena de Texto: " + texto);
Console.WriteLine("Fecha y Hora Actual: " + fechaHoraActual);
Console.WriteLine("Lista de Enteros: " + string.Join(", ", listaEnteros));
Console.WriteLine("Objeto Genérico: " + objetoGenerico);
Console.WriteLine("Variable Dinámica: " + variableDinamica);

Console.WriteLine("Hola mundo!");
