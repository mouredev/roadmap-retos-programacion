/**
 * EJERCICIO
 */

function numbers(number) {
  if (number < 0) {
    return;
  } else {
    console.log(number);
    number--;
    numbers(number);
  }
}

console.log('Números del 100 al 0 mediante recursividad:');
numbers(100)

/**
 * EXTRA
 */

function factorial(number) {
  if (number === 0) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

function fibonacci(number) {
  if (number === 0) {
    return 0;
  } else if (number === 1 || number === 2) {
    return 1;
  } else {
    return fibonacci(number - 2) + fibonacci(number - 1);
  }
}

console.log(`!6 = ${factorial(6)}`);
console.log(`Posición 8 de Fibonacci = ${fibonacci(8)}`);