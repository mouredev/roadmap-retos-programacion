fun isPalindromo(cadena: String): Boolean {
    var cadenaLimpia = cadena.replace(" ", "").toLowerCase()
    var cadenaInvertida = cadenaLimpia.reversed()
    return cadenaLimpia == cadenaInvertida
}

fun isAnagrama(cadena1: String, cadena2: String): Boolean {
    var cadena1Limpia = cadena1.replace(" ", "").toLowerCase()
    var cadena2Limpia = cadena2.replace(" ", "").toLowerCase()
    return cadena1Limpia.toCharArray().sorted() == cadena2Limpia.toCharArray().sorted()
}

fun isIsograma(cadena: String): Boolean {
    var cadenaLimpia = cadena.replace(" ", "").toLowerCase()
    return cadenaLimpia.toCharArray().distinct().size == cadenaLimpia.length
}

fun main() {
    var cadena = "Hola Mundo"

    println(cadena);

    // Concatenar

    var nombre = "Miguel"

    println("Hola " + nombre)

    // Interpolación de cadenas

    println("Hola $nombre")

    // Mayuscula

    println(nombre.toUpperCase())

    // Minuscula

    println(nombre.toLowerCase())

    // Longitud

    println(nombre.length)

    // Comparar cadenas

    var nombre2 = "Miguel"

    println(nombre == nombre2)

    // Subcadena

    println(nombre.substring(0, 3))

    // Reemplazar

    println(nombre.replace("M", "L"))

    // Buscar

    println(nombre.indexOf("g"))

    // Recorrer cadena

    for (letra in nombre) {
        println(letra)
    }

    // trim

    var nombre3 = " Miguel "
    println(nombre3.trim())

    println("Ana es palindromo: " + isPalindromo("Ana"))
    println("Miguel es palindromo: " + isPalindromo("Miguel"))

    println("Amor y Roma son anagramas: " + isAnagrama("Amor", "Roma"))
    println("Hola y Adios son anagramas: " + isAnagrama("Hola", "Adios"))

    println("Murcielago es isograma: " + isIsograma("Murcielago"))
    println("Miguelex es isograma: " + isIsograma("Miguelex"))
}