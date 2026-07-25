/*
* ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
* - Recuerda que todas las instrucciones de participación están en el
*   repositorio de GitHub.
*
* Lo primero... ¿Ya has elegido un lenguaje?
* - No todos son iguales, pero sus fundamentos suelen ser comunes.
* - Este primer reto te servirá para familiarizarte con la forma de participar
*   enviando tus propias soluciones.
*
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

void main() {
  // https://dart.dev/

  // Esto es un comentario de una línea

  // Esto es un comentario de una línea,
  // que ocupa varias líneas,
  // para no ser demasiado largo.

  /*
    Esto es un comentario de varias líneas,
    puedes usar '*' para buenas prácticas,
    y también '-' si deseas listar información.
  */

  /*
  * ¡Comentarios de varias líneas!
  * - Usas '*' en cada línea
  * - En algunos editores y temas cambian de color
  * - En mi editor (Visual Studio Code) son de color verdes
  * - Uso Atom One Dark theme 
  */

  /// Estos son comentarios tipo documentación para Dart,
  /// puedes usar `` para especificar fragmentos de códigos,
  /// así como keywords. También puedes usar [] 
  /// para enfatizar términos clave
  
  /// Por ejemplo, `void main() {}`,
  /// es la [función de alto nivel],
  /// donde dejo mis respuestas.
  
  /// Puedes también especificar código de un lenguaje así:
  /// ```dart
  /// void main() {
  ///   print('Hello World!');
  /// }
  /// ```
  
  /// Crear una [variable] en Dart:
  var myNum = 23; // Forma 1
  print(myNum); // Imprime: 23

  int myOtherNum = 46; // Forma 2
  print(myOtherNum); // Imprime: 46

  /// Crear una [constante] en Dart:
  const myName = 'Jesús'; // Forma 1
  print(myName);  // Imprime: 'Jesús'
  
  const String myLastName = 'Domínguez'; // Forma 2
  print(myLastName);  // Imprime: 'Domínguez'

  final myEyeColor = 'Brown'; // Forma 3
  print(myEyeColor);  // Imprime: 'Brown'

  final String myHairColor = 'Black'; // Forma 4
  print(myHairColor);  // Imprime: 'Black'

  /// [Datos primitivos] del lenguaje Dart:
  
  // int
  var myInt = 1;
  var myInt2 = 0xDEADBEEF;
  var myInt3 = 1_000_000;

  print(myInt); // Imprime: 1
  print(myInt2);  // Imprime: 3735928559
  print(myInt3);  // Imprime: 1_000_000

  // double
  var myDouble = 1.23;
  var myDouble2 = 1.23e5;
  var myDouble3 = 0.000_000_1;

  print(myDouble);  // Imprime: 1.23
  print(myDouble2); // Imprime: 123000.0
  print(myDouble3); // Imprime: 1e-7

  // String
  var myString = 'Hello World!';
  var myString2 = "Hello World!";
  var myString3 = '"Hello" World!';
  var myString4 = "'Hello' World!";
  var myString5 = 'Hello\' World!';
  var myString6 = "Hello\" World!";
  var myString7 = 'Hello' ' ' 'World!';
  var myString8 = 'Hello' " " 'World!';
  var myString9 = '''Hello...
  ...World!''';
  var myString10 = """Hello...
  ...World!""";
  var myString11 = r'Hello World! + \n';
  

  print(myString);  // Imprime: Hello World!
  print(myString2); // Imprime: Hello World!
  print(myString3); // Imprime: "Hello" World!
  print(myString4); // Imprime: 'Hello' World!
  print(myString5); // Imprime: Hello' World!
  print(myString6); // Imprime: Hello" World!
  print(myString7); // Imprime: Hello World!
  print(myString8); // Imprime: Hello World!
  print(myString9); // Imprime: Hello... \n ...World!
  print(myString10); // Imprime: Hello... \n ...World!
  print(myString11); // Imprime: 'Hello World! + \n'

  // Booleans
  var myBool = true;
  var myBool2 = false;
  bool myBool3 = true;

  print(myBool);  // Imprime: true
  print(myBool2); // Imprime: false
  print(myBool3); // Imprime: true

  // Symbols
  print(#mySymbol); // Imprime: Symbol("mySymbol")

  Symbol mySymbol = #miIdentificador;
  print('Symbol: $mySymbol'); // Imprime: Symbol: Symbol("miIdentificador")

  // Runes
  Runes myRune = Runes('🎯');
  print('Runes: $myRune');  // Prints: Runes: (127919)
  print('Runes as char: ${String.fromCharCodes(myRune)}');  // Prints: Runes: 🎯

  /// Imprimir en la terminal ¡Hola, [nombreLenguaje]!
  print('¡Hola, Dart!');  // Imprime: ¡Hola, Dart!
}
