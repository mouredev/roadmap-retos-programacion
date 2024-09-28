//* - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
/// https://dart.dev

//* - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...)
// Comentarios de una sola línea
// TODO: comentario para TODO

/* Comentarios 
multilínea */

//! Comentarios de documentación
/**  Los comentarios de documentación son comentarios de varias líneas 
 * o de una sola línea que comienzan con /// or /**.  */ 
*/

/// Usando /// en líneas consecutivas
/// tiene el mismo efecto que un comentario
/// de documento de varias líneas.

void main() {
  //* - Crea una variable (y una constante si el lenguaje lo soporta)
  var variable = "Mi variable"; // variable
  const castante = "Mi constante"; // constante

  //* - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...)
  int integer = 1;
  double decimal = 1.5;
  bool boolean = true;
  String string1 = 'Mi cadena de texto con simple commilla';
  String string2 = "Mi cadena de texto con doble comilla";

  Object object = 'Not single type';
  dynamic dynamicVariable = 'Or dynamic if necessary';
  dynamicVariable = 80;

  // Null safety
  String? nullableString; // Nullable type. Can be `null` or string.

  List<int> integers = [1, 3, 4, 6, 25, 99];
  Set<String> languages = {'dart', 'java', 'python', 'c++', 'dart'};
  Map<String, dynamic> person = {'name': 'Gerard', 'age': 43, 'result': 9.25};

  //* - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
  print('¡Hola MoureDev, desde ${languages.first}!');
  print('integers $integers');
  print('languages $languages');
  person.forEach((key, value) {
    print('$key: $value');
  });
}
