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

// 🔥 EJERCICIO
const imprimirNumeros = (n) => n < 0 || (console.log(n), imprimirNumeros(n-1))
imprimirNumeros(100)

// 🔥 Extra

// Fibonacci
// F(0) = 0, F(1) = 1
// F(n) = F(n - 1) + F(n - 2) para n > 1.
const fibonacci = (n) => n === 0 ? 0 : n === 1 ? 1 : fibonacci(n-1) + fibonacci(n-2)

console.log("Fibonacci en posición 5:", fibonacci(5)) // 5
console.log("Fibonacci en posición 10:", fibonacci(10)) // 55

// Factorial
// n! = n * (n - 1) * (n - 2) * ... * 1
// Caso base: 0! = 1.
const factorial = (n) => (n === 0 || n === 1) ? 1: n * factorial(n - 1)

console.log("Factorial de 5:", factorial(5)); // 120
console.log("Factorial de 7:", factorial(7)); // 5040