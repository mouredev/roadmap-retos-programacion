//Documentación: https://developer.mozilla.org/es/docs/Web/JavaScript

// Comentario en una línea 

/*
  Comentario 
  en 
  varias 
  líneas
*/

// Variables 

// Declara una variable, opcionalmente la inicia a un valor
var variable

// Declara una variable local con ámbito de bloque, opcionalmente la inicia a un valor.
let local

// Declara un nombre de constante de solo lectura, ámbito de bloque y tiene que inicializarse 
const CONSTANTE = Math.PI

// Los tipos de datos primitivos

// String -> Cadena de texto
const string = "Hola mundo"
const simple = 'Hola mundo'
const especial = `Hola mundo`

// Number 
const number = 123
const decimales = 1.5
const scientificNotation = 25e105

// BigInt -> es un tipo de dato introducido en JavaScript para representar números enteros de tamaño arbitrario. 
// Es útil para realizar operaciones matemáticas con números que superen los límites máximos y mínimos permitidos por JavaScript
// Para crearlo se añade un "n" al final 
const bigInt = 123n
const numeroNormal = 9000000000000000000111     // -> 9e+21 perdemos valor 
const numeroBigInt = 9000000000000000000111n   // -> No pierde valor 9000000000000000000111n

//Boolean 
let boolean = true
boolean = false

//Undefined -> indica que una variable no tiene un valor asignado
let sinValor  

//Symbol -> Identificadores que son únicos 
const sym1 = Symbol()

//Null -> indica que una variable tiene un valor nulo
const nulo = null

console.log("Hola JavaScript",scientificNotation)