/*
 * EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 *
 * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
 * debemos comenzar por el principio.
 */

// https://dart.dev/

/// Comentarios de
/// documentación.


/* Esto también es un comentario */


// Variables

late String color; // Es una variable que se establece antes de ser utilizada.

void main() {

  Object name = 'Clark';
  print(name);

  String surname = 'Kent';
  print(surname);

  int? number1 = 23; // Permite que el valor sea null.
  print(number1);

  int age = 35;
  print(age);

  color = 'black';
  print(color);

  final double price = 40.99;
  print(price);

  const double pi = 3.1415;
  print(pi);

  List numberList = [1, 2, 4];
  print(numberList);

  Set collection1 = {'one', 'four'};
  print(collection1);

  Map firstMap = {'name': 'John', 'surname': 'Constantine'};
  print(firstMap);

  print('¡Hola, Dart!');

}
