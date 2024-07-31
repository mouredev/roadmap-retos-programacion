


let cuentaAtras = num => {
  // Cuando parar
  if(num === 0) return 1;

  console.log(num);
  return cuentaAtras(num-1);
}

//cuentaAtras(100)

// DIFICULTAD EXTRA

// Calcular el factorial de un número concreto
let factorial = num => {
  if(num < 0) {
    console.log('No se aceptan numeros negativos')
    return 0;
  } else if (num === 0) { 
    return 1
  } else {
    console.log(num);
    return num * factorial(num-1);
  }
}

//console.log(factorial(5))

// Calcular el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci

let fibonacci = num => {
  if (num <= 0) {
    console.log('No se aceptan numeros negativos, ni el 0')
    return 0;
  } else if (num === 1) {
    return 0;
  } else if (num === 2) {
    return 1;
  } else {
    return fibonacci(num-2) + fibonacci(num-1)
  }
}

console.log(fibonacci(3))