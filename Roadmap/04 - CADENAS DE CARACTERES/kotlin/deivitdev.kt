fun main() {
    // String operations
    val str = "Hello, World!"
    println("Access specific character: ${str[1]}") // Access specific character
    println("Substring: ${str.substring(0, 5)}") // Substring
    println("Length: ${str.length}") // Length
    println("Concatenation: ${str + " How are you?"}") // Concatenation
    println("Repetition: ${str.repeat(2)}") // Repetition
    println("Uppercase: ${str.uppercase()}") // Uppercase
    println("Lowercase: ${str.lowercase()}") // Lowercase
    println("Replace: ${str.replace("World", "Kotlin")}") // Replace
    println("Split: ${str.split(", ")}") // Split
    println("Join: ${listOf("Hello", "World").joinToString(", ")}") // Join
    println("Interpolation: ${"The length of the string is ${str.length}"}") // Interpolation
    println("Contains: ${str.contains("World")}") // Contains

    // Check if two words are palindromes, anagrams, or isograms
    val word1 = "roma"
    val word2 = "amor"
    println("Is '$word1' a palindrome? ${isPalindrome(word1)}")
    println("Are '$word1' and '$word2' anagrams? ${areAnagrams(word1, word2)}")
    println("Is '$word1' an isogram? ${isIsogram(word1)}")
}

fun isPalindrome(word: String): Boolean = word == word.reversed()

fun areAnagrams(word1: String, word2: String): Boolean = word1.toCharArray().sorted() == word2.toCharArray().sorted()

fun isIsogram(word: String): Boolean = word.length == word.toSet().size