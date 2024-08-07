/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

namespace RetosProgramacion2024
{
    internal class Program
    {
        private static int VariableGlobal = 1000;

        static void Main(string[] args)
        {
            string str = "Hola";
            string str2;

            // String to char array
            char[] chr = str.ToCharArray();
            for (int i = 0; i < chr.Length; i++)
            {
                Console.WriteLine(chr[i]);
            }

            // Longitud string
            Console.WriteLine(str.Length);

            // Concatenación string
            str = "string 1";
            str2 = "string 2";

            str += str2;
            Console.WriteLine(str);


            str = "string 1";
            str2 = "string 2";

            str = String.Join(' ', str, str2);
            Console.WriteLine(str);

            // Repetición string
            // Assigna una caracter a la string un numero determinado de veces
            str = new string('a', 5);
            Console.WriteLine(str);

            // Recorrer string
            str = "Hola, soy una string";

            for (int i = 0;i < str.Length;i++)
            {
                Console.WriteLine(str[i]);
            }

            // Conversión mayusculas y minusculas
            Console.WriteLine(str);
            Console.WriteLine(str.ToUpper());
            Console.WriteLine(str.ToLower());

            // Reemplazo
            // Remplaza el los caracteres de una string por otro
            Console.WriteLine(str);
            Console.WriteLine(str.Replace('o', '?'));

            // Dividir cadena
            // El split divide la cadena en subcadenas
            string[] palabras = str.Split(' ');
            Console.WriteLine(String.Join(" ", palabras));

            // Unión
            string[] nombres = { "isaac", "sergi", "josep" };
            Console.WriteLine(String.Join(" ", nombres));


            // Interpolación
            str = "interpolada";
            Console.WriteLine($"Esta cadena es {str}");


            // Format
            Console.WriteLine(String.Format("Hola, esto es una {0} con {1}", "string", "formato"));

            // Verificación
            // Sirve para verificar si la candena contiene el un determinado valor dentro de la cadena
            str = "Hola Mundo";
            Console.WriteLine(str.Contains("Hola"));

            // Substring
            // Recupera una subcadena de la instacia indicando el indice del qual quieres empezar
            // y la cantidad de caracteres que quieres. Si no se indica la cantidad recupera todo lo que hay despues del indice
            str = "hola Mundo";
            Console.WriteLine(str.Substring(1,3));

            // Recupera una subcadena de la instancia empezado por la izquierda.
            // Solo se indica la cantidad de caracteres que queremos recuperar
            Console.WriteLine(str.PadLeft(4));

            // Hace lo mismo que PadLeft pero empezando por la derecha
            Console.WriteLine(str.PadRight(5));

            // Comparación
            str = "Hola";
            str2 = "Hola";
            Console.WriteLine(str.Equals(str2));
            Console.WriteLine(str.Equals(str2));

            // Insert
            // Sirve para insertar un caracter en una posición determinada de la string
            str = str.Insert(str.Length, "!");
            Console.WriteLine(str);

            // Remove
            // Sirve para quitar un caracter o varios caracteres de una string en una posición determinada
            str = str.Remove(str.Length-1);
            Console.WriteLine(str);

            // Trim
            // El trim sirve para eliminar los espacios que hay tanto al principio como al final del string
            str = "            hola    ";
            Console.WriteLine(str);
            Console.WriteLine(str.Trim());

            // Reto extra
            Console.WriteLine("\nReto extra");

            Console.WriteLine(AnalizarPalabra("salas", "salas"));
            Console.WriteLine(AnalizarPalabra("cava", "vaca"));
            Console.WriteLine(AnalizarPalabra("centrifugado ", ""));
            Console.WriteLine(AnalizarPalabra("casa", "vaca"));
        }

        private static string AnalizarPalabra(string str1, string str2)
        {
            if (EsPalindromo(str1, str2))
                return $"La palabra {str1} es un palíndromo";

            if (EsAnagrama(str1, str2))
                return $"La palabra {str2} es un anagra de {str1}";

            if (EsIsograma(str1))
                return $"La palabra {str1} es un isograma";

            return $"La palabra {str1} no es un palíndromo, anagrama o isograma"; 
        }

        private static bool EsPalindromo(string str1, string str2)
        {
            char[] palabra = str2.ToCharArray();
            palabra.Reverse();
            str2 = String.Concat(palabra);

            return str1 == str2;
        }

        private static bool EsAnagrama(string str1, string str2)
        {
            if (str1.Length != str2.Length)
                return false;

            char[] palabra1 = str1.ToCharArray();
            char[] palabra2 = str2.ToCharArray();

            Array.Sort(palabra1);
            Array.Sort(palabra2);

            for (int i = 0; i < palabra1.Length; i++)
            {
                if (palabra1[i] != palabra2[i]) 
                    return false;
            }

            return true;
        }

        private static bool EsIsograma(string str)
        {
            char[] palabra = str.ToCharArray();
            Array.Sort(palabra);

            for (int i = 1;i < palabra.Length; i++)
            {
                if (palabra[i - 1] == palabra[i])
                    return false;
            }

            return true;
        }
    }
}
