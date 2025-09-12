// Sitio web del lenguaje
// https://developer.mozilla.org/es/docs/Web/JavaScript

// Formas de elaborar comentarios

// Comentario de línea

/*
  Comentario multilínea
 */

/**
 * Esto también es un
 * comentario multilínea
 */

// Variables

/*
  var y let sirven para declarar variables
  var tiene un ámbito global o local,
  el hoisting con var permite mover
  la declaración en la cabecera del
  código inicializandolo en undefined
  let tiene un ámbito de bloque,
  el hoisting con let tambien mueve
  la declaración a la cabecera del 
  código pero no se inicializa
  var se encuentra en desuso, por
  buenas prácticas es mejor ocupar let
*/
var country = 'México';
let name = 'César';
// las constantes se manejan con const
const sex = 'Masculino';

// Variables para datos primitivos

// int
let age = 19;
// float
let height = 1.75;
// boolean
let alive = true;
let dead = false;
// string
let city = "México City";
// undefined
let status = undefined;
// Symbol
let my_symbol = Symbol('My symbol');

const language = 'JavaScript'
console.log(`¡Hola, ${language}!`);