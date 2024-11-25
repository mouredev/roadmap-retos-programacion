using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Runtime.ConstrainedExecution;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;
using System.Text;
using System.Threading.Tasks;

namespace PracticasLogicaProgramacion
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //EJERCICIOS
            //1. Crea un comentario en el código y coloca la URL del 
            //sitio web oficial del lenguaje de programación que has seleccionado.

            https://learn.microsoft.com/en-us/dotnet/csharp/

            //2. Representa las diferentes sintaxis que existen de crear comentarios
            //en el lenguaje (en una línea, varias...).

            //Este se utiliza para escribir comentarios de una sola linea.
            /*
            este se utiliza para escribir comentarios de varias lineas.
            */

            //3. Crea una variable (y una constante si el lenguaje lo soporta).

            private int num;
            private const int numConst;

            //4. Crea variables representando todos los tipos de datos primitivos
            //del lenguaje (cadenas de texto, enteros, booleanos...).

            //1. Enteros
            private int num1; //numeros enteros de 32 bits.
            private long num2; //numeros enteros de 64 bits.
            private short num3; //numeros enteros de 16 bits.
            private byte num4; //numeros enteros sin signo de 8 bits.
            private sbyte num5; //numeros enteros con signo de 8 bits.
            private uint num6; //numeros enteros sin signo de 32 bits,
            private ulong num7; //numeros enteros sin signo de 64 bits.
            private ushort num8; //numeros enteros sin signo de 16 bits.

            //2. Float
            private float num9; //Números de punto flotante de precisión simple (32 bits).
            private double num10; //Números de punto flotante de doble precisión (64 bits).

            //3. Decimal
            private decimal num11; //Números decimales de alta precisión, generalmente usados para cálculos financieros (128 bits).

            //4. Booleanos
            bool jump; // Representa valores booleanos (true o false).

            //5. Caracteres
            private char Caracter; //Representa un carácter Unicode UTF-16 (16 bits).

            //6. Cadenas
            private string name; //Secuencia de caracteres Unicode.

            //5. Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
            EJERCICIO ejercicio = new EJERCICIO();
            ejercicio.saludo();

        }
        public class EJERCICIOS
        {
            public void Saludo()
            {
                Console.WriteLines("¡Hola, [C#]!")
            }

        }
    }
}

namespace _00_SINTAXIS__VARIABLES__TIPOS_DE_DATOS_Y_HOLA_MUNDO
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // EJERCICIO:
            //1-Crea un comentario en el código y coloca la URL del sitio web oficial del
            //  lenguaje de programación que has seleccionado.
            //https://learn.microsoft.com/en-us/dotnet/csharp/

            //2-Representa las diferentes sintaxis que existen de crear comentarios
            //  en el lenguaje(en una línea, varias...).

            // Esta reprenta un comentario de una linea
            /*
             * esta representa un comentarios de varias lineas
             */

            //3-Crea una variable(y una constante si el lenguaje lo soporta).

            //4-Crea variables representando todos los tipos de datos primitivos
            //  del lenguaje(cadenas de texto, enteros, booleanos...).

            //5-Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
            EJERCICIOS ejercicios = new EJERCICIOS();
            ejercicios.getLenguaje();

        }
        public class EJERCICIOS
        {
            //3-Crea una variable(y una constante si el lenguaje lo soporta).
            private int myNum;
            private const int numConst = 0;

            //4-Crea variables representando todos los tipos de datos primitivos
            //  del lenguaje(cadenas de texto, enteros, booleanos...).
            private int num1; //Números enteros de 32 bits.
            private long num2; //Números enteros de 64 bits.
            private short num3; //Números enteros de 16 bits.
            private byte num4; //Números enteros sin signo de 8 bits.
            private sbyte num5; //Números enteros con signo de 8 bits.
            private uint num6; //Números enteros sin signo de 32 bits.
            private ulong num7; //Números enteros sin signo de 64 bits.
            private ushort num8; //Números enteros sin signo de 16 bits.
            private float myfloat; //Números de punto flotante de precisión simple(32 bits).
            private double num_double; //Números de punto flotante de doble precisión(64 bits).
            private decimal num_decimal; //Números decimales de alta precisión, generalmente usados para cálculos financieros(128 bits).
            private bool boolean; //Representa valores booleanos(true o false).
            private char char1; //Representa un carácter Unicode UTF-16 (16 bits).
            private string name; //Secuencia de caracteres Unicode.

            public void getLenguaje()
            {
                Console.WriteLine("¡Hola, [C#]!");
            }
        }
    }
}