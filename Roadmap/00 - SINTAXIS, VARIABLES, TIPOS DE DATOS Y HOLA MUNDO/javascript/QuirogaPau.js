// https://developer.mozilla.org/es/docs/Web/JavaScript
// Comentario de una linea
/* Comentario
de 
varias 
lineas */

// - Crea una variable (y una constante si el lenguaje lo soporta).

let variable;
const CONSTANTE = 3.14;

/* Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).*/

let string = "texto"; //Representa cadenas de textos.
let number = 10; //Representa numeros 
let booleano = false; //Representa un valor lógico y puede tener dos valores, ya sean true o false.
let BigInt = 1234567890123456789012345678901234567890n; //Representa valores numéricos que son demasiado grandes para ser representados por el tipo de dato number.
let valor = null; //Representa la ausencia intencional de cualquier valor, un valor nulo o «vacío»
let indefinido = undefined; // Representa una variable que no ha sido declarada o a la cual no se le ha asignado un valor.
let symbol = Symbol(); //El tipo symbol (símbolo) se utiliza para crear identificadores únicos para los objetos.

/* - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"*/
let javascript = "JavaScript";
console.log(`¡Hola, ${javascript}!`);