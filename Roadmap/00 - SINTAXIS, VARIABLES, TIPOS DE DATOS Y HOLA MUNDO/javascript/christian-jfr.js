// #00 - Sintaxis, Variables, Tipos de datos y Hola mundo.

/* 
1. Crea un comentario en el código y coloca la URL del sitio web oficial del 
lenguaje de programación que has seleccionado. 
*/

// https://developer.mozilla.org/en-US/docs/Web/JavaScript


/* 
2. Representa las diferentes sintaxis que existen de crear comentarios 
en el lenguaje (en una línea, varias...).
*/

// Comentario de una línea

/*
    Comentario 
    de 
    varias 
    lineas    
*/


/*
3. Crea una variable (y una constante si el lenguaje lo soporta).
*/

var variableVar = 1;
let variableLet = 2;
const constante = 3;


/*
4. Crea variables representando todos los tipos de datos primitivos 
del lenguaje (cadenas de texto, enteros, booleanos...).
*/

// String (cadenas de texto)
const nombre = 'Knives';
const mayor = "18";
const saludo = 'Hola mundo';
// Number (enteros y decimales)
const pi = 3.1416;
let edad = 18;
// BigInt
const numeroGrande = 1234567890123456789012345678901234567890n;
let numeroGrande2 = 10n;
// Boolean
const booleano = true;
let booleano2 = false;
// Null
const nulo = null;
// Undefined
const indefinido = undefined;
let myIndefinido;
// Symbol
let mySymbol = Symbol('clave');

/*
5. Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*/

console.log(`¡Hola, JavaScript!`)
