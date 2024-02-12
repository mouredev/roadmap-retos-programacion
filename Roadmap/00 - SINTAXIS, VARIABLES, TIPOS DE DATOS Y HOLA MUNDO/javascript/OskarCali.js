// **********     ENLACES DE REFERENCIA     **********
// Estandar de ECMAScript             ==>   https://ecma-international.org/publications-and-standards/standards/ecma-262/
// Especificacion de ECMAScript(2023) ==>   https://262.ecma-international.org/14.0/
// Referencia de JavaScript           ==>   https://developer.mozilla.org/es/docs/Web/JavaScript

// **********     FORMAS DE COMENTAR     **********
// Comentario en una sola linea
/* Comentario en
 * multiples lineas
 */

// **********     DECLARAR VARIABLES Y CONSTANTES     **********
// var  ==>   Declara una variable; puede tener cambios de valor y asignacion posterior
var globalScoped = "Valor";
globalScoped = 18;
// let  ==>   Declara una variable en el scope (local); puede tener cambios de valor y asignacion posterior
let localScoped;
localScoped = "Asignacion";
// const ==>  Constante en el scope; no puede cambiar de valor
const readOnlyScoped = "OskarCali";

// **********     TIPOS DE DATO (PRIMITIVOS)     **********
let _boolean = Boolean(true)
let _null = null
let _undefined = undefined
let _number = Number(87.654)
let _bigInt = BigInt(Number.MAX_SAFE_INTEGER)
let _string = String("OskarCali")
let _symbol = Symbol(894)

// **********     IMPRESION EN TERMINAL     **********
console.log("¡Hola, javascript!");

// **********     REFERENCIAS ADICIONALES     **********
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#comments
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#primitive_values