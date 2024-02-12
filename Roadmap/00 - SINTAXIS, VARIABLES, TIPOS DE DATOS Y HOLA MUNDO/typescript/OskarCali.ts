// **********     ENLACES DE REFERENCIA     **********
// Sitio web oficial    ==>   https://www.typescriptlang.org/

// **********     FORMAS DE COMENTAR     **********
// Comentario en una sola linea
/* Comentario en
 * multiples lineas
 */

// **********     DECLARAR VARIABLES Y CONSTANTES     **********
// var  ==>   Declara una variable; puede tener cambios de valor pero NO del tipo
var globalScoped = "Valor";
globalScoped = "Otro valor";
// let  ==>   Declara una variable en el scope (local); puede tener cambios de valor pero NO del tipo
let localScoped: number;
localScoped = 8;
// const ==>  Constante en el scope; no puede cambiar de valor
const readOnlyScoped = "OskarCali";

// **********     TIPOS DE DATO (PRIMITIVOS)     **********
let _boolean: boolean = true;
let _number: number = 792.186;
let _bigInt: bigint = 1684324n;
let _string: string = "OskarCali";
let _symbol: symbol = Symbol("Something");

// **********     IMPRESION EN TERMINAL     **********
console.log("¡Hola, typescript!");

// **********     REFERENCIAS ADICIONALES     **********
// https://www.typescriptlang.org/docs/handbook/variable-declarations.html
// https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#the-primitives-string-number-and-boolean
// https://www.typescriptlang.org/play?target=7&ts=5.3.3
