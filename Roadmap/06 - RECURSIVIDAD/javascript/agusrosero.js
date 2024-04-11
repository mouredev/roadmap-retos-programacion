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

// EJERCICIO:
function recursividad(numero) {
  if (numero >= 100) {
    console.log(numero);
  } else {
    return;
  }
  recursividad(numero - 1);
}

recursividad(100);

// DIFICULTAD EXTRA:
function calcularFactorial(numero) {
  if (numero === 0 || numero === 1) {
    return 1;
  } else {
    let factorial = 1;
    for (let i = 2; i <= numero; i++) {
      factorial *= i;
    }
    return factorial;
  }
}

console.log(calcularFactorial(4));

function fibonacci(posicion) {
  if (posicion === 0) {
    return 0;
  } else if (posicion === 1) {
    return 1;
  } else {
    let anterior = 0;
    let actual = 1;
    for (let i = 2; i <= posicion; i++) {
      let siguiente = anterior + actual;
      anterior = actual;
      actual = siguiente;
    }
    return actual;
  }
}

console.log(fibonacci(6));
