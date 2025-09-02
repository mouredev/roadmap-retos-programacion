// https://developer.mozilla.org/es/docs/Web/JavaScript

 // Comentario en una linea

/* Comentario
    de
    varias
    lineas
 */

/**
 * Comentario de JSDoc, sirve para documentar nuestro codigo, 
 * este comentario genera informacion para poder comprender y 
 * mantener nuestro codigo.Tiene como recursos el uso de 
 * etiqueras (@param, @return) para indicar valores de entrada y 
 * el retorno de la funcion
 */

/** 
 * funcion que devuelve la suma de dos paramentros
 * @param {*} a number
 * @param {*} b number
 * @returns number
 */

function sum(a,b)
{
    return a+b;
};


// Declaracion de una constante
const variable1="123";

// Declaracion de una variable
var variable2;
let variable3;


//Tipos de datos de primitivos
let v_Boo2= false // boolean es un tipo de dato logico que puede tener dos valores: true o false
let v_null= null; // null representa a una referencia que apunta a una inexistente o invalido onbjeto o direccion.
let v_undefined // undefined es una variable que no tiene un valor asignado
let v_int = 1 // number el dato tipo number representa tanto numeros enteros como numeros decimales
let v_bigInt= 9173294628n // BigInt es un tipo usado para contener numero muy grandes
let v_str = "Andres" // string el tipo string contiene cadenas de texto
let v_Symbol =Symbol("anything") // Symbol representa valores unicos e inmutables que se utilizan principalmente como identificadores unicos para propiedades de objetos.

//Impresion por consola
console.log("¡Hola, Javascript");