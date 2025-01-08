/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

/// https://dart.dev/

void main() {
  // Función sin parámetros ni retorno
  greet();

  //Función con un parámetro y sin retorno
  greetPerson('Gerard');

  //Función con un parámetro nominal y sin retorno
  greetPersonName(name: 'Gerard');

  //Función con varios parámetros y sin retorno
  calculateSum(5, 3);

  //Función con un parámetro y con retorno
  int result = square(4);
  print(result);

  //Función con varios parámetros y con retorno
  List<double> values = [2.5, 4.5, 6.5];
  double average = calculateAverage(values);
  print(average);

  //Función dentro de una función
  outerFunction();

  //Variables locales y globales
  print('Variable global antes de la modificación: $globalVariable');
  modifyGlobalVariable();
  print('Variable global después de la modificación: $globalVariable');
  localVariableExample();

  //*! DIFICULTAD EXTRA (opcional):
  int count = printNumbersAndCountTexts('Foo', 'Bar');
  print('Número de veces que se ha impreso el número: $count');
}

// Función sin parámetros ni retorno
void greet() {
  print('¡Hola!');
}

//Función con un parámetro y sin retorno
void greetPerson(String name) {
  print('¡Hola, $name!');
}

//Función con un parámetro nominal y sin retorno
void greetPersonName({required String name}) {
  print('¡Hola, $name!');
}

//Función con varios parámetros y sin retorno
void calculateSum(int a, int b) {
  int sum = a + b;
  print('La suma de $a y $b es $sum');
}

//Función con un parámetro y con retorno
int square(int number) {
  return number * number;
}

//Función con varios parámetros y con retorno
double calculateAverage(List<double> numbers) {
  double sum = 0;
  for (double number in numbers) {
    sum += number;
  }
  return sum / numbers.length;
}

//Función dentro de una función
void outerFunction() {
  void innerFunction() {
    print('Función interna');
  }

  innerFunction();
  print('Función externa');
}

//Variables locales y globales
int globalVariable = 10;

void modifyGlobalVariable() {
  globalVariable = 20;
  print('Variable global modificada: $globalVariable');
}

void localVariableExample() {
  int localVariable = 5;
  print('Variable local: $localVariable');
}

//*! DIFICULTAD EXTRA (opcional):
int printNumbersAndCountTexts(String text1, String text2) {
  int count = 0;

  for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      print('$text1 $text2');
    } else if (i % 3 == 0) {
      print(text1);
    } else if (i % 5 == 0) {
      print(text2);
    } else {
      print(i);
      count++;
    }
  }

  return count;
}
