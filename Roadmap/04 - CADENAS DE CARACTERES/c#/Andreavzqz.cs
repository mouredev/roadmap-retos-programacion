using System;

class Program 
{

static void Main(string[] args)
{
    //DECLARACION DE CADENAS
    string cadena1 = "Hola, Mundo";
    string cadena2 = "C# es genial";

    //1. Longitud de una cadena
    Console.WriteLine($"Longitud de cadena1: {cadena.Length}");

    //2. Acceso a caracteres especificos
    Console.WriteLine($"Primer caracter de cadena1: {cadena1[0]}");
    console.WriteLine($"Ultimo caracter de cadena1: {cadena1[cadena1.Length - 1]}");

    //3. Subcadenas
    Console.WriteLine($"Subcadena1 (0-4): {cadena1.Substring(0,4)}");

    //4. Concatenacion
    string concatenateda = cadena1 + cadena2
    Console.WriteLine($"Concatenacion: {concatenada}");

    //5. Repeticion(no hay operador directo en C#, pero podemos usar un bucle o método)
    string repetida = new string ('*', 10); // Repetir '*' 10 veces
    Console.WriteLine($"Repeticion: {repetida}");

    //6. Recorrido de una cadena
    Console.WriteLine("Recorrido de cadena1: ");
    foreach (char c in cadena1)
    {
        Console.WriteLine(c + "");
    }
    Console.WriteLine();

    //7. Conversion a mayusculas y minusculas
    Console.WriteLine($"Mayusculas: {cadena1.ToUpper()}");
    Console.WriteLine($"Minusculas: {cadena1.ToUpper()}");

    //8. Reemplazo
    string reemmplazada = cadena1.Remplace("Hola", "Adios");
    Console.WriteLine($"Reemplazo: {reemplazada}");

    //9. Division
    string[] palabras = cadena1.Split(' ');
    Console.WriteLine("Division: ");
    foreach (string palabra in palabra)
    {
        console.WriteLine(palabra);
    }

    //10. Union
    string unida = string.Join("-", palabras);
    Console.WriteLine($"Union: {unida}");

    //11. Interpolacion
    string nombre = "Andrea"
    string interpolada = $"Hola, {nombre}!";
    Console.WriteLine($"Interpolacion: {interpolada}");

    //12. Verificacion
    Console.WriteLine($"¿Cadena1 contiene 'Mundo'? {cadena1.Contains("Mundo")}");
    Console.WriteLine($"¿Cadena2 empieza con 'C#'? ¨{cadena2.StartWith("C#")}");
    Console.WriteLine($"¿Cadena2 termina con 'genial'? {cadena2.Trim().EndWith("genial")}");

    // Comprobación de Palíndromos, Anagramas e Isogramas
    // Solicitar al usuario que ingrese dos palabras
    Console.WriteLine("Introduce la primera palabra:");
    string palabra1 = Console.ReadLine().ToLower().Replace(" ", " ");

    Console.WriteLine("Introduce la segunda palabra:")
    string palabra2 = Console.ReadLine().ToLower().Replace(" "," ");

    //Comprobaciones
    Console.WriteLine($"¿La primera palabra '{palabra1}' es un palíndomo?: {EsPalindromo(palabra1)}");
    Console.WriteLine($"¿La segunda palabra '{palabra2}' es un palíndomo?: {EsPalindromo(palabra2)}");
    Console.WriteLine($"¿Las palabras '{palabra1}' y {palabra2}' son anagramas?: {SonAnagramas(palabra1, palabra2)}");
    console.WriteLine($"¿La primera palabra '{palabra1}' es un isograma?: {EsIsograma(palabra1)}");
    Console.WriteLine($"¿La segunda palabra '{palabra2}' es un isogramra?: {EsIsograma(palabra2)}");
    
    }
    //Funcion para comprobar si una palabra es palíndromo
    static bool EsPalindromo(string palabra)
    {
        char[] arr = palabra.ToCharArray();
        Array.Reverse(arr);
        string inversa = new string(arr);
        return palabra == inversa;
    }

    //Funcion para comprobar si dos palabras son anagramas
    string bool SonAnagramas(string palabra1, string palabra2)
    {
        if (palabra1.Length != palabra2.Length)
        {
            return false;
        }
        char[] arr1 = palabra1.ToCharArray();
        char[] arr2 = palabra2.ToCharArray();
        Array.Sort(arr1);
        Array.Sort(arr2);
        return new string(arr1) == new string(arr2);
    }

    //Funcion para comprobar si una palabra es isograma
    static bool EsIsograma(string palabra)
    {
        var caracteres = palabra.GroupBy(c => c);
        foreach (var grupo in caracteres)
        {
            if (grupo.Count() > 1)
            {
                return false;
            }
            return true;
        }
    }
  /*
  
EXPLICACION

*Entrada del Usuario:
Solicita al usuario que introduzca dos palabras.
Convierte ambas palabras a minúsculas y elimina los espacios para evitar discrepancias debido a mayúsculas o espacios.

*Comprobaciones:
-Palíndromos:
Una palabra es un palíndromo si se lee igual de adelante hacia atrás que de atrás hacia adelante.
La función EsPalindromo invierte la cadena y la compara con la original.
-Anagramas:
Dos palabras son anagramas si contienen las mismas letras en la misma cantidad, pero en un orden diferente.
La función SonAnagramas compara las longitudes de las palabras, ordena sus caracteres y verifica si las cadenas ordenadas son iguales.
-Isogramas:
Una palabra es un isograma si no tiene letras repetidas.
La función EsIsograma agrupa los caracteres de la palabra y verifica que ningún grupo tenga más de un elemento.

*Comprobación de Palíndromos:
Se invierte la cadena y se compara con la original para verificar si es un palíndromo.

*Comprobación de Anagramas:
Se ordenan los caracteres de ambas palabras y se comparan las cadenas resultantes.

*Comprobación de Isogramas:
Se agrupan los caracteres de la palabra y se verifica que ningún grupo tenga más de un elemento.
*/
}
