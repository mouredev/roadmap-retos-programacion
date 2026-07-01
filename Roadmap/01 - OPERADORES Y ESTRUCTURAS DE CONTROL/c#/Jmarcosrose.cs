//"01 - C#". Jmarcosrose.cs

using System;

namespace Jmarcosrose {
    class Program {
        public static void Main(string[] args) {
            int a = 15;
            int b = 5;
            int c = 10;
            int d = 4;
            int i;
            string Cadena = "Lógica de Programación en C#";
            //Operadores aritméticos
            Console.WriteLine("Suma de a y b: " + (a + b));
            Console.WriteLine("Resta de a y b: " + (a - b));
            Console.WriteLine("Multiplicacion de a y b: " + (a * b));
            Console.WriteLine("Division de a y b: " + (a / b));
            Console.WriteLine("Resto de una division de a y b: " + (a % b));

            //Operadores de comparación
            Console.WriteLine("Igualdad: " + (a == b));
            Console.WriteLine("Desigualdad: " + (a != b));
            Console.WriteLine("Mayor que: " + (a > b));
            Console.WriteLine("Menor que: " + (a < b));
            Console.WriteLine("Mayor o igual que: " + (a >= b));
            Console.WriteLine("Menor o igual que: " + (a <= b));

            //Operadores lógicos
            Console.WriteLine("Operador AND &&: " + (a + b == 20 && c + d == 14));
            Console.WriteLine("Operador OR ||: " + (a + b == 20 || c + d == 14));
            Console.WriteLine("Operador NOT !: " + !(c < d));

            //Operadores de asignación
            Console.WriteLine("a es igual a: " + a);           //Asignación
            Console.WriteLine("a más igual 1: " + (a += 1));   //Suma y asignación
            Console.WriteLine("a menos igual a: " + (a -= 1)); //Resta y asignación
            Console.WriteLine("a por igual a: " + (a *= 2));   //Multipilcacón y asignación
            Console.WriteLine("a entre igual a: " + (a /= 3)); //Divsión y asignación
            Console.WriteLine("a resto igual a: " + (a %= 2)); //Módulo y asignación

            //Operadores de pertenencia
            bool includeCadena = Cadena.Contains("C#");
            Console.WriteLine("Palabra incluida: " + includeCadena); //Da como resultado True
            
            //Operadores a nivel de bits
            Console.WriteLine(a & b);
            Console.WriteLine(Convert.ToString(a, 2));
            Console.WriteLine(Convert.ToString(b, 2));
            Console.WriteLine(Convert.ToString(a & b, 2) + " AND ");
            Console.WriteLine(Convert.ToString(a | b, 2) + " OR ");
            Console.WriteLine(Convert.ToString(a ^ b, 2) + " XOR ");
            Console.WriteLine(Convert.ToString(~a, 2) + " NOT ");
            Console.WriteLine(Convert.ToString(a >> 2, 2) + " Desplazamiento derecha ");
            Console.WriteLine(a >> 2);
            Console.WriteLine(Convert.ToString(a << 2, 2) + " Desplazamiento izquierda ");
            Console.WriteLine(a << 2);

            //Estructuras de control
            //Sentencia If
            if (a < b)
            {
                Console.WriteLine("a es menor que b");
            }
            else
            {
                Console.WriteLine("a es mayor que b");
            }

            //Bucle for
            for (i = 1; i <= 5; i++)
            {
                Console.WriteLine(i);
            }

            //Bucle while
            i = 0;
            while (i <= 5)
            {
                Console.WriteLine(i);
                i++;
            }

            //Excepciones
            try
            {
                Console.WriteLine("Ingresa un número:");
                int numero = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine($"Número ingresado: {numero}");
            }
            catch (FormatException ex)
            {
                Console.WriteLine("Error: El valor ingresado no es un número válido.");
            }
            finally
            {
                Console.WriteLine("Proceso finalizado.");
            }

            //Dificultad extra
            for (i = 10; i <= 55; i++)
            {
                if (i % 2 == 0 && i % 3 != 0 && i != 16)
                Console.WriteLine(i);
            }
        }
    
    }
}