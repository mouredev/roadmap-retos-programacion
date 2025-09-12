using System;

namespace _02_Funciones_Alcance
{
    internal class Program
    {
        // Variable Global (Colocarle static)
        static int globalVar = 24;

        static void Main(string[] args)
        {
            // Funcion sin parámetros ni retorno
            SinParametrosNiRetorno();

            // Funcion con un parámetro
            ConUnParametro("JoseEsmil04");

            // Funcion con varios parámetros
            ConVariosParametros("Hola", "estoy aprendiendo C#!");

            // Funcion con retorno
            int suma = ConRetorno(5, 10);
            Console.WriteLine($"La suma es: {suma}");

            // Funcion ya creada en el lenguaje
            Console.WriteLine("Esto es una Funcion ya creada en el lenguaje.");

            // Variables locales
            int localVar = 20;
            Console.WriteLine($"Variable local: {localVar}");
            Console.WriteLine($"Variable global: {globalVar}");

            // Funcion de la dificultad extra
            int count = ImprimirNumeros("Fizz", "Buzz");
            Console.WriteLine($"Las veces que imprimieron números en lugar de textos: {count}");

        }

        static void SinParametrosNiRetorno()
        {
            Console.WriteLine("Funcion sin Parametros ni Retorno!");
        }

        static void ConUnParametro(string str)
        {
            Console.WriteLine($"Esta funcion tiene un parametro y es: {str}");
        }

        static void ConVariosParametros(string str, string str2)
        {
            Console.WriteLine($"Mensaje: {str} {str2}");
        }

        static int ConRetorno(int num1, int num2)
        {
            return num1 + num2;
        }

        static int ImprimirNumeros(string str, string str2)
        {
            int count = 0;

            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0 && i % 5 == 0)
                {
                    Console.WriteLine($"{str}{str2}");
                }
                else if (i % 3 == 0)
                {
                    Console.WriteLine(str);
                }
                else if (i % 5 == 0)
                {
                    Console.WriteLine(str2);
                }
                else
                {
                    Console.WriteLine(i);
                    count++;
                }
            }

            return count;
        }

    }
}