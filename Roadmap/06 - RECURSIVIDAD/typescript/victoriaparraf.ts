function imprimirNumeros(n: number): void {
    // Caso base: cuando n es menor que 0, terminamos la recursión
    if (n < 0) {
        return;
    }
    // Imprime el número actual
    console.log(n);
    // Llama a la función recursivamente con el siguiente número decreciente
    imprimirNumeros(n - 1);
}

// Llamada inicial a la función con el valor 100
imprimirNumeros(100);

/*************/

function calcularFactorial(numero: number): number {
    // Caso base: cuando el número es 0 o 1, el factorial es 1
    if (numero <= 1) {
        return 1;
    }
    // Llamada recursiva: calcula el factorial de numero - 1 y multiplica por numero
    return numero * calcularFactorial(numero - 1);
}

function verificarNumero(numero: number): number {
    // Verifica si el número es menor que 0
    if (numero < 0) {
        throw new Error("El número debe ser no negativo");
    }
    // Calcula el factorial utilizando la función recursiva
    return calcularFactorial(numero);
}

// Ejemplo de uso
let resultado = verificarNumero(5);
console.log(resultado); // 120


function fibonacci(n: number): number {
    // Caso base: los primeros dos números en la sucesión de Fibonacci
    if (n === 0) {
        return 0;
    } else if (n === 1) {
        return 1;
    }
    // Llamadas recursivas para calcular los dos números anteriores
    return fibonacci(n - 1) + fibonacci(n - 2);
}

// Ejemplo de uso
let posicion = 10;
let valor = fibonacci(posicion);
console.log(`El valor en la posición ${posicion} de la sucesión de Fibonacci es ${valor}`);
