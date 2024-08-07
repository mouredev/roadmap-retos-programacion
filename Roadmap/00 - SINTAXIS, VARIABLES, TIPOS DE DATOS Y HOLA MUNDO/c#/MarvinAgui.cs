using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _00_SINTAXIS__VARIABLES__TIPOS_DE_DATOS_Y_HOLA_MUNDO
{
    internal class Program
    {
        enum weekdays { Monday, Tuesday, Wednsday, thursday, Friday, Saturday, Sunday};
        // Aqui observamos que tambine podemor declarar variables globales 
        // se dice que no es buena practica la utilizacion de este tipo de variables en C#, aunque dependera de la situacion

        static void Main(string[] args)
        {
            // En C# hay dos maneras de reprensentar los comentarios

            /* La primera es con dos barras // como observamos en la linea 13 del codigo y la segunda
               se utiliza para seleccionar varias libeas de cogido o comentar en varias lideas diferentes que es 
               lo que estoy haciendo en este comentario.
               - Aquí tenemos toda la documentacion Oficial de C#: https://learn.microsoft.com/es-es/dotnet/csharp/ */

            // Ahora vamor a declarar algunas variables y veremos tambien los tipos primivitos que tenemos en C#
            // En C# la sintaxis a¡para declaras las variables es: <tipo> <nombre_variable>

            var greet = "Hola";
            var age = 37;       // como podemos ver la palabra reservada "var" se puede utilizar para cualquier tipo de dato
            var pi = 3.14;      // es el propio compilador quien establece el tipo en funcion del valor que le demos a la variable 

            // Aqui tenemos la declaracion de una constante (cuyo valor no puede cambiar)
            const string despedida = "adios";

            //tipos de datos 

            /* TIPOS SIMPLES: Sbyte, short, int, long --- enteros con signo
                              Byte, unshort, uint, ulong --- enteros sin signo
                              Float, double --- punto flotante
                              Char --- caracteres
                              Decimal --- decimal de alta precisión
                              Bool --- booleano

               TIPO DATO enum --- como hemos visto en la variable global "Weekdays" 

            */

            // Algunos Ejemplos:

            bool verdadero = true;
            bool falso; // por default el tipo bool dara "false"

            Char letra = 'a';

            float numeros = 3.34f; // puede albergar hasta 4 bytes (32 bits) en memoria, que equivalen a 7 decimales

            double num = 2.3432; // Es el que mas se utiliza ya que puede albergar hasta 8 bytes (64 bits) que equivalen hasta 15 decimales de precision

            decimal precision = 322.9275624795m; // se utiliza para la maxima precision posible, para transacciones economicas por ejeplo
            // decimal alberga valores de hasta 16 bytes (128 bits)


            // Tipo String para representar cadenas de texto 

            string cadena = " Hola, C# ";

            // Tipo Matriz Unidimensional y Bidimensional
            int[] miArray = new int[5]; // array tipo int con 5 posiciones 
            string [] miArray2 = new string[] { "cocina", "baño", "salon", "comedor", "dormitorio" }; // aqui observamos un array de tipo string tambien con 5 posiciones 

            int[,] arrayBidimensional = new int[2, 3]; // los valores se refieren a 2 Filas, 3 Columnas 
            int[,] bidimensional2 = { {'a', 'b', 'c' }, {'d', 'e', 'f' } }; // al igual que el anterior este array contiene 2 Filas y 3 Columnas, ahora los valores estan asignados

            // Y para terminar sacaremos por consola nuestro " Hola, C#" y utilizaremos Console.ReadKey(); para que el programa espere y podamos observar lo que tenemos por consola

            Console.WriteLine(cadena);
            Console.ReadKey();

        }
    }
}
