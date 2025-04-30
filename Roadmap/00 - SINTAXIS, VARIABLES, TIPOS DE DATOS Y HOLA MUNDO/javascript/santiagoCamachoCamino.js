// 00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
// Santiago Camacho Camino
// 2025-04-21

/**
 * Crea un comentario en el código y coloca la URL del  
 * sitio web oficial del lenguaje de programación que ha
 * seleccionado.
 */
//Documentación de JavaScript
//https://developer.mozilla.org/es/docs/Web/JavaScript

/** 
 * Representa las diferentes sintaxis que existen de 
 * crear comentariosen el lenguaje (en una línea, 
 * varias...).
*/
// Se puede hacer comentarios con // o con /* */
// -> '//' para una línea
/**
 * -> '/*' para varias líneas
 */

/**
 * Crea una variable (y una constante si el lenguaje lo soporta).
 */
let variable1="Esto es un String";

const constante1="Esto es una constante";

/**
 * Crea variables representando todos los tipos de datos 
 * primitivos del lenguaje (cadenas de texto, enteros, 
 * booleanos...).
 */

let numero=2; //number
let testo="Hola mundo"; //string
let verdadero=true; //boolean
let falso=false; //boolean  
let undef=undefined; //undefined
let noDefinido;
let nulo=null; //Null
let bigInt=BigInt(123456789012345678901234567890); //bigint
let symbol=Symbol("Esto es un symbol"); //symbol

/**
 * Imprime por terminal el texto: "¡Hola, [y el nombre de 
 * tu lenguaje]!"
 */
console.log("!Hola, Javascript!");

