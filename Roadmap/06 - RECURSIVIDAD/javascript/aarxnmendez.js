// Función recursiva para imprimir números del 100 al 0
function imprimirNumeros(n) {
    if (n < 0) return;
    console.log(n);
    imprimirNumeros(n - 1);
}

imprimirNumeros(100);

// Ejercicio Extra: Función recursiva para calcular el factorial de un número
function factorial(n) {
    if (n === 0) return 1;
    return n * factorial(n - 1);
}

console.log(factorial(5)); // 120

// Ejercicio Extra: Función recursiva para calcular el valor de un elemento en la sucesión de Fibonacci
function fibonacci(n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(10)); // 55