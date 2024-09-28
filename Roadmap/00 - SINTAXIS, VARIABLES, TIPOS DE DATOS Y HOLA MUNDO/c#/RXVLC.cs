using System;

/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */
namespace R00
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //https://learn.microsoft.com/en-us/dotnet/csharp/

            //Comentario en una linea

            /* 
             * Comentario
             * en varias
             * lineas
             * */

            string prueba1 = "";
            const string prueba2 = "prueba";

            string cadenaDeTexto = "Esto es una cadena de texto";
            int numeroEntero = 3;
            double numeroConDecimales = 10.2;
            bool variableBooleana = false;
            string nombreLenguaje = "C#";

            Console.WriteLine($"¡Hola, {nombreLenguaje}!");

            Console.ReadKey();

        }
    }
}
