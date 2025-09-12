//# #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
//#### Dificultad: Fácil | Publicación: 26/12/23 | Corrección: 02/01/24

//## Ejercicio

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

//## Solución

//# Url del lenguaje  https://kotlinlang.org/ -> los comenterios simples empiezan por "//" Este es una línea de comentario.

/* 
Lo que es encuentre en medio de la barra asterisco y asterisco barra es un bloque de comenterio, 
puede ser de múltiples líneas. 
*/

var valorVariable: String = ""
val ValorConstante: Int = 10 // Kotlin permite declarar constantes con "val", val es inmutable, var es mutable.

// El tipado de datos en Kotlin es estático, se puede omitir el tipo y que lo infiera al darle el valor.
val booleano: Boolean = true // false
val entero: Int = 15
val decimal: Double = 1.2
val cadena: String = "Esto es una cadena"   

fun main() {
    println("¡Hola, Kotlin!")
}