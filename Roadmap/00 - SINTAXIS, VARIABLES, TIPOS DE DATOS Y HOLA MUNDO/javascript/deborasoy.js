// JavaScript - Sitio oficial: https://developer.mozilla.org/en-US/docs/Web/JavaScript

// comentario de una linea 
/* Representa las diferentes sintaxis que existen de crear comentarios
en el lenguaje (en una línea, varias...) */

//Crea una variable (y una constante si el lenguaje lo soporta).
let edadPersona = "25"; //variable
const  nombrePersona = "Débora"; //constante

//Crea variables representando todos los tipos de datos primitivos del lenguaje
/*
datos primitivos:
string, number, bigint, boolean, undefined y symbol
*/
let saludo = "ciao! come stai oggi?"; // tipo de dato : string (cadena de texto)
let añoActual = 2026; // tipo de dato : number (numeros enteros, decimales, binarios, ...)
let añosQueQuieroVivir = 9223372036854775807n; //tipo de dato : bigint 
let soltera = true; // tipo de dato: boolean ( con dos valores true o false) 
let fechaBoda; // tipo de dato : undefined ( la variable no tiene ningun valor asignado)

let fecha = new Date(2001,1,6);
let fechaNacimiento = Symbol(`Fecha de nacimiento`+` `+ fecha.toLocaleDateString()); // tipo de dato: symbol

// Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
console.log("¡Hola, JavaScript! I'm here");
