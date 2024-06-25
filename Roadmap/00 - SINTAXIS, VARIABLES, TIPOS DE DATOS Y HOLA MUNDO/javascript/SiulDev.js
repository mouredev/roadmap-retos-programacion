// URL de la pagina oficial:
// https://developer.mozilla.org/es/docs/Web/JavaScript

// --------------------------------------------------------------------------------------------------------
// TIPOS DE COMENTARIOS EN JAVASCRIPT:

// Comentario de una linea en JavaScript.

/* 
Esto tambien es un comentario
pero de varias lineas
en JavaScript .
*/

/**
 * Esto de aqui
 * tambien es un comentario
 * de varias lineas
 * en JavaScript
 * pero con asteriscos
 * para hacerlo mas "legible".
 */

// --------------------------------------------------------------------------------------------------------
// TIPOS DE VARIABLES EN JAVASCRIPT:

var helloWorld ;            // variable con scope global, que puede ser re-declarada y modificada (uso NO recomendado).
let userMessage;            // variable con scope limitado a un bloque de codigo y puede ser modificada (uso recomendado).
const USER_PASSWORD = 123;  // Variable Constante en JavaScript que no puede ser modificada.

// para las variables se usa calmeCase y para las Constantes se usa UPPER_SNAKE_CASE como tecnica de Naming en javaScript.

// --------------------------------------------------------------------------------------------------------
// TIPOS DE DATOS PRIMITIVOS

let myBolean = true;          // Bolean     -> El tipo boolean tiene sólo dos valores posibles: true y false.
let myString = 'hello world'; // String     -> cadena de texto donde se usan '' o "" para el string.
let myNumber = 123;           // Number     -> El tipo number representa tanto números enteros como de punto flotante.
let myBigInt = 32983192898n;  // BigInt     -> Para representar enteros de longitud arbitraria, se usa "n" para identificar que es BingInt.
let myNull = null;            // Null       -> Para valores desconocidos – un tipo independiente que tiene un solo valor nulo.
let myUndefined;              // Undefined  -> Para valores no definidos o "no asignados aun".
let mySymbol = Symbol("id");  // Symbol     -> Los Symbols se utilizan a menudo para añadir claves de propiedades únicas.

// --------------------------------------------------------------------------------------------------------
// IMPRIMIENDO UN SALUDO CON EL LENGUAJE DE PROGRAMACION USADO

console.log("¡Hola, JavaScript!"); //se reflejara en la terminal el saludo!.