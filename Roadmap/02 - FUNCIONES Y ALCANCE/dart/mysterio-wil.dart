import 'dart:math';

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

// --- Variable Global ---
String globalVar = "Soy una variable global";

void main() {
  print("===> Funciones básicas <===");

  // Sin parámetros ni retorno
  greet();

  // Con un parámetro
  greetPerson("Wilmer");

  // Con varios parámetros
  add(5, 3);

  // Con retorno
  int result = multiply(5, 3);
  print("El resultado de la multiplicación es $result");

  // Con parámetros por nombre y por defecto
  greetDefault("MoureDev");
  greetDefault("Wilmer", greeting: "Hello");

  // En Dart no hay una sintaxis para argumentos variables (variadic).
  // Se suele usar una Lista.
  print("Argumentos variables (pasando una Lista):");
  printArgs([1, "texto", true]);


  print("\n===> Funciones dentro de funciones <===");
  outerFunction();


  print("\n===> Funciones del core de Dart <===");
  var myList = [1, 2, 3, 4, 5];
  print("Usando la propiedad 'length' de una Lista: La lista tiene ${myList.length} elementos.");
  
  // Usando reduce para encontrar el máximo (se necesita importar 'dart:math')
  print("Usando 'reduce' de Iterable con la función 'max': El valor máximo es ${myList.reduce(max)}");


  print("\n===> Variable LOCAL y GLOBAL <===");
  myFunctionScope();

  // Modificar una variable global
  print("Antes de modificar: $globalVar");
  modifyGlobal();
  print("Después de modificar: $globalVar");


  /*
   * DIFICULTAD EXTRA (opcional):
   */
  print("\n====> DIFICULTAD EXTRA <====");
  int timesPrintedNumber = fizzBuzzExtra("Fizz", "Buzz");
  print("\nEl número se imprimió un total de $timesPrintedNumber veces.");
}

// --- Definiciones de funciones ---

void greet() {
  print("Hola, Dart!");
}

void greetPerson(String name) {
  print("Hola, $name!");
}

void add(int a, int b) {
  print("La suma de $a y $b es ${a + b}");
}

int multiply(int a, int b) {
  return a * b;
}

void greetDefault(String name, {String greeting = "Hola"}) {
  print("$greeting, $name!");
}

void printArgs(List<dynamic> args) {
  for (var arg in args) {
    print("- $arg");
  }
}

void outerFunction() {
  print("Esta es la función externa.");
  void innerFunction() {
    print("Esta es la función interna.");
  }
  innerFunction();
}

void myFunctionScope() {
  String localVar = "Soy una variable local";
  print(globalVar); // Acceso a la variable global
  print(localVar);
}

void modifyGlobal() {
  globalVar = "He modificado la variable global";
}

int fizzBuzzExtra(String text1, String text2) {
  int count = 0;
  for (int i = 1; i <= 100; i++) {
    bool isMultipleOf3 = (i % 3 == 0);
    bool isMultipleOf5 = (i % 5 == 0);

    if (isMultipleOf3 && isMultipleOf5) {
      print("$text1$text2");
    } else if (isMultipleOf3) {
      print(text1);
    } else if (isMultipleOf5) {
      print(text2);
    } else {
      print(i);
      count++;
    }
  }
  return count;
}
