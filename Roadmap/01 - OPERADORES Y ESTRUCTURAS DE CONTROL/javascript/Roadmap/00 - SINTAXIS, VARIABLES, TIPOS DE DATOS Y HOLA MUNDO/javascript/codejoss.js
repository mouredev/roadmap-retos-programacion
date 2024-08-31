// Especificacion oficial de Javascript: https://ecma-international.org
// Documentación más ocupada: https://developer.mozilla.org/es/docs/Web/JavaScript

// Javascript

// Doble diagonal para comentarios de una sola linea

/*
  Diagonal y asterisco para encerrar comentarios de bloque de varias lineas
*/

// --------------------------------
// Creación de variable
// Existen 3 formas, var y let, sin embargo, actualmente la que se recomienda usar es let
var variableConVar = 'Soy una variable con var'
let variableConLet = 'Soy una variable con let'
variableSinPalabraClave = 'Soy una variable sin palabra clave' // Este tipo de variable suele ocacionar problemas ya que se elevan a variables globales y pueden llevar a problemas de alcance

// --------------------------------
// Creación de constantes
const pi = 3.1416
// Se pueden declarar variasa constantes en una sola linea separando cada una con una coma «,»
const name = 'Josue', apellido = 'Quevedo'

// --------------------------------
// Datos primitivos
// Existen 6 tipos de datos primitivos en Javascript
const string = 'Soy un string'
const number = 10
const booleanTrue = true
const booleanFalse = false
const nullData = null
const undefinedData = undefined
const symbolData = Symbol('Soy un symbolo')

// --------------------------------
// Imprimiendo por terminal

console.log('Hola, Javascript');