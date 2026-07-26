import 'dart:io';

import '../../00 - SINTAXIS, VARIABLES, TIPOS DE DATOS Y HOLA MUNDO/dart/evelynnobile.dart';
import 'raulfauli.dart';

void main() {
  /* 
    * Los Strings son inmutables. Aunque no puedan modificarse puedes crear un nuevo String a traves sus métodos.
    * Se reprensentan por una secuencia de unidades en codigo Unicode UTF-16. 
    Esto permite al lenguaje guardar los números en memoria en un Code Unit de 16 bits. a excepción de emojis y
    caracteres especiales (ej chinos) que se almacenan en 2 pares de 16 bits (pares sustitutos).
    Esto implica que emojis generen el doble de longitud (en vez de un .length de 1 da 2). 
  */

  stdout.write(
    '\n*************** Caracteres *******************************\n',
  );
  String word = 'Esternocleidomastoideo';

  stdout.write('\n<< Operadores >>\n\n');

  print('La palabra tiene ${word.length} letras');
  print('La segunda letra es: ${word[1]}');
  print('La palabra repetida 3 veces: ${(word + ' ') * 3}');

  stdout.write('\n<< Posicionamiento especial >>\n\n');

  print('Código Unicode de la primera letra: ${word.codeUnitAt(0)}'); // E = 69
  print('Tiene el código hash: ${word.hashCode}');
  print('Las runas de la palabra son: ${word.runes}'); // devuelve un iterable
  // termino simil a Go que muestra el code point unico sin importar el numero de bloques de 16 bits.

  stdout.write('\n<< Busquedas >>\n\n');

  print(
    '¿La palabra contiene a "${word.substring(7, 13)}"?: ${word.contains('cleido')}',
  );
  print(
    '¿La palabra comienza con "${word.substring(0, 5)}"?: ${word.startsWith('Ester')}',
  );
  print(
    '¿La palabra termina con "${word.substring(13, 18)}"?: ${word.endsWith('masto')}',
  );
  print(
    '¿El fragmento "${word.substring(18, 22)}" empieza en la letra ${word.indexOf('ideo')}',
  );
  // De no conincidir el String devuelve el valor int -1

  String sentence = 'Soy una oración loca';
  print('La oración tiene ${'a'.allMatches(sentence).length} "a"');

  stdout.write('\n<< Transformaciones >>\n\n');

  print('Oración en mayúsculas: ${sentence.toUpperCase()}');

  // Un entero puede transformarse a String, no es el caso del String a lista como en Python.

  String connectWords(String sentence) {
    List<String> quotationSentence = sentence
        .splitMapJoin(
          RegExp(r'\s+'), // Busca uno o más espacios
          onMatch: (match) => match[0]!, // Mantiene los espacios intactos
          onNonMatch: (word) => '"$word"',
        )
        .split(' ');
    // Split() convierte el String en una lista de tipo String para trabajar con los metodos deseados

    if (sentence.isNotEmpty) {
      String result = quotationSentence.length == 1
          ? quotationSentence.first
          : '${quotationSentence.sublist(0, quotationSentence.length - 1).join(', ')} y ${quotationSentence.last}';
      return result;
    }
    return 'No se ha encontrado palabras';
  }

  print('Palabras entre comillas y con nexo "y": ${connectWords(sentence)}');

  String spacingWord = '    hola    ';
  print('Palabras sin espacios: ${spacingWord.trim()}');

  String saludo = 'Hola hola. ¿Cómo andas?';
  print(
    '${saludo.replaceAll(RegExp(r'\bhola\b', caseSensitive: false), 'chau')}',
  );

  stdout.write(
    '\n************** Creación de string con StringBuffer  **************\n',
  );

  var sb = StringBuffer();
  sb
    ..write('Usa un StringBuffer para una ')
    ..writeAll(['eficiente', 'creación', 'de String'], ' ')
    ..write('.');

  var fullString = sb.toString();
  // De esta forma se crea un String (una vez que se aplica toString()) al que se añaden otras cadenas

  print(fullString);

  String word2 = 'Hola';
  String word3 = 'Chau';
  print(word2.compareTo(word3)); // 1
  // devuelve -1 si la primer palabra es menor, 0 si son iguales y 1 si es mayor alfabeticamente.

  stdout.write('\n**************** Extra ***********************\n\n');

  bool success = false;
  String wordSecondInput = '', wordInput = '';
  void checkWords(String word, String wordSecond) {
    stdout.write('Ingrese la primer palabra: ');
    wordInput = stdin.readLineSync() ?? '';
    stdout.write('Ingrese la segunda palabra: ');
    wordSecondInput = stdin.readLineSync() ?? '';

    word = wordInput.toLowerCase().trim();
    wordSecond = wordSecondInput.toLowerCase().trim();
    // Se eliminan espacios y se pasan a minusculas

    List<String> listWord = word.split('').toList();
    List<String> listWordSecond = wordSecond.split('').toList();
    bool checkPalindrome() {
      List<String> listWordReversed = listWord.reversed.toList();

      if (listWordReversed.join() == listWordSecond.join()) {
        print('¡Las palabras "$word" y "$wordSecond" son bifrontes!');
        // es lo inverso :o
        success = true;
      }
      if (listWord.reversed.join() == listWord.join()) {
        print('$word es un palíndromo');
        success = true;
      }
      if (listWordSecond.reversed.join() == listWordSecond.join()) {
        print('$wordSecond es un palíndromo');
        success = true;
      }

      return success;
      // ! De forma nativa en dart la unica forma de comparar el contenido de listas
      // ! sin importar paquetes es convertirlas en string
      // Alternativa -> paquete collection y su método listEquals()
    }

    bool checkAnagram() {
      if (listWord.toSet().containsAll(listWordSecond) &&
          listWordSecond.toSet().containsAll(listWord)) {
        print('¡Las palabras "$word" y "$wordSecond" son anagramas!');
        success = true;
      }
      return success;
    }

    bool checkIsogram(String word) {
      Map<String, int> isoMap = {};
      for (String letter in word.split('')) {
        isoMap[letter] = (isoMap[letter] ?? 0) + 1;
      }
      bool isIsogram = true;
      List values = isoMap.values.toList();
      int isogramLength = values[0];

      for (int wordCount in values) {
        if (wordCount != isogramLength) {
          isIsogram = false;
          break;
        }
      }
      if (isIsogram) {
        print('La palabra $word es un isograma de grado $isogramLength');
        return success = true;
      }
      return success;
    }

    if (wordInput.isEmpty || wordSecondInput.isEmpty) {
      print('Ingrese ambas palabras');
    }

    if (word.length >= 3 &&
        wordSecond.length >= 3 &&
        word != wordSecond &&
        !wordInput.isEmpty &&
        !wordSecondInput.isEmpty) {
      checkIsogram(word);
      checkIsogram(wordSecond);
      checkAnagram();
      checkPalindrome();
    }

    if (word.length < 3 || wordSecond.length < 3) {
      print('Las palabras deben tener al menos 4 letras');
    }

    if (word == wordSecond && !wordInput.isEmpty && !wordSecondInput.isEmpty) {
      print('Las palabras son iguales ingrese dos palabras diferentes');
    }
    if (word != wordSecond &&
        !success &&
        !wordInput.isEmpty &&
        !wordSecondInput.isEmpty &&
        word.length >= 3 &&
        wordSecond.length >= 3) {
      print('No se encontraron palindromos, anagramas o isogramas');
    }
  }

  checkWords(wordInput, wordSecondInput);
}
