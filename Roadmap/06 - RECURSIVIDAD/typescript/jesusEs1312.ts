// Función recursiva que imprime los números del 100 al 0
const imprimirNumeros = (numero: number) => {
    if (numero >= 0) {
        console.log(numero);
        imprimirNumeros(numero - 1);
    }
};

// Función recursiva que calcula el factorial de un número
const factorial = (numero: number): number => {
    if (numero === 0) {
        return 1;
    }
    return numero * factorial(numero - 1);
}

// Función recursiva que calcula el número de la serie de Fibonacci
const fibonacci = (numero: number): number => {
    if (numero === 0) {
        return 0;
    }
    if (numero === 1) {
        return 1;
    }
    return fibonacci(numero - 1) + fibonacci(numero - 2);
}

// Llamada a las funciones
imprimirNumeros(10);
console.log(factorial(5));
console.log(fibonacci(10));