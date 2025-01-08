// using System;
// using System.Collections.Generic;
// using System.Linq;
// using System.Threading.Tasks;

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

namespace Reto00
{
    public class lobogeekmx
    {
        // Pagina web de C# -->  https://dotnet.microsoft.com/es-es/languages/csharp

        // Comentario de una sola línea

        /*
            Este es un comentario multilinea 

        */

        var primer_variable = "primer variable";

        const string VARIABLE_CONSTANTE = "Esta variable no cambia"; // por convencion se declara en mayuscula

        int i = 0;

        long l = 1234567890123456789L; // Se agrega una "L" al final 

        float f = 45.5f; // Se agrega la "f" al final. Float y decimal son mas rapidos. 7 digitos

        double d = 3.14; // precision de 15 digitos

        decimal de = 4562.25M; // Se agrega una "M" al final. Principlmente usado para dinero

        char c = 'S';

        bool b = true;

        Console.WriteLine("¡Hola, C#!")
    }
}