// ╔═══════════════════════════════════════╗
// ║ Autor:  maguzdev                      ║
// ║ GitHub: https://github.com/maguzdev   ║
// ║ 2026 -  JavaScript                    ║
// ╚═══════════════════════════════════════╝

// -----------------------------------------------------
// 00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
// -----------------------------------------------------

// SOLUCIONES DE EJERCICIO:

// 1. Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

/**
 * URL del sitio web oficial del lenguaje de programación JavaScript.
 * https://developer.mozilla.org/es/docs/Web/JavaScript
 */

// 2. Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

// Esto es un comentario de una línea

/* 
* Esto es
* un comentario
* de varias líneas
*/

// 3. Crea una variable (y una constante si el lenguaje lo soporta).
const name = "Manuel"
const language = "JavaScript"
let age = 38;

// 4. Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

// Hay 7 tipos de datos primitivos:

// - Cadenas de texto (string):
let textStrings = "Retos de Programación";

// - Números enteros o flotantes (number):
let numbersIntegers = 87;
let numbersFloats = 87.5;

// - Booleanos lógicos (boolean):
let booleansTrue = true; // verdadero
let booleansFalse = false; // falso

// - Indefinidos o sin valor asignado (undefined):
let undefinedValues = undefined;

// - Nulos o ausentes de valor (null):
let nullValues = null;

// - Símbolos únicos e inmutables (symbol):
let uniqueSymbols = Symbol("symbol");

// - Números enteros muy grandes y precisos (bigInt):
let bigNumbers = 9007199254740992n;

// 5. Imprime por terminal el texto: "¡Hola, [y el nombre del lenguaje]!"
console.log(`¡Hola, ${language}!`)