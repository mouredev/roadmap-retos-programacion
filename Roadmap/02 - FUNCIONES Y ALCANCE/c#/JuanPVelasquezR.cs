/*
 * EJERCICIO:
 * - Crea ejemplos de funciones b�sicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin par�metros ni retorno, con uno o varios par�metros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza alg�n ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer m�s o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una funci�n que reciba dos par�metros de tipo cadena de texto y retorne un n�mero.
 * - La funci�n imprime todos los n�meros del 1 al 100. Teniendo en cuenta que:
 *   - Si el n�mero es m�ltiplo de 3, muestra la cadena de texto del primer par�metro.
 *   - Si el n�mero es m�ltiplo de 5, muestra la cadena de texto del segundo par�metro.
 *   - Si el n�mero es m�ltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La funci�n retorna el n�mero de veces que se ha impreso el n�mero en lugar de los textos.
 *
 * Presta especial atenci�n a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el c�digo se entienda.
 */


internal class Program
{
    static bool globalVariable = true;

    static void Main(string[] args)
    {

        /*
          * EJERCICIO:
          * - Crea ejemplos de funciones b�sicas que representen las diferentes
          *   posibilidades del lenguaje:
          *   Sin par�metros ni retorno, con uno o varios par�metros, con retorno...
          * - Comprueba si puedes crear funciones dentro de funciones.
          * - Utiliza alg�n ejemplo de funciones ya creadas en el lenguaje.
          * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
          * - Debes hacer print por consola del resultado de todos los ejemplos.
          *   (y tener en cuenta que cada lenguaje puede poseer m�s o menos posibilidades)
          *
          * DIFICULTAD EXTRA (opcional):
          * Crea una funci�n que reciba dos par�metros de tipo cadena de texto y retorne un n�mero.
          * - La funci�n imprime todos los n�meros del 1 al 100. Teniendo en cuenta que:
          *   - Si el n�mero es m�ltiplo de 3, muestra la cadena de texto del primer par�metro.
          *   - Si el n�mero es m�ltiplo de 5, muestra la cadena de texto del segundo par�metro.
          *   - Si el n�mero es m�ltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
          *   - La funci�n retorna el n�mero de veces que se ha impreso el n�mero en lugar de los textos.
          *
          * Presta especial atenci�n a la sintaxis que debes utilizar en cada uno de los casos.
          * Cada lenguaje sigue una convenciones que debes de respetar para que el c�digo se entienda.
          */

        FuncionSinRetorno();

        FuncionParametros(40000, 6, "Null");

        Console.WriteLine($"El precio del producto es: {FuncionRetorno(3000, 3)}");

        //El mismo Console.Writeline es una funci�n propia del lenguaje





        // Dificultad extra

        Console.WriteLine(Desafio("Hola", "Mundo"));

    }


    static void FuncionSinRetorno()
    {
        Console.WriteLine("Funci�n sin par�metros");
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