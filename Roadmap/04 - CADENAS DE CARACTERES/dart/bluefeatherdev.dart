/*
* EJERCICIO:
* Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
* en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
* - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
*   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
*
* DIFICULTAD EXTRA (opcional):
* Crea un programa que analice dos palabras diferentes y realice comprobaciones
* para descubrir si son:
* - Palíndromos
* - Anagramas
* - Isogramas
*/

/// [DIFICULTAD EXTRA]:
void checkTwoWords(String word1, String word2) {
  /// Analizar si son [palíndromos] individualmente:
  var reversedWord1 = word1.split('').reversed.join();
  var reversedWord2 = word2.split('').reversed.join();
  print('¿"$word1" es palíndrome? : ${word1 == reversedWord1}');
  print('¿"$word2" es palíndrome? : ${word2 == reversedWord2}');

  /// Analizar si son [anagramas] entre sí:
  dynamic charsWord1 = word1.split('')..sort();
  dynamic charsWord2 = word2.split('')..sort();
  charsWord1 = charsWord1.join();
  charsWord2 = charsWord2.join();
  print('¿"$word1" y "$word2" son anagramas? : ${charsWord1 == charsWord2}');

  /// Analizar si son [isogramas] individualmente:
  bool isIsogram(String word) {
    bool isIsogramWord = true;
    Set setWord = word.split('').toSet();
    List listWord = setWord.toList();
    for (var char in listWord) {
      var countChar = RegExp(char).allMatches(word).length;
      if (countChar > 1) { 
        isIsogramWord = false;
        break;
      }
    }
    return isIsogramWord;
  }
  print('¿"$word1" es un isograma? : ${isIsogram(word1)}');
  print('¿"$word2" es un isograma? : ${isIsogram(word2)}');
}

