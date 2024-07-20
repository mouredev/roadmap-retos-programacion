// Documentación oficial https://developer.mozilla.org/es/docs/Web/JavaScript

// Comentario de una sola línea

/* 
  comentario 
  de 
  varias lineas
*/

// variable
let nombre = 'Juan';
// mutación de variable
nombre = 'el nuevo nombre es: Sebastián';


// constante
// por convención el nombre se escribe en mayúsculas
const PI = 3.1416;

// datos primitivos

// comillas simples
let myString = 'Hola mundo';
// comillas dobles
let otherString = "Otra cadena de texto";
// Backticks o comillas invertidas
let phrase = `Podemos incrustar otro string ${myString}`;

// entero
let myInteger = 33;
// flotante
let myFloat = 3.9;
// Infinity: el resultado es Infinity, también esta -Infinity
let myInfinity = 1 / 0;
// la n al final significa que es un BigInt
let myBigInt = 1234567890123456789012345678901234567890n; 

// Boolenos
let myBool = true;
myBool = false;

// NaN: Resultado debido a una operación matemática incorrecta
let notAtNumber = 'esto no es un numero' / 2; 

/* 
null: representa nada, vacío o desconocido, es un valor especial
se aisgna de manera explícita
*/
let myNull = null;

/* 
undefined, es un valor especial, siginifica valor no asignado.
Al declarar una variable pero al no ser asignada, su valor es undefined;
este valor se puede asignar manualmente, pero no se recomienda, para ello
usamos null, para asignar un valor "vacío" o "desconocido".
Undefined es un valor inicial reservado para cosas que aún no 
han sido asignadas, es decir se asgina automaticamente para aquellas varialbles
que no han sido inicializadas con ningún valor de manera explícita.
*/
let myUndefined = undefined; // Asignado manualmente
console.log({myUndefined});
let indefinido; // Valor inicial implícito undefined
console.log({indefinido})

console.log("Hola, JavaScript")