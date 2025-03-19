/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
*/

using System;

class Strings
{
    // Acceso a caracteres específicos
    // https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/indexers/using-indexers
    static void getChars()
    {
        Console.WriteLine("string str = \"Hello C#!\";");
        string str = "Hello C#!";
        Console.WriteLine("str[0]: " + str[0]); // H
        Console.WriteLine("str[6]: " + str[6]); // W
    }

    // Subcadenas
    // https://learn.microsoft.com/en-us/dotnet/api/system.string.substring?view=net-8.0
    static void getSubstrings()
    {
        Console.WriteLine("string str = \"Hello C#!\";");
        string str = "Hello C#!";
        Console.WriteLine("str.Substring(6): " + str.Substring(6)); // C#!
        Console.WriteLine("str.Substring(0, 5): " + str.Substring(0, 5)); // Hello
    }

    // Longitud
    // https://learn.microsoft.com/en-us/dotnet/api/system.string.length?view=net-8.0
    static void getLength()
    {
        Console.WriteLine("string str = \"Hello C#!\";");
        string str = "Hello C#!";
        Console.WriteLine("str.Length: " + str.Length); // 12
    }

    // Concatenación
    // https://learn.microsoft.com/en-us/dotnet/api/system.string.concat?view=net-8.0
    static void getConcatenation()
    {
        Console.WriteLine("string str1 = \"Hello\";");
        Console.WriteLine("string str2 = \"C#!\";");
        string str1 = "Hello";
        string str2 = "C#!";
        Console.WriteLine("string.Concat(str1, str2): " + string.Concat(str1, str2)); // HelloC#!
    }

    // Repetición
    // https://blog.nimblepros.com/blogs/repeat-string-in-csharp/
    static void getRepetition()
    {
        /*
          C# no provee como tal un método para repetir una cadena, pero puedes hacerlo usando la función Repeat de la clase Enumerable.
        */
        Console.WriteLine("string text = \"Hello\";");
        Console.WriteLine("int n = 3;");
        string text = "Hello";
        int n = 3;
        Console.WriteLine("string.Concat(Enumerable.Repeat(text, n)): " + string.Concat(System.Linq.Enumerable.Repeat(text, n))); // HelloHelloHello
    }

    // Recorrido
    // https://learn.microsoft.com/en-us/dotnet/api/system.string.tochararray?view=net-8.0
    static void getTraversal()
    {
        Console.WriteLine("string str = \"Hello C#!\";");
        string str = "Hello C#!";
        char[] arr = str.ToCharArray();
        foreach (char c in arr)
        {
            Console.WriteLine(c);
        }
    }

    // Conversión a mayúsculas y minúsculas
    // https://learn.microsoft.com/en-us/dotnet/api/system.string.toupper?view=net-8.0
    // https://learn.microsoft.com/en-us/dotnet/api/system.string.tolower?view=net-8.0
    static void getCaseConversion()
    {
        Console.WriteLine("string str = \"Hello C#!\";");
        string str = "Hello C#!";
        Console.WriteLine("str.ToUpper(): " + str.ToUpper()); // HELLO C#!
        Console.WriteLine("str.ToLower(): " + str.ToLower()); // hello c#!
    }

    // Reemplazo
    // https://learn.microsoft.com/en-us/dotnet/api/system.string.replace?view=net-8.0
    static void getReplacement()
    {
        Console.WriteLine("string str = \"Hello C#!\";");
        string str = "Hello C#!";
        Console.WriteLine("str.Replace(\"C#\", \"World\"): " + str.Replace("C#", "World")); // Hello World!
    }

    // División
    // https://learn.microsoft.com/en-us/dotnet/api/system.string.split?view=net-8.0
    static void getSplit()
    {
        Console.WriteLine("string str = \"Hello C#!\";");
        string str = "Hello C#!";
        string[] arr = str.Split(' ');
        foreach (string s in arr)
        {
            Console.WriteLine(s);
        }
    }

    // Unión
    // https://learn.microsoft.com/en-us/dotnet/api/system.string.join?view=net-8.0
    static void getJoin()
    {
        Console.WriteLine("string[] arr = {\"Hello\", \"C#!\"};");
        string[] arr = { "Hello", "C#!" };
        Console.WriteLine("string.Join(\" \", arr): " + string.Join(" ", arr)); // Hello C#!
    }

    // Interpolación
    // https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/tokens/interpolated
    static void getInterpolation()
    {
        Console.WriteLine("string name = \"C#\";");
        string name = "C#";
        Console.WriteLine($"Hello {name}!"); // Hello C#!
    }

    // Verificación
    // https://learn.microsoft.com/en-us/dotnet/api/system.string.contains?view=net-8.0
    static void getVerification()
    {
        Console.WriteLine("string str = \"Hello C#!\";");
        string str = "Hello C#!";
        Console.WriteLine("str.Contains(\"C#\"): " + str.Contains("C#")); // True
    }

