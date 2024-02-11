//EJERCICIO 00-SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO


//-------------------------------------------------------------
//- Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.

// JAVASCRIPT https://developer.mozilla.org/es/docs/Web/JavaScript


//--------------------------------------------------------------
//- Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).

//comentario de una linea
/*comentario de 
varias 
lineas
*/


//---------------------------------------------------------------
// - Crea una variable (y una constante si el lenguaje lo soporta).

let variable = 'esto es una variable'
const constante = 'esto es una constante'


//----------------------------------------------------------------
// - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).

//STRING
let texto = 'string'            //cadena de texto

//NUMBER
let integer = 37                //numero entero 
let float = 37.1                //numero decimal

//NULL
let datoNull = null             //dato objeto

//UNDEFINED
let noDefinido = undefined      //dato no definido

//BOOLEAN
let booleano = true             //dato booelano
let booleano1 = false           //dato booleano

//BIGINT
let bigInt = 50n                //dato bigint (numero muy grande)

//SYMBOL
let simbol = Symbol('whaterver')



//----------------------------------------------------------------

 //- Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 console.log('Hola Javascrip!')