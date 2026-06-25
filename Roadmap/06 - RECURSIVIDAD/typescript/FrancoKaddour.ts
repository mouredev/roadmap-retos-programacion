// https://www.typescriptlang.org/

// Función recursiva: imprime de 100 a 0
function countdown(n: number): void {
  if (n < 0) return;
  console.log(n);
  countdown(n - 1);
}
countdown(100);

// Dificultad extra

// Factorial
function factorial(n: number): number {
  if (n <= 1) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(5));  // 120
console.log(factorial(10)); // 3628800

// Fibonacci
function fibonacci(n: number): number {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}
console.log(fibonacci(0));  // 0
console.log(fibonacci(1));  // 1
console.log(fibonacci(8));  // 21
console.log(fibonacci(10)); // 55
