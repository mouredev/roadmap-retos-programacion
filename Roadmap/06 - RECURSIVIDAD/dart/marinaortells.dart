/// URL del sitio web oficial: https://dart.dev/

void main() {
  print100(100);

  /// Dificultad extra
  
  print(factorial(3));
  print(fibonacci(10));
}

print100(int num) {
  if (num == 0 ) { print(0); }
  else { 
    print(num);
    print100(num - 1); }
}

factorial(int num) {
  
  if (num == 0) { return 1; }
  else { return num * factorial(num - 1); }

}

fibonacci(int num) {

/// [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
  if (num <= 1 ) { return num; }
  return (fibonacci(num - 1) + fibonacci(num - 2));
}
