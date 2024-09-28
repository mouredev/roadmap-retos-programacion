using System;

class Program
{
    static void esPalindromo(string str)
    {
        char[] reverse = str.ToCharArray();
        Array.Reverse(reverse);

        string reversedString = new string(reverse);

        if (str == reversedString)
        {
            Console.WriteLine("La palabra es Palíndromo");
        }
        else
        {
            Console.WriteLine("La palabra no es Palíndromo");
        }
    }

    static bool esAnagrama(string str1, string str2)
    {
        // Verificar si ambas cadenas tienen la misma longitud
        if (str1.Length != str2.Length)
        {
            return false;
        }

        // Convertir las cadenas a arreglos de caracteres y ordenarlos
        char[] arr1 = str1.ToCharArray();
        char[] arr2 = str2.ToCharArray();

        Array.Sort(arr1);
        Array.Sort(arr2);

        // Comparar los arreglos ordenados
        for (int i = 0; i < arr1.Length; i++)
        {
            if (arr1[i] != arr2[i])
            {
                return false;
            }
        }

        // Si todos los caracteres son iguales, son anagramas
        return true;
    }

    static bool esIsograma(string str)
    {
        // Convertir la cadena a un array de caracteres
        char[] caracteres = str.ToCharArray();

        // Ordenar el array para facilitar la comparación
        Array.Sort(caracteres);

        // Verificar si hay caracteres repetidos
        for (int i = 0; i < caracteres.Length - 1; i++)
        {
            if (caracteres[i] == caracteres[i + 1])
            {
                return false; // Hay caracteres repetidos
            }
        }

        // Si no hay caracteres repetidos, es un isograma
        return true;
    }

    static void Main()
    {
        // Crear una cadena
        string cadena1 = "Hola, ";
        string cadena2 = "mundo!";

        // Acceso a caracteres específicos
        char primerCaracter = cadena1[0];
        char ultimoCaracter = cadena2[cadena2.Length - 1];

        Console.WriteLine("Primer carácter: " + primerCaracter);
        Console.WriteLine("Último carácter: " + ultimoCaracter);

        // Longitud de la cadena
        int longitud = cadena1.Length;

        Console.WriteLine("Longitud de la cadena: " + longitud);

        // Concatenación
        string concatenacion = cadena1 + cadena2;

        Console.WriteLine("Concatenación: " + concatenacion);

        // Repetición
        string repeticion = new string('!', 3);

        Console.WriteLine("Repetición: " + repeticion);

        // Recorrido
        foreach (char caracter in concatenacion)
        {
            Console.WriteLine(caracter);
        }

        // Conversión a mayúsculas y minúsculas
        string mayusculas = concatenacion.ToUpper();
        string minusculas = concatenacion.ToLower();

        Console.WriteLine("Mayúsculas: " + mayusculas);
        Console.WriteLine("Minúsculas: " + minusculas);

        // Reemplazo
        string reemplazo = concatenacion.Replace("mundo", "amigo");

        Console.WriteLine("Reemplazo: " + reemplazo);

        // División
        string[] partes = concatenacion.Split(',');

        foreach (string parte in partes)
        {
            Console.WriteLine("Parte: " + parte.Trim());
        }

        // Unión
        string[] palabras = { "Hola", "cómo", "estás" };
        string union = string.Join(" ", palabras);

        Console.WriteLine("Unión: " + union);

        // Interpolación
        string nombre = "RX";
        int edad = 30;

        string mensaje = $"Hola, me llamo {nombre} y tengo {edad} años.";

        Console.WriteLine(mensaje);

        // Verificación
        bool contieneMundo = concatenacion.Contains("mundo");

        Console.WriteLine("Contiene 'mundo': " + contieneMundo);

        // Comparación de cadenas
        string str1 = "abc";
        string str2 = "def";

        bool sonIguales = String.Equals(str1, str2);
        int comparacion = String.Compare(str1, str2);

        // Búsqueda y posición
        int indice = cadena1.IndexOf("la");
        int ultimoIndice = cadena1.LastIndexOf("la");

        // Eliminación y truncamiento
        string nuevaCadena = cadena1.Remove(2, 3);
        string truncada = cadena1.Substring(0, 4);

        // Formato
        string formato = String.Format("La temperatura es {0} grados Celsius.", 25);

        // Caracteres especiales
        string nuevaLinea = "Primera línea\nSegunda línea";
        string tabulacion = "Columna1\tColumna2";

        // Espacios en blanco
        string conEspacios = "   Hola   ";
        string sinEspacios = conEspacios.Trim();

        //Dificultad extra:
        string s1 = "asdsaa";
        string s2 = "aasdsa";
        Console.WriteLine();
        esPalindromo(s1);
        Console.WriteLine();

        if (esAnagrama(s1, s2))
        {
            Console.WriteLine("La palabra es Anagrama");
        }else { Console.WriteLine("La palabra no es Anagrama"); }
        Console.WriteLine();

        if (esIsograma(s1))
        {
            Console.WriteLine("La palabra es Isograma");
        }
        else { Console.WriteLine("La palabra no es Isograma"); }

        Console.ReadKey();
    }
}
