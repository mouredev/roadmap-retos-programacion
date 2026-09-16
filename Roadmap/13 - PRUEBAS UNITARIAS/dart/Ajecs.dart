import 'dart:io';

/*
  Con el fin de realizar una prueba unitaria es recomendable utilizar la librería nativa "test".
  ! Esto implica crear el archivo pubspec.yaml. 
  Para evitar esto, y debido a la simpleza del ejercicio, se puede aplicar el método assert() para 
  evaluar el comportamiento de la función. 
  * Las aserciones se visualizan solo habilitando el "modo aserción" mediante el flag --enable-asserts
  (ej -> dart --enable-asserts Ajecs.dart)
*/

void main() {
  stdout.writeln('\n****************** Pruebas unitarias ******************\n');

  num sumNumbers(num num1, num num2) {
    if (num1 is! int || num2 is! int) {
      throw ArgumentError('Ambos argumentos deben ser números enteros.');
    } else
      return num1 + num2 * 3; // No concuerda con la aserción.
  }

  void testSumNumbers() {
    assert(
      sumNumbers(2, 3) == 5,
      'Error: 2 + 3 debería ser 5 😐',
    ); // "AssertionError"
    // El mensaje del assert solo se muestra cuando se evalúa como false.
    //  El programa se detiene y se muestra en terminal el mensaje del assert.
  }

  // testSumNumbers();

  print('¡Todas las pruebas pasaron con éxito!');

  print('El resultado de la suma es: ${sumNumbers(2, 3)}');

  stdout.writeln(
    '\n********************** Extra ***************************\n',
  );

  String nativeDateParse(DateTime date) {
    int day = date.day;
    int month = date.month;
    int year = date.year;
    return '${day.toString().padLeft(2, '0')}-${month.toString().padLeft(2, '0')}-$year';
  }

  Map<String, dynamic> programmer = {
    'name': 'Nicolás Coriale',
    'age': 39,
    'birthdate': nativeDateParse(DateTime(1986, 9, 7)),
    'languages': ['Dart', 'Javascript', 'Python', 2], // AssertionError
  };

  print(programmer['birthdate']);

  void testAllFields() {
    assert(
      [
        'name',
        'age',
        'birthdate',
        'address', // Campo que no existe en el mapa
      ].every((field) => programmer.containsKey(field)),
      'El mapa no contiene todos los campos solicitados',
    );
  }

  void testCorrectData() {
    assert(
      programmer['name'].runtimeType == String,
      'El nombre debe ser una cadena',
    );
    assert(programmer['age'].runtimeType == int, 'La edad debe ser un entero');
    assert(
      programmer['birthdate'].runtimeType == String,
      'La fecha debe ser un String',
    );
    assert(
      programmer['languages'].runtimeType == List<String>,
      '\nLos lenguajes debe ser una Lista de String',
    );
  }

  print('');
  // testAllFields();
  testCorrectData();
}
