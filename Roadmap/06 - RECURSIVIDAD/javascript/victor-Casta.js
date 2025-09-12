/*
   * Entiende el concepto de recursividad creando una función recursiva que imprima
   * números del 100 al 0.
*/

const getNumbers = (number) => {
  if (number < 0) {
    return;
  }
  console.log(number);
  return getNumbers(number - 1);
};

console.log(getNumbers(100));


/*
 * DIFICULTAD EXTRA (opcional):
  * Utiliza el concepto de recursividad para:
  * - Calcular el factorial de un número concreto (la función recibe ese número).
  * - Calcular el valor de un elemento concreto (según su posición) en la 
  *   sucesión de Fibonacci (la función recibe la posición).
*/

const myFactorial = (number) => {
  if(number === 0) {
    return 1;
  }
  return number * myFactorial(number - 1)
}

console.log(myFactorial(5));

const fibonacci = (n) => {
  // Caso base: primeros dos elementos de Fibonacci son 0 y 1
  if (n === 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }
  // Caso recursivo: Fibonacci(n) = Fibonacci(n - 1) + Fibonacci(n - 2)
  return fibonacci(n - 1) + fibonacci(n - 2);
};

// Ejemplo: calcular el 7mo elemento en la sucesión de Fibonacci
console.log(fibonacci(7)); // Output: 13
