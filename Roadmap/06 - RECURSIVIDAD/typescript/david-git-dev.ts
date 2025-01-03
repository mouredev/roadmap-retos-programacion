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
function oneHundredToZero(count:number){
  if(count<0){
    return 0;
  }
  console.log(count)
oneHundredToZero(count-1);
}
function factorial(n: number):number {
  if (n <= 1) {
    console.log(n);
    return 1;
  }
  console.log(n);
  return n * factorial(n - 1);
}
function fibonacci(n: number):number {
  if (n <= 1) {
    return n;
  }
  let res = fibonacci(n - 1) + fibonacci(n - 2);
  return res;
}