void main() {
  /// Cadenas de ejemplo para operaciones:
  String myString = 'Hello, Dart!';
  String text1 = 'Blue';
  String text2 = 'Feather';
  String text3 = 'Banana';
  String text4 = '  Hello  ';
  
  /// 1. [Concatenación]:
  print(text1 + ' ' + text2);             // Blue Feather
  print('Blue' ' ' 'Feather');            // Blue Feather

  /// 2. [Repetición]:
  print(text1 * 2);                       // BlueBlue
  print(text2 * 3);                       // FeatherFeatherFeather

  /// 3. [Indexación]:
  print(text1[0]);                        // B
  print(text1[1]);                        // l
  print(text1[2]);                        // u
  print(text1[3]);                        // e
  print(text1[text1.length - 1]);         // e

  /// 4. [Longitud]:
  print(text1.length);                    // 4

  /// 5. [Slicing]:
  print(myString.substring(0, 5));        // Hello
  print(myString.substring(7, 11));       // Dart

  /// 6. [Búsqueda]:
  print(myString.contains('Dart'));       // true

  /// 7. [Reemplazo]:
  print(text3.replaceAll('a', 'e'));      // Benene
  print(text3.replaceAllMapped('a', 
    (w) => 'e'                            // Benene
  ));  
  print(text3.replaceFirst('a', 'e'));    // Benana
  print(text3.replaceFirstMapped('a', 
    (w) => 'e'                            // Benana
  ));  
  print(text3.replaceRange(0, 2, 'Le'));  // Lenana

  /// 8. [División]:
  print(myString.split(', '));            // [Hello, Dart!]

  /// 9. [Mayúsculas y minúsculas]:
  print(myString.toLowerCase());          // hello, dart!
  print(myString.toUpperCase());          // HELLO, DART!

  /// 10. [Eliminar espacio en extremos]:
  print(text4.trim());                    // hello
  print(text4.trimLeft());                // hello  
  print(text4.trimRight());               //   hello  

  /// 11. [Búsqueda al principio y al final]:
  print(text1.startsWith('B'));           // true
  print(text1.startsWith('b'));           // false
  print(text1.endsWith('e'));             // true
  print(text1.endsWith('E'));             // false

  /// 12. [Búsqueda de posición]:
  print(text1.indexOf('u'));              // 2
  print(myString.indexOf('Dart'));        // 7

  /// 13. [Búsqueda de ocurrencias]:
  final countA 
    = RegExp('a').allMatches(text3).length;
  print(countA);                          // 3

  /// 14. [Interpolación]:
  print('text1: ${text1}');               // text1: Blue
  print('text2: ${text2}');               // text2: Feather
  print('text3: ${text3}');               // text3: Banana

  /// 15. [Lista de caracteres]:
  print(text1.split(''));                 // [B, l, u, e]
  print(text2.split(''));                 // [F, e, a, t, h, e, r]
  print(text3.split(''));                 // [B, a, n, a, n, a]

  /// 16. [Lista de cadenas a cadena]:
  List<String> list = [text1, ' ', text2];
  print(list.join());                     // Blue Feather

  /// 17. [Cadenas a tipos numéricos]:
  print(int.parse('23'));                 // 23
  print(double.parse('1.6180'));          // 1.818
  print(num.parse('23'));                 // 23
  print(num.parse('1.6180'));             // 1.818

  /// 18. Otros métodos: `.allMatches()`:
  var exp = RegExp(r'a');
  var found = exp.allMatches(text3);
  for (var match in found) {
    print('Match "${match.group(0)}" en posición ${match.start}');
  }

  /// 19. Otros métodos: `.codeUnitAt()`:
  print(text1.codeUnitAt(0));             // 66              
  print(text1.codeUnitAt(1));             // 108    
  print(text1.codeUnitAt(2));             // 117
  print(text1.codeUnitAt(3));             // 101

  /// 20. Otros métodos: `.compareTo()`:
  print(text1.compareTo(text1));          // 0
  print(text1.compareTo(text2));          // -1
  print(text1.compareTo(text3));          // 1 

  /// 21. Otros métodos: `.lastIndexOf()`:
  print(text3.lastIndexOf('a'));          // 5

  /// 22. Otros métodos: `.matchAsPrefix()`:
  var regExp = RegExp(r'Dart');
  var match = regExp.matchAsPrefix(myString, 7);
  print(match);                           // Match found

  /// 23. Otros métodos: `.padLeft()`:
  print(myString.padLeft(16, '+'));       // ++++Hello, Dart!

  /// 24. Otros métodos: `.padRight()`:
  print(myString.padRight(16, '+'));      // Hello, Dart!++++
  
  /// 25. Otros métodos: `.splitMapJoin()`:
  print(text4.splitMapJoin(RegExp(r'Hello'),
    onMatch: (m) => '${m[0]}',
    onNonMatch: (n) => '*',
  ));                                     // *Hello*

  /// 25. Otros métodos: `.toString()`:
  print(23.toString());                   // '23'

  /// 26. [Getters de String]:
  print(myString.codeUnits);              // [72, 101, 108, 108, 111, 44, 32, 68, 97, 114, 116, 33]
  print(myString.hashCode);               // 181428680
  print(myString.isEmpty);                // false
  print(myString.isNotEmpty);             // true
  print(myString.length);                 // 12
  print(myString.runes);                  // (72, 101, 108, 108, 111, 44, 32, 68, 97, 114, 116, 33)
  print(myString.runtimeType);            // String

  /// 27. Operador `*` en String:
  print('Hello' * 2);                     // HelloHello

  /// 28. Operador `+` en String:
  print('Hello' + ' ' + 'Dart');          // Hello Dart

  /// 29. Operador `==` en String:
  print('Flutter' == 'React');            // False

  /// 30. Operador `!=` en String:
  print('Flutter' != 'React');            // True

  /// 31. Operador `[]` en String:
  print('Hello'[1]);                      // e

  /// [DIFICULTAD EXTRA]:
  checkTwoWords('ana', 'john');           // ejemplo para palíndromes
  checkTwoWords('amor', 'roma');          // ejemplo para anagramas
  checkTwoWords('hola', 'hello');         // ejemplo para isogramas
}
