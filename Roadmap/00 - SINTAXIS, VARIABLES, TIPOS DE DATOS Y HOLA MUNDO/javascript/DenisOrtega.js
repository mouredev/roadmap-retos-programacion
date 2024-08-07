// Lo primero ya elegiste el lenguaje? : Si
// JavaScript https://developer.mozilla.org/es/docs/Web/JavaScript


/**
 * Esto es un comentario
 * de varias lineas.
 */


let lenguaje = "JavaScript";
console.log("Elijo:", lenguaje);

// Variables

let miVariable = 10;  // Las variables pueden cambiar su valor.
miVariable = 20;
console.log(miVariable);

var miOtraVariable = 30;  // var es muy similar a let, pero tiene un alcance global.
miOtraVariable = 40;
console.log(miOtraVariable);

// Constantes

const PI = 3.1416;  // Las constantes no pueden cambiar su valor. En cambio puedes cambiar sus propiedades cuando se trata de un objeto.
console.log(PI);

const persona = {   // En este caso, la constante persona es un objeto, por lo que sus propiedades pueden cambiar.
    nombre: "Denis",
    edad: 36
};
console.log(persona);

persona.edad = 37;
console.log(persona);

// Tipos de datos

let numero = 10;
let cadena = "Hola mundo";
let booleano = true;
let arreglo = [1, 2, 3];
let objeto = {nombre: "Denis", edad: 37};
let nulo = null;
let indefinido = undefined;
let simbolo = Symbol("simbolo");
let fecha = new Date();
let error = new Error("Error");


// typeof devuelve el tipo de dato de una variable.
console.log(typeof numero);  // Devuelve "number"  Pueden ser enteros o decimales.
console.log(typeof cadena);  // Devuelve "string"  Las cadenas de texto deben ir entre comillas dobles o simples.
console.log(typeof booleano); // Devuelve "boolean" Pueden ser true o false.
console.log(typeof arreglo); // Devuelve "object" Los arreglos son objetos.
console.log(typeof nulo);  // Devuelve "object"  Es un error de JavaScript.
console.log(typeof indefinido); // Devuelve "undefined"  Es un error de JavaScript.
console.log(typeof simbolo); // Devuelve "symbol"  Se usa para identificadores únicos.
console.log(typeof fecha);  // Devuelve "object"  Se usa para trabajar con fechas.
console.log(typeof error);  // Devuelve "object" Se usa para trabajar con errores.
console.log(typeof objeto);  // Devuelve "object"  Los objetos son colecciones de propiedades.

// Operadores

let a = 10;
let b = 5;

let suma = a + b; // Suma
let resta = a - b; // Resta
let multiplicacion = a * b; // Multiplicación
let division = a / b; // División 
let modulo = a % b; // Módulo (resto de la división) 
let exponente = a ** b; // Exponente (a elevado a la b)
let incremento = a++; // Incremento en 1
let decremento = b--; // Decremento en 1 
let negacion = !true; // Negación (no) Devuelve false si el operando es true.
let and = true && false; // AND (y) Devuelve true si ambos operandos son true.
let or = true || false; // OR (o) Devuelve true si al menos uno de los operandos es true.
let igualdad = a == b; // Igualdad Devuelve true si los operandos son iguales. solo compara el valor.
let igualdadEstricta = a === b; // Igualdad estricta Devuelve true si los operandos son iguales y del mismo tipo.
let desigualdad = a != b; // Desigualdad Devuelve true si los operandos no son iguales.
let desigualdadEstricta = a !== b; // Desigualdad estricta Devuelve true si los operandos no son iguales o no son del mismo tipo.
let mayorQue = a > b; // Mayor que Devuelve true si el operando de la izquierda es mayor que el de la derecha.
let menorQue = a < b; // Menor que Devuelve true si el operando de la izquierda es menor que el de la derecha.
let ternario = a > b ? "a es mayor que b" : "b es mayor que a"; // Operador ternario : la primera expresion es cuando la condicion es verdadera, la segunda cuando es falsa.

console.log(
    suma,
    resta,
    multiplicacion,
    division,
    modulo,
    exponente,
    incremento,
    decremento,
    negacion,
    and,
    or,
    igualdad,
    igualdadEstricta,
    desigualdad,
    desigualdadEstricta,
    mayorQue,
    menorQue,
    ternario
);


console.log("Hola mundo!");
console.log("Fin del ejercicio.");






