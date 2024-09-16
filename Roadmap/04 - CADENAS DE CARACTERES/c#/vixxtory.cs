using static System.Runtime.InteropServices.JavaScript.JSType;

namespace Cadenas
{
    class Program
    {

        static void Main(string[] args)
        {
            string text = "Hello, World!";
            //Longitud de cadena 
            int length = text.Length;
            Console.WriteLine("La longitud de la cadena es: " + length);

            //Método Trim: eliminar los caracteres en blanco al inicio y al final de una cadena 
            //Los caracteres en blanco incluyen espacios, tabulaciones y saltos de línea.
            string textTrim = "   Hello, World!   ";
            string trimText = textTrim.Trim();
            Console.WriteLine("La cadena original es: " + textTrim);
            Console.WriteLine("La cadena después de utilizar Trim es: " + trimText);

            //Método TrimEnd: eliminar los caracteres en blanco al final de una cadena de caracteres.
            string trimEndText = textTrim.TrimEnd();
            Console.WriteLine("La cadena original es: " + textTrim);
            Console.WriteLine("La cadena después de utilizar TrimEnd es: " + trimEndText);

            //Método TrimStart:  eliminar los caracteres en blanco al inicio de una cadena.
            string trimStartText = textTrim.TrimStart();
            Console.WriteLine("La cadena original es: " + textTrim);
            Console.WriteLine("La cadena después de utilizar TrimStart es: " + trimStartText);

            /*
            ELIMINAR O CORTAR PARTE DE LA CADENA
            */
            //Método Substring (desde el carácter en la posición 7 hasta la posición 5 después de él)
            string newText = text.Substring(7, 5);
            Console.WriteLine("La cadena original es: " + text);
            Console.WriteLine("La nueva cadena es: " + newText);

            //Metodo Substring: Recorta una cadena
            string newTextSubString = text.Substring(7); //desde el carácter en la posición 7 hasta el final
            Console.WriteLine("La cadena original es: " + text);
            Console.WriteLine("La nueva cadena es: " + newTextSubString);

            //Metodo Replace: Reemplaza un carácter por otro, también una subcadena por otra subcadena
            string newTextReplace = text.Replace('o', 'O');
            Console.WriteLine("La cadena original es: " + text);
            Console.WriteLine("La nueva cadena es: " + newTextReplace);

            string newTextReplace2 = text.Replace("Hello", "Hi");
            Console.WriteLine("La cadena original es: " + text);
            Console.WriteLine("La nueva cadena es: " + newTextReplace2);

            //Método ToUpper: convierte una cadena a mayúsculas
            //(Si se desea modificar la cadena original, se debe asignar la nueva cadena a la misma variable)
            string newTextToUpper = text.ToUpper();
            Console.WriteLine("La cadena original es: " + text);
            Console.WriteLine("La nueva cadena es: " + newTextToUpper);

            //Método ToLower: convierte una cadena a minúsculas.
            string newTextToLower = text.ToLower();
            Console.WriteLine("La cadena original es: " + text);
            Console.WriteLine("La nueva cadena es: " + newTextToLower);

            /*
             * CONCATENACION DE STRING 
             */
            //La mas comun es con el operador +
            string firstString = "Hola";
            string secondString = "Manuelita";
            string combinedString = firstString + " " + secondString + "!";
            Console.WriteLine(combinedString);

            //Metodo Concat
            string combinedString2 = string.Concat(firstString, " ", secondString, "!");
            Console.WriteLine(combinedString2);

            /*
             * CONCATENAR NUMEROS Y STRING
             */
            //Primero es necesario convertir los números a cadenas de caracteres mediante el método ToString()
            int number = 42;
            string message = "La respuesta es: " + number.ToString();
            Console.WriteLine(message);

            //INTERPOLACION DE STRING: es una forma de crear una nueva cadena a partir de una plantilla de cadena y valores dinámicos.
            //La sintaxis para la interpolación de cadenas es $"{expression}", donde expression es una expresión que se evalúa y se convierte en una cadena.

            string name = "John";
            int age = 30;
            Console.WriteLine($"Mi nombre es {name} y tengo {age} años.");

            //Tambien puede realizarse el formateo con el metodo Format
            Console.WriteLine(string.Format("Mi nombre es {0} y tengo {1} años", name, age));

            //ACCESO A CARACTERES
            //Se puede acceder a los caracteres individuales de una cadena utilizando el índice.
            //El indice de una cadena comienza en cero y se extiende hasta la longitud de la cadena menos uno.
            string message2 = "Hola Victoria";
            char firstCharacter = message2[0];
            char sixthCharacter = message2[5];
            Console.WriteLine($"The first character is: {firstCharacter}");
            Console.WriteLine($"The sixth character is: {sixthCharacter}");

            //CARACTERES ESPECIALES
            //Se representan mediante secuencias de escape, que comienzan con el carácter de barra invertida (\)
            /*
             Algunos ejemplos son:
            \n: nueva línea
            \r: retorno de carro
            \t: tabulación
            \\: barra invertida
            \": comilla doble
            \': comilla simple
             */
            string message11 = "Hello\nWorld";
            Console.WriteLine(message11);

            string message22 = "Hello\rWorld";
            Console.WriteLine(message22);

            string message3 = "Hello\tWorld";
            Console.WriteLine(message3);

            string message4 = "Hello\\World";
            Console.WriteLine(message4);

            string message5 = "Hello\"World";
            Console.WriteLine(message5);

            string message6 = "Hello\'World";
            Console.WriteLine(message6);

            //Metodo Parse: Conversion entre cadenas y otros tipos de datos
            string numeroTexto = "10";
            int numeroParse = int.Parse(numeroTexto);
            string stringBooleano = "false";
            Console.WriteLine(numeroParse.GetType());
            Console.WriteLine(bool.Parse(stringBooleano).GetType());

            //Metodo Split(): permite dividir una cadena en subcadenas utilizando un separador específico.
            string s1 = "Hola,amigo, ¿cómo estás?";
            string[] stringSplit = s1.Split(',');
            foreach (var word in stringSplit)
            {
                Console.WriteLine($"<{stringSplit}>");
            }

            //Metodo Contains(value): true si el parámetro de value aparece dentro de esta cadena; en caso contrario, false.
            Console.WriteLine(s1.Contains("Hola"));
            Console.WriteLine(s1.Contains("?"));
        }
    }
}

