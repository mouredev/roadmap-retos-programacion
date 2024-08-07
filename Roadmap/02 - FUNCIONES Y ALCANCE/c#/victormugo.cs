namespace _02_funciones
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * EJERCICIO:
             * - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
             *      Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
             * - Comprueba si puedes crear funciones dentro de funciones.
             * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
             * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
             * - Debes hacer print por consola del resultado de todos los ejemplos.
             *      (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
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


            // ------------- Funciones básicas

            // Método sin parámetros ni retorno
            MethodNoParametersNoReturn();

            // Método con uno o varios parámetros
            string parameter1 = "Parametro 1";
            MethodParametersNoReturn(parameter1);

            // Función sin parámetros y retorno
            string res = FunctionNoParametersReturn();
            Console.WriteLine(res);

            // Función con parámetros y retorno
            int a = 5;
            int b = 7;
            int result = 0;
            result = FunctionParametersReturn("suma", a, b);
            Console.WriteLine(result);

            result = FunctionParametersReturn("resta", a, b);
            Console.WriteLine(result);

            result = FunctionParametersReturn("multiplicar", a, b);
            Console.WriteLine(result);

            result = FunctionParametersReturn("dividir", a, b);
            Console.WriteLine(result);

            result = FunctionParametersReturn("resto", a, b);
            Console.WriteLine(result);


            // ------------- Funciones dentro de funciones
            FunctionExample();

            // ------------- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
            FunctionOwnLanguage();

            // ------------- Función concepto Variable Local y Global
            string cadenaTexto = "Soy la cadena de texto en concepto GLOBAL";
            Console.WriteLine(cadenaTexto);
            FunctionVariables();
            Console.WriteLine(cadenaTexto);



            // ------------- Dificultad extra
            int contador = ComparaCadenas("cadena1", "cadena2");
            Console.WriteLine($"Contador: {contador}");
        }


        public static void MethodNoParametersNoReturn()
        {
            Console.WriteLine("Hola. Soy un método que no devuelve nada");
        }


        public static void MethodParametersNoReturn(string parameter1)
        {
            Console.WriteLine($"Hola. Soy el parametro 1: {parameter1}");
        }


        public static string FunctionNoParametersReturn()
        {
            string cadena1 = "Soy la cadena 1 declarada en la función";
            return cadena1;
        }


        public static int FunctionParametersReturn(string operacion, int a, int b)
        {
            int result = 0;
            switch(operacion)
            {
                case "suma":
                    result = a + b;
                    break;

                case "resta":
                    result = a - b;
                    break;

                case "multiplicar":
                    result = a * b;
                    break;

                case "dividir":
                    result = a / b;
                    break;

                default:
                    result = -1;
                    break;
            }

            return result;
        }

        public static void FunctionOwnLanguage()
        {
            string cadena = "Esto es una cadena, separada por una coma";
            string[] partes = cadena.Split(",");

            for (int i = 0; i < partes.Length; i++)
            {
                Console.WriteLine($"Partes cadena: {partes[i]}");
            }
        }

        public static void FunctionVariables()
        {
            string cadenaTexto = "Soy la cadena de texto en concepto LOCAL";
            Console.WriteLine(cadenaTexto);
        }

        public static void FunctionExample()
        {
            string result = FunctionInsideFunction(5);
            Console.WriteLine(result);
        }

        public static string FunctionInsideFunction(int number1)
        {
            string cadena1 = "No es un 5";
            if (number1 == 5)
            {
                cadena1 = "Es un 5";
            }

            return cadena1;
        }



        public static int ComparaCadenas(string cadena1, string cadena2)
        {
            int contador = 0;

            Console.WriteLine("---------------------------------------");

            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0 && i % 5 == 0)
                {
                    // Múltiplo de 3 y 5
                    Console.WriteLine($"{cadena1} - {cadena2}");
                    continue;
                }
                else if (i % 3 == 0)
                {
                    // Múltiplo de 3
                    Console.WriteLine($"{cadena1}");
                    continue;
                } 
                else if (i % 5 == 0)
                {
                    // Múltiplo de 5
                    Console.WriteLine($"{cadena2}");
                    continue;
                }
                else
                {
                    Console.WriteLine($"{i}");
                    contador++;
                }
            }

            return contador;
        }

    }
}
