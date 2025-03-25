/* * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]! */

 // 1. https://developer.mozilla.org/en-US/docs/Web/JavaScript

 //2  Comentario de una linea
 /*
 Comentario 
 de varias lineas
 */

// 3. Crear una variable
let variable =  "variable";
// Variable constante
const pi = 3.14159;

// 4. Crear variables representando todos los tipos de datos primitivos.
let number = 10; // De tipo Number
let begint = 1234378938438478374 // De tipo Number grande
let undefined; //Es un tipo de datos indfinido
let nulo = null; // Es un tipo de dato Nulo
let string = "cadena"; // Es un tipo de dato cadena o llamado string
let booleano = true; // Es un tipo de dato bolleano solo puede tener 2 valores (True or False)
let simbol = Symbol('id_clave'); // Es un tipo de dato unico e inmutable

// Algunos otros tipos de datos no primitivos
let lista = [1,2,3]; // Es un tipo de dato Array
let listaClaveValor = {         // Es un tipo de dato Objeto
    clave1 : "valor1",
    clave2 : "valor2"
};

// 5. Imprimir "¡Hola, [y el nombre de tu lenguaje]!"
console.log("¡Hola, JavaScript!");