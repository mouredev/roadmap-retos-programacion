/*
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


// https://developer.mozilla.org/en-US/docs/Web/JavaScript

// Comment in one line

/**
 * comment
 * in
 * block
 */


const constant = 'This is a constant'

let variable = 'This is a variable'

var globalVariable= 'This is a global variable'


// 7 PRIMITIVE TYPES:

// 1 - String
let string = 'This is a string'

// 2 - Number   
let number = 10
let float = 10.5

// 3 - BigInt
let bigInt = BigInt(9007199254740991) // 9007199254740991n

// 4 - Boolean
let boolean = true

// 5 - Undefined
let undefinedVariable

// 6 - Symbol
let symbol = Symbol('This is a symbol')

// 7 - Null
let nullVariable = null


// Print in terminal:
console.log("¡Hola, JavaScript!")