/*
THIS IS A BLOCK COMMENT ON MULTIPLE LINES
 SITIO OFICIAL SOBRE EL LENGUAJE DE PROGRAMACION KOTLIN
    https://kotlinlang.org/docs/getting-started.html#is-anything-missing
 */

//    THIS IS AN END-OF-LINE COMMENT

// constant variables and must be a global variable
const val MYFIRSTCONSTANT = "HOLA"
fun main(){


    /* variables
        val to declare variables that are assigned a value only once. These are immutable, can't be reassigned a different value after initialization
        var to declare variables that can be reassigned. There are mutable variables, and you can change their values after initialization
     */
    val x : Int = 5
    //5

    var xx : Int = 5
    xx++

    // You can omit the type  after the variable name
    //Declares the variable x with the value
    val xxx = 8



    // Primitive data types are

    val integer: Byte = 127
    val short: Short = 32767
    val int: Int = 2147483647
    val long: Long = 9223372036854775807

    val float: Float = 4.4f
    val double: Double = 4.4

    val char: Char = '1'

    val boolean:  Boolean = true

    val string : String = "Apanialo pepe"


    print("!Hola, KOTLIN!")


}
