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



// Especificacion oficial de Javascript: https://ecma-international.org
// Documentación más ocupada: https://developer.mozilla.org/es/docs/Web/JavaScript

// Javascript

// Doble diagonal para comentarios de una sola linea

/*
  Diagonal y asterisco para encerrar comentarios de bloque de varias lineas
*/

// --------------------------------
// Creación de variable
// Existen 3 formas, var y let, sin embargo, actualmente la que se recomienda usar es let
var variableConVar = 'Soy una variable con var'
let variableConLet = 'Soy una variable con let'


// --------------------------------
// Creación de constantes
const pi = 3.1416
// Se pueden declarar variasa constantes en una sola linea separando cada una con una coma «,»
const name = 'conrado', apellido = 'Gonzalez'

// --------------------------------
// Datos primitivos
// Existen 6 tipos de datos primitivos en Javascript
const string = 'Soy un string'
const number = 20
const booleanTrue = true
const booleanFalse = false
const nullData = null
const undefinedData = undefined
const symbolData = Symbol('Soy un symbolo')

// --------------------------------
// Imprimiendo por terminal

console.log('Hola, Javascript');