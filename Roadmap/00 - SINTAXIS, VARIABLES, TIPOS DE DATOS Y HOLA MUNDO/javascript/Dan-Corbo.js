/* 
* EJERCICIO:
* 1- Crea un comentario en el código y coloca la URL del sitio web oficial del
* lenguaje de programación que has seleccionado.
* 2- Representa las diferentes sintaxis que existen de crear comentarios en el
* lenguaje (en una línea, varias...).
* 3- Crea una variable (y una constante si el lenguaje lo soporta).
* 4- Crea variables representando todos los tipos de datos primitivos del
* lenguaje (cadenas de texto, enteros, booleanos...).
* 5- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" 
*/


/* Soluciones */

/* 1 */

// La pagina oficial de Javascript es: https://developer.mozilla.org/es/docs/Web/JavaScript

/* 2 */

//  Esta es la sintaxis para un comentario en una linea

/* esta es 
la sintaxis 
para un comentario 
en varias lineas 
*/

/* 3 */

let variable = "Esta es una variable local";

var variable1 = "Esta es una variable global";

const constante = "Esta es una constante";

/* 4 */

let cadenaDeTexto = "Esta es una cadena de texto o string";

let enteros = 24;

let decimales = 2.5;

let BigInt = 123456789012345678901234567890n;

let booleanos = true > false;

let Nulo = null;

let indefinido = undefined;

let valorNaN = NaN;

let Symbol = Symbol('mi Simbolo');

let arreglos = ['Daniel', 24, 'Uruguay', 1];

let objetos = new Date("2024-01-06");

/* 5 */

console.log("¡Hola, JavaScript!");