//https://kotlinlang.org/

//comentario de una línea

/*comentario
en
varias
líneas*/

fun main() {
    //constante
    val CONSTANTE = 2

    //variable
    var variable = 3

    //tipos de variables
    var byteVar :Byte = 20
    var shortVar :Short = 20
    var intVar :Int = 20
    var longVar :Long = 20
    var floatVar :Float = 2.2f
    var doubleVar :Double = 0.3
    var charVar :Char = 'Y'
    var booleanVar :Boolean = true

    var bitmapLocation = 0b00100001 // Literal binario 0b ó 0B   33
    var chestColor = 0xCCC // Literal hexadecimal 0x ó 0X   3276

    // Literales reales
    var exp1 = 3.211e2  //321.1
    var exp2 = .0001e10 // 1000000.0
    var exp3 = 48e5 //4800000.0
    var exp4 = 10e-4 //0.001

    //Caracteres de escape
    /**
    \t: Tabulación
    \b: Retroceso
    \r: Retorno de carro
    \n: Salto de línea
    \': Apostrofe
    \": Comilla doble
    \\: Backslash
    \$: Símbolo de dólar
    \u+XXXX: Símbolo Unicode con 4 dígitos hexadecimales

     */

    //mensaje por consola
    println("¡Hola, Kotlin!")

}