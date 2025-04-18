
//Pagina de Compilador En Linea Ideal para ejerecicios basicos 
//   https://pl.kotl.in/AoeqZtsuv

//Pagina Oficial del Lenguaje 
//   https://kotlinlang.org/docs/home.html

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                     Tipos de Comentarios                                                         //
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Comentario de una sola línea

/*
   Comentario de varias líneas.
   Puede ocupar más de una línea.
*/

/*
   Comentario de bloque anidado
   /* Comentario interno */
*/

/**
 * Comentario de documentación (KDoc)
 * Usado para documentar funciones, clases, etc.
 */

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                 Crear variable y constante                                                       //
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Variable mutable (puede cambiar su valor)
var miVariable = 10

// Constante (no puede cambiar su valor)
val miConstante = 20

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                           Variables con tipos de datos primitivos                                                //
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Cadenas de texto (String)
val miCadena: String = "Hola, Kotlin!"

// Enteros (Int)
val miEntero: Int = 42

// Números decimales (Double, Float)
val miDecimal: Double = 3.1416
val miFloat: Float = 2.5f

// Booleanos (Boolean)
val miBooleano: Boolean = true

// Caracteres (Char)
val miCaracter: Char = 'K'

// Byte (8 bits), Short (16 bits), Long (64 bits)
val miByte: Byte = 127
val miShort: Short = 32000
val miLong: Long = 123456789L

fun main() {
    holaMundo()
}

fun holaMundo(){
  val saludo: String = "Hola Mundo. El Lengueje es Kotlin"
    println(saludo)
}



