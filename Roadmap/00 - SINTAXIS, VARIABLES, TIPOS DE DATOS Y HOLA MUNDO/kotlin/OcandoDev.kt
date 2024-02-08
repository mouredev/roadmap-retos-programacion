//Documentacion oficial de Kotlin => https://kotlinlang.org/docs

//Tipos de comentarios

// Comentario de una linea

/* 
    Comentario 
    de varias
    lineas
*/

fun main(){

    //Variables y constantes
    val dev = "OcandoDev" //Las constantes se definen con val 
    var exercise = 0 //Las variables se definen con var

    //Tipos de datos en Kotlin
    var _string: String = "Cadena de texto"
    var _int: Int = 1
    var _boolean: Boolean = false
    var _float: Float = 26.9f
    var _double: Double = 26.9
    var _char: Char = 'A'
    var _byte: Byte = 127
    var _short: Short = 32767
    var _long: Long = 9223372036854775807
    var _array: Array<Int> = arrayOf(1,2,3)

    var language = "Kotlin"

    print("Hola, $language!")
}