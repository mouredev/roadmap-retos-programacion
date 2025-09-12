//"use strict";
// ------- DOCUEMNTACION --------

// https://developer.mozilla.org/es/docs/Web/JavaScript

// ------- COMENTARIOS  --------

// Son los mismos que C++
// comentario inline
/*
comentarios
en bloque
*/

// No se pueden anidar comentarios

// ------- VARIABLES Y CONSTANTES --------

// Existen 3 tipos de delcaraciones de variables

// scope global
var variableInt = 1;

// Scope local
let variableString = "hola";

const MI_CONSTANTE_PI = 3.1416;

// variable global no declarada, puede crearte problemas
x = 12;

// ------- TIPOS DE DATOS --------

// En el último ECMAScript define 8 tipos de datos en Js

let myBoolean = true;
let myNull = null;
let myUnd = undefined;
//numerico
let myInt = 10;
let myFloat = 10.5;
// formato de precición arbritrario BIG
let myBig = 9007199254740992n;
let myString = "Mi texto";
// Instancia unica e inmutable
let mySymbol = Symbol();
let mySym2 = Symbol("something");
let myObj = new Object(null);

// ------- IMPRESION --------

console.log("¡Hola, Javascript!");