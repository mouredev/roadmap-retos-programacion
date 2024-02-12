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
namespace RetosProgramacion2024
{
    internal class Reto0
    {
        static void Main(string[] args)
        {
            // https://learn.microsoft.com/es-es/dotnet/csharp/
            // Comentario de una linea
            /* Comentario de 
             * varias
             * lineas
             */

            //Crear variable y constante
            int a = 1;
            const int b = 2;

            // Tipos primitivos
            sbyte mySbyte = 1;
            byte myByte = 1;
            short myShort = 1;
            ushort myUShort = 1;
            int myInt = 1;
            uint myUInt = 1;
            long myLong = 1;
            ulong myULong = 1;
            float myFloat = 1;
            double myDouble = 1;
            decimal myDecimal = 1;
            char myChar = '\0';
            bool myBoolean = false;

            Console.WriteLine("¡Hola, C#!");
        }
    }
}
