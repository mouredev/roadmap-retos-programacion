using System;
using System.Runtime.InteropServices;

class sintaxisVariables
{
    static void Main()
    {
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

        //Ejercicio

        //El leguaje de programación que estoy utilizando es C#: https://learn.microsoft.com/en-us/dotnet/csharp/

        //Esto es para crear comentarios de una linea.

        /*
         * Así 
         * Se crean
         * Comentarios de 
         * Varias Lineas
         *  
         */

        /// <summary>
        /// Esto es un comentario en formato XML
        /// </summary>

        //Variable
        string variable = "Esto es una variable";

        //Constante (Por convención, las constantes se declaran con nombre en MAYÚSCULAS)
        const double PI = 3.1416d;

        //Variables con todos los tipos de datos primitivos
        //Cadena de texto
        string maquina = "Esto es una variable de texto";

        //Variables para representar numero decimales
        //Para representar decimales grandes
        double pi = 0.0d;

        //Para representar decimales pequeños
        float numeroFlotante = 0.0f;

        //Para representar decimales muy exactos
        decimal numeroDecimalExacto = 0.0m;

        //Variable para representar números enteros
        int num = 5;

        //Variable boolean, true or false
        bool verdaderoOfalso = true;

        //Arreglos
        //Arreglo de enteros de tamaño fijo
        int[] numero = [5];

        //Arreglo inicializado
        int[] numeros = [5, 6, 3];
        string[] supermercado = ["aguacate", "papas", "Peras", "MANZANAS"];
        object[] arreglo = [1, "Peras", "uvas", 24, 23.5, "Libro"];

        //Tuplas
        (int, string) par = (1, "Hola");

        //Hola Mundo
        Console.WriteLine("¡Hola, C#!");






    }
}

