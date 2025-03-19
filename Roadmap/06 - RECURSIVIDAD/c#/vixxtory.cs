using System.Runtime.Intrinsics.X86;
using System.Security.Cryptography.X509Certificates;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace RetosProgramacion
{
    class Program
    {
        static void Main(string[] args)
        {
            //La recursividad ocurre cuando una funcion o metodo se llama a si mismo 
            //¿Cómo podemos detectar soluciones que podrían resolverse de forma más fácil con una aproximación recursiva?
            //Cuando tengamos un problema que tiene varios pasos, y el resultado de ejecutar cada paso nos deja un problema igual al anterior.
            //int n = 0;
            //imprimirNumeros(n);
            //int factor = 3;
            //Console.WriteLine(factorial(factor));
            int posicion = 14;
            Console.WriteLine(fibonacci(posicion));
        }
        static void imprimirNumeros(int num)
        {
            //Caso base
            if (num <= 100)
            {
                imprimirNumeros(num + 1);
                Console.WriteLine(num);
            }
        }
        static int factorial(int n)
        {
            if (n < 0)
            {
                Console.WriteLine("No es posible calcular el factorial de un numero negativo");
            }
            //Caso base 
            if (n == 0)
                return 1;
            else
                return n * factorial(n - 1);
        }
        static int fibonacci(int p)
        {
            if (p == 0)
                return 0;
            if (p == 1)
                return 1;
            else
                return fibonacci(p - 1) + fibonacci(p - 2);
        }
    }
}


