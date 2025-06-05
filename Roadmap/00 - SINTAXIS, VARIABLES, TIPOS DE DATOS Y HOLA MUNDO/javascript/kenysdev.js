/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
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

// https://www.ecma-international.org/publications-and-standards/standards/ecma-262/
// https://developer.mozilla.org/es/docs/Web/JavaScript

/**
 * Documentación
 * @param {string} name - Usuario
 * @returns {string} Un saludo.
 */
function hello(name) {
    return `Hola, ${name}!`;
}

let x = 5           // Variable numérica.
const PI = 3.14159; // una constante.

// Tipos de datos primitivos (https://developer.mozilla.org/es/docs/Web/JavaScript/Data_structures#valores_primitivos).
let isAdult = true;    // Tipo Boolean
let emptyValue = null; // Tipo Null
let undefinedVariable; // Tipo Undefined
let price = 9.99;      // Tipo Number
let name = "Kenys";    // Tipo String
let hugeNumber = 9007199254740991n; // Tipo BigInt
let sym = Symbol("id"); // Tipo Symbol

console.log(typeof price);
console.log("¡Hola, JavaScript!");
