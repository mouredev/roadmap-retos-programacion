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



/* Soluciones */


function recursividad(num) {
  if (num < 0) {
    return;
  } else {
    console.log(`Número: ${num}`);
    recursividad(num - 1);
  }
}

recursividad(100);


/* Extra - Opcional */


function factoriales(num) {
  if (num === 0) {
    return 1;
  } else {
    return num * factoriales(num - 1);
  }
}

console.log(factoriales(8));


function fibonacci(posicion) {
  if (posicion === 0 || posicion === 1) {
    return posicion;
  } else {
    return fibonacci(posicion - 1) + fibonacci(posicion - 2);
  }
}

console.log(fibonacci(25));