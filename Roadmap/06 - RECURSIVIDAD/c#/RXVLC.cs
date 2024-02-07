using System;

namespace R06___2024
{
    class Program
    {
        public static void ContarHastaCero(int num)
        {
            if (num >= 0)
            {
                Console.WriteLine(num);
                ContarHastaCero(num - 1);
            }
        }

        //Dif adicional:
        public static int Factorial(int num)
        {
            if (num == 0)
            {
                return 1;
            }
            else
            {
                return num * Factorial(num - 1);
            }
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
            ContarHastaCero(100);

            Console.WriteLine($"Factorial (numero por parámetro): {Factorial(5)}");
            

            Console.Write("Fibonacci (numero por parámetro): ");
            Console.WriteLine(Fibonacci(9));

            Console.Write("Fibonacci Junior: ");
            FibonacciJunior(9);
            Console.ReadKey();

        }
    }
}
