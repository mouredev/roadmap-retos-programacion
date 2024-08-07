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

 fun main() {
    strings()
 }

 fun strings() {
    val cadena: String = "Hola Kotlin!"
    val cadena2: String = "Hola Python!"
    
/* --- Propiedades --- */

    // longitud: Se llama a length sin usar () porque es una propiedad de la cadena y no un metodo.
    println("La longitud de la cadena es: ${cadena.lenght}")


/* --- Functions --- */

    // compareTo(): Devuelve 0 si las dos cadenas son iguales, <0 si es menor que la cadena recibida y >0 si es mayor 
    println(cadena.compareTo(cadena2))
    println(cadena2.compareTo(cadena))

    // equals(): Compara si dos objetos son iguales, devuelve booleano
    if (cadena.equals(cadena2)) println("Las cadenas coinciden") else println("Las cadenas no coinciden")

    // get(): Devuelve el caracter en la posicion indicado
    println(cadena.get(5))

    // hashCode(): Devuelve el hashCode del objeto
    println(cadena.hashCode())

    // plus(): Devuelve un string resultado de la concatenacion de ambos objetos
    println(cadena.plus(cadena2))

    // SubSequence(): devuelve una secuencia de caracteres más genérica
    println(cadena.subSequence(0,4))

    /* --- Propiedades de extensión --- */
    // indices: Devuelve el rango de índices de caracteres válidos para esta secuencia de caracteres.
    println(cadena2.indices)

    // lastIndex: Devuelve el índice del último carácter de la secuencia de caracteres o -1 si está vacío.
    println(cadena2.lastIndex)


/* --- Funciones de extension --- */

    // substring() devuelve una nueva cadena específica 
    println(cadena.substring(0,4))
    println(cadena.substring(5, 11))

    // contains(): Devuelve true si la secuencia de caracteres contiene la  secuencia de caracteres especificada como subcadena.
    if (cadena.contains("Kot")) println("Subcadena encontrada") else println("Subcadena no encontrada")
    if (cadena.contains("aaa")) println("Subcadena encontrada") else println("Subcadena no encontrada")

    // count(): Devuelve la longitud de la secuencia de caracteres.
    println(cadena2.count())

    // drop(): Devuelve un string con los primeros n caracteres eliminados
    println(cadena.drop(5))

    // dropLast(): Devuelve un string con los ultimos n caracteres eliminados
    println(cadena.dropLast(5))

    // filter(): Devuelve una cadena que contiene sólo aquellos caracteres de la cadena original que coinciden con el predicado dado.
    val palabras = listOf("Hola", "Adiós", "Gato", "Perro", "Ratón")
    val palabrasConA = palabras.filter { palabra -> 'a' in palabra.toLowerCase() }

    println("Palabras originales: $palabras")
    println("Palabras que contienen 'a': $palabrasConA")

    // format()
    val integerNumber = String.format("%07d", 31416)
	println(integerNumber)

	val floatNumber = String.format("%+.4f", 3.141592)
	println(floatNumber)

	val helloString = String.format("%S %S", "hello", "world")
	println(helloString)

    //split()
    println(cadena.split(""))

    // Conversion a mayusculas y minusculas
    println(cadena.uppercase())
    println(cadena.lowercase())

    esPalindromo("anilina")
    esPalindromo("El perro de san roque no tiene rabo")
    esAnagrama("roma", "amor")
    esAnagrama("palabra", "arbol")
    esIsograma("murcielago")
    esIsograma("escritura")
 }

 fun esPalindromo(texto: String) {
    /* 
        Palabra o frase cuyas letras están dispuestas de tal manera que resulta 
        la misma leída de izquierda a derecha que de derecha a izquierda
    */

    val textoSinEspacios = texto.replace("\\s".toRegex(), "")
    val longitud = textoSinEspacios.length

    for (i in 0 .. longitud / 2) {
        if (textoSinEspacios[i] != textoSinEspacios[longitud - 1 - i]) {
            println("La cadena NO es un Palindromo")
            return
        }
    }

    println("La cadena SI es un Palindromo")
 }

 fun esAnagrama(texto1: String, texto2: String) {
    /*  
        una palabra es anagrama de otra si las dos tienen las mismas letras, 
        con el mismo número de apariciones, pero en un orden diferente.   
    */

    val texto1Array = texto1.toCharArray().sortedArray()
    val texto2Array = texto2.toCharArray().sortedArray()

    if (texto1Array.contentEquals(texto2Array)) {
        println("La cadena SI es un Anagrama")
    }
    else {
        println("La cadena NO es un Anagrama")
    }
 }

 fun esIsograma(texto: String) {
    /*
        Un isograma es una palabra o frase en la cual no hay letras o caracteres repetidos. 
        En otras palabras, cada letra o caracter en un isograma aparece exactamente una vez. 
    */
    val textoEnMinusculas = texto.lowercase()
    val conjuntoDeCaracteres = textoEnMinusculas.toCharArray().toSet()

    if (conjuntoDeCaracteres.size == textoEnMinusculas.length) {
        println("La cadena SI es un Isograma")
    }
    else {
        println("La cadena NO es un Isograma")
    }
    
 }