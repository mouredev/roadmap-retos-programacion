/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
class Program
{

    public static void Main(string[] args)
    {
        Operaciones("C#", "Python");
        Console.WriteLine("\n-- Dificultad Extra --\n");
        DificultadExtra("Palindromo", "Isograma");
        Console.WriteLine("\n----\n");
        DificultadExtra("Ana", "OlLo");
    }

    private static void Operaciones(string texto1, string texto2)
    {
        // Acceso a caracteres
        Console.WriteLine("-- Acceso a Indices de un texto --");
        Console.WriteLine($"Indice 0 del Texto 1: {texto1[0]}");
        Console.WriteLine($"Indice 3 del Texto 2: {texto2[3]}\n");

        // Crear subcadenas
        Console.WriteLine("-- Crear Subcadenas --");
        Console.WriteLine($"Subcadena del texto 1: {texto1.Substring(1)}");
        Console.WriteLine($"Subcadena del texto 2: {texto2.Substring(3)}\n");

        // Longitudes
        Console.WriteLine("-- Longitudes --");
        Console.WriteLine($"Longitud del texto 1: {texto1.Length}");
        Console.WriteLine($"Longitud del texto 2: {texto2.Length}\n");

        // Concatenación de cadenas
        Console.WriteLine("-- Concatenación --");
        Console.WriteLine($"Forma 1:" + texto1 + " " + texto2);
        Console.WriteLine($"Forma 2: {texto1} {texto2}\n");

        // Repetición
        Console.WriteLine("-- Repetición --");
        for (int i = 0; i < 3; i++) { Console.WriteLine(texto1); }
        for (int i = 0; i < 3; i++) { Console.WriteLine(texto2); }

        // Recorrido
        Console.WriteLine("\n-- Recorrido --");
        foreach (char i in texto1 ) { Console.WriteLine(i); }

        // Conversión a mayúsculas
        Console.WriteLine("\n-- Conversión a mayúsculas --");
        Console.WriteLine(texto1.ToUpper());
        Console.WriteLine(texto2.ToUpper());

        // Conversión a minúsculas
        Console.WriteLine("\n-- Conversión a minúsculas --");
        Console.WriteLine(texto1.ToLower());
        Console.WriteLine(texto2.ToLower());

        // Reemplazo
        Console.WriteLine("\n-- Reemplazo --");
        Console.WriteLine(texto1.Replace('#', '+'));
        Console.WriteLine(texto2.Replace('o', '0'));

        // Unión
        Console.WriteLine("\n-- Unión --");
        Console.WriteLine(texto1.Concat(texto2));

        // Interpolación
        Console.WriteLine("\n-- Interpolación --");
        Console.WriteLine($"Lenguaje 1 es: {texto1} y el 2 es: {texto2}");

        // Verificación
        Console.WriteLine("\n-- Verificación --");
        Console.WriteLine(texto1 == texto2);

    }

    // Dificultad Extra
    private static void DificultadExtra(string texto1, string texto2)
    {
        // Anagrama
        bool EsAnagrama()
        {
            char[] arreglo1 = texto1.ToLower().ToCharArray();
            char[] arreglo2 = texto2.ToLower().ToCharArray();

            Array.Sort(arreglo1);
            Array.Sort(arreglo2);

            return arreglo1.SequenceEqual(arreglo2);
        }

        if (EsAnagrama())
        {
            Console.WriteLine("Los textos son anagramas.");
        }
        else
        {
            Console.WriteLine("Los textos no son anagramas");
        }

        // Palíndromos
        string txt1 = texto1.ToLower();
        string txt2 = texto2.ToLower();

        if (txt1.Equals(new string(txt1.Reverse().ToArray())))
        {
            Console.WriteLine($"{texto1} es palíndromo.");

            if (txt2.Equals(new string(txt2.Reverse().ToArray())))
            {
                Console.WriteLine($"{texto2} es palíndromo.");
            }
            else
            {
                Console.WriteLine($"{texto2} no es palíndromo.");
            }
        } else if (txt2.Equals(new string(txt2.Reverse().ToArray())))
        {
            Console.WriteLine($"{texto1} no es palíndromo.");
            Console.WriteLine($"{texto2} es palíndromo.");
        }
        else
        {
            Console.WriteLine($"{texto1} no es palíndromo.");
            Console.WriteLine($"{texto2} no es palíndromo.");
        }

        // Isogramas
        
        string text1 = texto1.ToLower();
        string text2 = texto2.ToLower();

        if(text1.Length == text1.Distinct().Count())
        {
            Console.WriteLine($"{texto1} es Isograma");
        }
        else
        {
            Console.WriteLine($"{texto1} no es Isograma");
        }

        if (text2.Length == text2.Distinct().Count())
        {
            Console.WriteLine($"{texto2} es Isograma");
        }
        else
        {
            Console.WriteLine($"{texto2} no es Isograma");
        }


    }

}
