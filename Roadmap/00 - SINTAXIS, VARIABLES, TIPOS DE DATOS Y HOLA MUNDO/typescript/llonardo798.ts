// 1. URL del sitio web oficial de TypeScript: https://www.typescriptlang.org/

// 2. Tipos de comentarios en TypeScript:

// Comentario de una línea

/*
  Comentario de varias líneas
*/

/**
 * Comentario de documentación (JSDoc)
 * @param {string} nameDoc - Nombre de la persona
 * @returns {string} Saludo
 * @example greet('Luis') // => '¡Hola, Leonardo!'
 */

// 3. Creación de variables y constantes:

const EDAD: number = 25;
let variables: string = "Leonardo";

// 4. Tipos de datos primitivos:

let nombre: string = 'Leonardo Aedo'; // Cadena de texto (string),  con comillas simples, dobles o backticks (``)
let edad: number = 25; // Número entero (number)
let todoOk: boolean = true; // Booleano (boolean) con valores true o false
let nulo: null = null; // Valor nulo (null)
let indefinido: undefined = undefined; // Valor indefinido (undefined)
let simbolo: symbol = Symbol('Simbolo'); // Valor único (symbol) e inmutable
let numeroGrande: bigint = 9007199254740991n; // Número entero grande (bigint)
let cualquierCosa: any = 'Hola'; // Cualquier tipo de dato (any)
cualquierCosa = 25; // Se puede cambiar el tipo de dato

// 5. Imprimir en consola;

console.log(`¡Hola, TypeScript!`);

