fun main(args: Array<String>) {
// Esta es la pagina del lenguaje https://kotlinlang.org/

// Con esto representamos un comentario en una sola linea

/*Aqui tenemos 
para meter comentarios en varias
lineas */

//  ✅ Creamos una variable
var language = "kotlin"

//  ✅ Creamos una constante
val pi = 3.14

// ✅ Tipos de datos primitivos de tipo Integer (Byte, Short, Int, Long)
var exm_byte : Byte = 6
println("Ejemplo de byte: $exm_byte")

var exm_short : Short = 5555
println("Ejemplo de short: $exm_short")

var exm_int : Int = 429496
println("Ejemplo de int: $exm_int")

var exm_long : Long = 999999999999234 
println("Ejemplo de long: $exm_long")

// ✅ Tipos de datos primitivos de tipo Unsigned Integers (UByte, UShort, UInt, ULong)
var exm_Ubyte : UByte = 6u // tiene un rango entre 0-8 
println("Ejemplo de Ubyte: $exm_Ubyte")

var exm_Ushort : UShort = 5555u 
println("Ejemplo de Ushort: $exm_Ushort")

var exm_Uint : UInt = 429496u 
println("Ejemplo de Uint: $exm_Uint")

var exm_Ulong : ULong = 999999999999234u
println("Ejemplo de Ulong: $exm_Ulong")

// ✅ Tipos de datos primitivos de tipo Floating point  (Float, Double)
var exm_float : Float = 2.43f
println("Ejemplo de Float: $exm_float")

var exm_double : Double = 125.55566
println("Ejemplo de Double: $exm_double")

// ✅ Tipos de datos prmitivo de tipo Booolean
var exm_bol : Boolean = true
println("Ejemplo de boolean a : $exm_bol")
exm_bol = false
println("Ejemplo de boolean a : $exm_bol")

// ✅ Tipo de dato Char 
var exm_char : Char = 'a'
println("Ejemplo char : $exm_char")

// ✅ Tipo de dato String
var exm_string : String = "Kotlin"
println("Hola $exm_string!!!")


}
