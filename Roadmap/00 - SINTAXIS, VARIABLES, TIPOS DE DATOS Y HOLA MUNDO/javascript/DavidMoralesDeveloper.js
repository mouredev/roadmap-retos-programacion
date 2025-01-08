/*   EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" */
// 1
//  Mi primer comentario despues de el ejercicio "https://developer.mozilla.org/es/docs/Web/JavaScript"

// 2
//  comentario en una sola linea
/*  comentario de mas lineas
linea 1 */

// 3
const constante = 'soy una constante'
let variable = 'soy una variable'

// 4

const string  = 'soy un string'
const number = 5 //'soy un numero entero o decimal'
number = number(1) //1
const numberEntero = 123n  //BigInt numeros muy grandes enteros
number = BigInt(number) // 5n
const booleanos = true //false
let sym2 = Symbol("foo") //symbol
let sym = new Symbol(); // TypeError
//extras
const nada = null // null
const noencontrado = undefined //undefined

//5
console.log("¡Hola, Javascript!")