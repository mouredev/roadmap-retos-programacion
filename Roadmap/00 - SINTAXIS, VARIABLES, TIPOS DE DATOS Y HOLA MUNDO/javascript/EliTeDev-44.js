/*
_____________________________________
https://github.com/JDesing
2025 - JavaScript
___________________________________________________
00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
---------------------------------------------------
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

// Documentación:
// https://www.ecma-international.org/publications-and-standards/standards/ecma-262/
// https://developer.mozilla.org/es/docs/Web/JavaScript

// Comentario de una línea

/*
Comentario
de varias
líneas
*/
// _______________________
// Creando tipos de Variables y Constantes
let = miVariable = "JDesing" // Variable
const PI = 3.14159; // Constante

// _______________________
// Tipos de datos primitivos (https://developer.mozilla.org/es/docs/Web/JavaScript/Data_structures#valores_primitivos).
// Variables con datos Primitivos
let numero = 2025          // Tipo Number (número entero).
let decimal = 3.14         // Tipo Number (número decimal).
let miString = 'JDesing'   // Tipo String (cadena de texto).
let boleanoTrue = true     // Tipo Boolean (booleano).
let boleanoFalse = false   // Tipo Boolean (booleano).
let nulo = null            // Tipo Null (valor nulo).
let indefinido              // Tipo Undefined (variable no definida).
let numeroGrande = 1447999254740991n // Tipo BigInt (número entero grande).
let simbolo = Symbol("id") // Tipo Symbol (valor único e inmutable).

// Mostrando el tipo de dato de cada variable
console.log("===============================")
console.log("Tipos de datos primitivos:")
console.log(typeof numero)
console.log(typeof decimal)
console.log(typeof miString)
console.log(typeof boleanoTrue)
console.log(typeof boleanoFalse)
console.log(typeof nulo)
console.log(typeof indefinido)
console.log(typeof numeroGrande)
console.log(typeof simbolo)

// _______________________
// Imprimiendo en consola
console.log("¡Hola, JavaScript!")
