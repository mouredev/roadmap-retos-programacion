/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */

fun main() {
    var str1: String = "Hola"
    var str2: String = "Mundo"

    // Acceso a un caracter especifico
    println(str1[1])
    println(str1.get(1))

    // Substring
    str1 = "Esto es una string"
    println(str1.substring(12))
    println(str1.substring(0, 4))

    // Longitud de la string
    println(str1.length)

    // Concatenación
    str1 = "Hola "
    println(str1.plus(str2))

    // Repeticion
    str1 = "a"
    println(str1.repeat(5))

    // Añadir valor tanto al inicio o al final si no cumple una longitud minina.
    str1 = "Hola"
    println(str1.padEnd(8,'!'))
    println(str1.padStart(8,'!'))

    // Mayusculas, minusculas
    println(str1)
    println(str1.uppercase())
    println(str1.lowercase())

    // Reemplazo
    str1 = "hola mundo"
    println(str1.replace('o', '?'))

    // División
    val palabras: List<String> = str1.split(' ')
    println(palabras.toString())

    // Verificación
    println(str1.contains("hola"))

    // Trim
    str1 = "    hola    "
    println(str1.trim())

    // recorrido
    str1 = "abcdefg"
    for (i in str1){
        println(i)
    }

    // Interpolación
    str1 = "interpolación"
    println("Esto es una prueba de $str1")

    // Reto extra
    println(analizarPalabra("rayar", "rayar"))
    println(analizarPalabra("cava", "vaca"))
    println(analizarPalabra("prueba", ""))
}

fun analizarPalabra(str1: String, str2: String): String {
    if (esPalindromo(str1, str2))
        return "$str1 es un palindromo"

    if (esAnagrama(str1, str2))
        return "$str2 es un anagrama de $str1"

    if (esIsograma(str1))
        return  "$str1 es un isograma"

    return "$str1 no es ni un palindromo, anagrama o isograma"
}

fun esPalindromo(str1: String, str2: String): Boolean {
    return when (str1){
        str2.reversed() -> true
        else -> false
    }
}

fun esAnagrama(str1: String, str2: String): Boolean {

    if (str1.length != str2.length)
        return false

    var palabra1: CharArray = str1.toCharArray()
    var palabra2: CharArray = str2.toCharArray()

    palabra1.sort()
    palabra2.sort()

    for (i in palabra1.indices){
        if (palabra1[i] != palabra2[i]){
            return false
        }
    }

    return true
}

fun esIsograma(str1: String): Boolean{
    var palabra = str1.toCharArray()
    palabra.sort()

    var letras: String = ""

    for (i in palabra.indices){
        if (letras.contains(palabra[i])){
            return false
        } else {
            letras += palabra[i]
        }
    }

    return true
}