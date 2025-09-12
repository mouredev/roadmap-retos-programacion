/**
 * Función recursiva para imprimir números del 100 al 0.
 * @param numero El número actual a imprimir.
 */
function imprimirNumeros(numero: number): void {
    // Caso base: si el número es menor que 0, terminamos la recursión
    if (numero < 0) {
        return;
    }
    
    // Imprimimos el número actual
    console.log(numero);
    
    // Llamada recursiva con el número decrementado
    imprimirNumeros(numero - 1);
}

/**
 * Función recursiva para calcular el factorial de un número.
 * @param n El número del cual calcular el factorial.
 * @returns El factorial del número.
 */
function factorial(n: number): number {
    // Casos base: factorial de 0 y 1 es 1
    if (n === 0 || n === 1) {
        return 1;
    }
    
    // Llamada recursiva: n * factorial(n-1)
    return n * factorial(n - 1);
}

/**
 * Función recursiva para calcular el valor de un elemento en la sucesión de Fibonacci.
 * @param posicion La posición del elemento en la sucesión de Fibonacci.
 * @returns El valor del elemento en la posición dada.
 */
function fibonacci(posicion: number): number {
    // Casos base: posiciones 0 y 1 de Fibonacci son 0 y 1 respectivamente
    if (posicion === 0) {
        return 0;
    }
    if (posicion === 1) {
        return 1;
    }
    
    // Llamada recursiva: suma de los dos elementos anteriores
    return fibonacci(posicion - 1) + fibonacci(posicion - 2);
}

// Pruebas de las funciones
console.log("Números del 100 al 0:");
imprimirNumeros(100);

const numeroFactorial: number = 5;
console.log(`\nFactorial de ${numeroFactorial}: ${factorial(numeroFactorial)}`);

const posicionFibonacci: number = 7;
console.log(`Elemento en la posición ${posicionFibonacci} de Fibonacci: ${fibonacci(posicionFibonacci)}`);