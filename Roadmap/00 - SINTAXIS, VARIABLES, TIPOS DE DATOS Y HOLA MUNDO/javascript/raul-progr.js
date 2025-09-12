/* La pagina oficial de JS es : https://developer.mozilla.org/es/ */

/* esto es un comentario en una linea */
/* esto
es
un
comentario
en
varias
lineas
*/

/* declaracion de variables */

var variable = "esta es una variable";
let otraVariable = "esta es una variable, pero se usa en el scope de un bloque"
const Pi = 3.1415 /* esta es una constante, nunca cambia de valor */

/* Datos primitivos */

var texto = "Esto es un string";
var numero = 69.69; /* esto es un numero, puede ser float tambien */
var numeroGrande = BigInt(Number.MAX_SAFE_INTEGER); /* esto es un bigint */
var numeroGrande2 = 9007199254740991n; /* esto tambien es un bigint, se agrega n al final */
/* comparemos si los bigints son iguales */
if (numeroGrande === numeroGrande2){
    console.log(true);
} else{
    console.log(false);
}
var buleano = true; /* variable boolean con valor true asignado, puede ser false */
var indefinida; /* el valor primitivo undefined es cuando una variable no se le a asignado un valor */
var nulo = null;
/* hola Javascript!!! */

console.log("¡Hola, Javascript!");