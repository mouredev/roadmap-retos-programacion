/*   EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" */

//comentario de una línea https://developer.mozilla.org/es/docs/Web/JavaScript

/* Comentarios en
varias lineas */

let variableQuePuedeCambiar = "este es un string que se puede modificar"; // let permite modificar el valor que se ha guardado
const variableQueNoPuedeModificarse = "variable que no se va a modificar"; // el valor de const no se puede modificar

//Tipos de datos primitivos en JS
let number = 13;
let string = "Javascript";
let boolean = true;
let variableNull = null;
let variableUndefined = undefined;
let array = ["pera", "manzanar", "limon"];
let objeto = { nombre: "David", edad: 34, pais: "Colombia" };

console.log("Hola", string);
