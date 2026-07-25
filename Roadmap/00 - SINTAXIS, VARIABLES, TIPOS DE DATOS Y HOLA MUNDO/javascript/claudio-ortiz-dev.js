/**
 * ============================================================================
 * EJERCICIO 01 - FUNDAMENTOS DE JAVASCRIPT
 * ============================================================================
 * 
 * @author Claudio Ortiz Dev
 * @date 2026-01-31
 * @description Ejercicio completo sobre fundamentos de JavaScript con
 *              ejemplos prácticos, buenas prácticas y documentación detallada.
 * 
 * Sitio oficial: https://developer.mozilla.org/es/docs/Web/JavaScript
 * Especificación: https://www.ecma-international.org/publications-and-standards/standards/ecma-262/
 * 
 * ============================================================================
 */

// ============================================================================
// 1️1 COMENTARIOS EN JAVASCRIPT
// ============================================================================

// Comentario de una sola línea: útil para explicaciones breves
// Se usa con dos barras diagonales //

/*
 * Comentario multilínea: ideal para bloques de texto más largos
 * o para comentar temporalmente secciones de código.
 * 
 * Tip: Atajo de teclado en VS Code
 * - Línea única: Ctrl + / (Windows) o Cmd + / (Mac)
 * - Multilínea: Alt + Shift + A (Windows) o Option + Shift + A (Mac)
 */

/**
 * Comentario JSDoc: El estándar profesional para documentar código
 * Se usa para documentar funciones, clases y módulos.
 * Los editores modernos lo usan para autocompletado y ayuda contextual.
 * 
 * @example
 * // Este tipo de comentario es el que usan las bibliotecas profesionales
 * @see https://jsdoc.app/
 */

// ========================================
// 2. VARIABLES Y CONSTANTES
// ========================================

// VARIABLE: Su valor puede cambiar
let miVariable = "Puedo cambiar";
var otraVariable = "Esta es la forma antigua (evitar usar var)";

// CONSTANTE: Su valor NO puede cambiar
const MI_CONSTANTE = "No puedo cambiar";


// ========================================
// 3. TIPOS DE DATOS PRIMITIVOS
// ========================================

// STRING (Cadena de texto)
let texto = "Hola, soy un texto";
let otroTexto = 'También puedo usar comillas simples';
let textoModerno = `Y comillas invertidas para templates`;

// NUMBER (Números enteros y decimales)
let numeroEntero = 42;
let numeroDecimal = 3.14;
let numeroNegativo = -17;

// BOOLEAN (Verdadero o Falso)
let esVerdadero = true;
let esFalso = false;

// UNDEFINED (Variable declarada pero sin valor asignado)
let sinValor;
// Si imprimes sinValor, verás: undefined

// NULL (Ausencia intencional de valor)
let valorNulo = null;

// SYMBOL (Valor único e inmutable - avanzado)
let simbolo = Symbol("descripcion");

// BIGINT (Números muy grandes - ES2020)
let numeroGigante = 123456789012345678901234567890n;


// ========================================
// 4. IMPRIMIR EN LA CONSOLA
// ========================================

console.log("¡Hola, JavaScript!");

// También puedes imprimir las variables:
console.log("\n--- Mis Variables ---");
console.log("Texto:", texto);
console.log("Número entero:", numeroEntero);
console.log("Número decimal:", numeroDecimal);
console.log("Boolean verdadero:", esVerdadero);
console.log("Boolean falso:", esFalso);
console.log("Undefined:", sinValor);
console.log("Null:", valorNulo);


// ========================================
// EXTRA: Información útil
// ========================================

console.log("\n--- Información Extra ---");
console.log("Tipo de 'texto':", typeof texto);
console.log("Tipo de 'numeroEntero':", typeof numeroEntero);
console.log("Tipo de 'esVerdadero':", typeof esVerdadero);
console.log("Tipo de 'sinValor':", typeof sinValor);
console.log("Tipo de 'valorNulo':", typeof valorNulo);
