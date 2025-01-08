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

/* 00- Sintaxis, variables, tipo de datos, hola mundo */

//------------------------------------------------------------------------------------------

// Comentarios
/* https://developer.mozilla.org/es/docs/Web/JavaScript */

// variables
var variable1 = "variable";
let lenguaje = 'JavaScript';
const texto = 'constante';

// datos primitivos

const string = 'string';
const number = 10;
const bigInt = 65654654654654654n;
const boolean = true;
const symbol = Symbol('numero');
let indefinido;

console.log(`
    La variable es tipo: ${typeof string} \n
    La variable es tipo: ${typeof number} \n
    La variable es tipo: ${typeof bigInt} \n
    La variable es tipo: ${typeof boolean} \n
    La variable es tipo: ${typeof symbol} \n
    La variable es tipo: ${typeof indefinido}
`);

// Hola mundo
console.log(`Hola, ${lenguaje}!`);