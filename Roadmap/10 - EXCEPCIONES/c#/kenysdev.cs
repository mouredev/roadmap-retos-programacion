/*
╔═══════════════════════════════════════╗
║ Autor:  Kenys Alvarado                ║
║ GitHub: https://github.com/Kenysdev   ║
║ 2024 -  C#                            ║
╚═══════════════════════════════════════╝
-----------------------------------------------
EXCEPCIONES 
-----------------------------------------------
- Representan una forma de controlar el comportamiento de un programa
  cuando se produce un error.
- Mas sobre excepciones en: 
learn.microsoft.com/dotnet/csharp/language-reference/language-specification/exceptions
*/
// ___________________________________________
// Capturar excepción
using System.Security.Cryptography.X509Certificates;

int a = 7, b = 0;
try{
    int r = a / b;
}
catch (DivideByZeroException){
    Console.WriteLine("Error de división por cero");
}

// ___________________________________________
// Cuando se desconoce el tipo de excepción
var myList = new int[]{ 1, 2, 3 };
try{
    Console.WriteLine(myList[7]);
}
catch (Exception){
    Console.WriteLine("Excepción");
}

// ___________________________________________
// Saber qué excepción ha ocurrido
try{
    int r = int.Parse("uno") + 2;
}
catch (Exception ex){
    Console.WriteLine($"Excepción: {ex.GetType()}");
}

// ___________________________________________
// Capturar diferentes excepciones
try{
    // int r = int.Parse("uno") + 2;
    string r = 7 + "txt";
}
catch (FormatException){
    Console.WriteLine("Error al convertir");
}
catch (Exception){
    Console.WriteLine("Error de tipos");
}

// ___________________________________________
// Uso de finally
// Se ejecuta siempre, haya o no una excepción.
try{
  int r = a / b;
}
catch (Exception){
  Console.WriteLine("Excepción");
}
finally{
  Console.WriteLine("Bloque finally");
}

// ___________________________________________
// Uso de throw para ejecutar una excepción

//throw new DivideByZeroException("Error de división");
//throw new IndexOutOfRangeException();
//throw new InvalidCastException("..");

// -------------------------------------------
// Definiendo excepcion personalizada
// -------------------------------------------

try{
  throw new CustomException("Mensaje de error personalizado");
}
catch (CustomException ex){
  Console.WriteLine($"Excepción personalizada: {ex.Message}");
}


/*-------------------------------------------
   Ejercicio
  -------------------------------------------
* Crea una función que sea capaz de procesar parámetros, pero que también
* pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
* corresponderse con un tipo de excepción creada por nosotros de manera
* personalizada, y debe ser lanzada de manera manual) en caso de error.
* - Captura todas las excepciones desde el lugar donde llamas a la función.
* - Imprime el tipo de error.
* - Imprime si no se ha producido ningún error.
* - Imprime que la ejecución ha finalizado. */

Console.WriteLine("\n___________\nEjercicio:");
Operation(10, "uno");
Operation(10, 0);
Operation(10, 5);
Operation(10, 2);

static void Division(int a, int b){
  if (b % 2 != 0){
    throw new OddNumberError();    
  }
  Console.WriteLine($"\n- El resultado es: {a / b}");
}

static void Operation(int a, object b){
  try{
    Division(a, (int)b);
    Console.WriteLine("- No hubo errores.");
  }
  catch (InvalidCastException ex){
    Console.WriteLine($"\nError: No se permite texto. -> {ex.GetType()}");
  }
  catch (DivideByZeroException ex){
    Console.WriteLine($"\nError: No es posible dividir entre 0. -> {ex.GetType()}");
  }
  catch (OddNumberError ex){
    Console.WriteLine($"\nError: no dividir entre impares. -> {ex.GetType()}");
  }
  finally{
    Console.WriteLine("- Operación terminada.");
  }
}

// ___________________________________________
// Heredar clase 
class CustomException(string message) : Exception(message){

}

class OddNumberError : Exception{
  public OddNumberError() : base() { }
}
