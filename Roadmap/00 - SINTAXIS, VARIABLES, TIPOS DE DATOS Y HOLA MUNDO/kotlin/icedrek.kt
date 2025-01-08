/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

// Sitio oficial: https://kotlinlang.org/

// Comentario de una linea con '//'

/*
 * Comentario de
 * varias lineas
 */

var a = 1  // tras el codigo tambien se pueden incluir comentarios

// VARIABLES
// las variables se escriben con letras minúsculas
// Para definir una variable se utiliza "var"
var variable = "hola"

// si el nombre de la variable es compuesto, se utiliza camelCase
var variableNombreCompuesto = "hola"

// también se puede definir el tipo de la variable
var variableTipo: String = "hola"


// En Kotlin se pueden definir las constantes de dos formas
// Mediante "val", se genera una variable de solo lectura
val variableInmutable = "hola"

// Mediante "const", se genera una constante. 
// Se utiliza cuando se conoce el valor de la constante de antemano
// Se escribe en mayusculas para diferenciarla
const val PI = 3.14

// TIPOS
val variableByte: Byte = 8 // Puede tomar valores entre -128 y 127
val variabteShort: Short = 16 // Puede tomar valores entre -32768 y 32767
val variableInt: Int = 32 // Puede tomar valores entre -2^31 y 2^31 - 1
val variableLong: Long = 64 // Puede tomar valores entre -2^63 y 2^63 - 1

val variableFloat: Float = 32.00f //Puede tener hasta 7 dígitos decimales
val variableDouble: Double = 64.00 //Puede tener hasta 16 dígitos decimales

val variableBoolean: Boolean = true //Puede tener valores 'true' o 'false'

val variableChar: Char = 'a' //Se definen con comilla simple para que no se interprete como String(de lo contrario dara error)
val variableString: String = "cadena de texto" // Se utiliza para almacenar cadenas alfanumericas

//para mostrar un valor por pantalla se utiliza la funcion println()
println("hola Python") 

// tambien podemos mostrar el valor de una variable
val lenguaje = "Kotlin"
println("hola ${lenguaje}")
