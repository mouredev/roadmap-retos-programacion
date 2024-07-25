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

/* 
Esto es lo que me dijo ChatGPT al preguntar sobre el sitio oficial de Javascript =>

El lenguaje de programación JavaScript no tiene un sitio web oficial único y exclusivo, ya que es un lenguaje de programación de código abierto mantenido por la comunidad y está estandarizado por el organismo ECMA International. Sin embargo, hay recursos importantes relacionados con JavaScript que son muy utilizados y ampliamente reconocidos:

Documentación oficial de JavaScript (MDN Web Docs): Este es uno de los recursos más completos y confiables para aprender sobre JavaScript. Puedes encontrar la documentación en el siguiente enlace: MDN Web Docs - JavaScript https://developer.mozilla.org/en-US/docs/Web/JavaScript

Sitio web de ECMAScript: ECMAScript es el estándar en el que se basa JavaScript. El sitio web de ECMAScript proporciona información sobre las especificaciones actuales y anteriores del lenguaje: ECMAScript https://tc39.es/

Sitio web de Node.js: Node.js es un entorno de ejecución de JavaScript en el lado del servidor. Su sitio web oficial es una fuente valiosa de información y recursos para desarrolladores de Node.js: Node.js https://nodejs.org/en

Sitio web de npm (Node Package Manager): npm es el gestor de paquetes más grande del ecosistema JavaScript. Su sitio web es una referencia importante para buscar, compartir y administrar paquetes de software para Node.js: npm https://www.npmjs.com/

Estos son algunos de los recursos más relevantes para los desarrolladores que trabajan con JavaScript. 

Y esto agrego yo:
Otro que es bastante útil es https://www.w3schools.com/js/default.asp
*/

//Este es un single line comment o comentario de una sola linea

/*
Este es un multi-line comment 
o comentario de múltiples líneas
*/

//Variables con var y let
var variableCreadaConVar;
let variableCreadaconLet;

//Constante
const CONSTANTE = "debo Inicializar las constantes con un valor";

//Datos primitivos
//Javascript es un lenguaje dinámico con tipos dinámicos.
//Las variables no son asociadas con un tipo en particular y se pueden reasignar con valores de otro tipo.
//Es weakly typed por lo que permite conversion de tipo de manera implícita.

/*Los tipos de datos primitivos son:
  1. String
  2. Number
  3. Bigint
  4. Boolean
  5. Undefined
  6. Null
  7. Symbol
  8. Object
*/

let varString = "Esta es una variable de tipo String";
let varNumber = 125.63; //Esta es una variable de tipo number
let varBigint = 123654789741258963n;
let varBoolean = true;
let varUndefined = undefined;
let varNull = null;
let varSymbol = Symbol();
let varObject = { prop1: 1, prop2: "dos" };

elNombreDeMiLenguaje = "Javascript";
console.log(`¡Hola, ${elNombreDeMiLenguaje}!`);
