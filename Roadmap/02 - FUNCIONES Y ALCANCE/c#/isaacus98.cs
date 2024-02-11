/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

using static System.Net.Mime.MediaTypeNames;

namespace RetosProgramacion2024
{
    internal class Reto2
    {
        private static int VariableGlobal = 1000;

        static void Main(string[] args)
        {
            FuncionSinRetorno();

            FuncionSinRetornoConUnParametro("Hola");

            FuncionSinRetornoConDosParametros("parámetro 1", "parámetro 2");

            // Función con parámetro opcional definido.
            FuncionSinRetornoConParametroOpcional("Hola");
            // Función con parámetro opcional en el qual no se ha definido el parámetro.
            FuncionSinRetornoConParametroOpcional();

            FuncionSinRetornoConParams(1, 2, 3, 4, 5);
            FuncionSinRetornoConParams(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

            Console.WriteLine(Suma(5, 10));

            Console.WriteLine(CalcularFactorial(10));

            // Función lambda
            Func<int, int> square = x => x * x;
            Console.WriteLine(square(5));

            // Función del propio lenguaje.
            string str = "hola";
            Console.WriteLine(str.ToUpper()); // Función ToUpper: Convierte la minúsculas en mayúsculas.

            // Función global
            // Las variables globales se pueden usar en todas las funciones de la classe.
            // Las variables locales solo se pueden usar dentro de la función donde se han definido.
            Console.WriteLine(VariableGlobal);

            // Reto extra
            Console.WriteLine($"Se ha impreso un total de {RetroExtra("FIZZ", "BUZZ")} números.");
        }

        private static int RetroExtra(string str1, string str2)
        {
            int contadorNumeros = 0;

            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0 & i % 5 == 0)
                {
                    Console.WriteLine($"{str1} {str2}");
                } 
                else if (i % 3 == 0)
                {
                    Console.WriteLine(str1);
                }
                else if (i % 5 == 0)
                {
                    Console.WriteLine(str2);
                }
                else
                {
                    Console.WriteLine(i);
                    contadorNumeros++;
                }
            }

            return contadorNumeros;
        }

        // Función sin parametros
        private static void FuncionSinRetorno()
        {
            Console.WriteLine("Función sin retorno");
        }

        // Función con 1 parametro
        private static void FuncionSinRetornoConUnParametro(string str)
        {
            Console.WriteLine(str);
        }

        // Función con 2 parámetros
        private static void FuncionSinRetornoConDosParametros(string str1, string str2)
        {
            Console.WriteLine($"Primer parametro: {str1}");
            Console.WriteLine($"Segundo parametro: {str2}");
        }

        // Función con parámetro opcional.
        // Los parámetros opcionales siempre se definen al final de la lista de parámetros.
        private static void FuncionSinRetornoConParametroOpcional(string parametroOpcional = "parametro opcional")
        {
            Console.WriteLine(parametroOpcional);
        }

        /* Función con parámetro params
         * El parametro params siempre se define al final de la lista de parametros
         * El orden seria el siguiente: parametros obligatorios, parametros opcionels, paremetro params.
         * El parámetro de params sirve para declarar una función en el que no se conoce el número de parámetros que recibe.
         * La función recibe una cantidad variable de parametros que se agrupa en un array.
         */
        private static void FuncionSinRetornoConParams(params int[] numeros)
        {
            foreach(int numero in numeros)
            {
                Console.WriteLine(numero);
            }
        }

        // Función que devuelve un valor.
        private static int Suma(int num1, int num2)
        {
            return num1 + num2;
        }

        // Función dentro de una función.
        // https://learn.microsoft.com/es-es/dotnet/csharp/programming-guide/classes-and-structs/local-functions
        private static int CalcularFactorial(int numero)
        {
            return FuncionDentroDeFuncion(numero);

            int FuncionDentroDeFuncion(int num)
            {
                return num < 2 ? 1 : num * FuncionDentroDeFuncion(num - 1);
            }  
        }
    }
}
