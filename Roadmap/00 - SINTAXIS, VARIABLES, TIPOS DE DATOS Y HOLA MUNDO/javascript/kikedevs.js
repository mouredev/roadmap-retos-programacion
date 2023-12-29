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

const urlPaginaOficialJavaScript = 'https://developer.mozilla.org/es/docs/Web/JavaScript'

//=== COMENTARIOS ===
// Comentario en una línea  del sitio web oficial de JavaScript: https://developer.mozilla.org/es/docs/Web/JavaScript

/* Comentario de varias lineas del sitio web oficial de Javascript:
https://developer.mozilla.org/es/docs/Web/JavaScript
*/

/*=== DECLARACIÓN DE VARIABLES ===
En javascript existe diferentes formas de declarar variables, primero conozcamo su anatonomia

let nombreVariable = 'valor';
let -------------- - -------;
--- nombreVariable - -------;
--- -------------- = 'valor';
DECLARACIÓN       | ASIGNACIÓN
*/

/*=== FORMAS DE DECLARAR UNA VARIABLE ===
Para declarar constante utilizaremos la palabra reservada {const}

const PI = 3.141592

Para declarar no constantes utilizaremos las palabras reservadas {let} & {var}
La diferencia principal de var y let es que uno tiene un scope de bloque mientras que la otra es global

let --> Alcance bloque
var --> Alcance global
*/

/*=== TIPO DE DATOS ===
Existen 10 tipos de datos

PRIMITIVOS = ['string', 'number', 'boolean', 'undefined', 'null', 'symbol', 'bigint']
COMPLEJOS = ['object', 'array', 'function']
*/

//STRING
let variableString = 'Hello world'

//NUMBER
let variableNumber = 10;

//BOOLEAN
let variableBoolean = true;

//NULL
let variableNula = null;

//UNDEFINED
let variableIndefinida;

//SYMBOL --> Sirven para crear identificadores
let variableSymbol = Symbol('Descripcion del símbolo');

//BIGINT --> Sirven para representar numeros extremadamente largos
let bigintLiteral = 1234567890123456789012345678901234567890n;
let bigintLiteral2 = BigInt(1234567890123456789012345678901234567890);

//OBJECT
let MoureDev = {
    nombre: "Brais Moure",
    tecnologias: ['Swift','Object-C','Kotlin','Java','Python','Flutter'],
    esUnCrack: true,
    pais: "España",
    ocupacion: "Desarrollador de Software"
};

//ARRAY
let tecnologias = ['Swift','Object-C','Kotlin','Java','Python','Flutter'];

//FUNCTION
function cambiarOcupacion (object){
    object.ocupacion = 'Desarrollador de Software Android & IOS';
};

cambiarOcupacion(MoureDev);


const LENGUAJEDEPROGRAMACION = 'JavaScript';

console.log(`¡Hola, ${LENGUAJEDEPROGRAMACION}!`);