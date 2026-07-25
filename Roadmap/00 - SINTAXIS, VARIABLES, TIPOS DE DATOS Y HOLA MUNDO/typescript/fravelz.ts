// https://www.typescriptlang.org/

// Comentario de una sola linea

/*
Comentario de
varias lineas
*/ 

let varName: string = "Valor de la variable";
const CONSTANTE: string = "Valor de la constante";

let numberType: number = 7_799; //7799 con guion bajo para mejor lectura
let bigInt: bigint = 9007199254740991n; // Numero grande

let booleanType: boolean = false;
let stringType: string = "string";

let nullType: null = null; // null por defecto
let undefinedType: undefined = undefined; // undefined solo al colocarlo explicitamente

const symbolType: symbol = Symbol('id'); // Tipo de dato simbolo

let numberArray: number[] = [1, 2, 3];
let stringArray: string[] = ["a", "b", "c"];

console.log ("Hola, TypeScript");

export {}; // Evita el error de "Cannot redeclare block-scoped variable" al ejecutar el código en un entorno global

// > Autor: Fravelz
