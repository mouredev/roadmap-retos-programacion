using System;

/*
* - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
*/

// This is a one line comment

/* This
is a multiple 
lines comment.
*/

//* - Crea un comentario en el código y coloca la URL del sitio web oficial del
// *   lenguaje de programación que has seleccionado.


// https://dotnet.microsoft.com/es-es/languages/csharp


 //* - Crea una variable (y una constante si el lenguaje lo soporta).

 //const int myvar = 25;


namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
      const int myNum = 15;
      //myNum = 20;  // This makes an error
      Console.WriteLine(myNum);

      Console.WriteLine(myNum);

      double pi = 3.14;  // A float data type variable
      string name = "Luis";  // A string type variable
      bool answ = true;

      Console.WriteLine(pi);
      Console.WriteLine(name);
      Console.WriteLine(answ);

      Console.WriteLine("Hola C sharp!");
    }
  }
}
