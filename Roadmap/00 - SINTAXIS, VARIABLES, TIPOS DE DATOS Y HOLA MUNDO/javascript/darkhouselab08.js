// URL del sitio web oficial de JavaScript
// https://developer.mozilla.org/es/docs/Web/JavaScript

// --- Comentarios ---

// Esta es la sintaxis de un comentario en una sola línea.

/*
  Esta es la sintaxis
  para un comentario
  en múltiples líneas.
*/

// --- Variables y Constantes ---

// Una variable (let) permite que su valor cambie.
let myVariable = "Esta es mi primera variable";
myVariable = "Este es un nuevo valor para mi variable"; // El valor cambió

// Una constante (const) no puede ser reasignada después de su creación.
const MY_CONSTANT = "Este es un valor constante";
// Si intentaras: MY_CONSTANT = "Otro valor"; // Esto daría un error.

// --- Tipos de Datos Primitivos (con más ejemplos) ---

// 1. String (Cadena de texto)
let myString = "Hola, Franco";
let myOtherString = 'Esto también es un string.';
let email = "darkhouselab08@gmail.com";

// 2. Number (Número) - JavaScript no distingue entre enteros y flotantes.
let myInteger = 42;
let myFloat = 3.1416;
let myNegativeNumber = -10;

// 3. Boolean (Booleano) - Solo puede ser Verdadero o Falso
let isLearning = true;
let isFinished = false;

// 4. Undefined (Indefinido)
// Una variable que ha sido declarada pero aún no tiene valor.
let myFutureValue;
// console.log(myFutureValue); // Esto imprimiría 'undefined'

// 5. Null (Nulo)
// Representa la ausencia intencional de cualquier valor. Es un "valor vacío" a propósito.
let myEmptyValue = null;

// 6. BigInt
// Para números enteros que son demasiado grandes para el tipo 'Number'.
let myBigNumber = 90071992547409912345n; // La 'n' al final lo define como BigInt

// 7. Symbol
// Para crear identificadores únicos (lo usarás en temas avanzados).
let myUniqueId = Symbol("id");
let myOtherUniqueId = Symbol("id");
// myUniqueId === myOtherUniqueId; // Esto sería 'false'

// --- Impresión por Terminal ---

// (En JavaScript, la "terminal" es la "consola" del navegador o de Node.js)
console.log("¡Hola, JavaScript!");

// (Bonus: Cómo imprimir el tipo de dato, como en el ejemplo de Python)
console.log(typeof myString);      // Imprimirá "string"
console.log(typeof myInteger);     // Imprimirá "number"
console.log(typeof isLearning);    // Imprimirá "boolean"
console.log(typeof myFutureValue); // Imprimirá "undefined"
console.log(typeof myEmptyValue);  // Imprimirá "object" (¡un detalle peculiar de JS!)
console.log(typeof myBigNumber);   // Imprimirá "bigint"
console.log(typeof myUniqueId);    // Imprimirá "symbol"