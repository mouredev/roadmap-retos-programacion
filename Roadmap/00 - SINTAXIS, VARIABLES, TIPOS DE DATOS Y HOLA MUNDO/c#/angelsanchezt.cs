// Sitio Oficial del Lenguaje C#
// https://dotnet.microsoft.com/en-us/learn/csharp

// Comentario en una línea

/*
    Comentario de varias líneas
    ----------------
    Escribir su primera aplicación: https://aka.ms/dotnet-hello-world
    Descubra las novedades: https://aka.ms/dotnet-whats-new
    Explore la documentación: https://aka.ms/dotnet-docs
    Notificar problemas y encontrar el origen en GitHub: https://github.com/dotnet/core
*/

/// <summary>
/// Este es un comentario de Documentación XML
/// </summary>

/*
    En C#, puedes utilizar el scripting con el apoyo de dotnet-script. 
    Asegúrate de tener dotnet-script instalado en tu máquina para ejecutar este tipo de programas.

    1. Instalación del SDK de .NET, la ultima versión estable .NET 8.0

    2. Instalación de dotnet-script: Abre la línea de comandos y ejecuta el siguiente comando para instalar dotnet-script.
        dotnet tool install -g dotnet-script
    
    3. Ejecuta el script usando dotnet-script:
        dotnet script angelsanchezt.cs
*/

// Convenciones de Codigo en C#
// https://learn.microsoft.com/es-es/dotnet/csharp/fundamentals/coding-style/identifier-names
// Use PascalCase para los nombres de clase y los nombres de método.
// Use camelCase para los argumentos de método, las variables locales y los campos privados.
// Use PascalCase para los nombres de las constantes, tanto campos como constantes locales.
var miVariable = "Variable de Tipo String";

// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/const
const string MiConstante = "Constante: una variable que no puede cambiar su valor";

// Tipos de datos primitivos

// Tipos numéricos enteros
// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types
int numeroEntero = 512;
long numeroLargo = 12345690123456L;
short numeroCorto = 12;
byte numeroByte = 165;

// Tipos numéricos de punto flotante
// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types
float numeroFlotante = 3.14f;
double numeroDoble = 3.14159265359;
decimal numeroDecimal = 123.456m;


// Tipo carácter
// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/char
char caracter = 'A';

// Tipo booleano
// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool
bool esVerdadero = true;

// Referencia nula
string referenciaNula = null;

// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/reference-types#the-string-type
string cadenaCaracteres = "AngelSanchezT";

string nombreLenguaje = "C#";
Console.WriteLine($"¡Hola, {nombreLenguaje}!");



