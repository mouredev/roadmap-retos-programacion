/// #04 CADENAS DE CARACTERES

void main() {
  String cadena = "Hola Mundo!";

  print('Primer caracter: ${cadena[0]}');

  print('Subcadena: ${cadena.substring(0, 4)}');

  print('Longitud: ${cadena.length}');

  print('Eliminar espacios: ${cadena.trim()}');

  print('Concatenación: ${cadena + " " + cadena}');

  print('Repetición: ${cadena * 3}');

  print('Recorrido: ${cadena.split("").toList()}');

  print('División: ${cadena.split(" ")}');

  print('Unión: ${cadena.split(" ").join(" - ")}');

  print('Mayúsculas: ${cadena.toUpperCase()}');

  print('Minúsculas: ${cadena.toLowerCase()}');

  print('Reemplazo: ${cadena.replaceAll("o", "0")}');

  // Validaciones
  print('Es vacío: ${cadena.isEmpty}');

  print('Existe la letra "o": ${cadena.contains("o")}');

  print('Validar si es un número: ${cadena.contains(new RegExp(r'[0-9]'))}');

  print('Empieza por "Hola": ${cadena.startsWith("Hola")}');

  print('Termina por "Mundo!": ${cadena.endsWith("Mundo!")}');

  print('Posición de la letra "M": ${cadena.indexOf("M")}');

  print('Posición de la última letra "o": ${cadena.lastIndexOf("o")}');

  print('Posición de un carácter que no existe: ${cadena.indexOf("x")}'); // -1

  var noAlphanumericIndex = cadena.indexOf(new RegExp(r'[^0-9a-z\s]', caseSensitive: false));
  print('Carácter no alfanumérico: ${cadena[noAlphanumericIndex]}');

  var numero = "123";
  print('Transformar a número: ${int.parse(numero)}');
  print('Transformar a número: ${double.parse(numero)}');
  // print('Transformar a número: ${int.parse(cadena)}'); // Error
  print('Transformar a número: ${int.tryParse(cadena)}'); // null
  print('Transformar a cadena: ${numero.toString()}');

  // Extra
  String palindrome = 'Logré ver gol.';
  print('¿Es palíndromo "$palindrome"? ${isPalindrome(palindrome)}');

  String word1 = 'Brasil';
  String word2 = 'Silbar';
  print('¿Son anagramas "$word1" y "$word2"? ${isAnagram(word1, word2)}');

  String isogram = 'Centrifugadlos';
  print('¿Es isograma "$isogram"? ${isIsogram(isogram)}');

  String isogram2 = 'bebe';
  print('¿Es isograma de segundo ordern "$isogram2"? ${isIsogram(isogram2)}');

  print('Compruebo el caso contrario:');
  print(isPalindrome('No palindromo'));
  print(isAnagram('No', 'Anagrama'));
  print(isIsogram('No isograma'));
}

// Reemplar carácteres no alfabéticos y acentos y pasar a minúsculas
List<String> getCharList(String cadena) {
  cadena = cadena.toLowerCase();
  String accents = 'áéíóúü';
  String noAccents = 'aeiouu';
  for (int i = 0; i < accents.length; i++) {
    cadena = cadena.replaceAll(accents[i], noAccents[i]);
  }
  cadena = cadena.replaceAll(new RegExp(r'[^a-z]'), '');

  return cadena.split('').toList();
}

bool isPalindrome(String phrase) {
  var characters = getCharList(phrase);

  return characters.join() == characters.reversed.join();
}

bool isAnagram(String word1, String word2) {
  var characters1 = getCharList(word1);
  var characters2 = getCharList(word2);

  characters1.sort();
  characters2.sort();

  return characters1.join() == characters2.join();
}

bool isIsogram(String word) {
  List<String> characters = getCharList(word);
  Map<String, int> charactersCount = {};
  for (var character in characters) {
    charactersCount[character] = (charactersCount[character] ?? 0) + 1;
  }

  var firstCount = charactersCount.values.first;

  return charactersCount.values.every((count) => count == firstCount);
}
