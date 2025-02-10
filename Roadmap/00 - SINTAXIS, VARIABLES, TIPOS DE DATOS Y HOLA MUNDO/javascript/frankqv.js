// 🌐 URL oficial del lenguaje de programación JavaScript (creado en 1995)
// 🦊 https://developer.mozilla.org/es/docs/Web/JavaScript 
// 📖 Especificación oficial de ECMAScript: https://262.ecma-international.org/14.0/
// (La base estándar para el desarrollo de JavaScript)


// 🧐 Sabías que...
// - Fue creado en ¡10 días! por Brendan Eich mientras trabajaba para Netscape.
// - Su nombre original era "Mocha", luego "LiveScript", antes de ser rebautizado como "JavaScript".
// - Aunque su nombre sugiere relación con Java, no tienen nada que ver (puro marketing).


// 📝 Comentario de una sola línea
console.log("Este es un ejemplo de comentario de una sola línea.");

/*
 * Comentario de varias líneas:
 * JavaScript puede usarse tanto en el navegador como en el servidor
 * (¡gracias a Node.js desde 2009!).
 * Su flexibilidad lo ha convertido en uno de los lenguajes más populares del mundo.
 */



// Declaración de una variable 
let variable = "el valor puede variar cuantas veces quiera";

// Declaración de una constante (su valor no cambia)
const CONSTANTE = "Valor inmutable";

// Declarando variables de todos los tipos de datos primitivos
let cadenaDeTexto = "Soy un texto"; // String
let numeroEntero = 42; // Number (entero)
let numeroDecimal = 3.14; // Number (decimal)
let booleano = true; // Boolean
let indefinido; // Undefined
let nulo = null; // Null
let simbolo = Symbol("simbolo"); // Symbol (ES6+)



// Imprimir por terminal el texto "¡Hola, JavaScript!"
console.log("¡Hellouw JavaScript!");

// Extra: Ejemplo de un objeto y un array (no son primitivos, pero son importantes)
let objeto = { clave: "valor" }; // Object
let arreglo = [1, 2, 3, "cuatro"]; // Array

// Mostramos todas las variables por consola
console.log("Variables de tipos primitivos:");
console.log("Cadena de texto:", cadenaDeTexto);
console.log("Número entero:", numeroEntero);
console.log("Número decimal:", numeroDecimal);
console.log("Booleano:", booleano);
console.log("Indefinido:", indefinido);
console.log("Nulo:", nulo);
console.log("Símbolo:", simbolo);

// Extra: Mostramos el objeto y el array
console.log("Objeto:", objeto);
console.log("Arreglo:", arreglo);
