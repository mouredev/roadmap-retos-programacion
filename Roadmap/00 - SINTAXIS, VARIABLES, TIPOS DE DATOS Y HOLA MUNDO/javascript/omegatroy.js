// * - Crea un comentario en el código y coloca la URL del sitio web oficial del
//  *   lenguaje de programación que has seleccionado.
//  * - Representa las diferentes sintaxis que existen de crear comentarios
//  *   en el lenguaje (en una línea, varias...).
//  * - Crea una variable (y una constante si el lenguaje lo soporta).
//  * - Crea variables representando todos los tipos de datos primitivos
//  *   del lenguaje (cadenas de texto, enteros, booleanos...).
//  * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
//  *

// hola esto es un comentario en linea

/* 
  esto es un comentario en loque
  o tambien de varias lineas
*/

// una variable
let manga = 'Jujutsu Kaisen'

//una constante
const creador = "Gege Akutami"

// esta es una variable global. Desde hace años, ya no se recomienda usar var
var studio = "MAPPA"

// tipos de datos primitivos

let cadenaDeTexto = 'esto es una cadena de texto o mejor conocida como string'

let numeroEntero = 2024 // --> esto es un numero entero

let booleanos = true // los booleanos pueden ser true o false, 0 o 1

let nula = null // --> null es inexistente o inválido

let variableIndefinida // --> undefined no existe argumentos reales

let identificadorSymbol = Symbol('símbolo') // --> symbol Sirven para crear identificadores

let bigintLiteral = 9007199254740991n // --> bigint Sirven para representar numeros extremadamente largos
let bigintLiteral2 = BigInt(9007199254740991)

const mortalKombat = {
  nombre: 'mortal kombat',
  creadores: 'Ed Boon y John Tobias',
  año: 1992
} // esto es un objeto tiene clave valor

/*
  Básicamente, TODO lo que no sea un valor primitivo, es un objeto. 
  Así que tanto arreglos como funciones son considerados "Objetos". 
  Lo que si es verdad es que podemos considerar los arreglos y las funciones como 
  "sub-tipos de objetos", ya que estos se comportan como tal, pero tienen 
  propiedades y comportamientos especiales
*/

let arr = ['javaScript','python','java','rust','php'] // --> los array o listas pueden almacenar un conjunto de elementos

function soyUnaFuncion(){
  return console.log('¡Hola, javaScript!')
}

soyUnaFuncion()