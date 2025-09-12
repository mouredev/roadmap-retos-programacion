/*
EJERCICIO:
 1. - Crea un comentario en el código y coloca la URL del sitio web oficial del
      lenguaje de programación que has seleccionado.
 2. - Representa las diferentes sintaxis que existen de crear comentarios
      en el lenguaje (en una línea, varias...).
 3. - Crea una variable (y una constante si el lenguaje lo soporta).
 4. - Crea variables representando todos los tipos de datos primitivos
      del lenguaje (cadenas de texto, enteros, booleanos...).
 5. - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

*/


// 1 . https://developer.mozilla.org/es/docs/Web/JavaScript

// 2 . para comentario en una linea

/* para comentarios 
multilineas
es asi */

// 3.

let lenguaje = 'Javascript';
const CONSTANTE = 'se declara si o si con un valor';


// 4.

let string = 'cadenas de texto';
let number = 5;
let booleanos = true
let bigInt = 123456789n;
let nullType = null;
let undefinedType = undefined;
let simbolito = Symbol('mi-simbolo');

// 5.

console.log(`¡Hola, ${lenguaje}`);