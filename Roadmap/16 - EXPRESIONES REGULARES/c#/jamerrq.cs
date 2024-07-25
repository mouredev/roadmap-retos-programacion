/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */

using System;
using System.Text.RegularExpressions;

namespace Roadmap16
{
    class Regex
    {

        static void ExtraExercise()
        {
            // Usamos un texto con un email, un número de teléfono y una url
            // para probar las expresiones regulares.
            string generalText = "This is a text with an email: noreply@nowhere.com, a phone number: 123-456-7890 and a url: https://www.nowhere.com";

            // Definimos las expresiones regulares
            string emailPattern = @"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}";
            string phoneNumberPattern = @"\d{3}-\d{3}-\d{4}";
            string urlPattern = @"https?://[\w\.-]+";

            // Buscamos las coincidencias
            Match emailMatch = System.Text.RegularExpressions.Regex.Match(generalText, emailPattern);
            Console.WriteLine("Email: " + emailMatch.Value);
            Match phoneNumberMatch = System.Text.RegularExpressions.Regex.Match(generalText, phoneNumberPattern);
            Console.WriteLine("Número de teléfono: " + phoneNumberMatch.Value);
            Match urlMatch = System.Text.RegularExpressions.Regex.Match(generalText, urlPattern);
            Console.WriteLine("Url: " + urlMatch.Value);
        }

        static void Main(string[] args)
        {
            string textWithNumbers = "This is a text with 73 numbers 1729 in it 420.";
            string pattern = @"\d+";
            MatchCollection matches = System.Text.RegularExpressions.Regex.Matches(textWithNumbers, pattern);

            Console.WriteLine("Numbers Found:");
            foreach (Match match in matches)
            {
                Console.WriteLine(match.Value);
            }

            Console.WriteLine("\nExtra Exercise:");
            ExtraExercise();
        }
    }
}
