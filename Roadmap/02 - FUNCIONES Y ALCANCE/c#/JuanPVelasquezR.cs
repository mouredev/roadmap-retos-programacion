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


internal class Program
{
    static bool globalVariable = true;

    static void Main(string[] args)
    {

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

        FuncionSinRetorno();

        FuncionParametros(40000, 6, "Null");

        Console.WriteLine($"El precio del producto es: {FuncionRetorno(3000, 3)}");

        //El mismo Console.Writeline es una función propia del lenguaje





        // Dificultad extra

        Console.WriteLine(Desafio("Hola", "Mundo"));

    }


    static void FuncionSinRetorno()
    {
        Console.WriteLine("Función sin parámetros");
    }

    static void FuncionParametros(int precio, int cantidad, string perfil)
    {
        if (precio >= 30000 && cantidad > 4) { perfil = "VIP"; }

        Console.WriteLine($"El cliente tiene perfil: {perfil}");

    }


    static int FuncionRetorno(int precio, int Cantidad)
    {

        return precio + Cantidad;


    }



    public void FuncionInception()
    {
        /*     try
             {
                static void Funcion()
                 {

                     Console.WriteLine("Es posible");
                 }

             }
             catch (Exception ex)
             {
                 Console.WriteLine("No es posible");

             }
        */




    }


    static int Desafio(string cadena1, string cadena2)
    {
        int j = 0;
        for (int i = 1; i <= 100; i++)
        {
            j = i;

            if (i % 3 != 0 && i % 5 != 0)
            {
                Console.WriteLine(i);
            }
            else if (i % 3 == 0 && i % 5 == 0)
            {
                Console.WriteLine($"{cadena1} {cadena2}");
            }
            else if (i % 3 == 0)
            {
                Console.WriteLine(cadena1);
            }
            else if (i % 5 == 0)
            {
                Console.WriteLine(cadena2);
            }
        }

        return j;

    }
}