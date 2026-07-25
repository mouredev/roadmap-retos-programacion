/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

// URL del sitio oficial de JavaScript https://developer.mozilla.org/es/docs/Web/JavaScript

//Comentario de una linea

/*Comentario
de varias
lineas
*/

/**
 * Comentario par usar
 * con la documentacion automatica de JSDoc
 */

//Variable y constante
let nombre = "Manuel";
const nombreConst = "Manuel Constante";

//Variables con todos los tipos de datos primitivos
//String
let str1 = "Manolo";
//Number
let num1 = 100;
//bigInt
let bigInt1 = 1234567890123456789012345678901234567890n;
let bigInt2 = BigInt(651684734138461684341684634168434);
//Boolean
let bool1 = true;
//Null
let nul1 = null;
//Undefined
let und1;
//Symbol
let sym1 = Symbol("Manolo");

let nombreLenguaje = "JavaScript";
console.log("¡Hola, " + nombreLenguaje + "!");