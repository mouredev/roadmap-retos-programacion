/* 
# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga

* EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" */


/* 
JavaScript
No tiene una página oficial como tal, pero su documentación se encuentra en ECMASCRIPT y MDN
- https://ecma-international.org/publications-and-standards/standards/ecma-262/
- https://developer.mozilla.org/es/docs/Web/JavaScript
*/

// Comentario de una línea

let myvar
const name = "Duban"

// Tipos de datos primitivos
let name2 = "Duban"
let age = 26
let isStudent = true
let graduated
let status = new String("Estudiante")
let sym = Symbol("id")

console.log(typeof name2) // string
console.log(typeof age) // number
console.log(typeof isStudent) // boolean
console.log(typeof graduated) // undefined
console.log(typeof status) // object
console.log(typeof sym) // symbol

const language = "JavaScript"

console.log(`Hello, ${language}`)