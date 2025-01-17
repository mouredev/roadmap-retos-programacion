/****  CADENAS DE CARACTERES  *******
 * 
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 */

using System;
using System.Linq; //Para usar Reverse()

class Program
{
    static void Main()
    {
        //longitud
        string corta = "LOL";
        int cortaL = corta.Length;

        //vacia
        string vacia = string.Empty;

        //Concat
        string larguisima = string.Concat("Laughing a ", "lot ", corta);

        //Interpolacion
        string mensaje = $"He was {larguisima}";

        //Substring
        string porcion = mensaje.Substring(15);

        //Busqueda
        var indice = mensaje.IndexOf("lot"); //Encuentra la posición de una subcadena.

        //Contiene
        bool isThere = mensaje.Contains("Laughing"); //Verifica si contiene una subcadena. True|False

        //Verificar cómo comienza o termina la cadena.
        bool inicio = mensaje.StartsWith("He"); //true
        bool fin = mensaje.EndsWith("lol"); //true

        //Reemplazar texto
        string mensaje2 = mensaje.Replace("He", "She"); //reemplaza He con She

        //Mayusculas y minusculas
        string gritar = mensaje2.ToUpper();
        string susurrar = corta.ToLower();

        //Dividir y unir cadenas
        string texto = "uno,dos,tres";
        string[] partes = texto.Split(','); // ["uno", "dos", "tres"]
        // Divide la cadena en un arreglo basado en un delimitador.
        string unido = string.Join("-", partes); // "uno-dos-tres"
        // Une un arreglo en una sola cadena.

        //Trim - Elimina espacios al inicio y al final de la cadena.
        string saludo = "   Hola, mundo!   ";
        Console.WriteLine(texto.Trim()); // "Hola, mundo!"

        Console.WriteLine(gritar);

        Extra.Palindromo("reconocer");
        Extra.Palindromo("cielo");
        Extra.Anagrama("amor", "roma");
        Extra.Isograma("murcielago");
    }
}
/* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
*/
class Extra
{
    public static void Palindromo(string palabra1)
    {
        // Invertir la palabra - .Reverse es un metodo para Arrays
        string palabraInvertida = new string(palabra1.Reverse().ToArray());

        // Comparar la palabra original con la invertida
        if (palabra1 == palabraInvertida)
        {
            Console.WriteLine($"La palabra \"{palabra1}\" es un palíndromo.");
        }
        else
        {
            Console.WriteLine($"La palabra \"{palabra1}\" no es un palíndromo.");
        }
    }
    public static void Anagrama(string palabra1, string palabra2)
    {
        // Ordenar las letras de ambas palabras alfabeticamente
        string palabra1Ordenada = new string(palabra1.OrderBy(c => c).ToArray());
        string palabra2Ordenada = new string(palabra2.OrderBy(c => c).ToArray());

        // Comparar las palabras ordenadas
        if (palabra1Ordenada == palabra2Ordenada)
        {
            Console.WriteLine($"{palabra1} y {palabra2} son anagramas.");
        }
        else
        {
            Console.WriteLine($"{palabra1} y {palabra2} no son anagramas.");
        }
    }
    public static void Isograma(string palabra1) 
    //Un isograma es una palabra en la que ninguna letra se repite.
    {
        foreach (char letra in palabra1)
        {
            if (palabra1.Count(c => c == letra) > 1)
            {
                Console.WriteLine($"La palabra {palabra1} no es un isograma");
                break;
            }
        }
        Console.WriteLine($"La palabra {palabra1} si es un isograma");
    }
}
