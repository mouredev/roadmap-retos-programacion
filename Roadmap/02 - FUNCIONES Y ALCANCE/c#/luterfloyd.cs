/*
 EJERCICIO:
 - Crea ejemplos de funciones básicas que representen las diferentes
   posibilidades del lenguaje:
   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 - Comprueba si puedes crear funciones dentro de funciones.
 - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 - Debes hacer print por consola del resultado de todos los ejemplos.
   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

 DIFICULTAD EXTRA (opcional):
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

 Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
*/
using System;
using System.ComponentModel.Design.Serialization;
using System.Data;

internal class Program
{
    private static void Main(string[] args)
    {
        // FUNCION SIN PARAMENTROS NI VALOR DE RETORNO
        static void Saludando()
        {
            Console.WriteLine("Hola CSharp");
        }

        // FUNCION CON PARAMETROS Y RETORNANDO VALOR
        static float Operacion(string strOperador, float nValor1, float nValor2)
        {
            float nResultado = 0;
            switch (strOperador)
            {
                case "SUMA":
                    nResultado = nValor1 + nValor2;
                    break;
                case "RESTA":
                    nResultado = nValor1 - nValor2;
                    break;
                case "MULTIPLICACION":
                    nResultado = nValor1 * nValor2;
                    break;
                case "DIVISION":
                    nResultado = nValor1 / nValor2;
                    break;
                default:
                    Console.WriteLine("Error: operador invalido");
                    Environment.Exit(-1);
                    break;
            }
            return nResultado;
        }

        // FUNCIONES ANIDADAS
        (int, int) FactorialconIteraciones(int nValor)
        {
            int nIteraciones = 0;
            int nFactorial = 0;

            // FUNCION RECURSIVA: SE PUEDE INVOCAR A SI MISMA
            int Factorial(int nValor)
            {
                nIteraciones++; // ESTA VARIABLE ESTA DEFINIDA EN UN AMBITO SUPERIOR ASI QUE SE CONSERVA EL VALOR
                if (nValor == 0) return 1;
                return nValor * Factorial(nValor - 1);
            }

            nFactorial = Factorial(nValor);
            return (nIteraciones, nFactorial);

        }

        // EJERCICIO ADICIONAL: FUNCION QUE RECIBE DOS CADENAS Y RETORNA UN VALOR
        static int FizzBuzz(string strCadena1, string strCadena2)
        {
            int nContador = 0;

            for (int indice = 1; indice <= 100; indice++)
            {
                if (indice % 3 == 0 && indice % 5 == 0) Console.WriteLine(strCadena1 + strCadena2);
                else if (indice % 3 == 0) Console.WriteLine(strCadena1);
                else if (indice % 5 == 0) Console.WriteLine(strCadena2);
                else
                {
                    nContador++;
                    Console.WriteLine(indice);
                }
            }
            return nContador;
        }

        int nIteraciones = 0;
        int nFactorial = 0;
        int nFizzBuzz = 0;

        Saludando();
        Console.WriteLine(Operacion("SUMA", 2, 3));
        Console.WriteLine(Operacion("RESTA", 2, 3));
        (nIteraciones, nFactorial) = FactorialconIteraciones(4);
        Console.WriteLine("Factorial: " + nFactorial + " nro. de iteraciones: " + nIteraciones);
        nFizzBuzz = FizzBuzz("Fizz", "Buzz");
        Console.WriteLine("Resultado ejercicio adicional: " + nFizzBuzz);
    }
}