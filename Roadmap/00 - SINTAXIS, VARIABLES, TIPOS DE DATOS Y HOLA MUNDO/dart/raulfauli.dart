// https://dart.dev

// Comentario en línea

/* Comentario
en varias lineas */

void main() {
  // Variable
  var lenguaje = 'Dart';

  // Constante
  const PI = 3.14;
  final roadmaps = ['00', '01'];
  roadmaps.add('02');
  // roadmaps = ['02']; // Error

  // Tipos primitivos
  int number = 10;
  double decimal = 10.0;
  bool boolean = true;
  String string = "Text";

  dynamic dynamicVariable = 'Hola';
  dynamicVariable = 10;
  String? nullableString = null;

  List<int> punctuation = [10, 8, 9, 10];
  Set<String> languages = {'dart', 'java', 'python', 'c++', 'dart'};
  Map<String, dynamic> person = {'name': 'Raúl', 'age': 39, 'result': 9.25};

  // Imprime por terminal
  print('¡Hola, $lenguaje!');
}
