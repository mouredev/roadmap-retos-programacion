// Comentario de una sola linea

/* Este es un comentarios de
   multiples lineas */

// Pagina oficial de TypeScript
// https://www.typescriptlang.org/

// Variable
let saludar: string = 'Hola'

// Constante
const lenguaje: string = 'TypeScript'

// 📌 Datos Primitivos
// String
let texto: string = 'Texto'
console.log(typeof texto)

// Numbers
let numeros: number = 123
console.log(typeof numeros)

// Booleans
let verdadero: boolean = true
let falso: boolean = false 
console.log(typeof verdadero, typeof falso);

// Symbol
let simbolo: symbol = Symbol('Soy un tipo de dato Simbolo')
console.log(typeof simbolo);

// Bigint
let big: bigint = 9007199254740991n;
console.log(typeof big);

// Null
let vacio: null = null
console.log(typeof vacio);

// undefined
let sinDeclarar: undefined
console.log(typeof sinDeclarar);

/* Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!" */
console.log(saludar + ' ' + lenguaje)