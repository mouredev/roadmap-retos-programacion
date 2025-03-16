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

// Página principal de JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript


// Comentario en una linea 

/* 
    Este es un comentario de varias líneas
*/


//Crear una variable
let variable = "Mi variable"; 
variable = 1;  // Cambiar el valor de la variable
// console.log(variable);

//Crear una constante
const constante = "Mi constante";

//Crear variables de todos los tipos de datos primitivos
let miString = "Hola Mundo"; // Cadena de texto
let miNumero = 25; // Número entero 
let miBooleano = true; // Booleano, tambien puede ser False
let miFloat = 1.33; 
let miUndefined = undefined;
let miNull = null; 
let miSymbol = Symbol("Hola");
let miObjeto = {
            nombre: "Juan Pablo", 
            edad: 25};

console.log("¡Hola, JavaScript!");
