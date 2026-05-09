//1.- URL sitio web oficial de javascript:  https://developer.mozilla.org/es/docs/Web/JavaScript 

//2.- Sintaxis y tipos de comentarios

//2.1.- Este es un comentario de una sola línea
let comentarioLuegoDeLetra // También puedes agregar el comentario al finalizar el código.

/* 
*2.2.- Este es un comentario
*de varias líneas,
*tantas como quieras.
*
*/


//3.- Variables y Constantes

var declaracion1 = 'Declara una variable, opcionalmente la inicia a un valor'; //locales y globales
let declaracion2 = 'Declara una variable local con ámbito de bloque, opcionalmente la inicia a un valor'; // local con ámbito de bloque
const declaracion3 = 'Declara un nombre de constante de solo lectura y ámbito de bloque.'; // local con ámbito de bloque
declaracion4 = 'Variable global no declarada' //provoca problemas.

//4.- Datos primitivos

const datoBooleano = true | false;
const datoNull = null;
const datoUndefined = undefined;
const datoNumber = 1994;
const datoBigInt = 9007199254740992n;
const datoString = 'Las palomas pueden distinguir entre Picasso y Monet.';
const datoSymbol = Symbol('Simbolillo');
const datoObject = Object(datoSymbol);

const nombreLenguaje = 'Javascript';
//5.- Impresión en consola
console.log(`Hola, ${nombreLenguaje}`);