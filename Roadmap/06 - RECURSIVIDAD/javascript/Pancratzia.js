/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */

function countTo0(num) {
  console.log(num);

  if (num === 0) return;
  else countTo0(num - 1);
}

countTo0(100);

//DIFICULTAD EXTRA (opcional):

function nFactorial(num) {
  if (num === 0 || num === 1) return 1;
  else return num * nFactorial(num - 1);
}

function fibonacci(num) {
  if (num <= 1) return 1;
  else return fibonacci(num - 1) + fibonacci(num - 2);
}

const randomNum = Math.floor(Math.random() * 10 + 1);

console.log(`El factorial de ${randomNum} es ${nFactorial(randomNum)}`);
console.log(`El elemento ${randomNum} de la sucesión de Fibonacci es ${fibonacci(randomNum)}`);
