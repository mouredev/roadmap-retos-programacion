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


// ! Ejercicio 1

// Sitio web JavaScript
// https://developer.mozilla.org/es/docs/Web/JavaScript

// ! Ejercicio 2

// Este es un comentario de una sola linea

/**
 * Este es un comentario de multiples lineas
 * ejemplo
 * Hola mundo :D
 */

// ! Ejercicio 3 Crea una variable (y una constante si el lenguaje lo soporta).



let saludoQuePuedeCambiar = 'Hola gente';
const SALUDOQUENOPUEDECAMBIAR = 'Hola';


// ! Ejercicio 4 - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

// ? String
let cadenaTexto = 'Esto es una cadena de texto';
console.log( typeof cadenaTexto ); // string


// ? Number
let miPrimerNumero = 10;
console.log( typeof miPrimerNumero ); // number


// ? Boolean
let estaCorriendo = true;
console.log( typeof estaCorriendo ); // boolean


// ? null
let soyunNull = null;
console.log( typeof soyunNull );

// ? undefined
let deportista;
console.log( typeof deportista ); // undefined

// ? bigint

let numero2 = 23n;
console.log( typeof numero2 ); // bigint


// ! Ejercicio 5 Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

console.log(`Hola mundo desde JavaScript!`);






