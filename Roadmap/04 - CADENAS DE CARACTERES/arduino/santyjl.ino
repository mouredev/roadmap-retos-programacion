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

String string1 = "Hola Mundo ";
String string2 = "esto es arduino";

void setup() {
  Serial.begin(9600);

  // Acceso a caracteres específicos
  char tercerCaracter = string1[2];
  Serial.print("Acceso a caracteres específicos: ");
  Serial.println(tercerCaracter);

  // Subcadenas
  String subcadena = string1.substring(0, 5);
  Serial.print("Subcadena: ");
  Serial.println(subcadena);

  // Longitud
  int longitud = string1.length();
  Serial.print("Longitud: ");
  Serial.println(longitud);

  // Concatenación
  String string3 = string1 + string2;
  Serial.print("Concatenación: ");
  Serial.println(string3);

  // Repetición
  String repeticiones = repetirCadena(string3, 2);
  Serial.print("Repeticiones: ");
  Serial.println(repeticiones);

  // Recorrido
  Serial.print("Recorrido: ");
  for (int i = 0; i < string3.length(); i++) {
    char caracter = string3[i];
    Serial.print(caracter);
  }
  Serial.println();

  // Conversión a mayúsculas y minúsculas
  string3.toUpperCase();
  Serial.print("Mayúsculas: ");
  Serial.println(string3);
  string3.toLowerCase();
  Serial.print("Minúsculas: ");
  Serial.println(string3);

  // Reemplazo
  string3.replace("Arduino", "microPython");
  Serial.print("Reemplazo: ");
  Serial.println(string3);

  // División
  int espacioIndex = string3.indexOf(' ');
  String primeraPalabra = string3.substring(0, espacioIndex);
  String segundaPalabra = string3.substring(espacioIndex + 1);
  Serial.print("División - Primera Palabra: ");
  Serial.println(primeraPalabra);
  Serial.print("División - Segunda Palabra: ");
  Serial.println(segundaPalabra);

  // Unión
  String concatenacion = primeraPalabra + " " + segundaPalabra;
  Serial.print("Unión: ");
  Serial.println(concatenacion);

  // Interpolación
  int variable = 42;
  String mensaje = "El valor de la variable es " + String(variable);
  Serial.print("Interpolación: ");
  Serial.println(mensaje);

  // Verificación
  if (string3.indexOf("arduino") != -1) {
    Serial.println("Contiene 'arduino'");
  }

  //extra reto
  String resultadoPalindromo = palindromo("reconocer");
  Serial.print("Palíndromo: ");
  Serial.println(resultadoPalindromo);

  String resultadoAnagramas = Anagramas("listen", "silent");
  Serial.print("Anagramas: ");
  Serial.println(resultadoAnagramas);

  String resultadoIsograma = isograma("murcielago");
  Serial.print("Isograma: ");
  Serial.println(resultadoIsograma);
}

void loop() {
  // Tu código en el loop, si es necesario
}

String repetirCadena(String cadena, int veces) {
  String resultado = "";
  for (int i = 0; i < veces; i++) {
    resultado += cadena;
  }
  return resultado;
}

String palindromo(String texto) {
  if (texto != invertirTexto(texto)) {
    return "no es un palíndromo";
  } else {
    return "si es un palíndromo";
  }
}

String Anagramas(String texto1, String texto2) {
  if (texto1.length() != texto2.length()) {
    return "no es un anagrama";
  }

  for (int i = 0; i < texto1.length(); i++) {
    char caracter = texto1[i];

    if (texto2.indexOf(caracter) == -1) {
      return "no es un anagrama";
    }
  }

  // Si pasa todas las verificaciones, son anagramas
  return "si es un anagrama";
}

String isograma(String texto) {
  for (int i = 0; i < texto.length(); i++) {
    char caracter = texto[i];

    if (texto.indexOf(caracter, i + 1) != -1) {
      return "no es un isograma";
    }
  }
  return "si es un isograma";
}

String invertirTexto(String texto) {
  String textoInvertido = "";
  int longitud = texto.length();

  for (int i = longitud - 1; i >= 0; i--) {
    textoInvertido += texto[i];
  }

  return textoInvertido;
}
