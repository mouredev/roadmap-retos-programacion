
import java.io.File
import kotlin.text.lowercase
import kotlin.text.uppercase

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

open class LuisRetos {

    fun myStrings() {
        // String
        val myString = "Hola: soy una cadena de texto"
        println(myString)

        // Access to specific characters
        println("First character: ${myString[0]}")
        println("Last character: ${myString[myString.length - 1]}")
        println("Third character: ${myString.get(2)}")
        println("Substring from index 5 to 10: ${myString.subSequence(5, 10)}")
        println("Length of the string: ${myString.length}")

        // Concatenation
        val string1 = "Hello"
        val string2 = "World"
        val concatenatedString = string1 + " " + string2
        println("Concatenated string: $concatenatedString")

        // Repetition
        val repeatedString = "abc".repeat(3)
        println("Repeated string: $repeatedString")

        // Conversion to uppercase and lowercase
        val uppercaseString = myString.uppercase()
        val lowercaseString = myString.lowercase()
        println("Uppercase string: $uppercaseString")
        println("Lowercase string: $lowercaseString")

        // Replacement
        val replacedString = myString.replace("cadena", "frase")
        println("Replaced string: $replacedString")

        // Splitting
        val splitString = myString.split(":")
        println("Split string: $splitString")

        // Joining
        val joinedString = splitString.joinToString("-")
        println("Joined string: $joinedString")

        // Interpolation
        val name = "Luis"
        val age = 30
        val interpolatedString = "My name is $name and I am $age years old."
        println("Interpolated string: $interpolatedString")

        // Verification
        val containsHola = myString.contains("Hola")
        println("Contains 'Hola': $containsHola")
        println()
    }

    fun checkWords(word1: String, word2: String) {

        val reversedWord1 = word1.reversed()
        val reversedWord2 = word2.reversed()
        val isPalindrome1 = word1 == reversedWord1
        val isPalindrome2 = word2 == reversedWord2
        println("Is \"$word1\" a palindrome? $isPalindrome1")
        println("Is \"$word2\" a palindrome? $isPalindrome2")
        println()

        val sortedWord1 = word1.toCharArray().sorted().joinToString("")
        val sortedWord2 = word2.toCharArray().sorted().joinToString("")
        val isAnagram = sortedWord1 == sortedWord2
        println("Are \"$word1\" and \"$word2\" anagrams? $isAnagram")
        println()
        val isIsogram1 = word1.length == word1.toSet().size
        val isIsogram2 = word2.length == word2.toSet().size
        println("Is \"$word1\" an isogram? $isIsogram1")
        println("Is \"$word2\" an isogram? $isIsogram2")

    }
}

fun main() {
    val retos = LuisRetos()
    retos.myStrings()
    retos.checkWords("hola", "aloh")
    retos.checkWords("hola", "Taco cat")
    retos.checkWords("eye", "madam")
    retos.checkWords("radar", "level")
}