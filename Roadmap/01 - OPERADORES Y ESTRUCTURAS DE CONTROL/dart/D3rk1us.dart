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
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

void main() {
  
  var a, b, c, f, g;
  bool d, e;

  // Asignación

  a = 14;
  b = 40;

  d = true;
  e = false;

  f = Object();
  g = Object();

  // Aritméticos

  c = a + b;
  print(c);

  c = b - a;
  print(c);

  c = a / b;
  print(c);

  c = a % b;
  print(c);

  // Lógicos

  c = !d;
  print(c);

  c = d || e;
  print(c);

  c = e && d;
  print(c);

  // Comparación

  c = a > b;
  print(c);

  c = a < b;
  print(c);

  c = a == b;
  print(c);

  c = a != b;
  print(c);

  c = a <= b;
  print(c);

  c = a >= b;
  print(c);

  // Identidad

  print(f is int);
  print(g is! Object);
  
  // Condicionales

    c = a < b ? "True" : "False";
    print(c);

    c = a ?? b; // Si el valor de "a" fuera null, devuelve el valor de "b".
    print(c);


  /*
    * DIFICULTAD EXTRA (opcional):
    * Crea un programa que imprima por consola todos los números comprendidos
    * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
  */

  print("-------------------------------------------------");

  for (var i = 10; i <= 55; i++ ) {

    if (i % 2 == 0 && i != 16 && i % 3 != 0) {
      print(i);
    }
  }

}

