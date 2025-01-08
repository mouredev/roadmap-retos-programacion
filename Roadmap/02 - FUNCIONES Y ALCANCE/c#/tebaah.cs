internal class Program
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
    private static void Main(string[] args)
    {
        // Ejemplo de función sin parámetros ni retorno
        void Saludar()
        {
            Console.WriteLine("¡Hola!");
        }

        Saludar();

        // Ejemplo de función con un parámetro y retorno
        int Sumar(int a, int b)
        {
            return a + b;
        }

        Console.WriteLine(Sumar(2, 3));

        // Ejemplo de función con varios parámetros y retorno
        int Multiplicar(int a, int b, int c)
        {
            return a * b * c;
        }

        Console.WriteLine(Multiplicar(2, 3, 4));

        // Ejemplo de función con retorno
        int ObtenerNumero()
        {
            return 42;
        }

        Console.WriteLine(ObtenerNumero());

        // Ejemplo de función con parámetros
        void SaludarA(string nombre)
        {
            Console.WriteLine($"¡Hola, {nombre}!");
        }

        SaludarA("Mundo");

        // Ejemplo de función con parámetros y retorno
        string SaludarAConRetorno(string nombre)
        {
            return $"¡Hola, {nombre}!";
        }

        Console.WriteLine(SaludarAConRetorno("Mundo"));

        // Ejemplo de función dentro de otra función
        void FuncionExterna()
        {
            Console.WriteLine("Función externa");

            void FuncionInterna()
            {
                Console.WriteLine("Función interna");
            }

            FuncionInterna();
        }

        FuncionExterna();


        int ImprimirNumeros(string texto1, string texto2)
        {
            int contador = 0;
            for (int i = 1; i <= 100; i++)
            {
                if (i % 3 == 0 && i % 5 == 0)
                {
                    Console.WriteLine(texto1 + texto2);
                    contador++;
                }
                else if (i % 3 == 0)
                {
                    Console.WriteLine(texto1);
                    contador++;
                }
                else if (i % 5 == 0)
                {
                    Console.WriteLine(texto2);
                    contador++;
                }
            }
            return contador;
        }

        int vecesImpreso = ImprimirNumeros("Fizz", "Buzz");
        Console.WriteLine($"La función ImprimirNumeros se ha ejecutado {vecesImpreso} veces.");
    }
}