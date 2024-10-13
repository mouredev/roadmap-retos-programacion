// Author: EdiedRamos

function countdownToZero(value: number): void {
  if (value < 0) return;
  console.log(value);
  countdownToZero(value - 1);
}

function factorial(value: number): number {
  if (value < 0)
    throw new Error(
      "No se puede calcular el factorial para números negativos."
    );
  return value === 0 ? 1 : value * factorial(value - 1);
}

function fibonacci(value: number, memo: Record<number, number> = {}): number {
  if (value < 2) return value;
  if (memo[value]) return memo[value];
  return (memo[value] =
    fibonacci(value - 1, memo) + fibonacci(value - 2, memo));
}

(() => {
  // Numbers from 100 to zero
  console.log("Número desde el 100 hasta el cero");
  countdownToZero(100);

  // Factorial test
  const factorial5 = factorial(5);
  console.assert(factorial5 === 120);
  console.log("Factorial de 5: " + factorial5);

  // Fibonacci test
  const fibo60 = fibonacci(60);
  console.assert(fibo60 === 1548008755920);
  console.log("Valor de fibonacci en la posición 6: " + fibo60);
})();
