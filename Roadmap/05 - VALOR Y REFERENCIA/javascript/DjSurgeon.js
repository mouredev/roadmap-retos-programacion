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

/* 
Cuando hablamos de pasar una variable por valor y por referencia en JavaScript nos referimos a pasar una variable usando un valor primitivo o un valor no primitivo. Entonces, pasar una variable por valor se refiere a asignarle uno de los siete elementos con valores primitivos de JavaScript. Por su parte, pasar una variable por referencia quiere decir que estamos asignándole un elemento con un valor no primitivo, sea un objeto, un array o una función.
La diferencia entre pasar una variable por valor y por referencia en JavaScript es su relación con lo que sucede dentro y fuera de la función. Cuando pasamos una reference variable javascript, lo que «ocurre» dentro de la función «repercute» fuera de ella. Mientras tanto, cuando pasamos una variable por valor, lo que «ocurre» dentro de la función, «se queda» en la función, sin alterar el resto del código.
*/

// Pasamos por valor, con valores primitivos

let num1 = 15;
let arr1 = [1,2,3,4];

function pasoValor(num) {
  console.log(`Dentro de la función ${num} es ${num * 2}`);
}

pasoValor(num1);
console.log(`Fuera de la función es: ${num1} el valor original no se modifica.`);

function pasoReferencia(arr) {
  arr.push(5);
  console.log(`Dentro de la función ${arr}`);
}

console.log(`Antes de pasarlo ${arr1} por la función.`)
pasoReferencia(arr1);
console.log(`Fuera de la función ${arr1} el valor original se ha modificado.`);

// Extra =================

let num2 = 10;
let num3 = 20;

let arr2 = [0,1,2];
let arr3 = ["Sergio", "Vero"];

function pasoPorValor(num1, num2){
  let numA = num1;
  num2 = num1;
  num2 = numA;
  return[num1, num2];

}
console.log("Valores despues de la función por valor");
console.log(pasoPorValor(num2, num3));
console.log("Valores originales:")
console.log(num2, num3);

function pasoPorReferencia(arr1, arr2){
  let arrA = arr1;
  arr2 = arr1;
  arr2 = arrA;
  return arrA;
}

console.log("Valores despues de la función por referencia");
console.log(pasoPorReferencia(arr2, arr3));
console.log("Valores originales:")
console.log(arr2, arr3);
