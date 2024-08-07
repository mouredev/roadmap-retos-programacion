const val SecLastName = "Luyo"// la constantes "Const" se determinar en el tiempo de compilacion se usa como una variable global
fun main(){
//kotlin es un lenguaje de programacion moderno y con facil sintaxtis enfocado en reemplazar a java 
//creado por la empresa JetBrains
//Ademas de ser impulsado para uso en multiplitaforma y contar con todas las caracteristicas

//https://kotlinlang.org

//Tipos de comentarios
//comentarios de una sola linea
/*comentarios de multiples lineas
linea 1
linea 2
linea 3 */


//variables
var name = "Jhordan"

//constante
val lastName = "Luyo" // la constate val se determina en el tiempo de ejecucion


//Tipos de datos en kotlin

//datos numericos 
val byte:Byte = 127         //8 bits
val short:Short = 32767     //16 bit
val entero:Int = 233333     //32 bits
val long: Long = 12121212   //64 bits

//numericos con puntos flotantes
val float:Float = 12.4f         //Decimal de simple precisión
val double:Double = 23.233232   //Decimal de doble precisión

//cadenas y caracter
val cadena:String = "Cadena"  
val caracter: Char = 'C'

//dato booleano
val booleano:Boolean = true

//arrays
val array: Array = arrayOf(1,2,3)



print("¡Hola, kotlin!")
}
