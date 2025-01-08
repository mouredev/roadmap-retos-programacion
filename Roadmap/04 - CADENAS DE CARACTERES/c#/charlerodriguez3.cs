/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 *

 */

string word = "This is a word";
string word2 = "Hello";
string word3 = "World";
string word4 = null;

Console.WriteLine(word.IndexOf('s'));// find the specific position of the first letter found
Console.WriteLine(word.Substring(0,4);// substrings
Console.WriteLine(word.Length);//length of the string
//Options for concatenation
Console.WriteLine(word2 + word3);
Console.WriteLine("value of word2 {0} and value of word3 {1}",word2, word3);
Console.WriteLine($"{word2} {word3}");
Console.WriteLine(String.Concat(word,word2,word3));
Console.WriteLine(word.Replace('i','@'));//replacing
Console.WriteLine(String.IsNullOrWhiteSpace(word4));

/*
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas 
 */

     string word = "roma";
    string word2 = "amor";
    string word3 = "cuaderno";
    string word4 = "educaron";
    string word5 = "retos";
    string word6 = "acondicionar";

Array.Sort(word3.ToCharArray());



Console.WriteLine(isPalindrome(word, word2));//true
Console.WriteLine(isPalindrome(word, word3));//false
Console.WriteLine(isAnagram(word3, word4));//true
Console.WriteLine(isAnagram(word, word4));//false
Console.WriteLine(isIsogram(word5));//true
Console.WriteLine(isIsogram(word6));//false


static bool isPalindrome(string word, string word2) => word.Reverse().ToArray().SequenceEqual(word2.ToCharArray());
static bool isAnagram(string word, string word2)
{
    char[] newWord = word.ToCharArray();
    char[] newWord2 = word2.ToCharArray();
    Array.Sort(newWord);
    Array.Sort(newWord2);
    if (newWord.SequenceEqual(newWord2)) return true;
    
    return false;
}
static bool isIsogram(string wordI) => wordI.Length == wordI.Distinct().Count();