/* Sitio oficial: Mozilla Developer Network (MDN) | URL: https://developer.mozilla.org/es/docs/Web/JavaScript */

/* Este es un comentario de una linea */

/*  
    Este es 
    un comentario 
    de varias lineas 
*/

var var1 = 1; /* tienen alcance de función o alcance global, se pueden volver a declarar */
let var2 = 2; /* tienen alcance de bloque, no se pueden volver a declarar dentro del mismo bloque */
const var3 = 3; /* también tienen alcance de bloque, no pueden ser reasignadas a un nuevo valor */

let nombre = "Juan";              // String
let edad = 25;                    // Number
let precio = 19.99;               // Number (flotante)
let numeroGrande = 9007199254740991n; // BigInt
let esMayorDeEdad = true;         // Boolean
let esEstudiante = false;         // Boolean
let noDefinido;                   // undefined
let valorNulo = null;             // null
let simbolo = Symbol('descripcion'); // Symbol

console.log('¡Hola, JavaScript!'); //Imprime por terminal