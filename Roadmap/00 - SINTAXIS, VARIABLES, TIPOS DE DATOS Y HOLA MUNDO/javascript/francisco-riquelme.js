// Este es el desarrollo del ejercicio 00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO


// Url del sitio de javascript: https://developer.mozilla.org/es/docs/Web/JavaScript

// Este es un comentario de una sola línea

/*
Este es un comentario de varias líneas
que sirve para poder explicar codigo, en este ejemplo
lo realizamos en el lenguaje de programación JavaScript
*/

// Declaración de variables
var nombre = "Francisco Riquelme"; // Variable de tipo string
var edad = 30; // Variable de tipo number
const PI = 3.1416; // Variable de tipo number constante

// Crear valoriables de tipos de datos primitivos 
var esProgramador = true; // Variable de tipo boolean
var fechaNacimiento = new Date(1993, 5, 15); // Variable de tipo Date
var simbolo = Symbol("simbolo"); // Variable de tipo Symbol
var valorNulo = null; // Variable de tipo null
var valorIndefinido; // Variable de tipo undefined
var nombreCompleto = `${nombre} Pérez`; // Variable de tipo string utilizando template literals
var numero = 42; // Variable de tipo number
var numeroGrande = BigInt(9007199254740991); // Variable de tipo BigInt

// Imprimir en consola
console.log("¡Hola Javascript!"); // Imprime un mensaje en la consola