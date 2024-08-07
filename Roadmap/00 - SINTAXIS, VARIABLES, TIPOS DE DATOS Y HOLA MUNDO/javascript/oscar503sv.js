// Web oficial de JavaScript
// https://developer.mozilla.org/es/docs/Web/JavaScript

// Ejemplo de comentario en una linea

/*
Ejemplo de comentario 
en varias lineas
*/

// Declarar variables (metodo no recomendado)
var variable1 = 'Hola';
// Declarar variables (metodo si recomendado)
let variable2 = 'Hola mundo..';
// Declarar constantes
const variable3 = 'Esto no se podra modificar despues';

// Tipos de Datos Primitivos
// -- String >>
let cadena = 'Cadena de texto de cualquier longitud';
// -- Number >>
let numero1 = 5;
let numero2 = 6.77;
// -- BitInt (numeros muy grandes) >>
let numeroGrande1 = 1234567890123456789012345n;
let numeroGrande2 = BigInt(1234567890123456789012345);
// -- Boolean >>
let booleano1 = true;
let booleano2 = false;
// -- Undefined >>
let noDefinido = undefined;
// -- Symbol >>
let simbolo = Symbol('algo');
// -- Null >>
let nulo = null;

// Imprimir mensajes usando la consola del lenguaje
console.log('¡Hola, JavaScript!');
// Imprimir mensajes usando texto y valor de variables
let lenguaje = 'JavaScript';
console.log(`¡Hola, ${lenguaje}!`);