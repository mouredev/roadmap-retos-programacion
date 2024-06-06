function printNumbers(num) {
  if (num < 0) {
    return;
  }
  console.log(num);
  printNumbers(num - 1);
}

printNumbers(100);

//Dificultad Extra

//Factorial
function factorial(num) {
  if (num === 0 || num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

console.log(factorial(23));

//Fibonacci
function fibonacci(num) {
  if (num <= 1) {
    return num;
  }
  return fibonacci(num - 1) + fibonacci(num - 2);
}

console.log(fibonacci(23));
