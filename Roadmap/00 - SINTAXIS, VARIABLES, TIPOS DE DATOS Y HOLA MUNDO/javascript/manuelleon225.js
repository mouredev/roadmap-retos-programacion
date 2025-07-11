// Reto #00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
// Autor: manuelleon225
// Lenguaje: JavaScript
// Documentación: https://developer.mozilla.org/en-US/docs/Web/JavaScript

/* Comentarios largos
   permiten estar en varias líneas */
// Comentarios cortos de una sola línea

// VARIABLES
let a; // Declaramos variable sin valor (undefined)
let b = 0; // Declaramos variable con valor 0

console.log(a); // Muestra: undefined
console.log(b); // Muestra: 0

// CONSTANTES
const name = "Manuel";
console.log(name); // Muestra: Manuel

// TIPOS DE DATOS PRIMITIVOS
// Undefined
let undefinedVar; // undefined
console.log(undefinedVar); // Muestra: undefined

// Null
let nullVar = null; // null
console.log(nullVar); // Muestra: null

// String (Cadena, Texto o carácter)
let text = "Hola me llamo Manuel";
console.log(text); // Muestra: Hola me llamo Manuel

// Number (números enteros o decimales)
let number = 27;
console.log(number); // Muestra: 27
let number2 = 5.3;
console.log(number2); // Muestra: 5.3

// BigInt (número muy grande)
let bigNumber = 12345678901234567890n;
console.log(bigNumber); // Muestra: 12345678901234567890n

// Boolean (valor verdadero o falso)
const boolean = true;
console.log(boolean); // Muestra: true

// Symbol (valor único)
const symbol = Symbol("unique");
console.log(symbol); // Muestra: Symbol(unique)

// TIPOS DE DATOS NO PRIMITIVOS
// Objeto
let user = { name: "Manuel", edad: 30 };
console.log(user); // Muestra: { name: 'Manuel', edad: 30 }

// Array
let users = ["Jhoan", "Magdali", "Jose", "Doris"];
console.log(users); // Muestra: ['Jhoan', 'Magdali', 'Jose', 'Doris']

// Mensaje final
console.log("¡Hola, JavaScript!"); // Muestra: ¡Hola, JavaScript!