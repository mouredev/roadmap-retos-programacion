using System;

namespace R02___2024
{
    internal class Program
    {

        // Función sin parámetros ni retorno:
        static void SinParametrosNiRetorno()
        {
            Console.WriteLine("\nFunción sin parámetros ni retorno.");
        }

        //Función con uno / varios parámetros
        static void ConUnoOVariosParametros(string p1, string p2)
        {
            Console.WriteLine($"\nEste es el parámetro {p1}");
            Console.WriteLine($"\nEste es el parámetro {p2}");
        }

        //Función con retorno
        static int FuncionConRetorno()
        {
            Random rand = new Random();
            return rand.Next(0, 10);
        }

        // Variable global dentro de la clase Program
        private static string variableGlobal = "Soy una variable global";

        //Función de dificultad extra
        static int DifExtra(string s1, string s2)
        {
            int cont = 0;
            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0 && i % 5 == 0)
                {
                    Console.Write($" {s1}");
                    cont++;
                }
                else if (i % 5 == 0)
                {
                    Console.Write($" {s2}");
                    cont++;
                }
                else if (i % 3 == 0)
                {
                    Console.Write($" {s1 + s2}");
                    cont++;
                }
            }
            return cont;
        }

        static void Main(string[] args)
        {
            string p1 = "uno";
            string p2 = "dos";

            SinParametrosNiRetorno();

            ConUnoOVariosParametros(p1, p2);

            Console.WriteLine($"\nEsto es el return de una función que retorna un numero random {{0..10}}: {FuncionConRetorno()}");

            //No podría meter una función dentro de otra, pero podría crear una clase con varias funciones.

            //Funciones ya creadas en c#: Por ejemplo el compareTo

            int x = 3;
            Console.WriteLine($"\nCompare to: {x.CompareTo(3)}");

            //La variable p1 y p2 son locales, debido a que solo se usan en Main
            //Sin embargo la variable variableGlobal es global ya que se puede usar desde la clase program en cualquier función.
            Console.WriteLine($"\n{variableGlobal}\n");

            Console.WriteLine("Dificultad extra:\n");
            string s1 = "fizz", s2 = "buzz";

            Console.WriteLine($"\n\nEl numero ha salido {DifExtra(s1, s2)} veces");

            Console.ReadKey();


        }
    }
}
