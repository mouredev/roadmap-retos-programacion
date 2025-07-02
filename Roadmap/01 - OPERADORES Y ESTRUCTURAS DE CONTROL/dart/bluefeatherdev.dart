// ignore_for_file: unnecessary_type_check, dead_code, unnecessary_null_comparison

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
  /// ------- [Operadores] del lenguaje Dart -------
  
  // Operadores aritméticos
  num a = 2;
  num b = 3;

  num miSuma = a + b;
  num miResta = a - b;
  num miReverso = -a;
  num miProducto = a * b;
  num miDivision = a / b;
  num miDivisionEntera = a ~/ b;
  num miModulo = a % b;

  print('Suma: $miSuma');
  print('Resta: $miResta');
  print('Reverso: $miReverso');
  print('Producto: $miProducto');
  print('División: $miDivision');
  print('División entera: $miDivisionEntera');
  print('Módulo: $miModulo');

  // Operadores prefix y profix
  int x;
  int y;

  x = 0;
  y = ++x;  // Incrementa x ANTES de asignar valor y
  print(x == y);  // 1 == 1

  x = 0;
  y = x++;  // Incrementa x DESPUÉS de asignar valor y
  print(x == y);  // 1 != 0

  x = 0;
  y = --x;  // Decrementa x ANTES de asignar valor y
  print(x == y);  // -1 == -1

  x = 0;
  y = x--;  // Decrementa x DESPUÉS de asignar valor y
  print(x == y);  // 0 == -1

  // Operadores de igualdad y relacionales
  print(a == b);  // Igual que
  print(a != b);  // Diferente que
  print(a > b); // Mayor que
  print(a < b); // Menor que
  print(a >= b);  // Mayor o igual que
  print(a <= b);  // Menor o igual que

  // Operadores de testeo de tipos
  dynamic miValor = 46;

  print(miValor is int);      // true
  print(miValor is double);   // false
  print(miValor is num);      // true
  print(miValor is String);   // false

  print(miValor is! int);      // false
  print(miValor is! double);   // true
  print(miValor is! num);      // false
  print(miValor is! String);   // true

  var miNumero = miValor as int;  /// `as` para casting seguro
  print(miNumero + 10); // 56

  // Operadores de asignación
  int miInt = 1;
  num miNum = 1;

  print(miNum = 2);    /// `=` : miNum = value : asignación simple
  print(miNum += 2);   /// `+=` : miNum = miNum + value : asignación con suma
  print(miNum -= 2);   /// `-=` : miNum = miNum - value : asignación con resta
  print(miNum *= 2);   /// `*=` : miNum = miNum * value : asignación con multiplicación
  print(miNum /= 2);   /// `/=` : miNum = miNum / value : asignación con división
  print(miNum %= 2);   /// `%=` : miNum = miNum % value : asignación con módulo
  print(miInt ^= 2);   /// `^=` : miInt = miInt ^ value : asignación con XOR 
  print(miInt >>>= 2); /// `>>>=` : miInt = miInt >>> value : asignación con shift sin signo a la derecha
  print(miInt <<= 2);  /// `<<=` : miInt = miInt << value : asignación con desplazamiento a la izquierda
  print(miInt >>= 2);  /// `>>=` : miInt = miInt >> value : asignación con desplazamiento a la derecha
  print(miInt &= 2);   /// `&=` : miInt = miInt & value : asignación con AND
  print(miInt |= 2);   /// `|=` : miInt = miInt | value : asignación con OR
  print(miNum ~/= 2);  /// `~/=` : miNum = miNum ~/ value : asignación con división entera

  // Operadores lógicos
  bool c = true;
  bool d = false;

  print(!c);      /// `!` : Invertir valor booleano
  print(c || d);  /// `||` : OR
  print(c && d);  /// `&&` : AND

  // Operadores de bits y shifts
  final miValorBit = 0x22;
  final miMascaraBit = 0x0f;

  print(miValorBit & miMascaraBit);  /// `&` : AND
  print(miValorBit & ~miMascaraBit); /// `& ~` : AND NOT
  print(miValorBit | miMascaraBit);  /// `|` : OR
  print(miValorBit ^ miMascaraBit);  /// `^` : XOR

  print(miValorBit << 4);  /// `<<` : Shift left
  print(miValorBit >> 4);  /// `>>` : Shift right
  print(miValorBit >>> 4); /// `>>>` : Unsigned shift right
  print(-miValorBit >>> 4);  /// `>>>` : Unsigned shift right

  // Operadores para expresiones condicionales

  /// condition `?` true `:` false
  var esPublico = true;
  var visibilidad = esPublico ? 'public' : 'private';
  print(visibilidad); // Imprime: 'public'

  /// expr1 `??` expr2
  String userName(String? name) => name ?? 'Guest';
  print(userName('Jesús')); // Imprime: Jesús
  print(userName(null));  // Imprime: Guest

  /// Un poco más verboso con `?` y `:`
  String userName2(String? name) =>
    name != null ? name : 'Guest';
  print(userName2('Jesús')); // Imprime: Jesús
  print(userName2(null));  // Imprime: Guest

  // Operadores de notación cascada
  var miBuffer = StringBuffer();
  miBuffer.write('¡Hola');  /// Sin operadores
  miBuffer.write(', ');     /// de
  miBuffer.write('Dart!');  /// notación cascada
  print(miBuffer);  // Imprime: ¡Hola, Dart!

  var miOtroBuffer = StringBuffer()
    ..write('¡Hola')  /// `..`
    ..write(', ')
    ..write('Dart!');
  print(miOtroBuffer);  // Imprime: ¡Hola, Dart!

  StringBuffer? miNullableBuffer;
  miNullableBuffer
    ?..write('¡Hola') /// `?..`
    ..write(', ')
    ..write('Dart!');
  print(miNullableBuffer);  // Imprime: null

  // Operadores de propagación
  var e = [10, 20, 30];
  var f = [40, 50, 60];
  print([...e + f]);  // [10, 20, 30, 40, 50, 60]

  // Operadores de identidad (no existen, es una función de alto nivel)
  var g = [1, 2, 3];
  var h = g;
  var i = [1, 2, 3];

  print(identical(g, h)); // true : misma instancia
  print(identical(g, i)); // false : mismo contenido, instancia distinta
  print(g == i);  // true : igualdad de contenido

  // Operadores de pertenencia (no existen, son métodos de colecciones)
  var miLista = [10, 20, 30];
  var miMapa = {'a': 1, 'b': 2};

  print(miLista.contains(20));  // true
  print(miMapa.containsKey('a')); // true
  print(miMapa.containsValue(3)); // false

  /// ------- [Estructuras de control] de lenguaje Dart -------
  
  // For loop
  for (var i = 0; i < 5; i++) {
    print('i: $i');
  }

  var frutas = ['manzana', 'banana', 'naranja'];
  for (var fruta in frutas) print(fruta);

  // ForEach
  var miColeccion = [1, 2, 3];
  miColeccion.forEach(print);

  // While loop
  var j = 0;
  while (j < 5) {
    print('j: $j');
    j++;
  }

  var k = 0;
  while (k < frutas.length) {
    print(frutas[k]);
    k++;
  }

  // Do while loop
  var l = 0;
  do {
    print('l: $l');
    l++;
  } while (l < 5);

  var m = 0;
  do {
    print(frutas[m]);
    m++;
  } while (m < frutas.length);

  // if
  var isRaining = true;
  if (isRaining) {
    print('Está lloviendo ☔');
  }

  // if else
  var userAge = 15;
  if (userAge >= 18) {
    print('¡Puedes conducir!');
  } else {
    print('Debes ser mayor de edad');
  }

  // if else if 
  isRaining = false;
  var isSnowing = true;
  if (isRaining) {
    print('Está lloviendo ☔');
  } else if (isSnowing) {
    print('Está nevando ❄️');
  } else {
    print('Cielo despejado ⛅');
  }

  // if case
  var par = [1, 2];
  if (par case [int x, int y]) {
    print('$x, $y');
  }

  // Switch
  bool? nullableBool = null;
  switch (nullableBool) {
    case true:
      print('yes');
    case false:
      print('no');
    default:
      print('null accepted');
  }

  /// Throw
  /// ```dart
  /// throw FormatException('Some text');
  /// throw 'Out of llamas!';
  /// ``` 
  
  /// Try
  /// ```dart
  /// try {
  ///   dynamic foo = true;
  ///   print(foo++);
  /// } catch (e) {
  ///   print('Error: $e');
  /// } finally {
  ///   print('It\'s done');
  /// }
  /// ```
  
  // assert
  var myText = 'abc';
  assert(myText != null, 'Text must be not null');
  print(myText != null);  // true

  /// ------- [Programa extra] en Dart -------
  
  /// Números pares entre 10 y 55 incluidos,
  /// Sin el 16 y sin múltiplos de 3:
  for (var i = 10; i < 56; i++) {
    if ((i % 2 == 0 && !(i % 3 == 0)) || i == 55) {
      if (i != 16) {
        print(i);
      }
    }
  }
}
