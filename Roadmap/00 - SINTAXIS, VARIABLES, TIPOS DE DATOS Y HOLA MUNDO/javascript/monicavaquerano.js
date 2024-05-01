// 00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
// Monica Vaquerano
// https://monicavaquerano.dev

/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

// https://developer.mozilla.org/en-US/docs/Web/javascript

// One-line comments

/* 
More
than
one
line
comments 
*/

var variable = "soy una variable";
let variable2 = "soy una variable tambien";
const constante = "soy una constante";

// Strings
let str = "JavaScript";
// Numbers
let int = 1;
let float = 1.5;
let biggy = BigInt("123456789012345678901234567890");
// Booleans
let x = true;
let y = false;
// Object
let person = { name: "Monica", lastname: "Vaquerano" }
// Date
const today = new Date();
// Null
let nulo = null;
// Undefined
let indefinido = undefined;
// Arrays
let cars = ["Saab", "Volvo", "BMW"];

console.log(`¡Hola, ${str}!`)