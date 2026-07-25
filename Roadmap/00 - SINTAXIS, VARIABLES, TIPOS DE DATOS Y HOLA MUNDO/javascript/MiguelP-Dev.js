// URL del estandar de JavaScript
// https://tc39.es/ecma262/

// URL oficial de JavaScript
// https://developer.mozilla.org/es/docs/Web/JavaScript

// Comentario en una linea

/* Comentario
    en varias  
    lineas
*/

/* Variable Es el nombre que se le da a un pequeño compartimento en memoria.
Su nombre nos dice que está sujeta a cambios de su valor a en diferentes puntos del programa
la estructura de las variables es la siguiente:
    - Un nombre: para identificarlas
    - Un signo de igual: para asignarles un valor
    - Un valor: para darle un valor a la variable
    - Un tipo de dato: para saber el tipo de dato que tiene la variable */
let miVariable = 1;

// Constantes son variables que no puenden cambiar su valor.
const miConstante = 3.15;

// NOTAS: 
// En javascript los nombres de las variables se escriben en camelCase.
// Al finalizar la declararión de una línea de código se debe colocar un punto y coma (;).

// Tipos de datos

// Number
let myInt = 10;

let myFloat = 3.14;

// Boolean 
let x = true;
let y = false;

// Null
let myNull = null;

// Undefined
let myUndefined = undefined;

// BigInt
let myBigInt = 1234567890123456789012345678901234567890n;

// Symbol
let mySymbol = Symbol("foo");

// Object:
let person = {firstName:"John", lastName:"Doe"};

// Array object:
let cars = ["Saab", "Volvo", "BMW"];

// Date object:
let date = new Date("2022-03-25");

// Salida por consola
console.log("¡Hola, JavaScript!");
