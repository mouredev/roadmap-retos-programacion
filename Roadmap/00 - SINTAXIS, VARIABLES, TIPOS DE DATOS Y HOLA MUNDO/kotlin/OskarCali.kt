// https://kotlinlang.org/

// Comentario en una sola linea
/* Comentario en
 * multiples lineas
 */

// val -> variable de solo lectura, no puede cambiar de valor
// var -> variable mutable, que puede cambiar de valor
val x = 5
var y = 8

// Los datos primitivos/básicos son
//
// Enteros -> Byte, Short, Int, Long
// Enteros sin signo -> UByte, UShort, UInt, ULong
// Números con decimal -> Float, Double
// Booleanos -> Boolean
// Caracteres -> Char
// Cadenas de texto -> String

val entero: Int = 843
val text = "Hola comunidad"
val decimal: Double = 3.141592
val largeNumber: Long = 48_365_102_000
val aprendiendo = true

fun main() {
    print("¡Hola, Kotlin!")
}

// NOTAS FINALES
//
// 1) Se recomienda utilizar var solamente cuando sea necesario.
// 2) Los tipos de dato pueden ser inferidos al momento de la asignación o definirse después
//    del nombre de la variable con : (dos puntos) y el tipo de dato.
// 3) Para los números se pueden colocar _ (guion bajo) para mejorar la lectura
