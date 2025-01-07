/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#06 RECURSIVIDAD
---------------------------------------
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

// ________________________________________________________
function num(n) {
    console.log(n);
    // Base case
    if (n > 0) {
        num(n - 1);
    }
}
num(100);

// ________________________________________________________
// DIFICULTAD EXTRA

// Calcular el factorial de un número concreto
// 4! = 4 * 3 * 2 * 1 = 24
function factorial(n) {
    if (n !== 0) {
        return n * factorial(n - 1);
    } else {
        return 1;
    }
    /* explicación:
    factorial(4)
        | = 24 
     return 4 * factorial(3) -> (4 * 6)
                  | = 6 
         return 3 * factorial(2) -> (3 * 2)
                      | = 2 
             return 2 * factorial(1) -> (2 * 1)
                          | = 1 
                 return 1 * factorial(0) -> (1 * 1)
                              | = return 1 -> base case
    */
}

// Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci.
// n : |0|1|2|3|4|5|6|..
// fb: |0|1|1|2|3|5|8|..
//      |+|=^   |+|=^ ..
function fibonacci(n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
        /* explicación:
                            return 3
                  fibonacci(3)      / \    fibonacci(2)
                   / \ =2      +      / \ =1
             fibonacci(2) + fibonacci(1)    fibonacci(1) + fibonacci(0) -> base case
              / \ =1
        fibonacci(1) + fibonacci(0) -> base case
        */
    }
}

console.log(`Factorial de 4: \n${factorial(4)}`);
console.log(`Valor según posición 4 en Fibonacci:\n${fibonacci(4)}`);
