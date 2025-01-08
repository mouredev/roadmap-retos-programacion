const fibonacci = (n) => {
  if (n <= 1) {
    return n;
  }

  return fibonacci(n - 1) + fibonacci(n - 2);
};

const factorial = (n) => {
  if (n == 0) {
    return 1;
  }

  return n * factorial(n - 1);
};

console.log(fibonacci(20));
console.log(factorial(20));
