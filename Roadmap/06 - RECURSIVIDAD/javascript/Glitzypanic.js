// EJERCICIO
function countDown(number) {
  console.log(number);
  if (number === 1) {
    // Este es el caso base
    console.log("Boom!");
  } else {
    // Esta es la llamada recursiva
    return countDown(number - 1);
  }
}

countDown(100);

// EJERCICIO OPCIONAL 1
function factorial(numero) {
  if (numero === 0) {
    return 1;
  } else {
    return numero * factorial(numero - 1);
  }
}

factorial(10);
console.log(factorial(10));

// EJERCICIO OPCIONAL 2
function fibonacci(n) {
  if (n < 0) {
    console.log("La posición tiene que ser mayor que cero");
    return 0;
  } else if (n == 1) {
    return 0;
  } else if (n == 2) {
    return 1;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}

console.log(fibonacci(10));
