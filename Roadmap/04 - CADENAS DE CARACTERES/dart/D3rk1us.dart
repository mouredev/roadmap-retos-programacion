/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
 */

void main() {

  String cadena1 = 'Cadena con comillas simples.';
  String cadena2 = "Cadena con comillas dobles.";
  String cadena3 = '''
  Cadena
  multilinea 
  de tres comillas simples''';

  print(cadena1);
  print(cadena2);
  print(cadena3);

  // Subcadenas
  print(cadena1.substring(0, 10));

  // Longitud
  print(cadena2.length);

  // Concatenación
  print("Concatenación: " + cadena2); 

  // Repetición
  for (int i = 0; i <= 2; i++) {
    print('Repetición');
  }

  // Recorrido
  for (var c = 0; c < cadena2.length; c++) {
    print(cadena2[c]);
  }
  
  // Conversión a mayúsculas y minúsculas
  print(cadena1.toUpperCase());
  print(cadena3.toLowerCase());

  // Reemplazo
  print(cadena2.replaceAll('Cadena', 'Ejemplo'));

  // División
  print(cadena1.split(' '));

  // Unión
  print(cadena1.split(' ').join('-'));

  // Interpolación
  print("Esto es una $cadena2");

  // Verificación
  print(cadena1 == cadena2);
  print(cadena1.compareTo(cadena3));

  /*
  * DIFICULTAD EXTRA (opcional):
  * Crea un programa que analice dos palabras diferentes y realice comprobaciones
  * para descubrir si son:
  * - Palíndromos
  * - Anagramas
  * - Isogramas
  */

  String palabra1 = 'ana';
  String palabra2 = 'amor';

  print('$palabra1: ${palindromo(palabra1)}');
  print('$palabra2: ${palindromo(palabra2)}');

  print('$palabra1 y $palabra2: ${anagrama(palabra1, palabra2)}');

  print('$palabra1: ${isograma(palabra1)}');
  print('$palabra2: ${isograma(palabra2)}');

}

String palindromo(String palabra) {
  
  var palPalabra = palabra.split('').reversed.join();
  
  if (palabra == palPalabra) {
    return 'Es un palíndromo';
  } else {
    return 'No es palíndromo';
  }
}

String anagrama(String palabra1, String palabra2) {
  
  var anPalabra1 = palabra1.split('');
  anPalabra1.sort();
  
  var anPalabra2 = palabra2.split('');
  anPalabra2.sort();
 
  if (anPalabra1.join() == anPalabra2.join()) {
    return 'Son anagramas.';
  } else {
    return 'No son anagramas.';
  }
}

String isograma(String palabra) {
  int count = 0;
  var comprobar = palabra.split('');

  for (int i = 0; i < comprobar.length; i++) {

    for (var caracter in comprobar) {
      if (caracter == palabra[i]) {
        count += 1;
        if (count == 2) {
          return 'No es Isograma';
        }
      }
    }
    count = 0;
  }
  return 'Es un Isograma.';
}