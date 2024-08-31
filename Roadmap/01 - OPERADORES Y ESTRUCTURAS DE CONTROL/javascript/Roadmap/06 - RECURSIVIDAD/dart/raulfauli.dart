/// #06 RECURSIVIDAD

void main() {
  printNumbers(100);

  // Extra
  print(factorial(10));
  print(fibonacci(10));
  print(count); // 177 me parecen muchas iteraciones decido mejorar el algoritmo
  print(fibonacciWithStart(10));
  print(count2); // 10
}

printNumbers(int n) {
  if (n >= 0) {
    print(n);
    printNumbers(n - 1);
  }
}

// Extra
// 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880
int factorial(int n) {
  if (n <= 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
int count = 0;
int fibonacci(int n) {
  count++;
  if (n <= 1) {
    return n;
  }

  return fibonacci(n - 1) + fibonacci(n - 2);
}

int count2 = 0;
int fibonacciWithStart(int n, {(int, int) start = (0, 1)}) {
  count2++;
  if (n <= 1) {
    return (n == 0) ? start.$1 : start.$2;
  }

  return fibonacciWithStart(n - 1, start: (start.$2, start.$1 + start.$2));
}
