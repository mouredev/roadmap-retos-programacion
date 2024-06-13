// Author: Abraham Raies https://github.com/abrahamraies

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

 class program {
    static void Main(string[] args){
        Console.WriteLine("Operaciones con Cadenas de Caracteres\n");
        Operaciones();
        Console.WriteLine("\n\nAnálisis de Palabras\n");
        AnalizarPalabras();
    }

    static void Operaciones(){
        string texto1 = "Casa";
        string texto2 = "Grande";

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

        // Recorrido
        Console.WriteLine("-- Recorrido --");
        foreach (char i in texto1 ) { Console.WriteLine(i); }

        // Conversión a mayúsculas
        Console.WriteLine("\n-- Conversión a mayúsculas --");
        Console.WriteLine(texto1.ToUpper());

        // Conversión a minúsculas
        Console.WriteLine("\n-- Conversión a minúsculas --");
        Console.WriteLine(texto1.ToLower());

        // Reemplazo
        Console.WriteLine("\n-- Reemplazo --");
        Console.WriteLine(texto1.Replace("a", "o"));

        // División
        Console.WriteLine("\n-- División --");
        string[] palabras = texto1.Split("s");
        foreach (string palabra in palabras) { Console.WriteLine(palabra); }

        // Unión
        Console.WriteLine("\n-- Unión --");
        string[] palabras2 = {"Hola", "Mundo"};
        string union = string.Join(" ", palabras2);
        Console.WriteLine(union);

        // Interpolación
        Console.WriteLine("\n-- Interpolación --");
        Console.WriteLine($"Lenguaje 1 es: {texto1} y el 2 es: {texto2}");

        // Verificación
        Console.WriteLine("\n-- Verificación --");
        Console.WriteLine(texto1 == texto2);

        // Comparación
        Console.WriteLine("\n-- Comparación --");
        Console.WriteLine(texto1.CompareTo(texto2));

        // Igualdad
        Console.WriteLine("\n-- Igualdad --");
        Console.WriteLine(texto1.Equals(texto2));

        // Eliminar espacios en blanco
        Console.WriteLine("\n-- Eliminar Espacios en Blanco --");
        Console.WriteLine(texto1.Trim());

        // Busqueda
        Console.WriteLine("\n-- Busqueda --");
        Console.WriteLine(texto1.Contains("a"));

        // Comprobar si empieza con
        Console.WriteLine("\n-- Comprobar si empieza con --");
        Console.WriteLine(texto1.StartsWith("C"));

        // Comprobar si termina con
        Console.WriteLine("\n-- Comprobar si termina con --");
        Console.WriteLine(texto1.EndsWith("a"));

        // Comprobar si es nulo o vacio
        Console.WriteLine("\n-- Comprobar si es nulo o vacio --");
        Console.WriteLine(string.IsNullOrEmpty(texto1));

    }
 
    static void AnalizarPalabras(){
        string palabra1 = "oso";
        string palabra2 = "soso";

        // Palíndromos
        Console.WriteLine("-- Palíndromos --");
        Console.WriteLine(EsPalindromo(palabra1));
        Console.WriteLine(EsPalindromo(palabra2));

        // Anagramas
        Console.WriteLine("\n-- Anagramas --");
        Console.WriteLine(EsAnagrama(palabra1, palabra2));

        // Isogramas
        Console.WriteLine("\n-- Isogramas --");
        Console.WriteLine(EsIsograma(palabra1));
        Console.WriteLine(EsIsograma(palabra2));
    }

    static bool EsPalindromo(string palabra){
        string palabraInvertida = "";
        for (int i = palabra.Length - 1; i >= 0; i--){
            palabraInvertida += palabra[i];
        }
        return palabra == palabraInvertida;
    }

    static bool EsAnagrama(string palabra1, string palabra2){
        char[] palabra1Ordenada = palabra1.ToCharArray();
        char[] palabra2Ordenada = palabra2.ToCharArray();
        Array.Sort(palabra1Ordenada);
        Array.Sort(palabra2Ordenada);
        return new string(palabra1Ordenada) == new string(palabra2Ordenada);
    }

    static bool EsIsograma(string palabra){
        for (int i = 0; i < palabra.Length; i++){
            for (int j = i + 1; j < palabra.Length; j++){
                if (palabra[i] == palabra[j]){
                    return false;
                }
            }
        }
        return true;
    }
}
 