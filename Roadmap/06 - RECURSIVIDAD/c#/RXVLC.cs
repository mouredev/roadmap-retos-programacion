using System;

namespace R06___2024
{
    class Program
    {
        public static void Recursividad()
        {
            //Para imprimir varios numeros se puede hacer de varias formas, pero lo más normal es hacerlo con for, también podemos hacerlo con while/dowhile (bucles)
            for(int i = 100; i >= 0; i--)
            {
                Console.WriteLine(i);
            }
        }

        //Dif adicional:
        public static void Factorial(int num)
        {
            int res = 1;
            for(int i = 1; i<= num; i++)
            {
                res = res * i;
            }
            Console.WriteLine("\n"+res);
        }

        //Fibonacci:
        //Modo pro:
        public static int Fibonacci(int n)
        {
            if (n < 2)
                return n;
            else
                return Fibonacci(n - 1) + Fibonacci(n - 2);
        }

        //Modo principiante:
        public static void FibonacciJunior(int n)
        {
            int a = 0;
            int b = 1;
            int res = 0;

            for (int i = 2; i <= n; i++)
            {
                res = a + b;
                a = b;
                b = res;
            }
            Console.WriteLine(res);
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Recursividad del 100 al 0: ");
            Recursividad();

            Console.WriteLine("Factorial (numero por parámetro): ");
            Factorial(5);

            Console.WriteLine("Fibonacci (numero por parámetro): ");
            Console.WriteLine(Fibonacci(9));

            FibonacciJunior(9);
            Console.ReadKey();

        }
    }
}
