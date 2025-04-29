
/*
*Ejercicio
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

// Iniciando el ejercicio numero 00 de la ruta de estudio Roadmap

//https://www.ecma-international.org/ecma-262/. 

// primera forma de hacer comentarios en ua linea(//)

/* segunda forma de hacer
comentarios multiples en varias lineas*/

let variable = "cadena de texto";
const constante = "constante";
/* la palabra reservada var antes se usaba para declarar variables en javascript
pero ya no se usa en la actualidad */

//el punto y coma al final de una sentencia es opcional en javascript
let number= 10;//Representa tanto números enteros como números de punto flotante.
let numero = 1.5;

let boolean = true;//Representa valores lógicos: true (verdadero) o false (falso).
let booleano = false;

let nullValue = null;//Representa la ausencia intencional de cualquier valor
let undefinedValue = undefined;//Representa una variable a la que no se le ha asignado un valor.

let string = "cadena de texto"; //Representa secuencias de caracteres. Se pueden definir con comillas simples (' '), dobles (" ") o backticks (`).

let symbol = Symbol("symbol");  //Representa un valor único e inmutable.

let bigInt = 1234567890123456789012345678901234567890n;//de esta forma se declara un bigInt     
let bigInt2 = BigInt(1234567890123456789012345678901234567890);//otra  forma de declarar un bigInt

console.log("¡Hola, JavaScript!");//Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
