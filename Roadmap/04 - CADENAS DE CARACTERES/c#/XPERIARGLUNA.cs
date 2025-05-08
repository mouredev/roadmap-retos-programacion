using System;
using System.Linq;

class Program
{
    static void Main()
    {
        //Operaciones con strings


        //1. string vacia (Empty)
        string vacia = string.Empty;

        //2. concatenación(+)
        string lenguaje = "C#";
        string saludo = "Hola, " + lenguaje; 
        Console.WriteLine("Concatenación: " + saludo);

        //3. interpolación ($)
        Console.WriteLine($"Interpolación: Hola, {lenguaje}");

        // 4. longitud (Length) 
        Console.WriteLine("Longitud del texto: " + saludo.Length);

        //5. acceso a caracteres ([])
        Console.WriteLine("Primer carácter: " + saludo[0]);

        //6. substring 
        Console.WriteLine("Subcadena: " + saludo.Substring(1,3));

        //7. búsqueda 
        Console.WriteLine("Índice de 'C#': " + saludo.IndexOf("C#")); //busca la posición de una string
        Console.WriteLine("¿Contiene 'Hola'? " + saludo.Contains("Hola")); //busca si contiene una substring mediante un true or false
        Console.WriteLine("¿Empieza con 'Hola'? " + saludo.StartsWith("Hola")); //busca como empieza el string
        Console.WriteLine("¿Termina con 'C#'? " + saludo.EndsWith("C#")); //busca como termina el string

        //8. comparación 
        Console.WriteLine("¿'hola' == 'ola' " + ("hola" == "ola")); //compara si son iguales
        Console.WriteLine("Comparar 'abc' y 'xyz': " + string.Compare("abc", "xyz")); // compara y devuelve -1 si es menor, 0 si son iguales y 1 si es mayor
        Console.WriteLine("Equals ignorando mayúsculas: " + string.Equals("Hola", "hola", StringComparison.OrdinalIgnoreCase)); //compara e ignora mayúsculas y minúsculas usando OrdinalIgnoreCase

        //9. reemplazo
        Console.WriteLine("Reemplazar 'Hola' por 'Adios': " + saludo.Replace("Hola", "Adios"));

        //10. MAYUSCULAS/minusculas
        Console.WriteLine("Mayúsculas: " + saludo.ToUpper());
        Console.WriteLine("Minúsculas: " + saludo.ToLower());

        //11. dividir y unir cadenas
        string texto = "uno,dos,tres";
        string[] partes = texto.Split(','); // Divide la cadena en un arreglo basado en un delimitador.
        Console.WriteLine($"División: {texto}");

        string unido = string.Join("-", partes); // Une un arreglo en una sola cadena.
        Console.WriteLine($"Unión: {unido}");

        //12. eliminar espacios (Trim)
        string saludo2 = "   Hola, mundo!   ";
        Console.WriteLine(saludo2.Trim());

        //13. repetir cadena
        string estrellas = new string('*', 10);
        Console.WriteLine("Repetición de '*': " + estrellas);

        //14. recorrido 
        Console.WriteLine("Recorrido:");
        foreach (char c in texto)
        {
            Console.Write(c + " ");
        }
        Console.WriteLine();

        //15. verificaciones
        Console.WriteLine("¿Empieza con 'uno'? " + texto.StartsWith("uno"));
        Console.WriteLine("¿Contiene 'dos'? " + texto.Contains("dos"));
        Console.WriteLine("¿Termina en 'tres'? " + texto.EndsWith("tres"));

        //EXTRA
        Console.WriteLine("------EJERCICIO EXTRA-------");

        //solicito al usuario las 2 palabras diferentes
        Console.WriteLine("Ingresa la primer palabra: ");
        string palabra1 = Console.ReadLine().ToLower();

        Console.WriteLine("Ingresa la segunda palabra: ");
        string palabra2 = Console.ReadLine().ToLower();

        //Función para palíndromo (se lee igual en ambos sentidos)
        bool esPalindromo1 = palabra1 == new string(palabra1.Reverse().ToArray());
        bool esPalindromo2 = palabra2 == new string(palabra2.Reverse().ToArray());
        //Comprobación
        Console.WriteLine($"\n¿'{palabra1}' es palíndromo? {esPalindromo1}");
        Console.WriteLine($"¿'{palabra2}' es palíndromo? {esPalindromo2}");

        //Función para anagrama (se forma otra palabra usando las mismas palabras en otro orden)
        bool sonAnagramas = palabra1.OrderBy(c => c).SequenceEqual(palabra2.OrderBy(c => c));
        //Comprobación
        Console.WriteLine($"\n¿'{palabra1}' y '{palabra2}' son anagramas? {sonAnagramas}");

        // Función para isograma (cada letra aparece solo una vez)
        bool esIsograma1 = palabra1.Distinct().Count() == palabra1.Length;
        bool esIsograma2 = palabra2.Distinct().Count() == palabra2.Length;

        Console.WriteLine($"\n¿'{palabra1}' es isograma? {esIsograma1}");
        Console.WriteLine($"¿'{palabra2}' es isograma? {esIsograma2}");
    }
}
