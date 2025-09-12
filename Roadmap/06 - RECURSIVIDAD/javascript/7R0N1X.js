function reverse(n) {
  if (n === 0) {
    return 0;
  }
  console.log(n)
  return reverse(n - 1);
}

// console.log(reverse(100));


// Dificultad extra

let n = 5

function factorial(n) {
  if (n === 0) {
    return 1
  }
  return n * factorial(n - 1)
}

console.log(`El factorial de ${n} es ${factorial(n)}`)

function fibonacci(n) {
  if (n === 0 || n === 1) {
    return 0
  }
  if (n === 2 || n === 3) {
    return 1
  }
  return fibonacci(n - 1) + fibonacci(n - 2)
}

console.log(`El número ${n} en la sucesión de Fibonacci es ${fibonacci(n)}`)
