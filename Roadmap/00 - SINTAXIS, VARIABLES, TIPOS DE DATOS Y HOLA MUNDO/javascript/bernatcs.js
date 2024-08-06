// -1-

// https://developer.mozilla.org/es/docs/Web/JavaScript

// -2-

// Comentario en una línea

/* Comentario
en
varias
lineas */

// -3-

var miVariable = 'Esto es una variable'
const miConstante = 'Esto es una constante'

// -4-

var stringVariable = 'Esto es una variable con texto'
var stringVariable2 = "Esto es una variable con texto"
var stringVariable3 = `Esto es una variable con texto`
//console.log(typeof(stringVariable))

var numberVariable = 1
var numberVariable2 = NaN
//console.log(typeof(numberVariable))

var boolVariable = true
//console.log(typeof(boolVariable))

var objectVariable = [1, 2, 3, 4] // Aunque es un Array
var objectVariable2 = {
    Nombre: 'Bernat',
    Apellido: 'Cucarella',
}
//console.log(typeof(objectVariable))

// -5-
let nombreLenguaje = 'JavaScript'
console.log("¡Hola, " + nombreLenguaje + "!")