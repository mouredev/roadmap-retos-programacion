/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 */

void main() {
  print("### OPERADORES ###");

  // Operadores Aritméticos
  print("\n--- Aritméticos ---");
  var a = 10;
  var b = 3;
  print("Suma: 10 + 3 = ${a + b}");
  print("Resta: 10 - 3 = ${a - b}");
  print("Multiplicación: 10 * 3 = ${a * b}");
  print("División: 10 / 3 = ${a / b}");
  print("División entera: 10 ~/ 3 = ${a ~/ b}");
  print("Módulo: 10 % 3 = ${a % b}");

  // Operadores Lógicos
  print("\n--- Lógicos ---");
  print("AND (true && false): ${true && false}");
  print("OR (true || false): ${true || false}");
  print("NOT (!true): ${!true}");

  // Operadores de Comparación
  print("\n--- Comparación ---");
  print("Igualdad (10 == 3): ${10 == 3}");
  print("Desigualdad (10 != 3): ${10 != 3}");

  // Operadores de Asignación
  print("\n--- Asignación ---");
  var x = 5;
  x += 2;
  print("Suma y asignación: x += 2 -> x = $x");

  // Operador de tipo (is)
  print("\n--- Pertenencia/Tipo (is) ---");
  var texto = "Hola";
  print("¿La variable 'texto' es un String? ${texto is String}");

  // Operadores de Bits
  print("\n--- Bits ---");
  var p = 10; // 1010
  var q = 3;  // 0011
  print("AND a nivel de bits (10 & 3): ${p & q}");
  print("OR a nivel de bits (10 | 3): ${p | q}");

  /*
   * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
   *   que representen todos los tipos de estructuras de control que existan
   *   en tu lenguaje:
   *   Condicionales, iterativas, excepciones...
   */

  print("\n### ESTRUCTURAS DE CONTROL ###");

  // Condicionales
  print("\n--- Condicionales (if, else) ---");
  var edad = 18;
  if (edad < 18) {
    print("Eres menor de edad.");
  } else {
    print("Eres mayor de edad.");
  }

  // Iterativas
  print("\n--- Iterativas (for) ---");
  for (var i = 1; i <= 3; i++) {
    print(i);
  }

  print("\n--- Iterativas (while) ---");
  var contador = 3;
  while (contador > 0) {
    print(contador);
    contador--;
  }

  // Excepciones
  print("\n--- Excepciones (try, catch) ---");
  try {
    throw Exception('Este es un error de ejemplo');
  } catch (e) {
    print("Se capturó una excepción: $e");
  }

  /*
   * DIFICULTAD EXTRA (opcional):
   * Crea un programa que imprima por consola todos los números comprendidos
   * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
   */

  print("\n### DIFICULTAD EXTRA ###");
  for (var numero = 10; numero <= 55; numero++) {
    if (numero % 2 == 0 && numero != 16 && numero % 3 != 0) {
      print(numero);
    }
  }
}
