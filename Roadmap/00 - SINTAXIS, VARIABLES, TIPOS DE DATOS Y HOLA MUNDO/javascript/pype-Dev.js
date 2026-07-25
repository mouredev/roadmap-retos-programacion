// https://developer.mozilla.org/es/docs/Web/JavaScript

// Esto es un comentario breve en una sola línea código

/*
Este es un bloque de comentario o un comentario de varias lineas.
Aunque JavaScrip no cuente con un sitio oficial como si lo hacen otros lenguajes, contamos con tres referencias bastante grandes y muy útiles:
1. Estandar internacional ECMAScript: https://ecma-international.org/
2. Documentación más completa y autorizada utilizada por desarrolladores: https://developer.mozilla.org/es/docs/Web/JavaScript
3. Iniciativa impulsada por Google para mejorar las prácticas de programación: https://web.dev/javascript?hl=es-419
*/

/**
 * Aunque la sintaxis con el comentario en bloque es muy similar, esto es más que un comentario.
 * JSDoc es un lenguaje de marcado para documentar el código escrito en JS, permitiendo a los
 * desarrolladores destacar funciones, algoritmos, clases, etc.
 * 
 * NOTA: La información presente en este bloque es más poderosa y se puede integrar con otros ambientes.
 */


// Declarar varialbes en js
var name = "Felipe" //sentencia que dejo de ser utilizada tras la llegada de ES6

let edad = 23;
edad = 30;

// Declarar variables en js
const PI = 3.1416;

// Tipos de datos primitivos
let $precio = 100000; //number
let ciudad = "Bogotá"; //string
let esMayor = true; //boolean
let x; //undefined
let resultado = null; //null
const idUnico = Symbol("MySymbol"); //symbol
const numGrande = 4561654894516548974841515n; //BigInt

// Imprimir mensaje
let message = "JavaScript";
console.log(`¡Hola, ${message}!`)