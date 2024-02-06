// Sitio web C# https://dotnet.microsoft.com/es-es/languages/csharp

// Una linea
/*
  En varias
  varias
  varias
  varias
*/

using System;

namespace HolaMundo
{
  internal class lydaf 
  {
    static void main(string[] args)
    {
      var variable;
      const int constante;

      //Si se añade u antes de los tipos numericos como int, long, short, double, float se puede restringir a que sean positivos
      int entero = 1;
      long largo = 1234567890123456L;
      short corto = 12345;
      double flotanteMasPreciso = 2.1D;
      float flotante = 0.10f;
      string texto = "Esto es un string";
      char caracter = 'a';
      bool booleano = true;
      byte Byte = 255;

      Console.WriteLine("Hola, C#!!");
    }
  }
}