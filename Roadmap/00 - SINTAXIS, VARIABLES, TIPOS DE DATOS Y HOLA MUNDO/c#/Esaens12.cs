namespace _00_SINTAXIS__VARIABLES__TIPOS_DE_DATOS_Y_HOLA_MUNDO
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /* EJERCICIO:
* - Crea un comentario en el código y coloca la URL del sitio web oficial del
*   lenguaje de programación que has seleccionado.
* - Representa las diferentes sintaxis que existen de crear comentarios
*   en el lenguaje (en una línea, varias...).
* - Crea una variable (y una constante si el lenguaje lo soporta).
* - Crea variables representando todos los tipos de datos primitivos
*   del lenguaje (cadenas de texto, enteros, booleanos...).
* - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" */

            //https://dotnet.microsoft.com/es-es/languages/csharp SITIO OFICIAL DE C#

            // COMENTARIO EN UNA SOLA LINEA

            /* COMENTARIO
             * EN 
             * VARIAS
             * LINEAS */

            string variable; // variable de tipo string

            const double pi = 3.1416; // esto es una variable constante

            // Tipos Enteros

            // byte: Almacena un número entero sin signo de 8 bits (0 a 255)
            byte byteVar = 255;

            // sbyte: Almacena un número entero con signo de 8 bits (-128 a 127)
            sbyte sbyteVar = -128;

            // short: Almacena un número entero con signo de 16 bits (-32768 a 32767)
            short shortVar = -32768;

            // ushort: Almacena un número entero sin signo de 16 bits (0 a 65535)
            ushort ushortVar = 65535;

            // int: Almacena un número entero con signo de 32 bits (-2,147483648 a 2147483647)
            int intVar = -2147483648;

            // uint: Almacena un número entero sin signo de 32 bits (0 a 4294967295)
            uint uintVar = 4294967295;

            // long: Almacena un número entero con signo de 64 bits (-9223372036854775808 a 9223372036854775807)
            long longVar = -9223372036854775808;

            // ulong: Almacena un número entero sin signo de 64 bits (0 a 18446744073709551615)
            ulong ulongVar = 18446744073709551615;

            // Tipos de Coma Flotante

            // float: Almacena un número de punto flotante de precisión simple de 32 bits (±1.5e-45 a ±3.4e38), con 7 dígitos de precisión
            float floatVar = 3.14f;

            // double: Almacena un número de punto flotante de precisión doble de 64 bits (±5.0e-324 a ±1.7e308), con 15-16 dígitos de precisión
            double doubleVar = 3.141592653589793;

            // Tipo Decimal

            // decimal: Almacena un número de punto flotante decimal de 128 bits (±1.0e-28 a ±7.9e28), con 28-29 dígitos de precisión. Ideal para cálculos financieros
            decimal decimalVar = 3.1415926535897932384626433832m;

            // Tipo Booleano

            // bool: Almacena un valor booleano que puede ser true o false
            bool boolVar = true;

            // Tipo de Carácter

            // char: Almacena un carácter Unicode de 16 bits. Puede almacenar cualquier carácter Unicode
            char charVar = 'A';

            // Tipo de Cadena

            // string: Almacena una secuencia de caracteres. Es un tipo de referencia
            string stringVar = "Hola, mundo!";

            // Tipo de Puntero Nulo

            // object: El tipo base de todos los tipos en C#. Puede almacenar cualquier tipo de dato
            object objectVar = "Esto es un objeto";
            object objectVar2 = 35.6743;
            object objectVar3 = 'a';
            object objectVar4 = true;
            object objectVar5 = 456;

            string lenguaje = "C#";

            Console.WriteLine($" HOLA {lenguaje}");
        }
    }
}