    /*
     * DIFICULTAD EXTRA (opcional):
     * Crea un programa que analice dos palabras diferentes y realice
       comprobaciones para descubrir si son:
     * - Palíndromos
     * - Anagramas
     * - Isogramas
    */

    // Palíndromos
    static void isPalindrome(string str)
    {
        int l = 0;
        int h = str.Length - 1;
        while (h > l)
        {
            if (str[l++] != str[h--])
            {
                Console.WriteLine("No es un palíndromo");
                return;
            }
        }
        Console.WriteLine("Es un palíndromo");
    }

    // Anagramas
    static void isAnagram(string str1, string str2)
    {
        if (str1.Length != str2.Length)
        {
            Console.WriteLine("No es un anagrama");
            return;
        }
        char[] arr1 = str1.ToCharArray();
        char[] arr2 = str2.ToCharArray();
        Array.Sort(arr1);
        Array.Sort(arr2);
        for (int i = 0; i < arr1.Length; i++)
        {
            if (arr1[i] != arr2[i])
            {
                Console.WriteLine("No es un anagrama");
                return;
            }
        }
        Console.WriteLine("Es un anagrama");
    }

    // Isogramas
    static void isIsogram(string str)
    {
        for (int i = 0; i < str.Length; i++)
        {
            for (int j = i + 1; j < str.Length; j++)
            {
                if (str[i] == str[j])
                {
                    Console.WriteLine("No es un isograma");
                    return;
                }
            }
        }
        Console.WriteLine("Es un isograma");
    }

    // Resumen ejercicio extra
    static void MainExtra()
    {
        Console.WriteLine("========================================");
        Console.WriteLine("============= PALÍNDROMOS ==============");
        Console.WriteLine("========================================\n");
        Console.WriteLine($"isPalindrome(\"reconocer\"): ");
        isPalindrome("reconocer");
        Console.WriteLine($"isPalindrome(\"hola\"): ");
        isPalindrome("hola");
        Console.WriteLine("\n========================================");
        Console.WriteLine("============== ANAGRAMAS ===============");
        Console.WriteLine("========================================\n");
        Console.WriteLine($"isAnagram(\"hola\", \"aloh\"): ");
        isAnagram("hola", "aloh");
        Console.WriteLine($"isAnagram(\"hola\", \"mundo\"): ");
        isAnagram("hola", "mundo");
        Console.WriteLine("\n========================================");
        Console.WriteLine("============== ISOGRAMAS ===============");
        Console.WriteLine("========================================\n");
        Console.WriteLine($"isIsogram(\"reconocer\"): ");
        isIsogram("reconocer");
        Console.WriteLine($"isIsogram(\"hola\"): ");
        isIsogram("hola");
        Console.WriteLine($"isIsogram(\"mundo\"): ");
        isIsogram("mundo");
    }

    // Función principal
    static void Main()
    {
        Console.WriteLine("========================================");
        Console.WriteLine("=============== CARACTERES =============");
        Console.WriteLine("========================================\n");
        getChars();
        Console.WriteLine("\n========================================");
        Console.WriteLine("============== SUBCADENAS ==============");
        Console.WriteLine("========================================\n");
        getSubstrings();
        Console.WriteLine("\n========================================");
        Console.WriteLine("=============== LONGITUD ===============");
        Console.WriteLine("========================================\n");
        getLength();
        Console.WriteLine("\n========================================");
        Console.WriteLine("============== CONCATENACIÓN ===========");
        Console.WriteLine("========================================\n");
        getConcatenation();
        Console.WriteLine("\n========================================");
        Console.WriteLine("=============== REPETICIÓN =============");
        Console.WriteLine("========================================\n");
        getRepetition();
        Console.WriteLine("\n========================================");
        Console.WriteLine("=============== RECORRIDO ==============");
        Console.WriteLine("========================================\n");
        getTraversal();
        Console.WriteLine("\n========================================");
        Console.WriteLine("= CONVERSIÓN A MAYÚSCULAS Y MINÚSCULAS =");
        Console.WriteLine("========================================\n");
        getCaseConversion();
        Console.WriteLine("\n========================================");
        Console.WriteLine("=============== REEMPLAZO ==============");
        Console.WriteLine("========================================\n");
        getReplacement();
        Console.WriteLine("\n========================================");
        Console.WriteLine("=============== DIVISIÓN ===============");
        Console.WriteLine("========================================\n");
        getSplit();
        Console.WriteLine("\n========================================");
        Console.WriteLine("=============== UNIÓN ==================");
        Console.WriteLine("========================================\n");
        getJoin();
        Console.WriteLine("\n========================================");
        Console.WriteLine("============== INTERPOLACIÓN ===========");
        Console.WriteLine("========================================\n");
        getInterpolation();
        Console.WriteLine("\n========================================");
        Console.WriteLine("=============== VERIFICACIÓN ===========");
        Console.WriteLine("========================================\n");
        getVerification();
        Console.WriteLine("\n========================================");
        Console.WriteLine("============= EJERCICIO EXTRA ============");
        Console.WriteLine("========================================\n");
        MainExtra();
    }
}
