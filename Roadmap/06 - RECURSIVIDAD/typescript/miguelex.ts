function sumaRecursiva(a: number, b: number): number {
    if (b === 0) {
        return a;
    }
    return sumaRecursiva(a + 1, b - 1);
}

console.log("La suma de 3 + 5 usando recursividad es = " + sumaRecursiva(3, 5));

function potenciaRecursiva(a: number, b: number): number {
    if (b === 0) {
        return 1;
    }
    return a * potenciaRecursiva(a, b - 1);
}

console.log("El resultado de 2 elevado a 3 es: " + potenciaRecursiva(2, 3));

function imprimirNumeros(numero: number): void {
    if (numero >= 0) {
        console.log(numero);
        imprimirNumeros(numero - 1);
    }
}

console.log("De 100 a 0 usando rercursividad: ");
imprimirNumeros(100);

// Extra

function factorialRecursivo(a: number): number {
    if (a === 0) {
        return 1;
    }
    return a * factorialRecursivo(a - 1);
}

console.log("El factorial de 5 es: " + factorialRecursivo(5));

function fibonacciRecursivo(a: number): number {
    if (a === 0) {
        return 0;
    }
    if (a === 1) {
        return 1;
    }
    return fibonacciRecursivo(a - 1) + fibonacciRecursivo(a - 2);
}

console.log("El fibonacci de 6 es: " + fibonacciRecursivo(6));

console.log("A continuación, vamos a probar las funciones factorial y fibonacci de forma interactiva");


import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Introduce un número para calcular su factorial: ', (answer: string) => {
    console.log(`El factorial de ${answer} es: ${factorialRecursivo(parseInt(answer))}`);
    rl.question('Introduce un número para calcular su secuencia Fibonacci: ', (numero: string) => {
        console.log(`La secuencia Fibonacci de ${numero} es: ${fibonacciRecursivo(parseInt(numero))}`);
        rl.close();
    });
});