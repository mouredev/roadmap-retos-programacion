namespace exs49;
/*
_____________________________________
https://github.com/kenysdev
2024 - C#
_____________________________________
#49 EL ALMACÉN DE PAPÁ NOEL
------------------------------------

* EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 * 
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 * 
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y 
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 * 
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
*/

using System;
using System.Linq;

class Program
{
    static bool VerifyAllowedChar(string codeEntry)
    {
        foreach (char ch in codeEntry)
        {
            if (!"abc123".Contains(ch))
            {
                Console.WriteLine("Uno de los caracteres no está entre los permitidos.\n");
                return false;
            }
        }
        return true;
    }

    static string GetEntry()
    {
        while (true)
        {
            Console.Write("Código: ");
            string? codeEntry = Console.ReadLine();

            if (string.IsNullOrEmpty(codeEntry) || codeEntry.Length != 4)
            {
                Console.WriteLine("El código debe ser de 4 dígitos.\n");
                continue;
            }

            if (VerifyAllowedChar(codeEntry))
            {
                return codeEntry;
            }
        }
    }

    static bool IsOpen(string code)
    {
        string codeEntry = GetEntry();

        if (codeEntry == code)
        {
            return true;
        }

        Console.WriteLine("Código inválido.\n");

        for (int i = 0; i < codeEntry.Length; i++)
        {
            char ch = codeEntry[i];

            if (ch == code[i])
            {
                Console.WriteLine($"'{ch}' está en la posición correcta.");
            }
            else if (code.Contains(ch))
            {
                Console.WriteLine($"'{ch}' está en el código, pero en otra posición.");
            }
            else
            {
                Console.WriteLine($"'{ch}' no está presente en el código.");
            }
        }

        return false;
    }

    static void Main()
    {
        Console.WriteLine(@"
* Papá Noel tiene que comenzar a repartir los regalos...
* ¡Pero ha olvidado el código secreto de apertura del almacén!

- Tienes 10 intentos para adivinar el código que abre el almacén.
- Código de 4 caracteres. Permitidos: a, b, c, 1, 2, 3.
- Nota: No hay dígitos repetidos.");

        Random random = new();
        string characters = "abc123";
        string code = new(characters.OrderBy(x => random.Next()).Take(4).ToArray());

        for (int attempts = 1; attempts < 11; attempts++)
        {
            Console.WriteLine($"\n___________\nIntento #{attempts}");

            if (IsOpen(code))
            {
                Console.WriteLine("Código correcto, almacén abierto.");
                Console.WriteLine("Papá Noel ahora podrá entregar los regalos.");
                break;
            }

            if (attempts == 10)
            {
                Console.WriteLine("\n___________\nHas perdido.");
                Console.WriteLine("Papá Noel ya no podrá entregar los regalos.");
            }
        }
    }
}
