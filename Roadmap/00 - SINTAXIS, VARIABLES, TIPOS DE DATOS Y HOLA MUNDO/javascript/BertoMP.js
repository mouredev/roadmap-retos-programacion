// WEB OFICIAL
// Para encontrar información de JavaScript se puede utilizar la web:
// https://developer.mozilla.org/es/docs/Web/JavaScript

// COMENTARIOS
// En JavaScript tenemos 3 tipos de comentarios:
// - Comentarios de una única línea (// Comentario):
// Esto es un comentario de una línea y puede servir, por ejemplo, para explicar una variable.

// - Comentarios de varias líneas (/* Comentario */):
/* Esto es un comentario
 * de varias líneas y puede
 * servir para explicar una parte
 * más extensa del código. */

// - Comentarios de documentación (/** Comentario */):
/**
 * Este tipo de comentarios nos van a servir para documentar
 * nuestro código y van a permitir la generación de documentación
 * automática llamada JSDoc que facilita la comprensión
 * y el mantenimiento del código.
 * Al igual que pasa con otros lenguajes, pueden ir acompañados
 * de etiquetas como @param o @return que identifican valores
 * como los parámetros de entrada de la función o el valor de
 * retorno que produce la función. */

// VARIABLES Y CONSTANTES
/*  - Variables: En JavaScript podemos declarar una variable de dos formas:
                 a) Usando 'var' seguido del nombre de la variable: esta forma no es recomendable y se encuentra
                   actualmente en desuso.
                 b) Usando 'let' seguido del nombre de la variable. */
var miVariableVar = 33;
let miVariableLet = 33;

/* - Constantes: Usamos la palabra clave 'const' para declarar constantes en JavaScript. A diferencia de las variables,
                 las constantes siempre deben estar inicializadas al momento de su declaración. La convención común
                 en JavaScript es favorecer la inmutabilidad, por lo que es frecuente encontrar el uso de constantes
                 en el código. */
const miConstante = 'Alberto';

// DATOS PRIMITIVOS
/* En JavaScript existen 6 tipos de valores o datos primitivos, aunque al ser un lenguaje no tipado, no es necesario
   explicitar el tipo de la variable. */

const miString = 'Esto es un string'; // string: Sirve para almacenar cadenas de texto.

const miNumberEntero = 40; // number: Sirve para almacenar datos de tipo numérico, ya sean enteros o decimales.
const miNumberDecimal = 23.4;
const miBigInt = 123456789012345678901234567890n; /* bigint: Es otro tipo de dato numérico que permite representar
                                                             enteros más grandes que el tipo 'number'. Se define
                                                             agregando la letra "n" al final del número seguido de
                                                             "n". */
const miBoolean = true; // boolean: Este tipo de dato representa un valor lógico, que puede ser verdadero o falso.
let miUndefined; // undefined: Indica que una variable ha sido declarada pero aún no se le ha asignado un valor.
const miSymbol = Symbol('mi Symbol'); // symbol: Es un tipo de dato cuyas instancias son únicas e inmutables.
// También existe el null que aunque puede tomarse como primitivo, en realidad es propio de cada Object.

// IMPRESIÓN POR CONSOLA
console.log('¡Hola, JavaScript!');