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

console.log("+++++++++ IMPRIMIR LOS NÚMEROS DEL 100 AL 0 +++++++++");
function cuentaRegresiva(numero) {
  if (numero === 0) {
    return;
  }

  console.log(numero);
  return cuentaRegresiva(numero - 1);
}

console.log(cuentaRegresiva(100));

console.log("\n+++++++++ DIFICULTAD EXTRA: CALCULAR EL FACTORIAL DE UN NÚMERO CONCRETO +++++++++");
function calcularFactorial(numero) {
  if (numero === 0) {
    return 1;
  }

  return numero * calcularFactorial(numero - 1);
}

var numeroFactorial = 5;

console.log(`El factorial de ${numeroFactorial} es: ${calcularFactorial(numeroFactorial)}`);

console.log("\n+++++++++ DIFICULTAD EXTRA: CALCULAR EL VALOR DE UN ELEMENTO CONCRETO (SEGÚN SU POSICIÓN) EN LA SUCESIÓN DE FIBONACCI +++++++++");
function sucesionDeFibonacci(posicion) {
  if (posicion === 0) {
    return 0;
  } else if (posicion === 1) {
    return 1;
  }

  return sucesionDeFibonacci(posicion - 1) + sucesionDeFibonacci(posicion - 2);
}

var posicionEnSucesion = 8

console.log(`El valor de la posición ${posicionEnSucesion} en la sucesión de Fibonacci es: ${sucesionDeFibonacci(posicionEnSucesion)}`);
