using System;
using System.Collections.Generic;
using Systeme.Text.RegularExpressions;


namespace ExpresionesRegulares
{
    class Program
    {
        
        static void Main(string[] args)
        {

            // Ejemplo de texto con números
            string texto = "Mi número de telefono es: 123456789 y mi correo es: ejemplo@ejemplo.com. Hoy es 31/07/2024";

            // Expresion regular para encontrar números
            string patronNumeros = @"\d+";
            List<string> numerosEncontrados = new List<string>();

            foreach(Match match in Regex.Matches(texto, patronNumeros))
            {
                numerosEncontrados.Add(matches.Value);
            }

            Console.WriteLine("Números encontrados:");
            foreach(string numero in numerosEncontrados)
            {
                Console.WriteLine(numero);
            }


            // Difucultad extra
            string email = "ejemplo@ejemplo.com";
            string telefono = "+34 123456789";
            string url = "https://www.example.com";

            string patronEmail = @"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$";
            string patronTelefono = @"^\+?\d{1,4}?[\s.-]?\(?\d{1,4}?\)?[\s.-]?\d{1,4}[\s.-]?\d{1,4}[\s.-]?\d{1,9}$";
            string patronUrl = @"^https?://([\w-]+(\.[\w-]+)+)([/\w- ./?%&=]*)?$";


            Console.WriteLine($"\nEmail '{email}' es válido: {Regex.IsMatch(email, patronEmail)}");
            Console.WriteLine($"Teléfono '{telefono}' es válido: {Regex.IsMatch(telefono, patronTelefono)}");
            Console.WriteLine($"URL '{url}' es válida: {Regex.IsMatch(url, patronUrl)}");
        }
    }
/*


Explicación 

Extracción de Números del Texto:
Se define un texto con varios números incrustados.
Se utiliza una expresión regular \d+ para encontrar secuencias de dígitos. \d representa cualquier dígito y + indica una o más ocurrencias.
Regex.Matches se utiliza para encontrar todas las coincidencias en el texto. Los números encontrados se almacenan en una lista y se imprimen.

Validaciones Adicionales:

Validación de Email:
La expresión regular ^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$ valida un formato de email básico.
^[\w\.-]+ corresponde al nombre del usuario, @ es el carácter que separa el nombre del dominio, [a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$ valida el dominio.

Validación de Número de Teléfono:
La expresión regular ^\+?\d{1,4}?[\s.-]?\(?\d{1,4}?\)?[\s.-]?\d{1,4}[\s.-]?\d{1,4}[\s.-]?\d{1,9}$ valida números de teléfono con varios formatos.
Esta expresión permite un prefijo de código de país opcional con un +, seguido de una combinación de números y separadores como espacios, puntos o guiones.

Validación de URL:
La expresión regular ^https?://([\w-]+(\.[\w-]+)+)([/\w- ./?%&=]*)?$ valida URLs.
^https?:// asegura que la URL comienza con http o https.
([\w-]+(\.[\w-]+)+) valida el nombre de dominio.
([/\w- ./?%&=]*)?$ valida la ruta y los parámetros adicionales.


*/
}
