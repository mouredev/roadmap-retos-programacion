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

// Función para imprimir números del 100 al 0
function countDown(numero: number) {
  if (numero >= 0) {
    console.log(numero);
    countDown(numero - 1);
  }
}

countDown(100);

// Funcion extra: calcular el factorial de un número
function calculoFactorial(n: number): number {
  if (n < 0) {
    console.log("Los numeros negativos no son validos");
    return 0;
  } else if (n == 0) {
    return 1;
  } else {
    return n * calculoFactorial(n - 1);
  }
}

console.log(calculoFactorial(5)); // Debería imprimir 120

// Funcion extra: calcular valor de un elememnto (Fibonacci)
function calculoFibonacci(num: number): number {
  if (num <= 0) {
    console.log("La posicion debe ser mayor que cero");
    return 0;
  } else if (num == 1) {
    return 0;
  } else if (num == 2) {
    return 1;
  } else {
    return calculoFibonacci(num - 1) + calculoFibonacci(num - 2);
  }
}

console.log(calculoFibonacci(5));
