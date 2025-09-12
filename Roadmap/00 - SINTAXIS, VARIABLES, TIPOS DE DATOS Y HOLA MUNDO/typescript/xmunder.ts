/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

//Pagina oficial de typescript: https://www.typescriptlang.org/

// Esto es un comentario de una sola línea

/*
    Esto es un
    Comentario de
    varias líneas  
*/

let lenguaje:string = "typescript";
const edad:number = 21;

//Tipos de datos primitivos en typescript

// String
let miCadena:string = "Hola mundo";
// Number
let miNumero:number = 21;
// Boolean
let miBooleano:boolean = true;
// Null
let miNulo:null = null;
// Undefined
let miIndefinido:undefined = undefined;
// Symbol
let miSimbolo:symbol = Symbol("Simbolo");
// BigInt
let miBigint:bigint = 12345678901234567890n;

console.log(`¡Hola, ${lenguaje}!`)
