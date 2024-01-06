/*
    EJERCICIO:
    1) Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
    2) Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
    3) Crea una variable (y una constante si el lenguaje lo soporta).
    4) Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    5) Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
 */

// 1) https://dart.dev/guides

// 2) Comentario de una linea y varias

/*
  Comentario de varias lineas
 */

void main() {
  // 3) Variable y constante
  var variable = "texto";
  const pi = 3.1416;
  // 4) Tipos de variables primitivas o Tipos incorporados https://dart.dev/language/built-in-types
  // valores con tipo de dato dinamico
  dynamic variableDinamica = 'Hola';
  var variableVariable = 123;
  // variable que pude ser null, se agrega ?
  String? name = null;

  // Tipos numericos dart
  int numeroInt = 123;
  BigInt numeroBigInt = BigInt.from(123456789);
  double numeroDouble = 123.123;

  // Tipos texto
  String texto = 'texto';

  // Tipos boleano
  bool boolVerdadero = true;
  bool boolFalso = false;

  // Tipos list, record, sets y maps
  List<int> lista = [1, 2, 3, 4, 5, 6];
  Record registro = ('primero', a: 2, b: true, 'ultimo');
  Set<String> conjunto = {'rojo', 'cafe', 'azul'};
  Map<int, String> diccionario = {
    1: 'primero',
    2: 'segundo',
    3: 'tercero',
  };

  // 5) print Dart
  print("¡Hola, Dart!");
}
