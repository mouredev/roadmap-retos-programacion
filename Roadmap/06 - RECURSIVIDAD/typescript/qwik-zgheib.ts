/* -- exercise */
const printNumbers = (n: number): void => {
  if (n < 0) return;

  console.log(n);
  printNumbers(n - 1);
};

printNumbers(100);

/* -- extra challenge */
const factorial = (n: number): number => (n === 0 ? 1 : n * factorial(n - 1));

let number: number = 5;
console.log("Factorial of", number, "is", factorial(number));

const fibonacci = (n: number): number => (n === 0 ? 0 : n === 1 ? 1 : fibonacci(n - 1) + fibonacci(n - 2));

let position: number = 7;
console.log("Fibonacci number at position", position, "is", fibonacci(position));
