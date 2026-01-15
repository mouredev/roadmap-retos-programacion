
using System;

namespace retoProgramacion2025
{
  
  internal class reto01
  {
      // Variable global
      static int globalVariable = 70;
  
      private static void Main(string[] args)
      {
          MostrarOperadoresAritmeticos();
          MostrarOperadoresLogicos();
          MostrarOperadoresComparacion();
          MostrarOperadoresAsignacion();
          MostrarOperadoresIdentidad();
          MostrarEstructurasControl();
  
          Console.WriteLine("\nEjercicio Extra:");
          ImprimirNumeros();
      }
  
      // Operadores aritméticos
      static void MostrarOperadoresAritmeticos()
      {
          Console.WriteLine("Operadores aritméticos: ");
  
          int a = 5;
          int b = 2;
  
          Console.WriteLine($"a + b = {a + b}");
          Console.WriteLine($"a - b = {a - b}");
          Console.WriteLine($"a * b = {a * b}");
          Console.WriteLine($"a / b = {(double)a / b}");
          Console.WriteLine($"a % b = {a % b}");
      }
  
      // Operadores lógicos
      static void MostrarOperadoresLogicos()
      {
          Console.WriteLine("\nOperadores lógicos: ");
  
          bool x = true;
          bool y = false;
          
          Console.WriteLine($"El valor de x es: {x}");
          Console.WriteLine($"El valor de y es: {y}");
          Console.WriteLine("\n");
          
          Console.WriteLine($"x && y = {x && y}");
          Console.WriteLine($"x || y = {x || y}");
          Console.WriteLine($"!x = {!x}");
      }
  
      // Operadores de comparación
      static void MostrarOperadoresComparacion()
      {
          Console.WriteLine("\nOperadores de comparación: ");
  
          int a = 10;
          int b = 10;
  
          Console.WriteLine($"a == b = {a == b}");
          Console.WriteLine($"a != b = {a != b}");
          Console.WriteLine($"a > b = {a > b}");
          Console.WriteLine($"a < b = {a < b}");
          Console.WriteLine($"a >= b = {a >= b}");
          Console.WriteLine($"a <= b = {a <= b}");
      }
  
      // Operadores de asignación
      static void MostrarOperadoresAsignacion()
      {
          Console.WriteLine("\nOperadores de asignación: ");
  
          int c = 125;
          Console.WriteLine($"c = {c}");
  
          c += 10;
          Console.WriteLine($"c += 10 = {c}");
  
          c -= 20;
          Console.WriteLine($"c -= 20 = {c}");
  
          c *= 30;
          Console.WriteLine($"c *= 30 = {c}");
  
          c /= 50;
          Console.WriteLine($"c /= 50 = {c}");
  
          c %= 60;
          Console.WriteLine($"c %= 60 = {c}");
      }
  
      // Identidad / referencia
      static void MostrarOperadoresIdentidad()
      {
          Console.WriteLine("\nOperadores de identidad: ");
  
          string a1 = "Arroz";
          string a2 = "Galletas";
          
          Console.WriteLine($"El valor de a1 es: {a1}");
          Console.WriteLine($"El valor de a2 es: {a2}");
          Console.WriteLine($"a1 == a2 = {a1 == a2}");
          Console.WriteLine($"ReferenceEquals(a1, a2) = {ReferenceEquals(a1, a2)}");
      }
  
      // Estructuras de control
      static void MostrarEstructurasControl()
      {
          Console.WriteLine("\nEstructuras de control: ");
  
          int a = 45;
          int b = 7;
  
          // IF
          if (a > b)
              Console.WriteLine("a es mayor que b");
          else
              Console.WriteLine("a no es mayor que b");
  
          // SWITCH
          switch (a)
          {
              case 35:
                  Console.WriteLine("a es 35");
                  break;
              case 7:
                  Console.WriteLine("a es 7");
                  break;
              default:
                  Console.WriteLine($"a no es 35, su valor es: {a}");
                  break;
          }
  
          // FOR
          Console.WriteLine("\nFor:");
          for (int i = 0; i < 5; i++)
              Console.WriteLine(i);
  
          // WHILE
          Console.WriteLine("\nWhile:");
          int j = 0;
          while (j < 5)
              Console.WriteLine(j++);
  
          // DO-WHILE
          Console.WriteLine("\nDo-While:");
          int k = 0;
          do
          {
              Console.WriteLine(k++);
          } while (k < 5);
  
          // FOREACH
          Console.WriteLine("\nForeach:");
          int[] numeros = { 1, 2, 3, 4, 5, 6, 7 };
          foreach (int num in numeros)
              Console.WriteLine($"ForEach número: {num}");
  
          // Excepciones
          Console.WriteLine("\nExcepciones:");
  
          try
          {
              int x = 3;
              int y = 0;
              Console.WriteLine(x / y);
          }
          catch (Exception e)
          {
              Console.WriteLine("Error: " + e.Message);
          }
          finally
          {
              Console.WriteLine("Finally ejecutado");
          }
      }
  
      // Ejercicio extra: números pares entre 10 y 55, sin 16 ni múltiplos de 3
      static void ImprimirNumeros()
      {
          for (int i = 10; i <= 55; i++)
          {
              if (i % 2 == 0 && i != 16 && i % 3 != 0)
                  Console.WriteLine(i);
          }
      }
  }
}