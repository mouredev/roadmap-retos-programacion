/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 * lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 * en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 * del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

// Sitio web oficial de JavaScript:
// https://developer.mozilla.org/es/docs/Web/JavaScript

// Comentario en una línea

/*
  Esto también es
  un comentario
  en varias líneas
*/

// Variable
let myVariable = "Mi variable";
myVariable = "Nuevo valor de mi variable";

// Constante (por convención y por sintaxis)
const MY_CONSTANT = "Mi constante"; // 'const' no se puede reasignar

// Tipos de datos primitivos
let myString = "Mi cadena de texto";
let myOtherString = 'Mi otra cadena de texto';
let myNumber = 10;
let myFloat = 10.5;
let myBooleanTrue = true;
let myBooleanFalse = false;
let myUndefined = undefined;
let myNull = null;
let myBigInt = 1234567890123456789012345678901234567890n; // Primitivo BigInt
let mySymbol = Symbol("mi-simbolo"); // Primitivo Symbol

// Impresión por terminal
// (En JavaScript, "terminal" es la "consola" del navegador o de Node.js)
console.log("¡Hola, JavaScript!");