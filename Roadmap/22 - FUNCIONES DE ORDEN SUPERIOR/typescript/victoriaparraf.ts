/**
 * Características de las funciones de orden superior:
 * Toman funciones como argumentos: Permiten pasar funciones como parámetros, lo que permite modificar o extender su comportamiento.
 * Devuelven funciones: Pueden devolver nuevas funciones, lo que permite la creación de funciones personalizadas y reutilizables.
 * Composición y modularidad: Facilitan la composición de funciones más complejas a partir de funciones más simples.
 */

function applyOperation(a: number, b: number, operation: (x: number, y: number) => number): number {
    return operation(a, b);
}

const add = (x: number, y: number): number => x + y;
const multiply = (x: number, y: number): number => x * y;

console.log(applyOperation(5, 3, add)); // 8
console.log(applyOperation(5, 3, multiply)); // 15

function createMultiplier(multiplier: number): (value: number) => number {
    return (value: number) => value * multiplier;
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15

const numbers = [1, 2, 3, 4, 5];

// map
const doubled = numbers.map(num => num * 2);
console.log(doubled); // [2, 4, 6, 8, 10]

// filter
const evenNumbers = numbers.filter(num => num % 2 === 0);
console.log(evenNumbers); // [2, 4]

// reduce
const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
console.log(sum); // 15
