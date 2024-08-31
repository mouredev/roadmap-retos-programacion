
// https://developer.mozilla.org/es/docs/Web/JavaScript

/*
Otra forma de hacerlo es así que nos permite escribir en varias líneas
*/

//Las variables pueden cambiar de valor
var variableVar; //Variable de alcance global
let variableLet; //Variable de alcance de bloque
//Las constantes no pueden cambiar de valor, se deben inicializar cuando se declaran
const constantePi = 3.14;

//Number
let numberExample = 1;
//String
let stringExample = "¡Hola, Javascript!"
//Boolean
let booleanExample = false;
//Null, asigna un espacio vacío en memoria
let nullExample = null;
//Undefined, no está asignada a ninguna parte de la memoria
let undefinedExample = undefined;
//BigInt para números muy grandes
let bigIntExample = 1234567890987654321n;
// Symbol cuyas instancias son unicas e inmutables
let symbolExample = Symbol("SYMBOL");

console.log(stringExample);