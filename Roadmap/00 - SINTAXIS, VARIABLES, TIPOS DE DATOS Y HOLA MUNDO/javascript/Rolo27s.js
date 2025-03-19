// Usuario: Rolo27s - https://github.com/Rolo27s/Rolo27s
// Ejercicio #00 SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO
/* 
SITIO WEB OFICIAL DE JAVASCRIPT
https://developer.mozilla.org/es/docs/Web/JavaScript 
*/

// Comentario de una línea

/* 
Comentarios de varias líneas
Varias lineas...
Varias lineas...
while (true) ...
*/

// Declares a block-scoped, read-only named constant.
const E = 2.71828; // Declaración de una constante

// Declares a block-scoped, local variable, optionally initializing it to a value.
let variable_usuario_local = "Rolo27s"; // Declaración de una variable

// Declares a variable, optionally initializing it to a value.
var variable_usuario_global = "Rolo27s_GLOBAL"; // Declaración de una variable. Personalmente suelo codear usando let y modularizando.

// Hay siete tipos de datos primitivos en JavaScript:
// 1. Boolean
let tipo_booleano = true; // true o false
// 2. null (JS is case-sensitive)
let tipo_null = null; // Valor nulo. Cuidado que no es Null, NULL o cualquier otra variante. Debe ser estrictamente null (minúsculas).
// 3. undefined
let tipo_undefined = undefined; // Valor no definido.
// 4. Number
let tipo_numero_entero = 42; // Valor numérico entero.
let tipo_numero_decimal = 42.56; // Valor numérico decimal.
// 5. BigInt
let tipo_bigint = 9007199254740992n; // Valor numérico BigInt. Se remarca con la 'n' al final del numero.
// 6. String
let tipo_string = "Brais Moure - @mouredev"; // Valor numérico String.
// 7. Symbol
let tipo_Symbol = Symbol("mySymbol"); // Valor numérico Symbol.

/* Imprimimos por terminal un mensaje. 
Para hacer esto de manera literal necesitaríamos tener instalado NodeJS. 
https://nodejs.org/en
Ejecutamos nuestro archivo .js usando el comando: node 'nombre-de-tu-js.js'*/
console.log("¡Hola, JavaScript!");
