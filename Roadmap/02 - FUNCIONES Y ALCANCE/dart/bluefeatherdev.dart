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

/// 1. Ejemplo de una función en Dart:
void greet(String name) {
  print('Hello, $name!');
}

/// 2. Función sin parámetro ni retorno:
void greet2() {
  print('Hello, stranger!');
}

/// 3. Función con parámetro, sin retorno:
void greet3(String name) {
  print('How are you, $name?');
}

/// 4. Función con parámetro y retorno:
String greet4(String name) {
  return 'Hello, $name!';
}

/// 5. Función con varios parámetros y retorno:
String showAge(String name, int age) {
  return '$name is $age years old!';
}

/// 6. Funciones dentro de funciones:
int calculate(int x) {
  int doubleIt(int n) {
    return n * 2;
  }

  int squareIt(int n) {
    return n * n;
  }

  return squareIt(doubleIt(x));
}

/// 7. Algunas funciones del lenguaje:
void someBuiltInFunctions() {
  // print()
  print('Hello, Dart!');

  // int.parse()
  int myInt = int.parse('23');
  print(myInt); // 23

  // double.parse()
  double myDouble = double.parse('15.23');
  print(myDouble);  // 15.23

  // .toString()
  num myNum = 19;
  print(myNum.toString());  // '19'

  // .length
  List<int> myList = [1, 2, 3];
  print(myList.length); // 3

  // .contains()
  print(myList.contains(2));  // true

  // .map() and toList()
  var listToDouble = myList
    .map((e) => e * 2)
    .toList();
  print(listToDouble); // [2, 4, 6]

  // .where() and toList()
  var evens = myList
    .where((e) => e % 2 == 0)
    .toList();
  print(evens); // [2]

  // .split()
  var words = 'One, two, three'.split(', ');
  print(words); // [One, two, three] 

  // .toUpperCase()
  print('dart'.toUpperCase());  // DART
}

/// 8. Variable local:
List<int> countTo(int n) {
  var myLocalList = <int>[];
  for (var i = 0; i < n; i++) {
    myLocalList.add(i);
  }
  return myLocalList;
}

/// 9. Variable global
List<int> myGlobalList = [0, 1, 2];
void someFunction1() {
  var myLocalList = <int>[3, 4];
  myGlobalList += myLocalList;
}

/// 10. Funciones flecha
String greet5(String name) => 'Hello, $name!';

/// 11. Parámetros nombrados:
int? sum({int? a, int? b}) {
  if (a != null && b != null) return a + b;
  return null;
}

/// 12. Parámetros nombrados con valores por defecto:
String showMessage({
  String author = 'Unknown', 
  String msg = 'No message',
}) {
  return '$author: $msg';
}

/// 13. Parámetros nombrados obligatorios:
String greet6({required String fistName, String? lastName}) {
  if (lastName != null) return 'Hello, $fistName $lastName!';
  return 'Hello, $fistName!';
}

/// 14. Parámetros opcionales:
String greet7(String from, String msg, [String? device]) {
  var result = '$from says $msg';
  if (device != null) {
    result = '$result with a $device';
  }
  return result;
}

/// 15. Parámetros opcionales con valores por defecto:
String greet8(
  String from, 
  String msg, 
  [String? device = 'carrier pigeon']
) {
  var result = '$from says $msg with a $device';
  return result;
} 

/// 16. Funciones como parámetros:
void thisFunction(void Function() thatFunction) {
  print('Doing thisFunction...');
  thatFunction();
}

void thatFunction() {
  print('Doing thatFunction...');
}

/// 17. Funciones como parámetros de métodos:
void printElement(int element) {
  print('printElement: $element');
}

/// 18. Funciones asignadas a variables:
var greet9 = (name) => 'Hello, $name!';

/// 19. Uso de function types:
void greet10(String name, {String greeting = 'Hello'}) {
  print('$greeting, $name!');
}

void Function(String, {String greeting}) g = greet10;

/// 20. Uso de typedef en function types:
typedef Greeter = void Function(String, {String greeting});
Greeter g2 = greet10;

/// 21. Funciones anónimas:
void doSomething(int a, int b, Function operation) {
  final result = operation(a, b);
  print('Result: $result');
}

/// 22. Clausuras léxicas:
Function makeAdder(int addBy) {
  return (int i) => addBy + i;
}

/// 23. Tear-off:
var globalCodes = [15, 16, 19, 23];
var globalBuffer = StringBuffer();

