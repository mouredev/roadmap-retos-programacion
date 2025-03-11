// https://www.typescriptlang.org/

/*
This a multi-line comments
*/

/*
Comentarios para deshabilitar comprobaciones de TypeScript
Puedes usar // @ts-ignore o // @ts-nocheck para ignorar errores en líneas específicas.

Ignorar un error en una línea específica:
// @ts-ignore
let resultado: number = "Hola"; // No marca error aunque es incorrecto

Ignorar comprobaciones en todo el archivo:
// @ts-nocheck
let mensaje: number = "Esto no marcará error";

*/

// Comentarios de documentación (/** ... */)
/* TypeScript admite comentarios de documentación estilo JSDoc, útiles para proporcionar información sobre funciones, clases o variables. Estos comentarios pueden ser procesados por herramientas como TypeDoc.
*/

/**
 * Suma dos números y devuelve el resultado.
 * @param a Primer número
 * @param b Segundo número
 * @returns La suma de ambos números
 */

/*

function sumar(a: number, b: number): number {
    return a + b;
  }

*/


/*
let edad: number = 23; // Variable de tipo numero
edad = 26; // Se puede reasignar
console.log(edad); // Salida: 26
*/

/*
const nombre: string = "Santiago" // Constante de tipo string
// nombre = "Carlos"; // Esto daria un error porque no se puede reasignar
console.log(nombre); // Salida: Santiago
*/

let age: number = 23;
let nombre: string = 'Typescript';
let esEstudiante: boolean = true;

console.log('Hola, ' + nombre)