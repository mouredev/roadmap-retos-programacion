const urlPaginaOficialJavaScript = 'https://developer.mozilla.org/es/docs/Web/JavaScript'

//=== COMENTARIOS ===
// Comentario en una línea del sitio oficial de JavaScript: https://developer.mozilla.org/es/docs/Web/JavaScript

/* Comentario de varias lineas 
del sitio oficial de Javascript:
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