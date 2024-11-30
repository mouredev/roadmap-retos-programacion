/* 1.Crea un comentario en el código y coloca la URL del sitio web oficial del
lenguaje de programación que has seleccionado.*/

// https://developer.mozilla.org/es/docs/Web/JavaScript

/* 2.Representa las diferentes sintaxis que existen de crear comentarios
en el lenguaje (en una línea, varias...)*/

function comment() {
    // Este es un comentario JavaScript de una línea
    console.log("¡Hola mundo!");
  }
  comment();

  function comment() {
    /*Este es un comentario 
    JavaScript de varias líneas*/
    console.log("¡Hola mundo!");
  }
  comment();

// 3.Crea una variable (y una constante si el lenguaje lo soporta).

//antes del ES6 las variables solo se declaraban con VAR

var javascript = true;
var edad = 18; 
var precio = 9.99; 
var nombre = 'Juan';

let javascript = true;
let edad = 18; 
let precio = 9.99; 
let nombre = 'Juan'; 

const nombre = 'Juan'; // Es necesario agregar un valor 
// const nombre; Si la constante no tiene valor genera error

/* 4.Crea variables representando todos los tipos de datos primitivos
del lenguaje (cadenas de texto, enteros, booleanos...)*/

let javascript = true; // boolean
let edad = 18; // Entero
let precio = 9.99; // Float 
let nombre = 'Juan'; // String

// 5.Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

let nombre = 'JavaScript';
 console.log("Hola" + nombre)