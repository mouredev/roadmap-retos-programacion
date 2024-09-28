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
 * 
 * 
 * 
 * // url de javascript: https://developer.mozilla.org/es/docs/Web/JavaScript
 * 
 * // este es un comentario de una sola linea
 * 
 *  /* este es un comentario de varias lineas
 * que puedes explicar mas detallamante que esa una function o archivo en espeficico*/

/** 
 * Este es un comentario para documentar una funcion , varialbe o archivo en especifico
 @param {string} name - nombre de la persona
 @returns {string} - retorna un saludo
 */

 function saludo (name){
     return `Hola ${name}`
 }
 

 // variables y constantes

 const myConstant = 'soy una constante '; // constante que no cambia y su valor es string
 let  nombre = 'sixto'; // tipo de dato string
 let edad = 25; // tipo de dato numerico
 let isDeveloper = true; // tipo de dato booleano que puede ser true o false
 let variableNull = null; //  se declara una variable y se inicializa con valor null - no tiene valor o refereincia a un objeto
 let bigInt = 1234567890123456789012345678901234567890n; // tipo de dato para representar numero grandes 
 let symbol =   Symbol("hola soy inmutable"); // tipo de dato que se usa para crear identificadores unicos , datos primitivos inmutables , su valor no puede ser modificado una vez creado
 let indefinido = undefined; // se declara una variable pero no se ha inicializado
 let array = [1,3,5,7,2, 1]; // un array de numeros desordenados
let array2 = ['sixto', 'crack', 'moure', 'javascript']; // un array de string 


// Imprime por terminal el texto: "¡Hola, [Javascript]!"

let miLenguaje = 'Javascript';
console.log(`!Hola, ${miLenguaje}!`); // imprime por consola el saludo con el nombre del lenguaje