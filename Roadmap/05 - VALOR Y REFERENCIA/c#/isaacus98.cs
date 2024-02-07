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
namespace RetosProgramacion2024
{
    internal class Reto5
    {
        static void Main(string[] args)
        {
            // Variable por valor
            int numero = 1;
            Console.WriteLine(numero);

            FuncionPorValor(numero);
            Console.WriteLine(numero);

            // Variable por referencia
            int numero2 = 2;
            // La variable numeroRef hace referencia a la variable numero2.
            // Si se añade un valor a la variable de referencia se canviara el valor en la variable referenciada
            ref int numeroRef = ref numero2;
            Console.WriteLine(numeroRef);
            numeroRef = 4;
            Console.WriteLine(numeroRef);
            numero2 = 5;
            Console.WriteLine(numeroRef);

            FuncionPorReferencia(ref numero2);
            Console.WriteLine(numero2);

            // Reto extra
            Console.WriteLine("\nReto Extra\n");

            string str1 = "str1";
            Console.WriteLine($"Valor original de str1 {str1}");
            string str2 = "str2";
            Console.WriteLine($"Valor original de str2 {str2}");
            string respStr1;
            string respStr2;
            string[] str1Array = IntercambiarValores(str1, str2);
            respStr1 = str1Array[0];
            respStr2 = str1Array[1];
            Console.WriteLine($"Valor de la nueva variable respStr1 {respStr1}");
            Console.WriteLine($"Valor de la nueva variable respStr2 {respStr2}");
            Console.WriteLine($"Valor de str1 despues de llamar la función {str1}");
            Console.WriteLine($"Valor de str2 despues de llamar la función {str2}");


            Console.WriteLine();
            Console.WriteLine();


            string str3 = "str3";
            Console.WriteLine($"Valor original de str3 {str3}");
            string str4 = "str4";
            Console.WriteLine($"Valor original de str4 {str4}");
            string respStr3;
            string respStr4;
            string[] str2Array = IntercambiarValores(ref str3, ref str4);
            respStr3 = str2Array[0];
            respStr4 = str2Array[1];
            Console.WriteLine($"Valor de la nueva variable respStr3 {respStr3}");
            Console.WriteLine($"Valor de la nueva variable respStr4 {respStr4}");
            Console.WriteLine($"Valor de str3 despues de llamar la función {str3}");
            Console.WriteLine($"Valor de str4 despues de llamar la función {str4}");
        }

        // La función que recibe un parametro por valor, lo que recibe es una copia del valor de la variable que se le ha pasado como parametro.
        private static void FuncionPorValor(int numero)
        {
            numero++;
        }

        // La función que recibe un parametro por referencia lo que recibe es la referencia de la variable que le pasamos.
        // Si se modifica el valor de la variable dentro de la función, tambien se modificara en la variable que esta fuera de la función que se le haya pasado como parametro
        private static void FuncionPorReferencia(ref int numero)
        {
            numero++;
        }

        // Reto extra
        private static string[] IntercambiarValores(string str1, string str2)
        {
            string temp;
            temp = str1;
            str1 = str2;
            str2 = temp;
            return new string[] { str1, str2};
        }

        private static string[] IntercambiarValores(ref string str1, ref string str2)
        {
            string temp;
            temp = str1;
            str1 = str2;
            str2 = temp;
            return new string[] { str1, str2 };
        }
    }
}
