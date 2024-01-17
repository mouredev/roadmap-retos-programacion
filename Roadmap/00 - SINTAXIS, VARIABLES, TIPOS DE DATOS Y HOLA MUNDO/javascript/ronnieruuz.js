//#00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

// *** JAVASCRIPT *** https://developer.mozilla.org/es/docs/Web/JavaScript

// *** CREAR COMENTARIOS *** https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Grammar_and_types#comentarios
// Este es un comentario de una linea

/* Este es un comentario
 * más largo, de varias líneas
 */

// *** DECLARAR VARIABLES *** https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Grammar_and_types#variables
var variableVar; // No se recomienda utilizar var para crear variables.
let variableLet;
const variableConst = "1"; //Siempre debe estar inicializada (asignar un valor)

// TIPOS DE DATOS PRIMITIVOS https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Grammar_and_types#tipos_de_datos
//https://developer.mozilla.org/es/docs/Learn/Getting_started_with_the_web/JavaScript_basics#variables
let booleano = true;
let string = 'Bob';
let number = 10;
let array = [1,'bob','Steve', 10];

// *** IMPRIMIR HOLA MUNDO *** https://developer.mozilla.org/es/docs/Learn/Getting_started_with_the_web/JavaScript_basics#ejemplo_%C2%AB%C2%A1hola_mundo!%C2%BB
// Para imprimir por consola es necesario instalar NodeJS (https://nodejs.org/en)
console.log("¡Hola, JavaScript!");