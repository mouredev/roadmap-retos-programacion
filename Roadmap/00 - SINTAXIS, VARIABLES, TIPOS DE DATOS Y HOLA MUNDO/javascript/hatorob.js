// https://developer.mozilla.org/en-US/docs/Web/JavaScript

// comentario de una sola línea
/*
    comentario de multiple lineas
*/

//! var is global scope -> not recommend to use
var greeting = "Hello world";
//! let is block scope -> is recommend to use
let name = "Alejandro Toro";
//! const is global or block scope -> is constant, not variable
const baseUrl = "https://developer.mozilla.org/en-US/docs/Web/JavaScript";

//! primitive - init
let lenguaje = "Javascript";
let age = 29;
let isActive = true;
let notValue = null;
let noDefined = undefined;
//! primitive - end
//! other types - initi
let fruits = ["Manzana","Pera","Sandía","Banano"];
let user = {
    name: "Alejandro Toro",
    age: 29,
    userName: "hatorob"
}
//! other types - end

console.log(`¡Hola, ${lenguaje}!`);