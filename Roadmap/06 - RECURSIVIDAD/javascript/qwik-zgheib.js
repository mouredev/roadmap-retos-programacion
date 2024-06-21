/* -- exercise */
const printNumbers = (n) => {
  if (n < 0) return;

  console.log(n);
  printNumbers(n - 1);
};

printNumbers(100);

/* -- extra challenge */
const factorial = (n) => (n === 0 ? 1 : n * factorial(n - 1));

let number = 5;
console.log("Factorial of", number, "is", factorial(number));

const fibonacci = (n) => (n === 0 ? 0 : n === 1 ? 1 : fibonacci(n - 1) + fibonacci(n - 2));

let position = 7;
console.log("Fibonacci number at position", position, "is", fibonacci(position));

