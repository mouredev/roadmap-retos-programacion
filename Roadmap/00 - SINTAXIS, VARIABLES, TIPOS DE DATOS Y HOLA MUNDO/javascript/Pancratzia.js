/************ 1 - SITIO OFICIAL DE JAVASCRIPT ************/
/*
Podría decirse que, como standard (ECMAScript) el sitio oficial del lenguaje es: http://www.ecmascript.org/
Sin embargo, este sitio solo se ocupa de la estandarización.
Las especificaciones del lenguaje para desarrolladores se encuentra en el siguiente url: https://developer.mozilla.org/en/JavaScript
*/
/*********************************************************/

/************ 2 - TIPOS DE COMENTARIOS ************/

// COMENTARIOS DE UNA SOLA LINEA
/*
COMENTARIOS
DE
VARIAS
LINEAS
*/

/**************************************************/

/************ 3 - CREANDO VARIABLES ************/
var variableVar = "Una variable usando VAR"; //Desde hace años, ya no se recomienda usar VAR
let variableLet = "Una variable usando LET";
const CONSTANTE = "Una constante";
/***********************************************/

/************ 4 - TIPOS DE DATOS PRIMITIVOS ************/

let tipoCadena = "Hola, soy una cadena de texto";
//Los de tipo number pueden ser enteros o decimales
let tipoNumber = 42;
tipoNumber = 42.5;
let tipoBooleano = true;
let tipoIndefinido = undefined;
let tipoSimbolo = Symbol("mySymbol");
let tipoBigInt = 1234567890123456789012345678901234567890n;


let tipoNulo = null; //Aunque algunos ejemplos lo clasifican como primitivo, en la documentación de Mozilla (https://developer.mozilla.org/es/docs/Glossary/Primitive) se indica que es un "caso especial".

/*******************************************************/

/************ 5 - HOLA, JAVASCRIPT ************/
console.log("¡Hola, JavaScript!");
/**********************************************/