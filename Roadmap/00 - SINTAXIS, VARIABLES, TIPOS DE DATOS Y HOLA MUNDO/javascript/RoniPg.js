/*
 * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
 * - Recuerda que todas las instrucciones de participación están en el
 *   repositorio de GitHub.
 *
 * Lo primero... ¿Ya has elegido un lenguaje?
 * - No todos son iguales, pero sus fundamentos suelen ser comunes.
 * - Este primer reto te servirá para familiarizarte con la forma de participar
 *   enviando tus propias soluciones.
 *
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


//URL : https://developer.mozilla.org/es/docs/Web/JavaScript

// Comentario en una linea.
/*
* Comentario de varias lineas.
*/
let numero = 0 // Tipo Number, valores numericos
let flotante = 3.14 // Tipo float, valor numerico de coma flotante
let noEsUnNumero= Nan // Tipo Not at Number, valor NoEsUnNumero
let infinito = Infinity // Tipo Infinity, valor Infinito

let string = "" // Tipo string, valores de tipo texto
let comillaSimple = '' // Tipo string, valores de tipo texto
let comillasDobles= "" // Tipo string, valores de tipo texto
let textoFormateado = `${string}`// Tipo string, valores de tipo texto y formateados

let boleano = false; // Tipo Boolean, valores true, false.

let indefinido // Tipo Undefined, no contiene valor asignado
let nulo = null // Tipo Null, valor nulo
let simbolo = Symbol('')// Tipo Symbol, valor único e inmutable
let enteroGrande = 0n // Tipo BigInt, valores que superan el rango de los Number 


//Para crear una constante se añade utiliza la palabra reservada 'const'.

const constante = 0  // Las constantes aceptas los datos primitivos mencionados antes 

console.log("Hola JavaScript");
