/**
 * Imprime los números desde el número inicial hasta 0 de forma recursiva.
 *
 * @param startNumber - El número desde el cual comenzar a imprimir.
 * @returns void - No devuelve nada, solo imprime los números en consola.
 */
const printNumbers = (startNumber: number): void => {
  let currentNumber = startNumber;

  if (currentNumber === 0) {
    console.log(currentNumber);
    return;
  }

  console.log(currentNumber);

  printNumbers(currentNumber - 1);
};

// -------------------------------------------------------------------------------------------

/**
 * Calcula el factorial de un numero de forma recursiva.
 *
 * @param number - El número a calcular su factorial.
 * @returns number - resultado del factorial del numero.
 */
const calculateFactorial = (number: number): number => {
  if (number === 0) return 1;

  if (number < 0) {
    throw new Error("El número no puede ser negativo");
  }

  return number * calculateFactorial(number - 1);
};

// -------------------------------------------------------------------------------------------

/**
 * Calcula el valor de la sucesión de Fibonacci en la posición n.
 *
 * @param n - Posicion del numero de fibonacci.
 * @returns number - numero de la posicion n de fibonacci.
 */
const fibonacciAt = (n: number) => {
  if (n < 0) throw new Error("La posición no puede ser negativa");

  if (n === 0) return 0;
  if (n === 1) return 1;

  return fibonacciAt(n - 1) + fibonacciAt(n - 2);
};
