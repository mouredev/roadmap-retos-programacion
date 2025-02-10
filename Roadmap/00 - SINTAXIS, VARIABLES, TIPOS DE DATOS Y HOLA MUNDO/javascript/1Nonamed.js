// Documentación oficial de JavaScript : https://developer.mozilla.org/en-US/docs/Web/JavaScript

// Diferentes sintaxis para crear comentarios en JS

// Una línea: Comienza con '//' y sólo comenta la linea actual desde donde se escribe.

/* Múltiples líneas: Comentarios extensos. 
Comienzan por "/*" y comentará todo el texto que escribamos hasta que cerremos el comentario con un */

// Variables y Constantes
let name = 'Juan'
const ten = 10

// Datos primitivos
let lastname = 'López' // String
let age = 25 // Number
let isMale = true // Boolean
let address // Undefined
let stockAvailble = null // null
let myBigInt = 2343n // BigInt

let mySymbol = Symbol('unique') // Symbol
// Se utilizan para añadir llaves de propiedades únicas a un objeto que no sean iguales a las claves que cualquier otro código pueda añadir al objeto, y que están ocultas de otro código utilice normalmente para acceder al objeto. 

console.log("Hola, JavaScript")