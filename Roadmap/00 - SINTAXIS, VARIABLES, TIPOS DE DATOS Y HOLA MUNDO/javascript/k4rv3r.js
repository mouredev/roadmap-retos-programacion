// Documentación: https://developer.mozilla.org/en-US/docs/Web/JavaScript

// Utilizar "//" crea un comentario de una linea.

// Utilizar "/*<texto>*/" crea un comentario en varias lineas:
/* 
Esto es
un comentario
en varias
lineas.
*/

/////////////////////////////////////////////////////////////////////////

// --  TIPOS DE VARIABLES  --
let variable_1 = "Estos es una variable.";
var variable_2 = "Esta es la version antigua de una variable";
const constante_1 = "Esto es una constante";

// -- TIPOS DE DATOS PRIMITIVOS --

/*
Todos los tipos, excepto los objetos, definen valores inmutables (es decir, valores que no se pueden cambiar).
Por ejemplo (y a diferencia de C), las cadenas son inmutables. 
Nos referimos a los valores de estos tipos como "valores primitivos".
*/

// - Cadenas de texto (strings):

let texto_1 = 'Esto es una cadena de texto con comillas simples';
let texto_2 = "Esto es una cadena de texto con comillas dobles";
let texto_3 = `Esto es una cadena de texto con acentos`; // Acepta operaciones dentro con "${}" como: `la mitad de 100 es ${100 / 2}`.

// - Números

let numero_1 = 13; // Esto es un numero Entero o "INT" de integer.
let numero_2 = 13.27; // Esto es un numero Fraccionado o "FLOAT".
let numero_3 =  9007199254740992n; // Es es un "BigInt"
/*
El tipo BigInt es un primitivo numérico en JavaScript que puede representar
números enteros con precisión arbitraria. 
Con BigInts, puedes almacenar y operar de forma segura 
en números enteros grandes incluso más allá del límite seguro de 
enteros para Numbers.
*/

// - Boolean: representa una entidad lógica y puede tener dos valores: true y false.

let bool_1 = true;
let bool_2 = false;

// - Null, Undefined & Symbol

let nulo = null; // El valor null es un literal de Javascript que representa intencionalmente un valor nulo o "vacío".
let indefinido = undefined; // La propiedad global undefined representa el valor primitivo undefined.
let simbolo = Symbol("Simbolo"); // Symbol es un objeto incorporado cuyo constructor devuelve un symbol primitivo — también llamado Symbol value o simplemente Symbol — que está garantizado que sea único.

///////////////////////////////////////////////////////////////////

let nombre = "JavaScript";

console.log("Hello,",nombre);