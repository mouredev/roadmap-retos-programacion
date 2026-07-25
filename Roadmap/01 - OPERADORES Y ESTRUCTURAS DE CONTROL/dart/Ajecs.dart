import 'dart:io';

void main() {
  print(
    '************************ Operadores aritméticos **************************',
  );
  print('');

  print('Operador suma de 10 + 3: ${10 + 3}');
  print('Operador resta de 10 - 3: ${10 - 3}');
  print('Operador multiplicación de 10 * 3: ${10 * 3}');
  print('Operador division de 10 / 3: ${10 / 3}');
  print('Operador resto de 10 % 3: ${10 % 3}');

  print('Operador división entera 10 ~/ 3: ${10 ~/ 3}');

  print('');
  print(
    '********************** Operadores de comparación **************************',
  );
  print('');

  int val = 1;

  print('Operador mayor a > resulta: ${val > 0}'); // true
  print('Operador menor a < resulta: ${val < 0}'); // false
  print('Operador menor o igual <= resulta: ${val <= 1}'); // true
  print('Operador mayor o igual >= resulta: ${val >= 1}'); // true
  print('Operador igualdad == resulta: ${val == 1}'); // true
  print('Operador desigualdad != resulta: ${val != 1}'); // false

  // ! Dart no tiene operador exponencial ): aunque usa la funcion de la librería dart:math -> pow().

  // ! No existe un operador de identidad como es el caso de JavaScript con "===" se usa identical().
  // ! Tampoco de pertenencia como en pytho con "in" -> se usa contains().

  print('');

  print(
    '************************* Operadores de asignación ************************',
  );
  print('');

  num value = 5;
  print(
    'Si añado 3: ${value += 3}. y le resto 6: ${value -= 6}. Y lo multipico por 3: ${value *= 3}.  Y lo divido por 2: ${value ~/= 2}',
  );

  print('');
  print(
    '******************** Operadores de Lógicos ********************************',
  );
  print('');

  print(
    'operador OR ej. -> 10 + 4 = 14 || 2 + 2 = 6 es: ${10 + 4 == 18 || 2 + 2 == 4}',
  );
  // Ya que una de las dos condiciones se cumple
  print(
    'operador AND ej. -> 10 + 4 = 14 && 2 + 2 = 6 es: ${10 + 4 == 18 && 2 + 2 == 4}',
  );
  // Ya que una de las dos condiciones NO se cumple

  print('operador NOT ej. -> !(2 + 2 = 4) es: ${!(2 + 2 == 4)}'); // false
  print('');

  int or = 5 | 3; // 101 | 011
  int and = 5 & 3; // 101 & 011
  int xor = 5 ^ 3; // 101 ^ 011
  String orBinary = or.toRadixString(2).padLeft(3, '0');
  // PadLeft genera un valor fijo de digitos a los que se le agrega ceros a la izquierda de ser necesario.
  String andBinary = and.toRadixString(2).padLeft(3, '0');
  String xorBinary = xor.toRadixString(2).padLeft(3, '0');

  print('operador de bits OR ej -> 5 | 3 resulta en: $orBinary');
  print('operador de bits AND ej -> 5 & 3 resulta en: $andBinary');
  print('operador de bits XOR ej -> 5 ^ 3 resulta en: $xorBinary');

  /*
    ! Dart no devuelve un valor binario en la operaciones de bits, sino su expresión entera. Con el fin contrario se aplica el método toRadixString()
    Que es una conversión que devuelve un String.
  */

  // ---------------------- Estructuras de control ------------------------------

  // Estructuras condicionales

  print('');
  print(
    '******************** Ejemplo de estructura if/else if/ else ****************************',
  );
  print('');

  int suma = 4 + 2;
  if (suma > 6) {
    print('El resultado es mayor a 6');
  } else if (suma == 6) {
    print('El resultado es igual a 6');
  } else {
    print('El resultado es menor a 6');
  }

  print('');
  print('******************* Switch **************************');
  print('');

  int number1 = 10;
  int number2 = 2;
  String operation = 'equality';
  String divideNumbers() {
    int result = number1 ~/ number2;
    String message = 'El resultado de la división es $result';
    return message;
  }

  String multiplyNumbers() {
    int result = number1 * number2;
    String message = 'El resultado de la multiplicación es $result';
    return message;
  }

  String equalNumbers() {
    String comparation = number1 == number2
        ? 'Los valores son iguales'
        : 'Los valores son distintos';
    return comparation;
  }

  switch (operation) {
    case 'multiply':
      print(multiplyNumbers());
    case 'divide':
      print(divideNumbers());
    case 'equality':
      print(equalNumbers());
    default:
      'Operación nula o desconocida';
  }

  print('');
  print(
    '*********************** Estructuras repetitivas ******************************',
  );
  print('');

  for (int i = 0; i <= 5; i++) {
    stdout.write(' $i');
  }
  print('');

  const names = ['Enzo', 'Julian', 'Lionel', 'Diego', 'Mariana'];

  stdout.write('Los nombres con "e" y con "o" son: ');

  List<String> filteredNames = names
      .where((name) => name.toLowerCase().contains('e') && name.contains('o'))
      .toList();

  if (filteredNames.isNotEmpty) {
    String resultado = filteredNames.length == 1
        ? filteredNames.first
        : '${filteredNames.sublist(0, filteredNames.length - 1).join(', ')} y ${filteredNames.last}';

    print(resultado);
  }

  int val3 = 1;
  while (val3 < 9) {
    stdout.write('${val3++} ');
  }

  stdout.write(
    '\n\n******************** Excepciones ***************************\n\n',
  );

  try {
    print('${10 ~/ 0}'); // Con división de punto flotante devuelve "infinity";
  } catch (error) {
    print('Se ha producido un error: $error');
  } finally {
    print('Ha finalizado la excepción');
  }

  stdout.write(
    '\n***************************** Ejercicio extra ************************\n',
  );

  stdout.write('Números pares, no multiplos de 3 sin el 16:\n');

  final start = 10;
  final end = 55;
  var range = Iterable.generate(
    (end - start) + 1,
    (i) => i + start,
  ).where((n) => n % 2 == 0 && n % 3 != 0 && n != 16);

  for (int i in range) stdout.write('$i ');
}

/* 
  El método más similar a range que posee dart es el método .generate aplicado al objeto Iterable.
  De esta forma por defecto se crea un iterable que comienza en 0 y debe expresarse un un límite. 
  Con el fin de que se comporte como el método range, se define un principio ('i + start') y se aplica 
  el método where aplicable a listas e iterables que filtra los valores solicitados.  
*/