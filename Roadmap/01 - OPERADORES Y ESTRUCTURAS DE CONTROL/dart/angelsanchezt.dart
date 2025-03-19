/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

void main() {
  // Operadores
  // Aritméticos
  int suma = 5 + 3;
  int resta = 8 - 2;
  double division = 10 / 2;
  int multiplicacion = 4 * 6;
  int modulo = 15 % 4;

  // Lógicos
  bool and = true && false;
  bool or = true || false;
  bool not = !true;

  // De comparación
  bool igual = 5 == 5;
  bool noIgual = 5 != 3;
  bool mayorQue = 8 > 3;
  bool menorQue = 4 < 7;
  bool mayorIgual = 10 >= 10;
  bool menorIgual = 3 <= 5;

  // De asignación
  int x = 10;
  x += 5; // x = x + 5

  // De identidad
  String texto1 = "Hola";
  String texto2 = "Hola";
  bool identico = identical(texto1, texto2);

  // De pertenencia
  List<int> lista = [1, 2, 3, 4, 5];
  bool contiene = lista.contains(3);

  // Bits
  int a = 5; // Representado en binario como 0101
  int b = 3; // Representado en binario como 0011
  int resultadoBits = a & b; // AND bits: 0001

  print("Operadores:");
  print("Aritméticos: $suma, $resta, $division, $multiplicacion, $modulo");
  print("Lógicos: $and, $or, $not");
  print("De comparación: $igual, $noIgual, $mayorQue, $menorQue, $mayorIgual, $menorIgual");
  print("De asignación: $x");
  print("De identidad: $identico");
  print("De pertenencia: $contiene");
  print("Bits: $resultadoBits");

  // Estructuras de control
  // Condicionales
  if (x > 12) {
    print("x es mayor que 12");
  } else if (x == 12) {
    print("x es igual a 12");
  } else {
    print("x es menor que 12");
  }

  // Iterativas
  for (int i = 10; i <= 55; i++) {
    if (i % 2 == 0 && i != 16 && i % 3 != 0) {
      print("Número válido: $i");
    }
  }

  // Excepciones
  try {
    int resultadoDivisionPorCero = 5 ~/ 0; // Intento de división por cero
    print("Este mensaje no se imprimirá $resultadoDivisionPorCero");
  } catch (e) {
    print("Error: $e");
  }
}
