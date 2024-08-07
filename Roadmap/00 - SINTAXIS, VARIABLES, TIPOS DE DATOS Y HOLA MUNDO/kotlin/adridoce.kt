// https://kotlinlang.org/

// Comentario en una linea

/*
    Comentario multilinea
 */

const val PI = 3.1416                       // Constante, usando const debe de ser una variable global

fun main() {
    /*
        val se utiliza para declarar variables inmutables con valores conocidos en tiempo de ejecución, 
        mientras que const se utiliza para declarar constantes de tiempo de compilación cuyos valores son conocidos en tiempo de compilación.
    */

    var numero: Int = 1                     // Variable mutable
    val lenguaje: String = "Kotlin"         // Variable inmutable
    
    // Numeros enteros
    var byte: Byte = 127                    // 8 bits
    var short: Short = 32767                // 16 bits
    var entero: Int = 2147483647            // 32 bits
    var long: Long = 9223372036854775807    // 64 bits

    // Numeros de punto flotante o decimales
    var float: Float = 1.5f                 // 32 bits
    var double: Double = 1.5                // 64 bits

    // Caracteres
    var char: Char = 'A'

    // Cadenas de texto
    var string: String = "Hola mundo!"

    // Booleanos
    var booleano: Boolean = true            

    // Arrays
    val array: Array<Int> = arrayOf(1, 2, 3)

    print("Hola, $lenguaje")
    
}