fun main() {
    // Definir una cadena de caracteres
    val cadena = "Hola, mundo!"

    // Acceso a caracteres específicos
    val primerCaracter = cadena[0]
    val ultimoCaracter = cadena[cadena.length - 1]

    println("Acceso a caracteres:")
    println("Primer caracter: $primerCaracter")
    println("Último caracter: $ultimoCaracter")

    // Subcadenas
    val subcadena = cadena.substring(0, 4)
    println("\nSubcadena:")
    println("Subcadena de los primeros 4 caracteres: $subcadena")

    // Longitud de la cadena
    val longitud = cadena.length
    println("\nLongitud de la cadena:")
    println("Longitud de la cadena: $longitud")

    // Concatenación
    val otraCadena = " ¡Kotlin es genial!"
    val cadenaConcatenada = cadena + otraCadena
    println("\nConcatenación:")
    println("Cadena concatenada: $cadenaConcatenada")

    // Repetición
    val cadenaRepetida = cadena.repeat(3)
    println("\nRepetición:")
    println("Cadena repetida 3 veces: $cadenaRepetida")

    // Recorrido
    println("\nRecorrido:")
    for (caracter in cadena) {
        print("$caracter ")
    }

    // Conversión a mayúsculas y minúsculas
    println("\n\nConversión a mayúsculas y minúsculas:")
    val mayusculas = cadena.toUpperCase()
    val minusculas = cadena.toLowerCase()
    println("Mayúsculas: $mayusculas")
    println("Minúsculas: $minusculas")

    // Reemplazo
    val cadenaReemplazada = cadena.replace("mundo", "Kotlin")
    println("\nReemplazo:")
    println("Cadena con reemplazo: $cadenaReemplazada")

    // División
    val palabras = cadena.split(",")
    println("\nDivisión:")
    println("Cadena dividida por coma: $palabras")

    // Unión
    val nuevaCadena = palabras.joinToString("-")
    println("\nUnión:")
    println("Palabras unidas por guión: $nuevaCadena")

    // Interpolación
    val nombre = "Juan"
    val edad = 25
    val mensaje = "Hola, me llamo $nombre y tengo $edad años."
    println("\nInterpolación:")
    println("Mensaje interpolado: $mensaje")

    // Verificación
    val esDigito = cadena.all { it.isDigit() }
    println("\nVerificación:")
    println("¿La cadena contiene solo dígitos?: $esDigito")
}

// Ejercicio Extra
fun main() {
    // Ingresa las dos palabras que deseas analizar
    print("Ingresa la primera palabra: ")
    val palabra1 = readLine()!!.toLowerCase()

    print("Ingresa la segunda palabra: ")
    val palabra2 = readLine()!!.toLowerCase()

    // Comprobación de palíndromo
    val esPalindromo1 = esPalindromo(palabra1)
    val esPalindromo2 = esPalindromo(palabra2)

    // Comprobación de anagrama
    val esAnagrama = esAnagrama(palabra1, palabra2)

    // Comprobación de isograma
    val esIsograma1 = esIsograma(palabra1)
    val esIsograma2 = esIsograma(palabra2)

    // Mostrar resultados
    println("\nResultados:")
    println("Palabra 1 es palíndromo: $esPalindromo1")
    println("Palabra 2 es palíndromo: $esPalindromo2")
    println("Son anagramas: $esAnagrama")
    println("Palabra 1 es isograma: $esIsograma1")
    println("Palabra 2 es isograma: $esIsograma2")
}

fun esPalindromo(palabra: String): Boolean {
    val reversa = palabra.reversed()
    return palabra == reversa
}

fun esAnagrama(palabra1: String, palabra2: String): Boolean {
    return palabra1.toCharArray().sorted() == palabra2.toCharArray().sorted()
}

fun esIsograma(palabra: String): Boolean {
    val setDeCaracteres = HashSet<Char>()
    for (caracter in palabra) {
        if (!setDeCaracteres.add(caracter)) {
            return false // Si se encuentra un carácter repetido, no es un isograma
        }
    }
    return true
}
