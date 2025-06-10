// JavaScript URL = https://developer.mozilla.org/es/docs/Web/JavaScript

// 2.- Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

// Este es un ejemplo de un comentario de una sola linea

/* 
Este es un ejemplo
de un comentario
en varias lineas
.
*/

// 3.- Crea una variable (y una constante si el lenguaje lo soporta)
let miNombre = "Miguel" // Esta es una variable "let", una variable let
const miSegundoNombre = "Angel" // Esta es una variable "const", una variable constante "const"

// Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
let Number = 24, number = 24.5 // Tipo de dato primitivo: Number
let String = "Miguel Angel" // Tipo de dato primitivo: String
let BooleanTrue = true // Tipo de dato primitivo: Boolean (true)
let BooleanFalse = false // Tipo de dato primitivo: Boolean (false)
let Undefined // Tipo de dato primitivo: Undefined (indefinido)
let Null = null // Tipo de dato primitivo: Null (nulo/ninguno)
let symbol = Symbol("Symbol") // Tipo de dato primitivo: Symbol
let bigintN = 123456789101112131415161718192021222324252627282930313233n // Tipo de dato primitivo: BigInt (numeros de enteros grande)
let bigint = BigInt(123456789101112131415161718192021222324252627282930) // Tipo de dato primitivo: BigInt (numeros de enteros grande)

console.log("Tipo de dato: " + typeof Number + ", Tipo de dato primitivo (Number): " + Number)
console.log("Tipo de dato: " + typeof Number + ", Tipo de dato primitivo (Number): " + number)
console.log("Tipo de dato: " + typeof String + ", Tipo de dato primitivo (String): " + String)
console.log("Tipo de dato: " + typeof BooleanTrue + ", Tipo de dato primitivo (Boolean): " + BooleanTrue)
console.log("Tipo de dato: " + typeof BooleanFalse + ", Tipo de dato primitivo (Boolean): " + BooleanFalse)
console.log("Tipo de dato: " + typeof Undefined + ", Tipo de dato primitivo (Undefined): " + Undefined)
console.log("Tipo de dato: " + typeof symbol + ", Tipo de dato primitivo (Symbol): ", symbol)
console.log("Tipo de dato: " + typeof bigintN + ", Tipo de dato primitivo (BigInt): " + bigintN)
console.log("Tipo de dato: " + typeof bigint + ", Tipo de dato primitivo (BigInt): " + bigint)
console.log("Tipo de dato: " + typeof Null + ", Tipo de dato primitivo: " + Null)

// Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
console.log("Hola [JavaScript]¡")
