
/*
 * EJERCICIO:
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



//✅Pagina web del lenguaje. https://developer.mozilla.org/es/docs/Web/JavaScript

// ✅Este es un comentario en unas sola linea

/**
 * ✅Este es un comentario en varias lineas
 * como puedes ver 
 * estan en 3 lineas
 */

// ✅una variable tipo string
var lenguaje = 'Java Script'
// ✅una constante tipo number, con coma flotante
const pi = 3.14
// ✅variable de tipo  number, pero entero
var entero = 34
// ✅varialbe de tipo boolean 
var flag = true
// ✅variable de tipo BigInt
var granEntero = 12391239182938917785676283904n
// ✅variable de tipo null
var vacio = null
// ✅ variablede tipo symbol
var sym = Symbol();

console.log(`Hola, ${lenguaje}`)