using System;


namespace _01_Operadores_Estructuras
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Operadores aritméticos
            int a = 10;
            int b = 5;
            Console.WriteLine("Operadores aritméticos:");
            Console.WriteLine($"a + b = {a + b}"); // Suma
            Console.WriteLine($"a - b = {a - b}"); // Resta
            Console.WriteLine($"a * b = {a * b}"); // Multiplicación
            Console.WriteLine($"a / b = {a / b}"); // División
            Console.WriteLine($"a % b = {a % b}"); // Módulo

            // Operadores lógicos
            bool verdad = true;
            bool falso = false;
            Console.WriteLine("\nOperadores lógicos:");
            Console.WriteLine($"verdad && falso = {verdad && falso}"); // AND
            Console.WriteLine($"verdad || falso = {verdad || falso}"); // OR
            Console.WriteLine($"!verdad = {!verdad}"); // NOT

            // Operadores de comparación
            Console.WriteLine("\nOperadores de comparación:");
            Console.WriteLine($"a == b = {a == b}"); // Igualdad
            Console.WriteLine($"a != b = {a != b}"); // Desigualdad
            Console.WriteLine($"a > b = {a > b}"); // Mayor que
            Console.WriteLine($"a < b = {a < b}"); // Menor que
            Console.WriteLine($"a >= b = {a >= b}"); // Mayor o igual que
            Console.WriteLine($"a <= b = {a <= b}"); // Menor o igual que

            // Operadores de asignación
            Console.WriteLine("\nOperadores de asignación:");
            int c = 20;
            c += a; // Equivalente a c = c + a
            Console.WriteLine($"c += a -> c = {c}");
            c -= a; // Equivalente a c = c - a
            Console.WriteLine($"c -= a -> c = {c}");
            c *= a; // Equivalente a c = c * a
            Console.WriteLine($"c *= a -> c = {c}");
            c /= a; // Equivalente a c = c / a
            Console.WriteLine($"c /= a -> c = {c}");
            c %= a; // Equivalente a c = c % a
            Console.WriteLine($"c %= a -> c = {c}");

            // Operadores de bits
            Console.WriteLine("\nOperadores de bits:");
            int d = 6; // 110 en binario
            int e = 3; // 011 en binario
            Console.WriteLine($"d & e = {d & e}"); // AND bit a bit
            Console.WriteLine($"d | e = {d | e}"); // OR bit a bit
            Console.WriteLine($"d ^ e = {d ^ e}"); // XOR bit a bit
            Console.WriteLine($"~d = {~d}"); // NOT bit a bit
            Console.WriteLine($"d << 1 = {d << 1}"); // Desplazamiento a la izquierda
            Console.WriteLine($"d >> 1 = {d >> 1}"); // Desplazamiento a la derecha

            // Operadores de identidad y pertenencia (no nativos en C#, usando métodos de clase)
            Console.WriteLine("\nOperadores de identidad y pertenencia:");
            object obj1 = new object();
            object obj2 = obj1;
            Console.WriteLine($"obj1 es obj2: {object.ReferenceEquals(obj1, obj2)}"); // Identidad
            Console.WriteLine($"'a' pertenece a 'abcd': {"abcd".Contains('a')}"); // Pertenencia

            // Estructuras de control condicionales
            Console.WriteLine("\nEstructuras de control condicionales:");
            if (a > b)
            {
                Console.WriteLine("a es mayor que b");
            }
            else if (a < b)
            {
                Console.WriteLine("a es menor que b");
            }
            else
            {
                Console.WriteLine("a es igual a b");
            }

            // Estructuras de control iterativas
            Console.WriteLine("\nEstructuras de control iterativas:");
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine($"For loop, iteración: {i}");
            }

            int[] numeros = { 1, 2, 3 };
            foreach (var num in numeros)
            {
                Console.WriteLine($"Foreach Loop, iteración: {num}");
            }

            int j = 0;
            while (j < 5)
            {
                Console.WriteLine($"While loop, iteración: {j}");
                j++;
            }

            int k = 0;
            do
            {
                Console.WriteLine($"Do-while loop, iteración: {k}");
                k++;
            } while (k < 5);

            // Estructuras de control de excepciones
            Console.WriteLine("\nEstructuras de control de excepciones:");
            try
            {
                int resultado = a / 0;
            }
            catch (DivideByZeroException ex)
            {
                Console.WriteLine("Excepción capturada: " + ex.Message);
            }
            finally
            {
                Console.WriteLine("Bloque finally ejecutado.");
            }

            // DIFICULTAD EXTRA
            Console.WriteLine("\nDificultad extra:");
            for (int num = 10; num <= 55; num++)
            {
                if (num % 2 == 0 && num != 16 && num % 3 != 0)
                {
                    Console.WriteLine(num);
                }
            }
        }

    }

}

