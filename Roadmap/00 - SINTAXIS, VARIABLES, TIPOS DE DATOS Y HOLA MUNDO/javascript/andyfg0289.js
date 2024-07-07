/* 
EJERCICIO:
 * 1- Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * 2- Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * 3- Crea una variable (y una constante si el lenguaje lo soporta).
 * 4- Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * 5- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *  */

//  1- Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

// https://www.javascript.com/

//___________________________//

// 2- Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

// Comentario en una sola linea

/* 
Comentario de 
multiples lineas
*/

//___________________________//

// 3- Crea una variable (y una constante si el lenguaje lo soporta).

let edad = 35;

const nombre = "andy";

//___________________________//

//4- Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

// 1) Number

let entero = 12;
let flotante = 5.14;

// 2) String

let objeto = "carro";
let color = 'rojo';
let plantilla = `El ${objeto} es ${color}`;
console.log(plantilla); // El carro es rojo

// 3) Boolean

let verdadero = true;
let falso = false;

// 4) Undefined

let fruta; 

console.log(fruta)//undefined

// 5) Null

let nulo = null;

//6) Symbol 

let simbolo = Symbol('datos');

// 7) BigInt

let bigboy = BigInt(345234623563245623562362346234652354623546);

let bigGirl = 5234562346234623456234562345623465234n;

// 5 - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

console.log("!hola, JavaScript");