fun main() {

    var developer = "Alejandro"
    developer += " Ocando"

    println(developer)

    //Subcadena
    val substringDev = developer.substring(10,16)
    println(substringDev)

    //Busqueda y remplazo
    val modifiedString = developer.replace("Ocando", "Enrique")
    println(modifiedString)

    //Recorriendo una cadena
    println(developer[4])
    println(developer.get(4))

    for(char in developer)
        print(char)

    println()

    for(index in developer.indices)
        print("${developer[index]} ")

    println()

    println(developer.length)

    println()

    //Formas de concatenacion
    val repoOwner = "Brais " + "Moure"
    println(repoOwner)
    val mixedDataType = "Emocion: " + 100
    println(mixedDataType)
    val operation = "Resultado: " + (4 + 4)
    println(operation)

    println()

    val multiLineString = """
        This is
        a simple
        way to
        create
        a super
        string
    """.trimIndent()

    println(multiLineString)


    println()

    //Comparacion de cadenas
    val isEqual = "Kotlin" == "kotlin"
    println(isEqual)
    val isEqualIgnoreCase = "Kotlin".equals("kotlin", ignoreCase = true)
    println(isEqualIgnoreCase)

    //Trimming una cadena
    val trimmedString = "   Kotlin  "
    println(trimmedString.trim())

    //Split de cadenas
    val splittedText = "Programar es lo mejor!".split(" ")
    println(splittedText)

    //Upper y LowerCase
    val upper = "estoy en mayusculas"
    println(upper.uppercase())

    val lower = "ESTOY EN MINUSCULAS"
    println(lower.lowercase())

    //Contains
    println(lower.contains("a"))

    //Parseo de cadenas
    val favoriteNumber = "26"
    favoriteNumber.toInt()
    println(favoriteNumber)

    val chars = arrayOf('h','o','l','a')
    val charsString = String(chars.toCharArray())
    println(charsString)

    println()
    //Ejercicios

    val anagramWord1 = "Secure"
    val anagramWord2 = "Rescue"
    println("Es $anagramWord1 anagrama de $anagramWord2?: ${isAnagram(anagramWord1, anagramWord2)}")

    println()

    val palindrome = "Arepera"
    println("Es $palindrome un palindromo?: ${isPalindrome(palindrome)}")

    println()

    val isogram = "uncopyrightable"
    println("Es $isogram un isograma?: ${isIsogram(isogram)}")

}

fun isAnagram(word1: String, word2: String): Boolean{
    val ordenedWord1 = word1.lowercase().trim().toCharArray().sorted()
    val ordenedWord2 = word2.lowercase().trim().toCharArray().sorted()

    return ordenedWord1 == ordenedWord2
}

fun isPalindrome(original: String): Boolean{
    original.lowercase()
    var reversed = ""

    for(letter in original.trim()){
        reversed += letter
    }

    return original == reversed.trim()
}

fun isIsogram(original: String): Boolean{
    val manipulatedString = original.lowercase().trim()

    for(i in manipulatedString.indices){
        for(j in i + 1..<manipulatedString.length){
            if(manipulatedString[i] == manipulatedString[j]) return false
        }
    }
    return true
}