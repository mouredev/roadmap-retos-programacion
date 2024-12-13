fun main() {
    // Ejemplos de operaciones con cadenas
    val cadena = "Hola, Mundo!"
    
    // Acceso a caracteres específicos
    println("Primer carácter: ${cadena[0]}")
    println("Último carácter: ${cadena[cadena.length - 1]}")

    // Subcadenas
    println("Subcadena (3, 7): ${cadena.substring(3, 7)}")

    // Longitud
    println("Longitud: ${cadena.length}")

    // Concatenación
    val otraCadena = " Bienvenido"
    println("Concatenación: ${cadena + otraCadena}")

    // Repetición
    println("Repetición: ${"Hola".repeat(3)}")

    // Recorrido
    print("Recorrido: ")
    for (char in cadena) {
        print("$char ")
    }
    println()

    // Conversión a mayúsculas y minúsculas
    println("Mayúsculas: ${cadena.uppercase()}")
    println("Minúsculas: ${cadena.lowercase()}")

    // Reemplazo
    println("Reemplazo: ${cadena.replace("Mundo", "Kotlin")}")

    // División
    val palabras = cadena.split(", ")
    println("División: $palabras")

    // Unión
    println("Unión: ${palabras.joinToString(" - ")}")

    // Interpolación
    val nombre = "Alice"
    println("Interpolación: Hola, $nombre!")

    // Verificación
    println("¿Empieza con 'Hola'?: ${cadena.startsWith("Hola")}")
    println("¿Termina con '!'?: ${cadena.endsWith("!")}")
    println("¿Contiene 'Mundo'?: ${"Mundo" in cadena}")

    // DIFICULTAD EXTRA
    println("\nDIFICULTAD EXTRA:")
    val palabra1 = "reconocer"
    val palabra2 = "ceronorec"
    
    println("'$palabra1' es palíndromo: ${esPalindromo(palabra1)}")
    println("'$palabra2' es palíndromo: ${esPalindromo(palabra2)}")
    println("'$palabra1' y '$palabra2' son anagramas: ${sonAnagramas(palabra1, palabra2)}")
    println("'$palabra1' es isograma: ${esIsograma(palabra1)}")
    println("'$palabra2' es isograma: ${esIsograma(palabra2)}")
}

fun esPalindromo(palabra: String): Boolean {
    val palabraLimpia = palabra.lowercase().filter { it.isLetter() }
    return palabraLimpia == palabraLimpia.reversed()
}

fun sonAnagramas(palabra1: String, palabra2: String): Boolean {
    if (palabra1.length != palabra2.length) return false
    return palabra1.lowercase().toList().sorted() == palabra2.lowercase().toList().sorted()
}

fun esIsograma(palabra: String): Boolean {
    val letrasUnicas = mutableSetOf<Char>()
    for (letra in palabra.lowercase()) {
        if (letra in letrasUnicas) return false
        letrasUnicas.add(letra)
    }
    return true
}