/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 */

// por valor (valores primitivos)
let ejercicio = "caminar";
let copia = ejercicio;

ejercicio = "pesas";
console.log(ejercicio);
console.log(copia);

// por referencia (valores complejos)
const array = [1, 2, 3];
const array2 = array;
array.push(4);

console.log(array);
console.log(array2);

/*   - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
    "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
  (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes) */

// funciones por valor (valores primitivos)

let numeroRandom = 0;

function modificarNumero(numeroRandom) {
  return (numeroRandom = 4);
}

console.log(numeroRandom);
console.log(modificarNumero(2));

// funciones por referencia (valores complejos)

let tareas = ["trabajar", "estudiar", "entrenar"];

function agregarTarea(tareas) {
  return tareas.push("dormir");
}

console.log(agregarTarea(tareas));
console.log(tareas);

/*  * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */

// funcion por valor (valores primitivos)

let numero1 = 10;
let numero2 = 20;

function cambiarValorEnNumeros(numero1, numero2) {
  numero1 = 20;
  numero2 = 10;
  return [numero1, numero2];
}

const [copia1, copia2] = cambiarValorEnNumeros(numero1, numero2);

console.log(copia1);
console.log(copia2);

console.log(numero1);
console.log(numero2);
