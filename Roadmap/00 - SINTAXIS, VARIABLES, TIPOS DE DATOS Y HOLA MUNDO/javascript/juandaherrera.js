/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!
*/

// Página principal de JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript

// Comentario de una línea

/*
Comentario
de varias líneas
*/

let myVariable = "Juan David"; // Esta es una variable que puede cambiar
myVariable = "Juan David Herrera";

const MY_CONSTANT = "API_KEY"; // Esta es una constante que no puede cambiar

let myInt = 25; // Número entero
let myFloat = 1.33; // Número con punto flotante
let myBool = true; // Booleano
let myString = "Mi cadena de texto"; // Cadena de texto
let myOtherString = 'Mi otra cadena de texto'; // Otra forma de representar cadenas de texto
let myLanguage = "JavaScript"; // Nombre del lenguaje

console.log(`¡Hola, ${myLanguage}!`); // Imprime un saludo personalizado

console.log(typeof myInt); // Imprime el tipo de la variable myInt
console.log(typeof myFloat); // Imprime el tipo de la variable myFloat
console.log(typeof myBool); // Imprime el tipo de la variable myBool
console.log(typeof myString); // Imprime el tipo de la variable myString
