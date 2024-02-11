// Sitio Web Oficial: https://kotlinlang.org/

//Constante
const val LANGUAGE = "Kotlin"

fun main() {
    //Comentario de una linea

    /*
    * Comentario
    * de
    * varias
    * líneas
    */
    val firstNumber: Int = 12 //Variable inmutable (su valor no puede modificarse)
    var result: Int = 0 // Variable mutable (su valor puede modificarse)
    result = firstNumber * 2 // result = 24
//    Tipos Primitivos:

    // #Enteros
    val number: Int = 8
    val one: Short = 1
    val threeBillion: Long = 3_000_000_000
    val oneByte: Byte = 1

    // #Punto flotante
    val pi = 3.14 // Double
    val floatNumber: Float = 2.71f

    // #Constantes literales
    val hexadecimal = 0x0F
    val binaryNumber = 0b00001011
    val text: String = "Programación"
    val myTrue: Boolean = true
    val myFalse: Boolean = false
    val character: Char = 'C'
    val unicodeChar: Char = '\uFF00'
//    Caracteres de escape:

    /*
    \t: Tabulación
    \b: Retroceso
    \r: Retorno de carro
    \n: Salto de línea
    \': Apostrofe
    \": Comillas doble
    \\: Backslash
    \$: Símbolo de dólar
     */

    println("Hola $LANGUAGE")
}