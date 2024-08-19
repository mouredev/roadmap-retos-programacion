using System.Security.Cryptography.X509Certificates;

namespace _02_FUNCIONES_Y_ALCANCE
{
    internal class Program
    {
       

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

            string variableGlobal = "soy global"; //  variable global

            // METODO SIN PARAMETROS

            MetodoSinParametros();

            // METODO CON PARAMETROS

            Suma(15, 30);

            // METODO CON RETORNO

            static bool MetodoConRetorno()
            {
                bool resultado = false;
                string palabra = "edificio";
                if ("aeiou".Contains(palabra[0]))
                {
                    resultado = true;
                }
                else
                {
                    resultado = false;
                }
                return resultado;
            }

            bool resultado = MetodoConRetorno();

            if (resultado)
            {
                Console.WriteLine("la palabra empieza con vocal");
            }
            else
            {
                Console.WriteLine("la palabra empieza con consonante");
            }

            Metodo1("edificio");  // puedo ejecutar ambos metodos solamente llamando el Metodo1 ya que al llamar ese metodo se llama el otro

            
            // METODOS YA EXISTENTES EN C#

            string palabra = "Hola";
            string mayusculas = palabra.ToUpper(); // "HOLA"
            string minusculas = palabra.ToLower(); // "hola"

            Console.WriteLine(mayusculas);
            Console.WriteLine(minusculas);

            // METODO CON VARIABLE LOCAL

            static void VariableLocal()
            {
                string variableLocal = "soy local"; // variable local
            }


            DificultadExtra("primer texto", "segundo texto");
        }


        // METODO SIN PARAMETROS 

        static void MetodoSinParametros()
        {
            Console.WriteLine("este es el metodo ejecutandose");
        }

        // METODO CON PARAMETROS

        static void Suma(int a, int b)
        {
            Console.WriteLine($"la suma de {a} + {b} es: {a + b} ");
        }

        // METODO DENTRO DE OTRO METODO

        static void Metodo1(string palabra) // este es el primer metodo
        {
            Metodo2(palabra);  // podemos llamar a Metodo2 dentro de Metodo1
        }

        static void Metodo2(string palabra)   // este es el segundo metodo que se ejecuta cuando es llamado desde el primer metodo
        {
            if ("aeiou".Contains(palabra[0]))
            {
                Console.WriteLine("empieza con vocal");
            }
            else
            {
                Console.WriteLine("empieza con consonante");
            }
        }

        static int DificultadExtra(string a, string b)
        {
            int numerosContados = 0;

            for(int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0 && i % 5 == 0)
                {
                    Console.WriteLine(a + " Y " + b);
                }
                else if (i % 3 == 0)
                {
                    Console.WriteLine(a);
                }
                else if (i % 5 == 0)
                {
                    Console.WriteLine(b);
                }
                else
                {
                    Console.WriteLine(i);
                    numerosContados++;
                }
            }

            return numerosContados;
        }
    }
}
