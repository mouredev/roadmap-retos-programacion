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

using System;

class Roadmap_02
{

    public static string VariableGlobal = "Roadmap_02";

    // Funciones sin parametros ni valor de retorno
    static void FuncionSinParametroSinRetorno()
    {
        Console.WriteLine("Funcion Sin Parametros y Sin Retorno");
    }

    // Funciones sin parametros pero con valor de retorno.
    static string FuncionSinParametrosConRetorno()
    {
        return "Funcion Sin Parametros y Con Retorno";
    }

    // Funciones con parametros pero sin valor de retorno
    static void FuncionConParametrosSinRetorno(int a, int b)
    {
        Console.WriteLine($"Funcion Con Parametros sin retorno: suma {a} + {b} = {a + b}");
    }

    // Funciones con parametros y valor de retorno
    static string FuncionConParametrosConRetorno(string nombre, string apellido)
    {
        return $"Hola {nombre} {apellido}";
    }

    // Funciones dentro de una funcion
    static void Calculadora(int a, int b)
    {


        int Suma(int a, int b)
        {
            return a + b;
        }

        int Resta(int a, int b)
        {
            return a - b;
        }

        int Multiplicacion(int a, int b)
        {
            return a * b;
        }

        float Division(int a, int b)
        {
            return a / b;
        }

        Consola.WriteLine($"Suma : {a} + {b} = {Suma(a, b)}");
        Consola.WriteLine($"Resta : {a} - {b} = {Resta(a, b)}");
        Consola.WriteLine($"Multiplicacion : {a} * {b} = {Multiplicacion(a, b)}");
        Consola.WriteLine($"Division : {a} / {b} = {Division(a, b)}");
    }


    public static int RetoExtra(string str1, string str2)
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

    static void Main(string[] args)
    {
        FuncionSinParametroSinRetorno();

        string resultado1 = FuncionSinParametrosConRetorno();
        Console.WriteLine(resultado1);

        FuncionConParametrosSinRetorno(5, 12);

        string resultado2 = FuncionConParametrosConRetorno();
        Console.WriteLine(resultado2);

        Calculadora(5, 12);

        // Función lambda
        Func<int, int> square = x => x * x;
        Console.WriteLine(square(9));

        // Función del propio lenguaje.
        string alfabeto = "ABCDEFGHIJKLMNOPQRSTVWYZ";
        Console.WriteLine(alfabeto.ToLower());

        // Vareiable Glogal
        Console.WriteLine(VariableGlobal);

        // Variables locales
        static void VariablesLocales()
        {
            int a = 1;
            int b = 2;
            Console.WriteLine($"{a} + {b} = {a + b}");
        }

        string s1 = "fizz", s2 = "buzz";
        Console.WriteLine($"\n\nEl numero ha salido {RetoExtra(s1, s2)} veces");


    }


}