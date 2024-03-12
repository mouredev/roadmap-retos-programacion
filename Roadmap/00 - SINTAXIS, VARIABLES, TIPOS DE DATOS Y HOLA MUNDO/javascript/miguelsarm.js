// https://retosdeprogramacion.com/roadmap/ miguelsarm run #!1 javascript

/* este lo voy a hacer con javasript

varias lineas de codigo
pd: es igual que en css
*/

// declaring variables
var old = "this is the old version";
let variable;
const pi = 3.14159;
//=========================

// PRIMITIVE TYPE OF DATA BECAUSE IT ONLY STORES ONE VALUE

//number ==================
const constante = 3.14;
//=========================

//bigint ==================
const bignumber = 1234567890123456789012345678901234567890n; // you have to append an N at the end to indentified it as a bigint
// at this moment, BigInt is supported in Firefox/Chrome/Edge/Safari, but not in IE.
//=========================

//string ==================
variable = "hello";
let str = "single quotes hehe";
let str1 = `${variable}, Backticks as well hehe`; // You can insert or it allows embedding code by wrapping them in ${…} “extended functionality”
console.log(str1);
//=========================

//boolean(logical type)==================
let one = true; // yes
let zero = false; // no

//boolean type because of comparison
let comparison = 1 > 0;
console.log(typeof comparison); // boolean type
//=========================

// THE NULL VALUE ==========================
let age = null; // age is unknown.
// represents “nothing”, “empty” or “value unknown”.
//=========================

// undefined value ==========================
let people;
// If a variable is declared, but not assigned, then its value is undefined:
console.log(people);
//=========================

// SYMBOL  ==========================bol
const sym1 = Symbol("hello"); //guaranteed to be unique
console.log(variable == sym1); // false
// symbols are the only primitive data type that has reference identity (that is, you cannot create the same symbol twice)
//=========================

// END OF PRIMITIVE ======================================================================

// OBJECTS
const normalObj = {}; // create a normal object
// It is used to store various keyed collections and more complex entities.
console.log(typeof normalObj);
//=========================
console.log("¡Hola, Javascript!");
