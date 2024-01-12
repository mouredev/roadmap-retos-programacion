//Al igual que la mayoría de los lenguajes modernos, Kotlin admite comentarios de una sola línea (o fin de línea ) y de varias líneas ( bloque ).

//Comentario en una sola linea

/* Comentario en bloque o de varias lineas
        URL Sitio oficila Kotlin
        https://kotlinlang.org/
*/

//Los comentarios de bloque en Kotlin se pueden anidar.

/*Comentario inicia aqui
/*Contine un comentario anidado*/
y el comentario finaliza aqui! */

//*********** VARIABLES **********
var variable
val constante

//Enteros
var entero_AI: Int = 5 // asignación inmediata
var entero_Inf = 5 // se infiere el tipo "Int"
var entero_Sin_Inicializar: Int  //Tipo requerido cuando no tiene inicialización
entero_Sin_Inicializar = 5 // asignación diferida

var enteroLargo: Long = 3000000000

//Decimales
val pi = 3.14 //Double

//Para especificar explícitamente el Floattipo de un valor, agregue el sufijo fo F. Si dicho valor contiene más de 6 o 7 dígitos decimales, se redondeará: Float, actual value is 2.7182817
val float = 2.7182818284f

//Booleanos
val myTrue: Boolean = true
val myFalse: Boolean = false
val boolNull: Boolean? = null

//Char / Caracteres
val aChar: Char = 'a'

//Cadenas de Texto
val str = "abcd 123"

//Matrices
var riversArray = arrayOf("Nile", "Amazon", "Yangtze")
riversArray += "Mississipi" //Lo que hace es adicionar un valor mas a la matriz

fun main(){
    println("¡Hola, Kotlin!")
}
