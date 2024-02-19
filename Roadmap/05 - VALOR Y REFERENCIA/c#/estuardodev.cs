/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

using System.Runtime.CompilerServices;
using System;

namespace estuardodev
{
    class Program
    {
        private static void Main(string[] args)
        {
            int valor1 = 3;
            int valor2 = valor1;

            valor2 += 2;

            Console.WriteLine("Valor 1: " + valor1);
            Console.WriteLine("Valor 2: " + valor2);

            List<string> strings = new List<string>{
                "Python",
                "C#",
                "Java"
            };

            List<string> strings2 = strings;

            strings2.Add("C++");

            foreach(String i in strings)
            {
                Console.WriteLine("Valores de Strings 1: " + i);
            }

            foreach (String i in strings2)
            {
                Console.WriteLine("Valores de Strings 2: " + i);
            }

            Valor(5, 10);

            List<string> lista1 = new List<string>{
                "C#"
            };
            List<string> lista2 = new List<string>{
                "Python"
            };
            Referencia(lista1, lista2);

        }

        private static void Valor(int val1, int val2)
        {
            int valor = val1;
            val1 = val2;
            val2 = valor;

            Console.WriteLine("Valor del parámetro 1: " + val1);
            Console.WriteLine("Valor del parámetro 2: " + val2);
        }

        private static void Referencia(List<string> lista1, List<string> lista2)
        {
            List<string> refuerzo = lista1;
            lista1 = lista2;
            lista2 = refuerzo;
            lista1.Add("Lista 1");
            lista2.Add("Lista 2");

            foreach(string s in lista1)
            {
                Console.WriteLine("Valor lista 1: " + s);
            }
            foreach (string s in lista2)
            {
                Console.WriteLine("Valor lista 2: " + s);
            }
        }
    }
}