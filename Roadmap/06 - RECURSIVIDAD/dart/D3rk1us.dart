/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 * 
 */

void main() {

  print(recursividad(100));

  print('------------------------------');

  /*
    * DIFICULTAD EXTRA (opcional):
    * Utiliza el concepto de recursividad para:
    * - Calcular el factorial de un número concreto (la función recibe ese número).
    * - Calcular el valor de un elemento concreto (según su posición) en la 
    *   sucesión de Fibonacci (la función recibe la posición).
  */

  print(factorial(5));

  print('------------------------------');

  print(fibonacci(3));

}

// Funciones

int recursividad(int number) {

  if (number == 0) {
    return number;
  } else {
    print(number);
    return recursividad(number - 1);
  }

}

int factorial(int number) {

  if (number == 1) {
    return number;
  } else {
    return number * factorial(number - 1);
  }
}

int fibonacci(int position) {

  if (position == 0) {
    return 0;
  } else if (position == 1) {
    return 1;
  } else {
    return fibonacci(position - 1) + fibonacci(position - 2);
  }
}