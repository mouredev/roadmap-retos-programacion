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

// Página principal de JavaScript: https://developer.mozilla.org/es/docs/Learn_web_development/Core/Scripting/What_is_JavaScript

// Comentario de una línea

/*
Comentario
de varias líneas
*/

let name = "Juan Felipe"; // Esta es una variable que puede cambiar
var fullname = "Juan Felipe Zapata";

const MY_CONSTANT = "API_KEY"; // Esta es una constante que no puede cambiar

let int = 25; // Número entero
let float = 1.33; // Número con punto flotante
let bool = true; // Booleano
let string = "Mi cadena de texto"; // Cadena de texto
let otherString = 'Mi otra cadena de texto'; // Otra forma de representar cadenas de texto
let language = "JavaScript"; // Nombre del lenguaje

console.log(`¡Hola Mundo, Esto es ${language}!`); // Imprime un saludo personalizado

console.log(typeof int, int); // Imprime el tipo de la variable int
console.log(typeof float, float); // Imprime el tipo de la variable float
console.log(typeof bool, bool); // Imprime el tipo de la variable bool
console.log(typeof string, string); // Imprime el tipo de la variable string
