/*
* EJERCICIO:
* Entiende el concepto de recursividad creando una función recursiva que imprima
* números del 100 al 0.
*
* DIFICULTAD EXTRA (opcional):
* Utiliza el concepto de recursividad para:
* - Calcular el factorial de un número concreto (la función recibe ese número).
* - Calcular el valor de un elemento concreto (según su posición) en la 
*   sucesión de Fibonacci (la función recibe la posición).
*/

/// [Recursividad]: Números del 100 al 0
void countDownFrom(int number) {
  if (number >= 0) {
    print(number);
    countDownFrom(number - 1);
  }
}

/// [DIFICULTAD EXTRA]: factorial de un número
int getFactorial(int number) {
  if (number < 0) return 0;
  else if (number == 0) return 1;
  else return number * getFactorial(number - 1);
}

/// [DIFICULTAD EXTRA]: valor posición en sucesión de Fibonacci
int getFibonacci(int index) {
  if (index <= 0) return 0;
  else if (index == 1) return 0;
  else if (index == 2) return 1;
  else return getFibonacci(index - 1) + getFibonacci(index - 2);
}

void main() {
  /// [Recursividad]: Números del 100 al 0
  countDownFrom(100); // ...

  /// [DIFICULTAD EXTRA]: factorial de un número
  print(getFactorial(-5));  // 0
  print(getFactorial(0));   // 1
  print(getFactorial(5));   // 120

  /// [DIFICULTAD EXTRA]: valor posición en sucesión de Fibonacci
  print(getFibonacci(5));  // 3
  print(getFibonacci(6));  // 5
  print(getFibonacci(7));  // 8
}
