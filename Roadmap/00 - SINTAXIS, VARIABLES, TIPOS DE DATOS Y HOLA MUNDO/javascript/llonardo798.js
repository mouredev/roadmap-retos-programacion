// 1. URL del sitio web oficial de JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript

// 2. Sintaxis de comentarios en JavaScript:

// Comentario de una línea

/*
 *  Comentario de
 *  varias líneas
 */

/**
 * Comentario de varias líneas
 * en formato de documentación
 * (JSDoc)
 * 
 * @param {string} param1 - Descripción del parámetro
 * @returns {number} - Descripción del valor de retorno
 */

// 3. Creación de variables y constantes en JavaScript:
let variable = 'Variable en JavaScript!';

const constante = '¡Constantes en JavaScript!';

// 4. Tipos de datos primitivos en JavaScript:

let cadena = 'Cadena de texto';             // String (cadenas de texto) - Comillas simples
let otraCadena = "Otra cadena de texto";    // String (cadenas de texto) - Comillas dobles
let numero = 42;                            // Number (números) - Numeros enteros 
let decimal = 3.14;                         // Decimal (números) - Números decimales o de punto flotante
let bigInt = BigInt(9007199254740992);      // BigInt (números) - Números enteros que son más grandes que el límite que puede manejar number
let booleano = true;                        // Boolean (valores booleanos) - true o false
let valorNoDefinido;                        // Undefined (valor no definido) - Variable que no ha sido asignada
let valorNulo = null;                       // Null (valor nulo) - Valor nulo
let id = Symbol("id");                      // Symbol (símbolos) - Valor único e inmutable que puede ser utilizado como clave de una propiedad de un objeto

// 5. Imprimir por consola
console.log(`¡Hola, JavaScript!`);