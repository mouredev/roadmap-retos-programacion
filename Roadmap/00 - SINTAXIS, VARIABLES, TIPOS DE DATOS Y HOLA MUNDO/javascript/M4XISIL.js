/************ 1 - SITIO OFICIAL DE JAVASCRIPT ************/

// Pagina que encontre muy completa de JS, con la que me saco las dudas. Me parece que no tiene una oficial. https://developer.mozilla.org/en-US/docs/Learn/JavaScript

/*********************************************************/

/************ 2 - TIPOS DE COMENTARIOS ************/

// Para colocar un comentario en 1 sola linea.

/* Para comentar
en varias 
lineas */

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