/* EJERCICIO:
* - Crea un comentario en el código y coloca la URL del sitio web oficial del
*   lenguaje de programación que has seleccionado.
* - Representa las diferentes sintaxis que existen de crear comentarios
*   en el lenguaje (en una línea, varias...).
* - Crea una variable (y una constante si el lenguaje lo soporta).
* - Crea variables representando todos los tipos de datos primitivos
*   del lenguaje (cadenas de texto, enteros, booleanos...).
* - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
*
* ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
* debemos comenzar por el principio.
*/

//Web official 
//https://developer.mozilla.org/es/docs/Web/JavaScript

// one line for comment

/*
Multiple lines for comment
*/

//variables
var age=28
var city ="Bogota"

// constantes
const name="Giovany"

//datos primitivos

typeof "hola!" // "string"
typeof 42 // "number"
typeof true // "boolean"
typeof null // "object" ???
typeof undefined // "undefined"
typeof Symbol // "symbol"
typeof 23n // "bigint"

var programmingLanguage="JavaScript"
console.log(`¡Hola, ${programmingLanguage}`)