/// 24. Retornar múltiples valores:
(String, int) greet11() {
  return ('Hello', 23);
}

/// [DIFICULTAD EXTRA]:
int specialFunction(String a, String b) {
  int count = 0;
  for (var i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      print('$i: $a $b');
    } else if (i % 3 == 0) {
      print('$i: $a');
    } else if (i % 5 == 0) {
      print('$i: $b');
    } else {
      print('$i:');
      count++;
    }
  }
  return count;
}

/// 0. Función principal de alto nivel,
/// sirve como punto de entrada a toda app;
/// el argumento `List<String> args` es opcional:
void main() {
  /// 1. Ejemplo de una función en Dart:
  greet('Jesús'); // 'Hello, Jesús!'

  /// 2. Función sin parámetros ni retorno:
  greet2(); // 'Hello, stranger!'

  /// 3. Función con parámetros, sin retorno:
  greet3('Jesús'); // 'How are you, Jesús?'
  
  /// 4. Función con parámetros y retorno:
  print(greet4('Jesús')); // 'Hello, Jesús!'

  /// 5. Función con varios parámetros y retorno:
  print(showAge('Jesús', 21)); // 'Jesús is 21 years old!'

  /// 6. Funciones dentro de funciones:
  print(calculate(3));  // 36 → (3 * 2 = 6, 6 * 6 = 36)

  /// 7. Algunas funciones del lenguaje:
  someBuiltInFunctions(); // ...

  /// 8. Variable local:
  print(countTo(5)); // [0, 1, 2, 3, 4]

  /// 9. Variable global:
  print(myGlobalList); // [0, 1, 2]
  someFunction1();
  print(myGlobalList); // [0, 1, 2, 3, 4]

  /// 10. Funciones flecha
  print(greet5('Jesús')); // Hello, Jesús!

  /// 11. Parámetros nombrados:
  print(sum()); // null
  print(sum(a: 5, b: 6)); // 11

  /// 12. Parámetros nombrados con valores por defecto:
  print(showMessage()); // Unknown: No message
  print(showMessage(author: 'Jesús'));  // Jesús: No message
  print(showMessage(author: 'Jesús', msg: 'Keep it up!')); // Jesús: Keep it up!

  /// 13. Parámetros nombrados obligatorios:
  print(greet6(fistName: 'Jesús')); // Hello, Jesús!
  print(greet6(fistName: 'Jesús', lastName: 'Domínguez')); // Hello, Jesús Domínguez!

  /// 14. Parámetros opcionales:
  print(greet7('Jesús', 'Good evening')); // Jesús says Good evening
  print(greet7('Jesús', 'Good evening', 'Laptop')); // Jesús says Good evening with a Laptop

  /// 15. Parámetros opcionales con valores por defecto:
  print(greet8('Jesús', 'Good evening')); // Jesús says Good evening with a carrier pigeon
  print(greet8('Jesús', 'Good evening', 'Smartphone')); // Jesús says Good evening with a Smartphone

  /// 16. Funciones como parámetros:
  thisFunction(thatFunction); // ...

  /// 17. Funciones como parámetros de métodos:
  var myList = [1, 2, 3];
  myList.forEach(printElement); // ...

  /// 18. Funciones asignadas a variables:
  print(greet9('Jesús')); // Hello, Jesús!

  /// 19. Uso de function types:
  g('Jesús', greeting: 'Howdy');  // Howdy, Jesús!

  /// 20. Uso de typedef en function types:
  g2('Jesús', greeting: 'Howdy');  // Howdy, Jesús!

  /// 21. Funciones anónimas:
  doSomething(1, 5, (x, y) {return x + y;}); // Result: 6
  doSomething(2, 3, (x, y) => x * y); // Result: 6

  /// 22. Clausuras léxicas:
  var add2 = makeAdder(2);
  var add4 = makeAdder(4);
  var add6 = makeAdder(6);
  print(add2(3)); // 5 (3 + 2)
  print(add4(1)); // 5 (4 + 1)
  print(add6(-1)); // 5 (-1 + 6)

  /// 23. Tear-off:
  globalCodes.forEach(print); // Function, OK
  globalCodes.forEach(globalBuffer.write);  // Method, OK

  /// 24. Retornar múltiples valores:
  print(greet11()); // (Hello!, 23)

  /// [DIFICULTAD EXTRA]:
  print(specialFunction('fizz', 'buzz')); // 53
}
