/*https://tc39.es/ecma262 

https://developer.mozilla.org/es/docs/Web/JavaScript/*/

// Variables

let myVar = 10;

console.log(myVar);

var myVar2 = 20; //en desuso nada recomendable//

console.log(myVar2);

//constantes

const myVar3 = 30;

console.log(myVar3);

//Tipos de datos primitivos

let myString= "Hola Mundo";

let myNumber = 10;

let myBoolean = true;

let myBoolean2 = false;

let myUndefined = undefined;

let myNull = null;

console.log(myString, myNumber, myBoolean, myBoolean2, myUndefined, myNull);

//Tipos de datos especiales

let myNumberEnorme= BigInt(9007199254740991);

console.log(myNumberEnorme);

let mySymbol = Symbol("mi simbolo");

console.log(mySymbol);

let myNumberDecimal = 10.5;

console.log(myNumberDecimal);

let myInfinity = Infinity;

console.log(myInfinity);

let myNaN = NaN;

console.log(myNaN);


//Tipos de datos compuestos

let myArray = [10, 20, 30, 40, 50];

let myObject = {
    nombre: "Juan",
    edad: 30
};

console.log(myArray, myObject);

