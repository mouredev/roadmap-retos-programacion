/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
*/

// OPCIONAL: Ejecución del Script.
// Prerrequisitos:
//      1. Instalación de Node y NPM
// Instalación de Typescript de forma global:
//      npm install -g typescript
// Transpilar el codigo de Typescript a Javascript
//      tsc angelsanchezt.ts
// Ejecutar el codigo de Javascipt generado
//      node angelsachezt.js

// 1. Operadores

// Aritméticos
let suma: number = 10 + 5;
let resta: number = 20 - 7;
let multiplicacion: number = 6 * 8;
let division: number = 36 / 4;
let modulo: number = 15 % 4;

// Lógicos
let andLogico: boolean = true && false;
let orLogico: boolean = true || false;
let notLogico: boolean = !true;

// De comparación
let igual: boolean = 5 === 5;
let noIgual: boolean = (10 as number) !== (5 as number);
let mayorQue: boolean = 15 > 10;
let menorQue: boolean = 25 < 30;
let mayorIgual: boolean = 20 >= 18;
let menorIgual: boolean = 12 <= 15;

// De asignación
let x: number = 5;
x += 3; // x ahora es 8

// De identidad
let a: number = 10;
let b: number = 10;
let identidad: boolean = a === b;

// De pertenencia
let miArreglo: number[] = [1, 2, 3, 4, 5];
let pertenece: boolean = miArreglo.includes(3);

// Bits
let bitAnd: number = 5 & 3; // Operación AND a nivel de bits
let bitOr: number = 5 | 3;  // Operación OR a nivel de bits
let bitXor: number = 5 ^ 3; // Operación XOR a nivel de bits
let desplazamientoIzquierda: number = 8 << 2; // Desplazamiento a la izquierda
let desplazamientoDerecha: number = 8 >> 1;  // Desplazamiento a la derecha

// 2. Estructuras de control

// Condicionales
let numeroCondicional: number = 25;
if (numeroCondicional > 20) {
    console.log("El número es mayor que 20");
} else if (numeroCondicional === 20) {
    console.log("El número es igual a 20");
} else {
    console.log("El número es menor que 20");
}

// Iterativas
for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
}

// Excepciones
try {
    throw new Error("Este es un ejemplo de excepción");
} catch (error) {
    console.error(error.message);
}

// 3. Imprimir resultados por consola
console.log("Suma:", suma);
console.log("Resta:", resta);
console.log("Multiplicación:", multiplicacion);
console.log("División:", division);
console.log("Módulo:", modulo);

console.log("AND Lógico:", andLogico);
console.log("OR Lógico:", orLogico);
console.log("NOT Lógico:", notLogico);

console.log("Igualdad:", igual);
console.log("No igualdad:", noIgual);
console.log("Mayor que:", mayorQue);
console.log("Menor que:", menorQue);
console.log("Mayor o igual que:", mayorIgual);
console.log("Menor o igual que:", menorIgual);

console.log("Operador de asignación:", x);
console.log("Operador de identidad:", identidad);
console.log("Operador de pertenencia:", pertenece);

console.log("Operador Bitwise AND:", bitAnd);
console.log("Operador Bitwise OR:", bitOr);
console.log("Operador Bitwise XOR:", bitXor);
console.log("Desplazamiento a la izquierda:", desplazamientoIzquierda);
console.log("Desplazamiento a la derecha:", desplazamientoDerecha);
