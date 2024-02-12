using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace R05___2024
{
    internal class Program
    {
        //Dificultad adicional:
        //Para el valor lo realizo con tupla, podría hacerlo con listas también.
        static (int, int) IntercambiarValoresPorValor(int a, int b)
        {
            return (b, a);
        }

        static void IntercambiarValoresPorReferencia(ref int a, ref int b)
        {
            int temp = a;
            a = b;
            b = temp;
        }
        //Fin de dificultad adicional.

        static void ModificarValorReferencia(ref int valor)
        {
            valor = 0; // Modifica el valor proporcionado a 0
        }

        static int ModificarValorValor(int  valor)
        {
            return valor = valor + 1;
        }

        static void Main(string[] args)
        {
            //Por valor:
            int a = 10;
            int b = a; // Asignación por valor

            Console.WriteLine($"\nOriginal: a = {a}, b = {b}");

            b = 20; // Modificando b no afecta a
            Console.WriteLine($"\nDespués de modificar b: a = {a}, b = {b}");

            int x = 10;

            Console.WriteLine($"\nAntes de llamar a ModificarValorReferencia: a = {x}");
            ModificarValorReferencia(ref x);
            Console.WriteLine($"\nDespués de llamar a ModificarValorReferencia: a = {x}");

            int v = 10;
            Console.WriteLine($"\nAntes de llamar a ModificarValorValor: v = {v}");
            v = ModificarValorValor(v);
            Console.WriteLine($"\nDespués de llamar a ModificarValorValor: v = {v}");

            //Dificultad Adicional:


            Console.WriteLine("\nPor valor: ");

            // Por valor:
            int originalA = 10;
            int originalB = 20;

            Console.WriteLine($"\nValores originales: originalA = {originalA}, originalB = {originalB}");

            (int nuevoAValor, int nuevoBValor) = IntercambiarValoresPorValor(originalA, originalB);

            Console.WriteLine($"\nDespués de intercambiar por valor: originalA = {originalA}, originalB = {originalB}");
            Console.WriteLine($"\nNuevos valores: nuevoA = {nuevoAValor}, nuevoB = {nuevoBValor}");

            Console.WriteLine("\nPor Referencia: ");

            // Por referencia:
            int originalARef = 10;
            int originalBRef = 20;
            int antiguaOriginalARef = originalARef;
            int antiguaOriginalBRef = originalBRef;

            Console.WriteLine($"\nValores originales: originalA = {originalARef}, originalB = {originalBRef}");

            IntercambiarValoresPorReferencia(ref originalARef, ref originalBRef);

            Console.WriteLine($"\nDespués de intercambiar por referencia: originalA = {originalARef}, originalB = {originalBRef}");
            Console.WriteLine($"\nVariables antiguas: originalAAntigua = {antiguaOriginalARef}, originalBAntigua = {antiguaOriginalBRef}");


            Console.ReadKey();
        }
    }
    }

