//     Isograma: palabra o frase en la que cada letra aparece el mismo número de veces.
//     Palíndromo: Palabra o frase que se lee igual de derecha a izquierda, que de izquierda a derecha
//     Anagrama: si las dos tienen las mismas letras, con el mismo número de apariciones, pero en un orden diferente
fun differentWord(firstWord: String, secondWord: String): Boolean {
    return firstWord != secondWord
}

fun anagram(firstWord: String, secondWord: String): Boolean {
    val firstWordMap = firstWord.groupingBy { it }.eachCount()
    val secondWordMap = secondWord.groupingBy { it }.eachCount()

    return if (differentWord(firstWord, secondWord) && firstWord.length == secondWord.length) {
        firstWordMap == secondWordMap
    } else {
        false
    }
}

fun palindrome(firstWord: String, secondWord: String): Boolean {
    val textOne = firstWord.reversed()
    val textTwo = secondWord.reversed()

    return if (differentWord(firstWord, secondWord)) {
        firstWord == textOne && secondWord == textTwo
    } else {
        false
    }
}

fun isogram(firstWord: String, secondWord: String): Boolean {
    val textOne = firstWord.groupingBy { it }.eachCount()
    val textTwo = secondWord.groupingBy { it }.eachCount()

    return if (differentWord(firstWord, secondWord)) {
        firstWord.length == textOne.size && secondWord.length == textTwo.size
    } else {
        false
    }
}


fun checkWords(firstWord: String, secondWord: String): String {
    return when {
        anagram(firstWord, secondWord) -> "$firstWord y $secondWord forman un: anagrama."
        palindrome(firstWord, secondWord) -> "$firstWord y $secondWord forman un: palindromo"
        isogram(firstWord, secondWord) -> "$firstWord y $secondWord forman un: isograma"
        else -> "$firstWord y $secondWord no forman lo requerido"
    }
}


fun main() {
    val wordOne = "I love"
    val wordTwo = "Kotlin"
    val text = "Ejemplo de cadena"
    val parts = text.split(" ")

//  Acceso a caracteres específicos
    println("La tercera letra de la palabra \"$wordOne\" es: ${wordOne[3]}")
    println("La primera letra es: ${wordOne.first()}")
    println("La última letra es: ${wordOne.last()}")

//    Subcadena
    println("Subcadena a partir del índice 11 de la palabra \"$text\" : ${text.substring(11)}")

//    Longitud
    println("Longitud de la cadena ${text.length}")
//    Convertir en minúsculas
    println(wordOne.lowercase())

//    Convertir a mayúsculas
    println(wordTwo.uppercase())

//    Concatenar
    println("Cadena concatenada: $text en $wordTwo")

//    Repetición
    println("Repetición de cadena:")
    repeat(3) {
        println("$wordOne $wordTwo")
    }

//    Recorrido
    println("Recorriendo la cadena:")
    for (letter in text) {
        println(letter)
    }

//    Reemplazo
    println("Letra \"e\" reemplazada por \"X\": ${text.replace('e', 'X')}")

//    División
    println("Cadena separada por comas: $parts")

//    Verificación
    println("¿La cadena contiene la palabra \"Ejemplo\": ${text.contains("Ejemplo")}")

//    Comparación de cadenas
    println("¿La cadena 1 es igual a la cadena 2?: ${wordOne == wordTwo}")

//    Eliminación de espacios en blanco
    val whiteSpace = "             hola              "
    println("Eliminando espacios blancos al inicio: ${whiteSpace.trimStart()}")
    println("Eliminando espacios en blanco al final: ${whiteSpace.trimEnd()}")
    println("Eliminando todos los espacios en blanco: ${whiteSpace.trim()}")

//    Extracción de partes específicas
    val learning = "Roadmap de retos de programación"
    /*Puedes utilizar funciones como substringBefore, substringAfter, take, drop, takeLast, dropLast para extraer partes específicas de una cadena.*/
    println("Extrayendo el texto de la cadena $learning antes de la palabra \"de\": ${learning.substringBefore("de")}")
    println("Extrayendo el texto después de la palabra \"de\": ${learning.substringAfter("de")}")
    println("Extrayendo el texto a través del índice 10: ${learning.take(10)}")

//    Búsqueda de cadenas
    /*Puedes buscar subcadenas dentro de una cadena utilizando funciones como indexOf, lastIndexOf, contains, startsWith, endsWith.*/
    println("Índice de la palabra \"Roadmap\": ${learning.indexOf("Roadmap")}")
    println("El texto comienza con \"Z\"? : ${learning.startsWith("Z")}")

//    Expresiones regulares
    val age = "La edad es 30"
    val regexAge = Regex("[0-9]+")
    println(regexAge.find(age)?.value)

//    Ejercicio extra
    println("RESULTADO DEL EJERCICIO EXTRA:")
    println(checkWords("adan", "nada"))
    println(checkWords("reconocer", "anilina"))
    println(checkWords("animal", "lamina"))
    println(checkWords("sometemos", "sacas"))
    println(checkWords("huevo", "murciélago"))
    println(checkWords("cazador", "reappear"))
    println(checkWords("anagrama", "nagarama"))
    println(checkWords("caso", "saco"))
    println(checkWords("túnel", "tiburón"))
}