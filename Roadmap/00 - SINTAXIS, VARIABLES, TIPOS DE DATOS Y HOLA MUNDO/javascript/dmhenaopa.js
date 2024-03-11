/**
 * 00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
*/

 /**
 * Esta es la URL del sitio web oficial de Javascript correspondiente a la
 * estandarización del lenguaje JavaScript: https://ecma-international.org/
 * Documentación de referencia MDN web docs: https://developer.mozilla.org/es/docs/Web/JavaScript
 */

 /**
  * Existen diferentes sintaxis para crear comentarios en JavaScript:
  * 1. Cuando el comentario es de una sola linea se utiliza // al inicio 
  *    del comentario
  * 2. Cuando el comentario es de varias lineas se utilizan // /**/

/**
 * Variables en JavaScript
 * 1. Con var: Desaconsejada actualmente por problemas con scope
 * 2. Con let: Forma aconsejada para declarar variables
 * 3. Con const: Esta es la forma utilizada para declarar constantes
 */
var varFormaDesaconsejada = 1;
let varFormaAconsejada = 'String';
const constante = [0, 1, 2];

/**
 * Datos primitivos: string, number, bigint, boolean, undefined y symbol
 */
let string = 'Este es un string';
let numero = 12345;
let bigint1 = 1234567890n; //Indicación de un bigint con una 'n' al final 
let bigint2 = BigInt(1234567890);
let booleano = true;
let varUndefined;
let simbolo = Symbol('Key'); //Cadena dentro de Symbol es opcional

/**
 * Funcion para imprimir saludo a lenguaje
 * @param { String } miLenguaje - Lenguaje de programación seleccionado
 */
let paraImprimir = ( miLenguaje ) => {
    console.log(`¡Hola, ${miLenguaje}!`);
};

paraImprimir('JavaScript');
