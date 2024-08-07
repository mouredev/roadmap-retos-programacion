fun main() {

    // Concatenación
    var hello = "hello"
    var world = " world"

    println(hello + world)

    // Iterar
    val animals = "🐶🐵🐻"

    for (animal in animals) {
        print("$animal")
    }

    // Construcción a partir de caracteres
    val characters = arrayOf('H', 'e', 'l', 'l', 'o')
    val string = String(characters.toCharArray())
    println("\n$string")

    // Interpolación
    val name = "Diego"
    val message = "Su nombre es $name"
    println(message)

    // Unicode
    val character = "\u1F425"
    println(character)

    // Tamaño de la cadena
    val word = "esternocleidomastoideo"
    println(word.length)

    // Obtener un caracter
    val saludo = "hello world"
    println(saludo[2])

    // Insertar
    hello = hello.substring(0, 5) + "!"
    println(hello)

    // Eliminar
    hello = hello.replace("!", "")
    println(hello)

    // Subcadenas
    hello = saludo.substring(0, 5)
    println(hello)

    // Comparar
    val sameHello = "hello"

    if (hello == sameHello) {
        println("$hello y $sameHello son iguales")
    }

    // Repetición
    val doubleHello = hello.repeat(2)
    println(doubleHello)

    // Conversión mayúsculas
    val mayusHello = hello.toUpperCase()
    println(mayusHello)

    // Conversión minúsculas
    val minusHello = mayusHello.toLowerCase()
    println(minusHello)

    // Reemplazar caracter
    val helloDos = hello.replace('h', 'H')
    println(helloDos)

    // División
    val sentence = "hello world"
    val words = sentence.split(" ")
    println(words)

    // Verificación
    if (helloDos.contains('H')) {
        println("Contiene H")
    }

    checkWords("lacteo", "coleta")
}

// --------------- Ejercicio -----------------

fun checkWords(word1: String, word2: String) {
    if (isPalindromo(word1, word2)) {
        println("$word1 y $word2 son palíndromos")
    } else {
        println("$word1 y $word2 no son palíndromos")
    }

    if (isAnagrama(word1, word2)) {
        println("$word1 y $word2 son anagramas")
    } else {
        println("$word1 y $word2 no son anagramas")
    }

    if (isIsograma(word1)) {
        println("$word1 es un isograma")
    } else {
        println("$word1 no es un isograma")
    }

    if (isIsograma(word2)) {
        println("$word2 es un isograma")
    } else {
        println("$word2 no es un isograma")
    }
}

fun isPalindromo(word1: String, word2: String): Boolean {
    val reversedWord2 = word2.reversed()

    if (word1.length == word2.length) {

        for (i in word1.indices) {
            val character1 = word1[i]
            val character2 = reversedWord2[i]

            if (character1 != character2) {
                return false
            }
        }

        return true
    }

    return false
}

fun isAnagrama(word1: String, word2: String): Boolean {
    var word1Array = word1.toCharArray()
    var word2Array = word2.toCharArray()

    word1Array.sort()
    word2Array.sort()

    return word1Array.contentEquals(word2Array)
}

fun isIsograma(word: String): Boolean {
    var characters = mutableMapOf<String, Int>()
    var i = 0   

    for (character in word) {

        characters[character.toString()] = if (characters[character.toString()] != null) characters.getOrDefault(character.toString(), 0) + 1 else 1
    }

    for ((key, value) in characters) {

        if (i == 0) {
            i = value
        } else {
            if (i != value) {
                return false
            }
        }
    }

    return true
}

