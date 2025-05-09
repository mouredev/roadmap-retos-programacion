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

// EJERCICIOS

// - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
// El lenguaje escogido es Typescript  y la URL del sitio web oficial es https://www.typescriptlang.org/

// - Representa las diferentes sintaxis que existen de crear comentarios
// Podemos crear 2 tipos de comentarios: 
// 1. Comentario de una linea: 
// Comentario de una linea
// 2. Comentarios de varias lineas:
/* Esto es un comentario
de varias lineas */

// - Crea una variable (y una constante si el lenguaje lo soporta).
let isNumber: number = 2;
var isString: string = 'Hola';
const isBoolean: boolean = true;

// - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
let isNumDec: number = 4
let isNumHex: number = 0xf00d;
let isNumBinary: number = 0b1010;
let isNumOctal: number = 0o744
let isStr: string = 'Hola'
let isBool1: boolean = true
let isBool2: boolean = false
let isUnd: undefined = undefined
let isNull: null = null
let isSymbol: symbol = Symbol('a')

// - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
console.log('¡Hola, Typescript!')