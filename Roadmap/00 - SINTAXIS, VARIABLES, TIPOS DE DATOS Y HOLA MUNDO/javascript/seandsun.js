// El sitio web oficial: https://developer.mozilla.org/es/docs/Web/JavaScript

// ----------------------------------------------------------------------------------------------------

// Este es un comentario de una sola línea.

/*
Este es un
comentario de
varias líneas.
*/

/**
* Este comentario es para observar
* que cada línea inicia con un 
* asterísco ya que es más "elegante".
*/

// ----------------------------------------------------------------------------------------------------

var myUsername = "seandsun" // Variable global, puede ser re-declarada y modificada.
var myUsername = "hola"

let myAge = 26 // Variable cuyo alcance está limitado a un bloque de código, puede ser modificada.
myAge = 24

const SITIO_WEB = "https://retosdeprogramacion.com/" // Variable constante, no puede ser modificada.

// ----------------------------------------------------------------------------------------------------

let string = "Yo soy Groot" // Con comillas dobles ("")
string = 'Nosotros tenemos un Hulk' // Con comillas simples (')
string = `Podría estar haciendo esto todo el día` // Con "backticks" (`)

let number = 12 // Int
number = 3.14 // Float

let noBigInt = 9007199254740991 // Int
let BigInt = 9007199254740992n // El último "1" fue cambiado por un "2" y js ya no lo soporta como int.

let boolean = true
boolean = false

let symbol = symbol() // Crea valores únicos e irrepetibles

let isNull = null // Ausencia de valor

let noUndefined = "No soy indefinada" // "undefined" es un valor que se asigna automáticamente a variables sin valor
let undefined // Es una variable cuyo valor sí es "undefined" porque no se le ha asignado ningúl valor

// ----------------------------------------------------------------------------------------------------

console.log("!Hola, JavaScript¡")