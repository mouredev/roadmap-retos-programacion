/*
 *   EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

// https://kotlinlang.org/

// Single line comment

/* Multi
line
comment */

/**
 * Documentation comment
 */

var age = 22
age++ // this compiles, it's a variable

val name = "Brais" // runtime constant

/**
 * name = "Blas"
 * this won't compile
 * */

const val PI = 3.1415926535F // compile-time constant

// Primitive types

// Integer Numbers
val byte: Byte = 127 // (+-) 2.pow(7)
val short: Short = -32768 // (+-) 2.pow(15)
val int: Int = 2_147_483_647 // (+-) 2.pow(31)
val long: Long = 0L // to long number (+-) 2.pow(63)

// You can do the same with a U before the type to make it unsigned
val example: UShort = 65_535u // (+) 2.pow(16)

// Decimals
val float: Float = 0.000_000_1f
val double: Double = 0.000_000_000_000_000_2

// Booleans
val imSmart: Boolean = true

// Char
val initial: Char = 'B'

// String
val text: String = "string"

// Array
val lastNames: Array<String> = arrayOf("Fernández", "Vázquez")

println("Hola, Kotlin!")