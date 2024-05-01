//Author: Sandra Baigorri Saez
using System;

namespace _00
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
            //https://learn.microsoft.com/es-es/dotnet/csharp/

            //Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje(en una línea, varias...).
            // COMENTARIO EN UNA LINEA
            /* COMENTARIO EN VARIAS LINEAS COMENTARIO EN VARIAS LINEAS COMENTARIO EN VARIAS LINEAS 
              COMENTARIO EN VARIAS LINEAS COMENTARIO EN VARIAS LINEAS 
              COMENTARIO EN VARIAS LINEAS COMENTARIO EN VARIAS LINEAS COMENTARIO EN VARIAS LINEAS  */
            /// COMENTARIOS DE DOCUMENTACIÓN XLM

            //Crea una variable(y una constante si el lenguaje lo soporta).
            int variable = 0;
            const int constante = 0;

            //Crea variables representando todos los tipos de datos primitivos del lenguaje(cadenas de texto, enteros, booleanos...).
            string cadena = "";
            char caracter = ' ';
            bool booleano = false;
            int entero = 0;
            short entero_peque = 0;
            long entero_grande = 0;
            float decimal_peque = 0;
            double decimales = 0;
            decimal decimal_grande = 0;

            //Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
            Console.WriteLine("¡Hola, c#!");
        }
    }
}
