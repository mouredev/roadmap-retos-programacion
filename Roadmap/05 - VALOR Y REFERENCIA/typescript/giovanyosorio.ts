/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */


// Asignación por valor (tipos primitivos)
let num1: number = 10;
let num2: number = num1;
num2 = 20;
console.log(num1); // 10 (no cambia)
console.log(num2); // 20


// Asignación por referencia (objetos)
let obj1: { prop: number } = { prop: 10 };
let obj2: { prop: number } = obj1;
obj2.prop = 20;
console.log(obj1.prop); // 20 (cambia)
console.log(obj2.prop); // 20


// Función con paso por valor
function incrementaPorValor(num: number): number {
    return num + 1;
}

let a: number = 5;
let b: number = incrementaPorValor(a);
console.log(a); // 5 (no cambia)
console.log(b); // 6

// Función con paso por referencia
function modificaObjeto(obj: { prop: number }): void {
    obj.prop += 1;
}

let objA: { prop: number } = { prop: 5 };
modificaObjeto(objA);
console.log(objA.prop); // 6 (cambia)

// Intercambio por valor
function intercambiaPorValor(x: number, y: number): [number, number] {
    let temp: number = x;
    x = y;
    y = temp;
    return [x, y];
}

let valor1: number = 10;
let valor2: number = 20;
let [nuevoValor1, nuevoValor2] = intercambiaPorValor(valor1, valor2);
console.log(valor1, valor2); // 10, 20 (no cambian)
console.log(nuevoValor1, nuevoValor2); // 20, 10

// Intercambio por referencia
function intercambiaPorReferencia(obj1: { value: number }, obj2: { value: number }): void {
    let temp: number = obj1.value;
    obj1.value = obj2.value;
    obj2.value = temp;
}

let objValor1: { value: number } = { value: 10 };
let objValor2: { value: number } = { value: 20 };
intercambiaPorReferencia(objValor1, objValor2);
console.log(objValor1.value, objValor2.value); // 20, 10 (cambian)
