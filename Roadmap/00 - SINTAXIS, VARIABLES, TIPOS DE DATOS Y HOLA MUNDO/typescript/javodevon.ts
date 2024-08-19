//https://www.typescriptlang.org/

//Comentario en una linea: Para comentarios cortos y concisos, como explicar una línea de código en particular.

/**
 * Comentario multilinea: 
 * Se utilizan para comentarios más largos, 
 * como explicar una sección de código o documentar una función.
 */

//Variables Tipadas
var variable1: string = 'Variable de tipo Texto';
let variable2: string = 'Variable de tipo Texto';

/**
 * ¿Diferencia entre var y let?
 * Principalmente el scope
 * var: Tiene un alcance funcional o global.
 * let: Tiene un alcance de bloque.
 * 
 * Más información en https://www.typescriptlang.org/docs/handbook/variable-declarations.html
 */

//Constante tipada
const constante: boolean = false;

// Datos Primitivos (Disponibles en JS)
let edad: number = 30;
let saludo: string = "Hola, mundo!";
let valorBooleano: boolean = false;
let valorNulo: null = null;
let valorIndefinido: undefined = undefined;
let simbolo: symbol = Symbol("miSimbolo");
let numeroGrande: bigint = 1234567890123456789n;

console.log('¡Hola, Typescript!')