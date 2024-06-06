/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *

 */

//Recusrividad... mi peor enimgo
//¿Que es la recursividad? Técnica de programación que permite crear instrucciones que se repitan un número n de veces.
//En resumen: Una funcion que se llama a si misma

function imprimirNumeros(num) {
  // Caso base: cuando num es menor o igual a 0, detenemos la recursión
  //En la mayoria de los casos, hay que buscar la forma de como se detiene la recursividad
  if (num <= 0) {
    console.log(num);
    return;
  }
  // Imprime el número actual
  console.log(num);
  // Llama a la función recursivamente con el número decrementado en 1
  imprimirNumeros(num - 1);
}
// Llamamos a la función con 100 para comenzar desde ahí
imprimirNumeros(100);
console.log(`.........................................`);

/*  * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la
 *   sucesión de Fibonacci (la función recibe la posición).*/

// Factorizacion recursiva
function factorizacionRecursiva(fact) {
  // Casos base: termina puesto que llego al final, el 1! = 0 y 0! = 1
  if (fact == 0 || fact == 1) {
    console.log(fact);
    return 1;
  }
  //bandera
  console.log(fact, '!');
  // 5 * 4
  return fact * factorizacionRecursiva(fact - 1);
}
console.log('Factorial de 5:', factorizacionRecursiva(5)); // output: 120 = 5x4x3x2x1
console.log(`.........................................`);

// Función recursivo
function fibonacci(pos) {
  // Casos base: si la posición es 0 o 1, el valor es la misma posición
  if (pos === 0 || pos === 1) {
    return pos;
  }

  // Caso recursivo: fibonacci(pos - 1) + fibonacci(pos - 2)
  return fibonacci(pos - 1) + fibonacci(pos - 2);
}
console.log("Fibonacci de 0:", fibonacci(0)); // Resultado: 0
console.log("Fibonacci de 1:", fibonacci(1)); // Resultado: 1
console.log("Fibonacci de 2:", fibonacci(2)); // Resultado: 1
console.log("Fibonacci de 4:", fibonacci(4)); // Resultado: 3
console.log("Fibonacci de 6:", fibonacci(6)); // Resultado: 8
console.log(`.........................................`);

/*
n =	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	...
xn =0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	...
*/

console.log(`.........................................`);