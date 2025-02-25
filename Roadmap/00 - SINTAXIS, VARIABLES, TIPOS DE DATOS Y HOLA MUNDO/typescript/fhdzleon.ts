/* * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

/* 
Visita el sitio oficial de typescript: 
https://www.typescriptlang.org/
*/

// Comentario de una sola linea

/*  
Comentario
multilineas
*/

let edad: number = 45;
const nombre: string = "skulldev";

let string: string = "Esta es una cadena de texto";
let number: number = 0;
let bool: boolean = true;
let myArray: string[] = ["soy", "un", "array"];
let myObject: object = {};

let sayHello: () => void = () => console.log("hola typescript");

sayHello();
