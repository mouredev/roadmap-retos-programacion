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

// Typescript: https://www.typescriptlang.org/
/* Typescript añade tipos estáticos y funciones avanzadas a javascript */
// Comentario de una línea
/* Comentario
	de
	múltiples
	líneas
*/

// A la hora de definir variables y asignarles un valor no es necesario indicar el tipo ya que typescript lo infiere automáticamente

// Tipos de datos más primitivos son los más simples y son la forma más primitiva de representar estos datos

let years = 23
const NAME = 'Axel'

let myString = 'My string variable'
let myNumber = 42
let myBoolean = true
let myUndefinedVariable
let myNullVariable = null
let mySymbol = Symbol('my description') // es un valor único e inmutable(no se puede modificar), se pueden utilizar para añadir claves únicas a objetos
let myBigInt = 2n // datos numéricos muy grandes que no pueden ser representados con Number

console.log(typeof myString)
console.log(typeof myNumber)
console.log(typeof myBoolean)
console.log(typeof myUndefinedVariable)
console.log(typeof myNullVariable) // 'object', esto es por un bug histórico (no se soluciona porque puede romper internet)
console.log(typeof mySymbol)
console.log(typeof myBigInt)
