function imprimirNumerosDecrecientes(numero) {
  // Caso base
  if (numero < 0) {
    return;
  }

  console.log(numero);

  // Llamada recursiva
  imprimirNumerosDecrecientes(numero - 1);
}

// Uso
imprimirNumerosDecrecientes(100);

// Ejercicio extra
// Factorial
function calcularFactorial(numero) {
  if (numero === 0) {
    return 1;
  } else {
    return numero * calcularFactorial(numero - 1);
  }
}

const numero = 5;
const factorial = calcularFactorial(numero);

console.log(`El factorial de ${numero} es: ${factorial}`);

// Posicion Fibonacci
function fibonacci(posicion) {
  if (posicion === 1 || posicion === 2) {
    return 1;
  } else {
    return fibonacci(posicion - 1) + fibonacci(posicion - 2);
  }
}

const posicion = 10;
const valorEnPosicion = fibonacci(posicion);

console.log(
  `El valor en la posición ${posicion} de la sucesión de Fibonacci es: ${valorEnPosicion}`
);
