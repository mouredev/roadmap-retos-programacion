/* ╔══════════════════════════════════════╗
   ║ Autor:  Kenys Alvarado               ║
   ║ GitHub: https://github.com/Kenysdev  ║
   ║ 2024 -  C#                           ║
   ╚══════════════════════════════════════╝
   ----------------------------------------
   # Cadenas de Caracteres
   ----------------------------------------
*/
using System.Text;
// ________________________________________
// Declaración e inicialización
string msg;      
string msg1 = "";
string old_path = "c:\\Program Files";
string new_path = @"c:\Program Files"; // literal
string text = @"Permite cadenas de varias líneas, caracteres 
de barra diagonal inversa o comillas dobles insertadas.";
// Tabulación horizontal.
string columns = "Column 1\tColumn 2\tColumn 3"; 
// Salto de línea.
string rows = "Row 1\r\nRow 2\r\nRow 3";

// ________________________________________
// Longitud
string str1 = "abcd";
int length = str1.Length;
Console.WriteLine("longitud: " + length);

// ________________________________________
// Método Trim 
string str2 = "   str   ";
// Eliminar los caracteres en blanco al inicio y al final.
string trim_str = str2.Trim();
Console.WriteLine(trim_str);
// Eliminar al inicio.
string trim_start = str2.TrimStart();
Console.WriteLine(trim_start);
// Eliminar al final.
string trim_end = str2.TrimEnd();
Console.WriteLine(trim_end);

// ________________________________________
// Extraer una parte de la cadena.
string str3 = "Hello, world!";
string newStr3 = str3.Substring(7, 5);
Console.WriteLine(newStr3); // World

// Eliminar una parte de la cadena.
var sb = new StringBuilder(str3);
sb.Remove(7, 5);
Console.WriteLine(sb.ToString()); // Hello, !

// ________________________________________
// Reemplazar un carácter por otro
string str4 = "abc def";
string newStr4 = str4.Replace("c", "C");
Console.WriteLine(newStr4); // abC def
newStr4 = str4.Replace("def", "DEF");
Console.WriteLine(newStr4); // abc DEF

// ________________________________________
// Mayúsculas
string str5 = "abc";
string newStr5 = str5.ToUpper();
Console.WriteLine(newStr5); // ABC

// ________________________________________
// Minúsculas
string str6 = "ABC";
string newStr6 = str6.ToLower();
Console.WriteLine(newStr6); // abc

// ________________________________________
// Concatenación
string str_a = "a";
string str_b = "b";
int int_r = 7;
string combined_str = str_a + "-" + str_b + "=" + int_r.ToString();
Console.WriteLine(combined_str); // a-b=7

// ________________________________________
// Interpolación
string name = "Ben";
int age = 21; 
Console.WriteLine($"Soy {name} y tengo {age} años.");

// ________________________________________
// Acceso
string str7 = "abcd";
char endChar = str7[3];
Console.WriteLine(endChar); // d

// verificación
Console.WriteLine(str7.Contains("bc")); // true

// ________________________________________
// Iterar
foreach (char c in str7)
{
    Console.WriteLine(c);
}

/* ________________________________________
Ejercicio:
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos (Igual ambas direcciones)
* - Anagramas   (Reordenamiento de las letras de otra palabra)
* - Isogramas   (No hay letras repetidas)
*/

void exs(string str1, string str2)
{
    bool isAnagram = str1.OrderBy(c => c).SequenceEqual(str2.OrderBy(c => c));
    
    Console.WriteLine(@$"
    ________________________________________
    ""{str1}"" es un palíndromo?: {str1 == new string(str1.Reverse().ToArray())}
    ""{str2}"" es un palíndromo?: {str2 == new string(str2.Reverse().ToArray())}

    ""{str1}"" es un anagrama de ""{str2}""?: {isAnagram}

    ""{str1}"" es un isograma?: {str1.Length == str1.Distinct().Count()}
    ""{str2}"" es un isograma?: {str2.Length == str2.Distinct().Count()}
    ");
}

exs("reconocer","vida");
exs("notas","santo");
exs("héroe","radar");
