using System.Drawing;
using System.Security.Cryptography.X509Certificates;

namespace _05_valoryreferencia
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * EJERCICIO:
             * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
             *   su tipo de dato.
             * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
             *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
             * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
             *
             * DIFICULTAD EXTRA (opcional):
             * Crea dos programas que reciban dos parámetros (cada uno) definidos como
             * variables anteriormente.
             * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
             *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
             *   se asigna a dos variables diferentes a las originales. A continuación, imprime
             *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
             *   su valor en las segundas.
             *   Comprueba también que se ha conservado el valor original en las primeras.
             */


            // Ejemplo de asignación de varialbe por valor
            int a = 5;
            int b = a;
            a = 7;

            // a tiene el valor 7 y b tiene el valor 5
            Console.WriteLine($"a: {a}");
            Console.WriteLine($"b: {b}");


            // -------------------------------------------------------------------------------
            // -------------------------------------------------------------------------------


            // Ejemplo de asignación de variables por referencia
            int c = 10;
            Console.WriteLine($"c: {c}"); // c = 10
            _MetodoReferencia(ref c);

            Console.WriteLine($"c: {c}"); // c = 20


            // -------------------------------------------------------------------------------
            // -------------------------------------------------------------------------------


            // Ejemplos de funciones con variables que se les pasan por valor y por referencia

            // Pasar una variable por valor es que se hace una copia de la variable original y al salir del método, la copia se destruye
            int x = 5;
            _FuncionPorValor(x);
            Console.WriteLine($"x al final por valor: {x}");


            // Pasar una variable por referencia es que se conserva el valor de la variable original al salir del método
            // Usar ref cuando se deseen devolver dos o más valores en una función
            int y = 5;
            _FuncionPorReferencia(ref y);
            Console.WriteLine($"y al final por referencia: {y}");


            // -------------------------------------------------------------------------------
            // -------------------------------------------------------------------------------


            // Crea dos programas que reciban dos parámetros(cada uno) definidos como variables anteriormente.
            //      Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
            //      Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno se asigna a dos variables diferentes a las originales.
            //      A continuación, imprime el valor de las variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
            //      Comprueba también que se ha conservado el valor original en las primeras.


            int variable1 = 5;
            int variable2 = 10;

            Console.WriteLine($"variable1: {variable1}");
            Console.WriteLine($"variable2: {variable2}");

            int[] ints = _MetodoValor(variable1, variable2);

            int variable3 = ints[0];
            int variable4 = ints[1];

            Console.WriteLine($"variable3: {variable3}");
            Console.WriteLine($"variable4: {variable4}");

            Console.WriteLine($"variable1: {variable1}");
            Console.WriteLine($"variable2: {variable2}");


            // -------------------------------------------------------------------------------

            int variable5 = 15;
            int variable6 = 30;

            Console.WriteLine($"Valores antes del intercambio: variable5 = {variable5}, variable6 = {variable6}");

            _MetodoReferencia(ref variable5, ref variable6);

            Console.WriteLine($"Valores después del intercambio: variable5 = {variable5}, variable6 = {variable6}");
        }

        private static int[] _MetodoValor(int x, int y)
        {
            // x = 5
            // y = 10

            int aux = x;
            x = y;
            y = aux;

            // x = 10
            // y = 5

            return [x, y];

        }

        private static void _MetodoReferencia(ref int x, ref int y)
        {
            // x = 15;
            // y = 30;

            int temp = x;
            x = y;
            y = temp;

            // x = 30;
            // y = 15;
        }

        private static void _MetodoReferencia(ref int numero)
        {
            numero = 20;
        }

        private static void _FuncionPorValor(int x)
        {
            x *= 2;
            Console.WriteLine($"x dentro de la función: {x}");
        }

        private static void _FuncionPorReferencia(ref int y)
        {
            y *= 2;
            Console.WriteLine($"x dentro de la función: {y}");
        }
    }
}
