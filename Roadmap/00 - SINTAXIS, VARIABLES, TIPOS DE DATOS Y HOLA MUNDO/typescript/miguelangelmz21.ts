// https://www.typescriptlang.org/docs

// Comentario en una línea

/*
Comentario en varias líneas 
EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

// Crea una variable (y una constante si el lenguaje lo soporta).
let myVariable: string = "Mi variable";
myVariable = "He cambiado el valor de mi variable";
const myConstant: string = "Mi constante";
// myConstant = "He cambiado el valor de mi constante"; // Esto dará un error porque las constantes no se pueden reasignar

// Crea variables representando todos los tipos de datos primitivos
let myString: string = "Hola, TypeScript"; // Cadena de texto
let myNumber: number = 42; // Número (puede ser entero o decimal)
let myBoolean: boolean = true; // Booleano
let myUndefined: undefined; // Indefinido
let myNull: null = null; // Nulo
let mySymbol: symbol = Symbol("miSimbolo"); // Símbolo
let myBigInt: bigint = BigInt(9007199254740991n); // BigInt
// Imprime por terminal el texto
console.log(`¡Hola, TypeScript!`);