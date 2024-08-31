/*
    EJERCICIO:
    1) Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
    2) Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
    3) Crea una variable (y una constante si el lenguaje lo soporta).
    4) Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    5) Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

// 1) https://developer.mozilla.org/en-US/docs/Web/JavaScript

// 2) Comentario de una linea y varias

/*
    Comentario de varias lineas
 */

// 3) Variable y constante
let variable = "texto";
const pi = 3.1416;
// 4) Tipos de variables primitivas o Tipos incorporados https://developer.mozilla.org/en-US/docs/Glossary/Primitive

// Tipos de dato undefined y null
let nulo = null;
let indefinido = undefined;

// Tipos de dato numericos, number,BigInt
let numero = 123;
let decimal = 3.1416;
let color = 0xFF0000;
let numeroGrande = 9007199254740991n;

// Tipos de dato texto
let cadena = "Texto";

// Tipos de dato boleano
let boleanoVerdadero = true;
let boleanoFalso = false;

// Tipos de dato Symbol, se usa crear identificadores unicos
let variableSymbol = Symbol("descripcion");

// Tipos de dato lista y objectos
let lista = [1, 2, 3];
let objecto = { 1: "primero", 2: "segundo" };

// 5) print JavaScript
console.log("¡Hola, JavaScript!");