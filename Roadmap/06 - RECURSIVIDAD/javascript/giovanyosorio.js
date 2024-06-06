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

let cuentaAtras = numero => {
    //base case
    if (numero === 0) {
        return;
    }
    console.log(numero);
    return cuentaAtras(numero - 1);
};
cuentaAtras(100) // 

let factorial = (numero) => {

    if (numero < 0) {
        return -1
    }else if(numero ==0){
      return 1
    }else{
      return (numero*factorial(numero-1))
    }
};
factorial(5)

var fib = function(n) {
    if (n <= 1) return n;

    return fib(n-1) + fib(n-2);
}

fib(8)