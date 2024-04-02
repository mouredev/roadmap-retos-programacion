/**
 * * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 */

// Javascript - Los comentarios: este es un comentario de una línea, se puede colocar al inicio de la linea o al final

/* este es un comentario
 * más largo, de varias líneas
 */

/* - Crea una variable (y una constante si el lenguaje lo soporta).*/

/** VARIABLES : 
 *  var
        Declara una variable, opcionalmente la inicia a un valor.  se puede utilizar para declarar variables locales y globales, dependiendo del contexto de ejecución. (NO RECOMENDADO)
*/

var variableGlobal = 0;

/**
 * let
        Declara una variable local con ámbito de bloque, opcionalmente la inicia a un valor.
 */

let variable = 0;

/** CONSTANTES
 * const
        Declara un nombre de constante de solo lectura y ámbito de bloque.
 */

const constante = 0;

// * - Crea variables representando todos los tipos de datos primitivos
// *   del lenguaje (cadenas de texto, enteros, booleanos...).
/**
 * Javascript cuenta con Siete tipos de datos que son primitivos
 */

let entero = 9;             //Number
let conDecimal = 3.14159    //Number
let texto1 = 'Hola Mundo' ;  //String,
let texto2 = "Hola Mundo" ;  //String,
let texto3 = `Hola Mundo` ;  //String,
let verdader = true;        // Boolean
let falso = false;          // Boolean
let noDefinido;
let unDefinido = undefined  // Undefined
let conPrecision = 9007199254740992n; //BigInt
let sym1 = Symbol();        //Symbo (nuevo en ECMAScript 2015).
let  nulo = null            // null


// * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

console.log("¡Hola, javascript!")