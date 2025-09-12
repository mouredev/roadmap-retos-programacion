using System;

class Program
{
   static void Main()
   {
      // Operadores Aritméticos
      int num1 = 10;
      int num2 = 5;
      int suma = num1 + num2;
      int resta = num1 - num2;
      int multiplicacion = num1 * num2;
      int division = num1 / num2;
      int modulo = num1 % num2;
      int potencia = (int)Math.Pow(num1, num2);

      Console.WriteLine("Operadores Aritméticos:");
      Console.WriteLine($"Suma: {suma}");
      Console.WriteLine($"Resta: {resta}");
      Console.WriteLine($"Multiplicación: {multiplicacion}");
      Console.WriteLine($"División: {division}");
      Console.WriteLine($"Módulo: {modulo}");
      Console.WriteLine($"Potencia: {potencia}");

      // Operadores de Comparación
      bool igual = (num1 == num2);
      bool diferente = (num1 != num2);
      bool mayorQue = (num1 > num2);
      bool menorQue = (num1 < num2);
      bool mayorOIgual = (num1 >= num2);
      bool menorOIgual = (num1 <= num2);

      Console.WriteLine("\nOperadores de Comparación:");
      Console.WriteLine($"Igual: {igual}");
      Console.WriteLine($"Diferente: {diferente}");
      Console.WriteLine($"Mayor que: {mayorQue}");
      Console.WriteLine($"Menor que: {menorQue}");
      Console.WriteLine($"Mayor o igual: {mayorOIgual}");
      Console.WriteLine($"Menor o igual: {menorOIgual}");

      // Operadores Lógicos
      bool andOp = (num1 > 0) && (num2 < 0);
      bool orOp = (num1 > 0) || (num2 < 0);
      bool notOp = !(num1 > 0);

      Console.WriteLine("\nOperadores Lógicos:");
      Console.WriteLine($"AND: {andOp}");
      Console.WriteLine($"OR: {orOp}");
      Console.WriteLine($"NOT: {notOp}");

      // Operadores de Asignación
      int a = 5;
      a += 2;  // Equivalente a: a = a + 2
      int b = 10;
      b *= 3;  // Equivalente a: b = b * 3

      Console.WriteLine("\nOperadores de Asignación:");
      Console.WriteLine($"a: {a}");
      Console.WriteLine($"b: {b}");

      // Operadores de Desplazamiento
      int desplazamientoIzquierda = num1 << 2;
      int desplazamientoDerecha = num1 >> 2;

      Console.WriteLine("\nOperadores de Desplazamiento:");
      Console.WriteLine($"Desplazamiento Izquierda: {desplazamientoIzquierda}");
      Console.WriteLine($"Desplazamiento Derecha: {desplazamientoDerecha}");

      // Estructuras de Control - Condicionales
      if (num1 > num2)
      {
         Console.WriteLine("\nCondicionales:");
         Console.WriteLine("num1 es mayor que num2");
      }
      else if (num1 == num2)
      {
         Console.WriteLine("num1 es igual a num2");
      }
      else
      {
         Console.WriteLine("num1 es menor que num2");
      }

      // Estructuras de Control - Iterativas (While)
      Console.WriteLine("\nIterativas (While):");
      int contador = 0;
      while (contador < 5)
      {
         Console.Write(contador + " ");
         contador++;
      }

      // Estructuras de Control - Iterativas (Do-While)
      Console.WriteLine("\nIterativas (Do-While):");
      int otroContador = 0;
      do
      {
         Console.Write(otroContador + " ");
         otroContador++;
      } while (otroContador < 5);

      // Estructuras de Control - Iterativas (For)
      Console.WriteLine("\nIterativas (For):");
      for (int i = 0; i < 5; i++)
      {
         Console.Write(i + " ");
      }

      // Estructuras de Control - Excepciones
      try
      {
         int resultado = num1 / 0;
      }
      catch (DivideByZeroException)
      {
         Console.WriteLine("\n\nExcepciones:");
         Console.WriteLine("Error: División por cero");
      }

      
      // Reto extra...
      Console.WriteLine("Números entre 10 y 55 (incluidos), pares, que no son ni 16 ni múltiplos de 3:");

      for (int i = 10; i <= 55; i++)
      {
         if (i % 2 == 0 && i != 16 && i % 3 != 0)
         {
            Console.Write(i + " ");
         }
      }
   }
}