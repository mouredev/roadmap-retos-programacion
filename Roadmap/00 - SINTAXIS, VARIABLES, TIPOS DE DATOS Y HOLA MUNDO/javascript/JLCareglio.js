/*
 JavaScript no tiene un sitio web oficial como tal,
 pero las siguientes paginas son relevantes para el lenguaje:

 - MDN Web Docs: documentación oficial y mantenida por los creadores de JavaScript.
   (https://developer.mozilla.org/es/docs/Web/JavaScript)

 - ECMAScript: es el estándar que regula el lenguaje JavaScript
   (https://ecma-international.org/)
*/

// Este es un ejemplo de comentario de una linea.

/*
 Este es un ejemplo
 de comentario de
 multiples lineas
*/

// Declaración de variable y constante
let variable;
const LANG = "JavaScript";

// Hay 6 tipos de datos primitivos: string, number, bigint, boolean, undefined y symbol.
let my_string = "cadena de caracteres";
let my_number = 7;
let my_bigint = 7n;
let my_boolean = true;
let my_undefined = undefined;
let my_symbol = Symbol();
// null aparentemente es primitivo, pero de hecho es un caso especial para cada Object.

console.log(`¡Hola, ${LANG}!`);
