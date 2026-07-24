// https://dart.dev/

// Comentario de una línea.

/*
  Comentario de 
  varias líneas.
*/

/// Comentario de documentación de una línea: permite crear un vinculo entre corchetes (funciones, clases, variables, atributos y parametros) ej: [functionLinked].

void functionLinked() {
  // ...
}

/** 
  comentario de documentación de varias líneas 
  [variableLinked].
**/

/// Los doc comments permiten que el comando "dart doc" los encuentre en el código y genere una documentación en HTML.

int variableLinked = 5;

// Para buenas prácticas ver -> https://dart.dev/effective-dart/documentation



// -------------- Variables ---------------------

var nombre = "Juan"; // Variable de tipo dinámico (var).

// -------------- Constantes ---------------------

const PI = 3.14159; // Constante de tipo punto flotante (double).

// Tipos de datos primitivos

int num = 10; // Variable de tipo entero (int).
double decimal = 3.14; // Variable de tipo punto flotante (double).
bool truly = true; // Variable de tipo booleano (bool).
String text = "Hola, Dart!"; // Variable de tipo cadena de texto (String).

void main() {
  print("¡Hola, Dart!"); // Imprime un mensaje en la terminal.
}
