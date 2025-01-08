// https://www.typescriptlang.org/es

// Este es un ejemplo de comentario de una linea.

/*
 Este es un ejemplo
 de comentario de
 multiples lineas
*/

// Declaración de variable y constante
let variable: string;
const LANG = "TypeScript"; // LANG es string por inferencia de tipo

// Hay 7 tipos de datos primitivos: string, number, bigint, boolean, undefined, symbol y null.
let my_string: string;
let my_number: number;
let my_bigint: bigint;
let my_boolean: boolean;
let my_undefined: undefined;
let my_symbol: symbol = Symbol("clave");
let my_null: null;

console.log(`¡Hola, ${LANG}!`);
