using System.ComponentModel.DataAnnotations;
using System.Diagnostics.Metrics;

namespace _04_cadenas
{
    internal class Program
    {
        static void Main(string[] args)
        {
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
             *  - Palíndromos
             *  - Anagramas
             *  - Isogramas
            */

            string cadena = "Hola que tal";

            // Interpolación
            Console.WriteLine($"Cadena: {cadena}");

            // Conversión a mayúsculas
            Console.WriteLine($"Mayusculas: {cadena.ToUpper()}");

            // Conversión a minusculas
            Console.WriteLine($"Minusculas: {cadena.ToLower()}");

            // Longitud de caracteres
            Console.WriteLine($"Longitud: {cadena.Count()}");

            // División
            string[] partes = cadena.Split(" ");
            Console.WriteLine($"Partes {partes.Length}");
            for (int i = 0; i < partes.Length; i++) 
            { 
                Console.WriteLine($"Parte: {partes[i]}");
            }

            // Verificación
            if (String.IsNullOrEmpty(cadena))
            {
                Console.WriteLine("Cadena vacía");
            }

            // Reemplazo
            Console.WriteLine($"Reemplazo: {cadena.Replace(" ", ",")}");
            Console.WriteLine($"Reemplazo: {cadena.Replace(",", " ")}");

            // Subcadenas
            Console.WriteLine($"Subcadenas: {cadena.Substring(1,7)}");

            // Indice
            Console.WriteLine($"Indice: {cadena.IndexOf("q")}");

            // Eliminar:
            Console.WriteLine($"Eliminar: {cadena.Remove(4)}");

            // Último indice
            Console.WriteLine($"Ultimo indice: {cadena.LastIndexOf("a")}");
            
            // Concatenación
            string cadena2 = ". Estoy muy bien";
            Console.WriteLine($"Concatenación: {cadena += cadena2}");

            // Obtener caracters
            for (int i = 0; i < cadena.Length; i++)
            {
                Console.WriteLine(cadena[i]);
            }

            // Join
            string[] cadenas = { "Hola", "esto", "es", "un", "test" };
            Console.WriteLine($"Join: {string.Join(" ", cadenas)}");

            // Verificación
            Console.WriteLine($"Verificación: {cadenas.Contains("Hola")}");
            Console.WriteLine($"Verificación: {cadenas.Contains("Adios")}");


            // ---------------------- EJERCICIO
            Console.WriteLine("Introduzca palabra 1: ");
            string palabra1 = Console.ReadLine();

            Console.WriteLine("Introduzca palabra 2: ");
            string palabra2 = Console.ReadLine();

            if (!String.IsNullOrEmpty(palabra1) && !String.IsNullOrEmpty(palabra2))
            {
                palabra1 = palabra1.ToLower().Trim();
                palabra2 = palabra2.ToLower().Trim();


                // --- Palíndromo: Un palíndromo es una palabra o frase que se lee igual en un sentido que en otro
                if (VerificaPalindromo(palabra1, palabra2))
                {
                    Console.WriteLine($"{palabra1} y {palabra2} son palíndromos");
                }
                else
                {
                    Console.WriteLine($"{palabra1} y {palabra2} NO son palíndromos");
                }



                // --- Anagrama: Los anagramas son cambios en el orden de las letras de una palabra que dan lugar a otra palabra diferente (caso y saco)
                if (VerificaAnagrama(palabra1, palabra2))
                {
                    Console.WriteLine($"{palabra1} y {palabra2} son Anagramas");
                }
                else
                {
                    Console.WriteLine($"{palabra1} y {palabra2} NO son Anagramas");
                }



                // --- Isograma: Es una palabra o frase en la que cada letra aparece el mismo número de veces.
                // Si cada letra aparece solo una vez será un heterograma, si aparece dos, un isogroma de segundo orden y así sucesivamente
                if (VerificaIsograma(palabra1))
                {
                    Console.WriteLine($"{palabra1} es Isograma");
                }
                else
                {
                    Console.WriteLine($"{palabra1} NO es Isograma");
                }

                if (VerificaIsograma(palabra2))
                {
                    Console.WriteLine($"{palabra2} es Isograma");
                }
                else
                {
                    Console.WriteLine($"{palabra2} NO es Isograma");
                }
            }
        }


        /// <summary>
        /// Método para verificar si una palabra es palíndromo
        ///  Un palíndromo es una palabra o frase que se lee igual en un sentido que en otro
        /// </summary>
        /// <param name="word"></param>
        /// <returns></returns>
        public static bool VerificaPalindromo(string word1, string word2)
        {
            try
            {
                if (word1.Length == word2.Length)
                {

                    for (int i = 0; i < word1.Length; i++)
                    {
                        if (word1[i] != word2[word2.Length - i - 1])
                        {
                            return false;
                        }
                    }
                    return true;
                }
                else
                {
                    return false;
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }
        }


        /// <summary>
        /// Método para verificar si dos palabras son Anagramas
        /// Los anagramas son cambios en el orden de las letras de una palabra que dan lugar a otra palabra diferente (caso y saco)
        /// </summary>
        /// <param name="word1"></param>
        /// <param name="word2"></param>
        /// <returns></returns>
        public static bool VerificaAnagrama(string word1, string word2)
        {
            try
            {
                int counter = 0;

                if (word1.Length == word2.Length)
                {
                    for (int i = 0; i < word1.Length; i++)
                    {
                        for (int j = 0; j < word2.Length; j++)
                        {
                            if (word1[i] == word2[j] )
                            {
                                counter++;
                                break;
                            }
                        }
                    }

                    if (counter == word1.Length)
                    {
                        return true;
                    }

                    return false;
                } 
                else
                {
                    return false;
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }
        }


        /// <summary>
        /// Método para verificar si una palabra es Isograma
        /// Es una palabra o frase en la que cada letra aparece el mismo número de veces. 
        /// Si cada letra aparece solo una vez será un heterograma, si aparece dos, un isogroma de segundo orden y así sucesivamente
        /// </summary>
        /// <param name="word1"></param>
        /// <param name="word2"></param>
        /// <returns></returns>
        public static bool VerificaIsograma(string word)
        {
            try
            {
                int counter = 0;

                for (int i = 0; i < word.Length; i++)
                {
                    for (int j = 0; j < word.Length; j++)
                    {
                        if (i != j && word[i] == word[j])
                        {
                            counter++;
                        }
                    }

                    if (counter > 1)
                    {
                        return false;
                    }
                    counter = 0;
                }
                return true;
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }
        }
    }
}
