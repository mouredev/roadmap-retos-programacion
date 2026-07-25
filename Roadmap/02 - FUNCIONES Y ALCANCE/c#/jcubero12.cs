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

using system;

public class
 {

    static string global = "esto es una variable global";

    static void Main(string[] args)
    {

        //Funciones
        Console.WriteLine("Impresion de funciones: ");
        Saluda(); //Sin parámetros ni retorno
        SaludarA("Jose"); //Con un parámetro
        edad("Jose", 1980); //Con dos parámetros y retorno

        OuterFuncion();

        //Funcion creada por el lenguaje
        Random random = new Random();
        Console.WriteLine(random.Next());

        //Variables locales y globales
        variables();

    }

    static void Saluda()
    {
        Console.WriteLine("Hola mundo!");
    }

    static void SaludarA(string nombre)
    {
        Console.WriteLine("Hola, " + nombre);
    }


    static int edad(string nombre, int yearborn)
    {

        int edad = 2024 - yearborn;
        return $"Hola, {nombre}. Según tu año de nacimiento tienes {edad} años."
    }


    static void OuterFuncion()
    {
        Console.WriteLine("Estoy en la función outer");

        void InnerFuncion()
        {
            Console.WriteLine("Esto es una función inner");
        }

        InnerFuncion();
    }

    static void variables()
    {
        string local = "esto es una variable local";
        Console.WriteLine(local); //imprime "esto es una variable local"
        Console.WriteLine(global); //imprime "esto es una variable global"
    }

    //Ejercicio extra
    static int imprimirNumeros(string texto1, string texto2)
    {
        int contador = 0;
        for (int i = 1; i <= 100; i++)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                Console.WriteLine(texto1 + " " + texto2);
            }
            else if (i % 3 == 0)
            {
                Console.WriteLine(texto1);
            }
            else if (i % 5 == 0)
            {
                Console.WriteLine(texto2);
            }
            else
            {
                Console.WriteLine(i);
                contador++;
            }
        }
        return contador;
    }
}


