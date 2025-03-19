/*
EJERCICIO:
 - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
 - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
 - Crea una variable (y una constante si el lenguaje lo soporta).
 - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

// La web oficial de JavaScript es https://developer.mozilla.org/es/docs/Web/JavaScript

// Esta es la sintaxis apara generar comentarios en javaScript:

// Comentario en una línea

/* Esto es un comentario
de varias lineas*/

// Esta es la sintaxis para crear variables:

let my_variable = "Snake case"
let soyUnaVariable = "Lower Camel Case"
let SoyOtraVariable = "Upper Camel Case"

/*Se suele usar Upper Camel Case en los nombres de las clases y archivos. 
Lower Camel Case en los nombres de las variables o métodos.*/

// Esta es la forma de crear constantes:
const PI = 3.14159265359

// Estos son los diferentes tipos de datos primitivos en javaScript:
let myString = "Soy un String" // Type String
let myNumber = 42.622 // Type Number
let myBigInt = BigInt("123456789012345678901234567890") // type BigInt
let myBool = true // Type boolean
let myUndefined = undefined // Type Undefined
let mySymbol = Symbol //Type Symbol
let myNull = null // Type Null

console.log("Hola! JavaScript.")
console.log(myString)
console.log(typeof myNull)