/*
 * Kotlin es un lenguaje de programación moderno y conciso que se enfoca en
 * la interoperabilidad con Java. Puedes encontrar más información en su sitio
 * web oficial: https://kotlinlang.org/
 */

// Comentario de una línea
val mensaje: String = "¡Hola, Kotlin!" // Comentario en línea después de la declaración de la variable

/*
   Comentario multilinea
   para explicar
   varios detalles
*/

/**
 * Este es un comentario de documentación
 * Puedes acceder a él mediante herramientas de generación de documentación.
 */

// Variable y constante
var variableMutable = "Hola, Kotlin"
val constanteInmutable = 42

var texto: String = "Hola, " // Variable de tipo cadena de texto
var entero: Int = 10 // Variable de tipo entero
var decimal: Double = 5.5 // Variable de tipo decimal
var booleano: Boolean = true // Variable de tipo booleano

fun main() {
    println("$texto${mensaje.substringAfter(", ")}") // Imprime: ¡Hola, Kotlin!
}
