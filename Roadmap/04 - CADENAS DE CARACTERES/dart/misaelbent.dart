import 'dart:io';

import 'package:string/string.dart' as string;

void main(List<String> arguments) {
  print('''

ANALIZADOR DE PALABRAS
** Para empezar escribe dos palabras que creas son, palindromas, anagramas y/o isogramas

''');
  stdout.write('Ingresa la primera palabra: ');
  String? firstWord = stdin.readLineSync();
  stdout.write('Ingresa la primera palabra: ');
  String? SecondtWord = stdin.readLineSync();

  getWordsRelations(firstWord!, SecondtWord!);
  exit(0);
}

//OPERACIONES CON CADENAS DE CARACTERES

//CREAR
//Texto de una sola linea
String name = 'Misael';
String lastName = 'Bent';
//Texto multi linea
String parrafo = '''
Soy
programador
''';

//CONCATENACION

//Concatenacion con operador +
String fullName = name + ' ' + fullName;

//Concatenacion con interpolacion
String newFullName = '$name, $fullName';

//OBTENER LONGITUD DE LA CADENA
int nameLength = name.length;

//ACCEDER A CARACTER DE LA CADENA
String someCharacter = name[0];

//METODOS SOBRE CADENAS

//Poner todo en mayusculas
String upercase = name.toUpperCase();

//Poner en minusculas
String lowercase = name.toLowerCase();

//Quitar espacios entre caracteres
String fullnameWithOutSpace = fullName.trim();

//Obtener una subcadena de un acadena
String subString = fullName.substring(
    0, 4); //Recibe la posicion incial y final para la subcadena

//Verificar si dentro de una cadena hay otra cadena
bool isMisael = fullName.contains('Misael');

//Reemplazar todas las ocurrencias de una subcadena
String newName = fullName.replaceAll('Misael', 'Carlos');

//Reeemplazar la primera ocurrencia
String repeat = 'Corre, Lola corre, por favor, corre';
String newRepeat = repeat.replaceFirst('Corre', 'run'); //

//Separar las cadenas segun un separador
String example = 'Este, es un ejemplo';
List<String> words = example.split(','); // ['Este', 'es un ejemplo']
List<String> words2 = example.split(' '); //['Este,', 'es', 'un', 'ejemplo']

//Encontrar el indice de la primera ocurrencia
int first = fullName.indexOf('Bent');

//COMPARACION
bool isEqual = name == lastName;

//Comprobar si una cadena empeiza o termina por otra cadena
bool startWith = fullName.startsWith('Misael');
bool endWith = fullName.endsWith('Misael');

//EJERCIO EXTRA
getWordsRelations(String firstWord, String secondWord) {
  print('''
-- ANALISIS DE LAS PALABRAS --

1. Palindormas:
${isPalindromeWord(firstWord)}
${isPalindromeWord(secondWord)}

2. Isogramas: 
${isIsogram(firstWord)}
${isIsogram(secondWord)}

3. Anagramas:
${isAnagram(firstWord, secondWord)}
''');
}

//Esta funcion evalua si la palabra es palindroma
String isPalindromeWord(String word) {
  word.toLowerCase();
  List<String> first = word.split('');
  first = first.reversed.toList();
  String second = first.join();
  if (word.toLowerCase() == second.toLowerCase()) {
    return 'La palabra $word es palindroma';
  } else {
    return 'La palabra $word No es palindroma';
  }
}

//Esta funcion evalua si la palabra es un isograma
String isIsogram(String word) {
  List<String> first = word.toLowerCase().split('');
  Set<String> firstSet = Set.from(first);
  if (first.length == firstSet.length) {
    return 'La palabra $word es un isograma';
  } else {
    return 'La palabra $word NO es un isograma';
  }
}

//Esta funcion evalua si las palabras entre ellas son anagramas
String isAnagram(String firstWord, String secondWord) {
  List<String> first = firstWord.toLowerCase().split('');
  List<String> second = secondWord.toLowerCase().split('');
  first.sort();
  second.sort();
  if (first.join() == second.join()) {
    return 'Las palabra $secondWord es un anagrama de $firstWord';
  } else {
    return 'Las palabras $firstWord y $secondWord no son anagramas';
  }
}
