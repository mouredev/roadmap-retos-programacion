/*
EJERCICIO:
- Crea un comentario en el código y coloca la URL del sitio web oficial del
  lenguaje de programación que has seleccionado.
- Representa las diferentes sintaxis que existen de crear comentarios
  en el lenguaje (en una línea, varias...).
- Crea una variable (y una constante si el lenguaje lo soporta).
- Crea variables representando todos los tipos de datos primitivos
  del lenguaje (cadenas de texto, enteros, booleanos...).
- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */


// 🔥 sitio web oficial:  https://js.org/index.html
// Documentacion:  https://developer.mozilla.org/es/docs/Web/JavaScript

// 🔥 Una linea

/* 🔥 Varias
    Lineas
*/


// 🔥 Variables
let uno = "one" // let 
var dos = "two" // var
const tres = "three" // const


let hola = "hola" // siempre inicia con un caracter normal

let saludo // el valor es undefined
saludo = "Hola, que tal?" // asignar valor a la variable

var hello = "hello" // no recomendable y no es muy usado

const hi = "hi" // siempre se debe asignar la constante inicialmente


// 🔥 Tipos de datos

const nombre = "javascript" // String
console.log(typeof nombre)

const precio = 100 // number
const precio1 = 10.40 // number
const precio2 = -100 // number
const precio3 = "100" // String
const precio4 = '100' // String


const activo = false // boolean

const cliente = null // null
let cliente1 // undefined

const numeroGigante = BigInt(12345678912345678902345678)
console.log(typeof numeroGigante) // bigint


// 🔥 Saludo al lenguaje 
console.log("¡Hola," + nombre +"!")