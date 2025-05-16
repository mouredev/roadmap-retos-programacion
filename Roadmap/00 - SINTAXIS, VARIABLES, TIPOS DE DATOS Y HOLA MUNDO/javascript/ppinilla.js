//00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO

/*
 EJERCICIO:
 - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
 - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
 - Crea una variable (y una constante si el lenguaje lo soporta).
 - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

//- Sitio web oficial de JavaScript: https://developer.mozilla.org/es/docs/Web/JavaScript

//a one line comment

/* this is a longer, 
multi-line comment
*/

//- Declaraciones de variables:
//Declara una variable, opcionalmente la inicia a un valor.
var user = "ppinilla";

//Declara una variable local con ámbito de bloque, opcionalmente la inicia a un valor.
let age = 23;

//Declara un nombre de constante de solo lectura y ámbito de bloque
const PI = 3.14

// - Tipos de datos primitivos
let float = 1.5
let int = 10
let booleanoT = true
let booleanoF = false
let string = "JavaScript"
let n = null
let undf = undefined

// - Imprimir por terminal
console.log("¡Hola, JavaScript!");

console.log(typeof(float));
console.log(typeof(int));
console.log(typeof(booleanoT));
console.log(typeof(booleanoF));
console.log(typeof(string));
console.log(typeof(n));
console.log(typeof(undf));