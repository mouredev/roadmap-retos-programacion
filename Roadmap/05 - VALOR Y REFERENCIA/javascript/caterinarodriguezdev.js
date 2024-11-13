/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */


const a = 10;

const modificandoCopia = (a) => a = 30;


modificandoCopia(a);

console.log(a);

const p = {
    nombre: 'Teseo'
}

const modificandoReferencia = (p) => p.nombre = 'Egeo';

modificandoReferencia(p);

console.log(p);


const edad = 25;
const nombre = 'Caterina';

const intercambioValores = (a, b) => {
    let valorA = a;

    a = b;
    b = valorA;

    return {a, b}
}

const {a: edad2, b: nombre2} = intercambioValores(edad, nombre);

console.log('antes:', edad, nombre);
console.log('después:', edad2, nombre2);

const obj1 = { nombre: 'John B.'} 
const obj2 = { nombre: 'Ada Lovelace'}
const intercambioReferencias = (obj1, obj2) => {

    let temp = obj1;
    obj1 = obj2;
    obj2 = temp;

    return {obj1, obj2}
}

const {obj1: obj1Interchanged, obj2: obj2Interchanged} = intercambioReferencias(obj1, obj2);

console.log('originales');
console.log(obj1);
console.log(obj2);
console.log('intercambiados');
console.log(obj1Interchanged);
console.log(obj2Interchanged);