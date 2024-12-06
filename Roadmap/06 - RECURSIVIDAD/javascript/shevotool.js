/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 */

function recursiva(numero) {
  if (numero < 0) {
    return;
  }
  console.log(numero);
  recursiva(numero - 1);
}

recursiva(100);

/*  * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * */
function calcularFactorial(numero) {
  if (numero === 0 || numero === 1) {
    return 1;
  }
  return numero * calcularFactorial(numero - 1);
}
console.log(calcularFactorial(5));

/* 
 - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).
*/
function calcularValorElemento(posicion) {
  if (posicion === 0) return 0;
  if (posicion === 1) return 1;

  let anterior = 0;
  let actual = 1;
  for (let i = 2; i <= posicion; i++) {
    let siguiente = anterior + actual;
    anterior = actual;
    actual = siguiente;
  }
  return actual;
}
console.log(calcularValorElemento(6));
