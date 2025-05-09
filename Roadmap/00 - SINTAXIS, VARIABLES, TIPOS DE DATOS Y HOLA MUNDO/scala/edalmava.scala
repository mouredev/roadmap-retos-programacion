// Comentario de una línea
/* 
    Comentario de varias 
    líneas
*/

// Sitio oficial: https://scala-lang.org/

// Variables y tipos de datos: https://docs.scala-lang.org/scala3/book/taste-vars-data-types.html

// Inmutables
val a = 0

// Mutables
var c = 1
c = 2          // Una variable var puede ser reasignada

// Declaración de tipos

val x: Int = 1 // Declaración explícita de tipo
val y =  1     // Declaración implícita de tipo

// Tipo primitivos (built-in)
val b: Byte = 1
val i: Int = 1
val l: Long = 1
val s: Short = 1
val d: Double = 2.0
val f: Float = 3.0

val int = 123      // Por defecto es Int
val flo = 1.0      // Por defecto es Double

val lon = 1_000L   // val lon: Long = 1000
val dou = 2.2D     // val dou: Double = 2.2
val fla = 3.3F     // val fla: Float = 3.3

val lenguaje = "Scala" //String
val char = 'a'         // Char

// booleanos
val falso: Boolean = false
val verdadero = true

println(s"¡Hola, $lenguaje!")
