/// URL del sitio web oficial: https://dart.dev/

import 'dart:io';

void main() {

  var dart = 'dart'; // Declaración de strings/cadena de caracterses
  var python = 'PYTHON';
  var python2 = 'python';
  var frase = '         Me gusta programar en dart     ';
  var multilinea = ''' Esto es un
  texto multilínea. 
  ¿Cómo estás? 
  ''';
  var mensaje = 'Hola, me llamo Marina';


  print('$dart + " " + $python'); // Concatenación de strings 
  /// Se interpola con ${}
  print(dart.toUpperCase()); // Convertir a mayúsculas
  print(python.toLowerCase()); // Convertir a minúsculas
  print(frase.trim()); // ELimina los espacios en blanco
  print(frase.startsWith('Me')); // Verificar si comienza con esa cadena
  print(frase.contains("programar")); // Verifica si contiene esa cadena
  print(dart == python); // Verificar si las dos cadenas son iguales
  print(python2.length); // Longitud de una candena
  print(mensaje.replaceAll("Marina", "María"));

  List<String> char = mensaje.split(''); // División de un string
  /// Esto es una forma de recorrer
  for (var caracteres in char) { // .runes lo divide en caracteres
    print(caracteres);
  }
  /// Otra forma de recorrer pero devuelve en Unicode
  for(var char in mensaje.runes) {
    print(char);
  }

  init();

}

/// Dificultad extra

void init() {
  print("Introduce una palabra: "); 
  var pal1 = (stdin.readLineSync())!.toLowerCase();
  List<String> pal1Split = pal1!.split('').toList();
  print("¿La palabra es isograma?: ${isograma(pal1Split)}");
  print("¿La palabra es un palíndromo?: ${palindromo(pal1Split)}");
  print("¿Las palabras son anagramas?: ${anagramas(pal1Split)}");
}

bool? isograma(List<String> palabra) {
  /// Isograma: Una frase/palabra donde no hay letras repetidas
  for (int i = 0; i < palabra.length - 1; i++) {
    for (int j = i + 1; j < palabra.length; j++) {
      if (palabra[i] == palabra[j]) {
        return false;
      }
    } 
  } return true;
}

bool? palindromo(List<String> palabra) {
if (palabra.join() == palabra.reversed.join()) {
  return true;
} else { return false; }
}

bool? anagramas(List<String> palabra1) {
  print("Introduce otra palabra: "); 
  var palabra2 = stdin.readLineSync();
  List<String> palabra2Split = palabra2!.split('').toList();
  
  if (palabra1.length != palabra2Split.length) {
    return false;
  }

  for (int i = 0; i < palabra1.length; i++) {
    if (!palabra2Split.contains(palabra1[i])) {
      return false;
    }
  }

  for (int j = 0; j < palabra2Split.length; j++) {
    if (!palabra1.contains(palabra2Split[j])) {
      return false;
    }
  }

  return true;
}
