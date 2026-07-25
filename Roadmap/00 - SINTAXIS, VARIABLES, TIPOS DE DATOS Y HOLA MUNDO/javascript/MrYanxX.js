// # #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
// > #### Dificultad: Fácil | Publicación: 26/12/23 | Corrección: 02/01/24

//  * EJERCICIO:
//  * - Crea un comentario en el código y coloca la URL del sitio web oficial del
//  *   lenguaje de programación que has seleccionado.
//  * - Representa las diferentes sintaxis que existen de crear comentarios
//  *   en el lenguaje (en una línea, varias...).
//  * - Crea una variable (y una constante si el lenguaje lo soporta).
//  * - Crea variables representando todos los tipos de datos primitivos
//  *   del lenguaje (cadenas de texto, enteros, booleanos...).
//  * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"


//1. 
// https://developer.mozilla.org/es/docs/Web/JavaScript


// Comentario de una linea
/*
Comentario de 
varias lineas
*/

// variables 
let variable = 0
const constante = 1

// Variables para cada tipo de dato
let number = 1
let bool = true
let string = 'string'
let undefined
let nullValue = null
let symbol = Symbol('ThisIsASymbol')
let bigInt = BigInt(821983619283712837721893791287398123791283791283)
let bigIntAlternative = 89176291837981273928631716319836981273912873273827329982n
let valueNaN = NaN

//Nota: NaN pertenece al grupo de datos primitivos number

console.log(typeof valueNaN);


//Console
console.log('Hola, Javascript');






