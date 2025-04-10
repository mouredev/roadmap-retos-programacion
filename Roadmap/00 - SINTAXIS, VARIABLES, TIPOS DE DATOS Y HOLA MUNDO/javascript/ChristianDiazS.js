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





//          Lo primero... ¿Ya has elegido un lenguaje?
// Ya elegí un lenguaje de programación, 'JavaScript'.


//      * - Crea un comentario en el código y coloca la URL del sitio web oficial del
//      *   lenguaje de programación que has seleccionado.
// URL JavaScript: https://developer.mozilla.org/es/docs/Web/JavaScript


//      * - Representa las diferentes sintaxis que existen de crear comentarios
//      *   en el lenguaje (en una línea, varias...).
// Para crear comentarios con JavaScript podemos utilizar la siguiente sintaxis: 
// Para hacer un comentario en una sola línea utilizamos dos barras ( // ) como al inicio de ésta línea de comentario.
/* 
    Para hacer un comentario ocupando varias líneas,
    usamos una barra seguida de un asterisco (/*) para la apertura del comentario
    y un asterisco seguido de una barra (como al final de éste comentario) para el cierre del mismo.
*/


//      * - Crea una variable (y una constante si el lenguaje lo soporta).
let myName = "Christian";    // La variable let se puede cambiar o actualizar su valor.  
const daysInWeek = 7;        // La variable const no se puede cambiar ni actualizar su valor.


//      * - Crea variables representando todos los tipos de datos primitivos
//      *   del lenguaje (cadenas de texto, enteros, booleanos...).
let string = "Cadena de texto";  // Representa texto. Se define entre comillas dobles ("") o comillas simples ('').
let number = 4;  // Representa números incluyendo enteros y decimales.
let bigint = 12345678901234567890n;  // Representa números enteros grandes, que superan el límite de los números.
let boolean1 = true;  // Representa valores lógicos.
let boolean2 = false;  // Representa valores lógicos.
let vacio = null;  // Representa la ausencia de un valor o una variable que no tiene valor asignado.
let variable = undefined;  // Representa una variable que ha sido declarada pero no le ha sido asignado ningún valor. 
const symbol1 = symbol;  // Representa un valor único e inmutable. Se utiliza principalmente para crear claves de objeto.


//      * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
console.log("Hola, JavaScript" );
