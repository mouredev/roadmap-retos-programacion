/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 */

function ejercicio() {
  let numero = 100;
  conteoRecursivo(numero);
}

function conteoRecursivo(numero) {
  if (numero == 0) {
    console.log(`numero: ${numero}`);
    return;
  }
  if (numero > 0) {
    console.log(`numero: ${numero}`);
    return conteoRecursivo(numero - 1);
  }
}

ejercicio();

/*
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
 */

function extra() {
  let numeroFactorial = 5;
  let posicionFibonacci = 6;
  let resultadoFactorial = factorialRecursivo(numeroFactorial);
  console.log("\n\t factorial de un numero \n");
  console.log(
    `el factorial del numero ${numeroFactorial}! es : ${resultadoFactorial}`
  );
  console.log("\n\t numero fibonacci \n");
  let resultadoFibonacci = fibonacciRecursivo(posicionFibonacci);
  console.log(
    `el numero fibonacci en la posicion ${posicionFibonacci} es : ${resultadoFibonacci}`
  );
}

function factorialRecursivo(numero) {
  if (numero == 1) {
    return 1;
  }
  if (numero >= 1) {
    return numero * factorialRecursivo(numero - 1);
  }
}

function fibonacciRecursivo(numero) {
  if (numero == 0) return 0;
  if (numero == 1) return 1;
  return fibonacciRecursivo(numero - 1) + fibonacciRecursivo(numero - 2);
}

extra();
