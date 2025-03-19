/// 02 FUNCIONES Y ALCANCE

void main() {
  helloWorld();
  sayHello('Raúl');

  double result = average(10, 20);
  print('La media de 10 y 20: $result');

  functionWithAnotherFunction();
  // anotherFunction(); // Error

  // Funciones del lenguaje [dart:core]
  assert('  hello  '.trim() == 'hello');
  assert('Never odd or even'.contains('odd'));
  final now = DateTime.now();
  print('Hora actual es: $now');
  final value = BigInt.parse('12345678901234567890');
  print('Valor BigInt: $value');

  // Variables globales
  testGlobalVariables();
  print('La variable local sigue siendo $localVariable');

  // Extra
  int totalNumbers = extraFunction("Fizz", "Buzz");
  print('Total de números impresos: $totalNumbers');
}

// Función sin parametros retorno
void helloWorld() {
  print('Hello World!');
}

// Función con parametros
void sayHello(String name) {
  print('Hello $name!');
}

// Función con parametros y retorno
double average(int a, int b) {
  return (a + b) / 2;
}

// Función con otra función
void functionWithAnotherFunction() {
  void anotherFunction() {
    print('I am another function');
  }

  anotherFunction();
}

// Testear global variables
const globalVariable = 10;
const localVariable = 10;
void testGlobalVariables() {
  print('La variable global es $globalVariable');
  int localVariable = 20;
  print('Ahora localVarible está definida dentro de la función y es $localVariable');
}

// Extra
int extraFunction(String first, String second) {
  int countNumbers = 0;
  for (int i = 1; i <= 100; i++) {
    if ((i % 3 == 0) && (i % 5 == 0)) {
      print('$first$second');
    } else if (i % 3 == 0) {
      print(first);
    } else if (i % 5 == 0) {
      print(second);
    } else {
      print(i);
      countNumbers++;
    }
  }
  return countNumbers;
}
