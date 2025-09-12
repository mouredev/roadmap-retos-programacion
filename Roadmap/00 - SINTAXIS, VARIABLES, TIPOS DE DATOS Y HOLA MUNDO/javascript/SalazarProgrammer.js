/*
EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

// Sitio web oficial de JavaScript: https://developer.mozilla.org/es/docs/Web/JavaScript
// También puedes visitar: https://www.javascript.com/

/*
 * DIFERENTES SINTAXIS DE COMENTARIOS EN JAVASCRIPT:
 */

// Comentario de una línea

/*
    Comentario de múltiples líneas
    que puede abarcar varias líneas
    de código
*/

/**
 * Comentario de documentación JSDoc
 * @param {string} nombre - Descripción del parámetro
 * @returns {string} - Descripción del retorno
 */

// VARIABLES Y CONSTANTES
let variable = 'Soy una variable'; // Variable que puede cambiar
const constante = 'Soy una constante'; // Constante que no puede cambiar

// TIPOS DE DATOS PRIMITIVOS EN JAVASCRIPT
let cadenaTexto = 'Hola Mundo'; // String
let numeroEntero = 42; // Number (entero)
let numeroDecimal = 3.14; // Number (decimal)
let booleanoVerdadero = true; // Boolean
let booleanoFalso = false; // Boolean
let nulo = null; // Null
let indefinido = undefined; // Undefined
let simbolo = Symbol('miSimbolo'); // Symbol (ES6)
let bigInt = 9007199254740991n; // BigInt (ES2020)

// IMPRIMIR POR TERMINAL
console.log('¡Hola, JavaScript!');

// También puedes mostrar las variables
console.log('Cadena de texto:', cadenaTexto);
console.log('Número entero:', numeroEntero);
console.log('Booleano:', booleanoVerdadero);

// Ejemplo de uso de template strings (más moderno)
const lenguaje = 'JavaScript';
console.log(`¡Hola, ${lenguaje}!`); // Usando template literals

// Fin del programa
