/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */


void main()
{
  //NOTA IMPORTANTE: En Dart, las cadenas de caracteres se pueden definir con comillas simples o dobles
  //                y se pueden usar indistintamente. En este ejemplo se usan comillas dobles.

  // Hay multitud de operaciones que se pueden realizar con cadenas de caracteres.
  // A continuación se muestran algunos ejemplos de las más comunes:

  String cadena = "Hola Mundo";
  
  // Substring -> devuelve una subcadena de la cadena original
  // indexOf -> devuelve la posición de la primera ocurrencia de un carácter
  print('Operación - Substring + indexOf: ${cadena.substring(0, cadena.indexOf(' '))}'); // Hola

  // length -> devuelve la longitud de la cadena
  print('Operación - length:  ${cadena.length}'); // 10
  
  // toUpperCase -> devuelve la cadena en mayúsculas
  print('Operación - toUpperCase: ${cadena.toUpperCase()}'); // HOLA MUNDO

  // toLowerCase -> devuelve la cadena en minúsculas
  print('Operación - toLowerCase: ${cadena.toLowerCase()}'); // hola mundo

  // replaceAll -> devuelve la cadena reemplazando todas las ocurrencias de un carácter por otro
  print('Operación - replaceAll: ${cadena.replaceAll('o', '0')}'); // H0la Mund0

  // replaceRange -> devuelve la cadena reemplazando los caracteres entre dos posiciones
  print('Operación - replaceRange: ${cadena.replaceRange(0, 4, 'Adios')}'); // Adios Mundo

  // replaceFirst -> devuelve la cadena reemplazando la primera ocurrencia de un carácter
  print('Operación - replaceFirst: ${cadena.replaceFirst('o', '0')}'); // H0la Mundo


  // split -> devuelve una lista de cadenas separadas por un carácter
  print('Operación - split: ${cadena.split(' ')}'); // [Hola, Mundo]

  // trim -> devuelve la cadena sin espacios al principio ni al final
  print('Operación - trim: ${cadena.trim()}'); // Hola Mundo

  // trimLeft -> devuelve la cadena sin espacios al principio
  print('Operación - trimLeft: ${cadena.trimLeft()}'); // Hola Mundo

  // trimRight -> devuelve la cadena sin espacios al final
  print('Operación - trimRight: ${cadena.trimRight()}'); // Hola Mundo

  // contains -> devuelve true si la cadena contiene un carácter o una subcadena
  print('Operación - contains(Hola): ${cadena.contains('Hola')}'); // true
  print('Operación - contains(M): ${cadena.contains('M')}'); // true
  print('Operación - contains(X): ${cadena.contains('X')}'); // true

  // startsWith -> devuelve true si la cadena empieza por un carácter o una subcadena
  print('Operación - startsWith(Hola): ${cadena.startsWith('Hola')}'); // true

  // endsWith -> devuelve true si la cadena termina por un carácter o una subcadena
  print('Operación - endsWith(do): ${cadena.endsWith('do')}'); // true

  // compareTo -> devuelve un número negativo si la cadena es menor que otra, 0 si son iguales
  // o un número positivo si la cadena es mayor que otra
  print('Operación - compareTo: ${cadena.compareTo('Hola Mundo')}'); // 0
  print('Operación - compareTo: ${cadena.compareTo('Hola Mundo!')}'); // -1
  print('Operación - compareTo: ${cadena.compareTo('H')}'); // 1

  // codeUnitAt -> devuelve el código Unicode de un carácter en una posición determinada
  print('Operación - codeUnitAt: ${cadena.codeUnitAt(0)}'); // 72

  // join -> devuelve una cadena uniendo los elementos de una lista
  List<String> lista = ['Hola', 'Mundo'];
  print('Operación - join: ${lista.join(' ')}'); // Hola Mundo

  //EJERCICIO EXTRA

  // Palíndromo
  String palindromo = "Dabale arroz a la zorra el abad";
  print('Es palíndromo "$palindromo": ${esPalindromo(palindromo)}'); // true 

  // Anagrama
  String palabra1 = "Mary";
  String palabra2 = "Army";
  print('Es anagrama "$palabra1" y "$palabra2"?: ${esAnagrama(palabra1, palabra2)}'); // true

  // Isograma
  String isograma = "Isograma";
  String isograma2 = "Murcielago";
  print('Es isograma "$isograma": ${esIsograma(isograma)}'); // false
  print('Es isograma "$isograma2": ${esIsograma(isograma2)}'); // true

}

bool esPalindromo(String cadena)
{
  //Limpiar espacios y convertir a minúsculas
  String cadenaLimpia = cadena.toLowerCase().replaceAll(' ', '');
  
  //Invertir cadena: 
  //  1º - convertir a minúsculas 
  //  2º - eliminar espacios 
  //  3º - convertir a lista
  //  4º - invertir lista 
  //  5º - convertir a cadena
  String cadenaInvertida = cadena.toLowerCase().replaceAll(' ', '').split('').reversed.join();

  if (cadenaLimpia == cadenaInvertida)
    return true;

  return false;
}

bool esAnagrama(String palabra1, String palabra2)
{

  //Convertir a minúsculas
  palabra1 = palabra1.toLowerCase();
  palabra2 = palabra2.toLowerCase();

  //Ambas palabras deben tener la misma longitud
  if (palabra1.length != palabra2.length)
    return false;

  // Todas las letras de la palabra1 deben estar en la palabra2
  for (int i = 0; i < palabra1.length; i++)
  {
    if (!palabra2.contains(palabra1[i]))
      return false;
  }

  // Todas las letras de la palabra2 deben estar en la palabra1
  for (int i = 0; i < palabra2.length; i++)
  {
    if (!palabra1.contains(palabra2[i]))
      return false;
  }  

  return true;
}

bool esIsograma(String cadena)
{
  //Convertir a minúsculas
  cadena = cadena.toLowerCase();

  //Recorrer la cadena
  for (int i = 0; i < cadena.length; i++)
  {
    //Si la cadena contiene más de una ocurrencia de un carácter, no es isograma
    if (cadena.indexOf(cadena[i]) != cadena.lastIndexOf(cadena[i]))
      return false;
  }

  return true;
}
