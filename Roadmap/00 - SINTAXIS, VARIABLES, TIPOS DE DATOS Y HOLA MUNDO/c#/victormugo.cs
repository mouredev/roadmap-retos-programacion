namespace _00_sintaxis
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // EJERCICIO:
            //  * -Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
            //  * -Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje(en una línea, varias...).
            //  * -Crea una variable(y una constante si el lenguaje lo soporta).
            //  * -Crea variables representando todos los tipos de datos primitivos del lenguaje(cadenas de texto, enteros, booleanos...).
            //  * -Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"


            // * -Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
            // https://learn.microsoft.com/en-us/dotnet/csharp/



            //  * -Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje(en una línea, varias...).
            // Ejemplo de comentario en línea
            /*
             * Ejemplo de comentario en varias líneas
             * 
            */



            //  * -Crea una variable (y una constante si el lenguaje lo soporta).
            string example = "Hola";
            const string constant = "Victor";


            //  * -Crea variables representando todos los tipos de datos primitivos del lenguaje(cadenas de texto, enteros, booleanos...).
            string name = "Victor";
            char firstLetter = 'V';

            short age2 = 4000;
            int age = 400000000;
            long age3 = 4000000000000000000;

            ushort age4 = 40000;
            uint age5 = 4000000000;
            ulong age6 = 4000000000000000000;

            double weight = 75.6;
            float height = 1.778f;
            decimal longPlay = 1.87665m;

            string[] arrayExample = ["Patatas", "Fruta", "Comida"];

            bool working = true;


            //  * -Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
            string langName = "C#";
            Console.WriteLine($"¡Hola, {langName}!");
        }
    }
}
