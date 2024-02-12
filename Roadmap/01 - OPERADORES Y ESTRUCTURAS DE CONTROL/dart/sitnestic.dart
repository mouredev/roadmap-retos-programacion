import 'dart:math';

void main() {
//* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
// Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
// (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
// https://dart.dev/language/operators

//* - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
//que representen todos los tipos de estructuras de control que existan en tu lenguaje:
//Condicionales, iterativas, excepciones...

//* - Debes hacer print por consola del resultado de todos los ejemplos.

  int a = 5;
  int b = 7;

  /// Operadores aritméticos
  print("""

  Operadores aritméticos""");
  print('a = $a; b = $b');
  var add = a + b;
  print('Add $a + $b =  $add');
  assert(a + b == add);
  var subtract = a - b;
  print('Subtract $a - $b =  $subtract');
  assert(a - b == subtract);
  var reverse = -subtract;
  print(
      'Unary minus, also known as negation (reverse the sign of the expression) -$subtract =  $reverse');
  var multiply = a * b;
  print('Multiply $a * $b =  $multiply');
  assert(a * b == multiply);
  var divide = b / a;
  print('Divide $b / $a =  $divide');
  assert(b / a == divide); // Result is a double
  var divideInteger = b ~/ a;
  print('Divide, returning an integer result $b ~/ $a =  $divideInteger');
  assert(b ~/ a == divideInteger); // Result is an int
  var modulo = b % a;
  print('Get the remainder of an integer division (modulo) $b % $a =  $modulo');
  assert(b % a == modulo); // Remainder

  /// Igualdad y operadores relacionales
  print("""

  Igualdad y operadores relacionales""");
  print('a = $a; b = $b');
  var greaterThan = a > b;
  print('Greater than >: $b > $a es $greaterThan');
  assert(b > a);
  var lessThan = a < b;
  print('Less than <: $a < $b es $lessThan');
  assert(a < b);
  var greaterThanOrEqual = a >= b;
  print('Greater than or equal to >=: $a >= $b es $greaterThanOrEqual');
  assert(b >= a);
  var lessThanOrEqual = a <= b;
  print('Less than or equal to <=: $a <= $b es $lessThanOrEqual');
  assert(a <= b);
  var equal = a == b;
  print('Equal; see discussion below ==: $a == $b es $equal');
  assert(a == a);
  var notEqual = a != b;
  print('Not equal !=: $a != $b es $notEqual');
  assert(a != b);

  /// Operadores de prueba de tipo
  print("""

  Operadores de prueba de tipo""");
  String typeString = 'GSF';
  // Using is to compare
  print(typeString is String);

  double typeDouble = 3.3;
  // Using is! to compare
  print(typeDouble is! int);

  /// Operadores de asignación
  print("""

  Operadores de asignación""");
  print('a = $a; b = $b');
  var assignment = a * b; //
  print('=(Simple Assignment ) $assignment = $a * $b');
  var nullAssignment = null;
  nullAssignment ??= a + b;
  print(
      '??=(Assign the value only if the variable is null) $nullAssignment ??= $a + $b');
  nullAssignment ??= a * b;
  print(
      '??=(Assign the value only if the variable is null) $nullAssignment ??= $a * $b ===> Not assigned because is not null');
  a += 10; //
  print('a += 10  == $a');
  a -= 5; //
  print('a -= 5  == $a');
  a *= 2; //
  print('a *= 2  == $a');
  nullAssignment /= 2; //
  print('d /= 2  == $nullAssignment');
  a %= 3; //
  print('a %= 3  == $a');

  /// Operadores lógicos
  print("""

  Operadores  lógicos""");
  print('a = $a; b = $b');
  var foo = a + b;
  var bar = b - a;
  print(
      'logical AND: $a + $b == $foo && $b - $a == $bar es ${a + b == foo && b - a == bar}');
  print(
      'logical OR: $a + $b == $foo || $b - $a == $bar es ${a + b == foo || b - a == bar}');
  print(
      'inverts the following expression (changes false to true, and vice versa): !true es ${!true}');

  /// Expresiones condicionales
  print("""

  Expresiones condicionales""");
  bool isPublic = Random().nextBool();
  var visibility = isPublic ? 'public' : 'private';
  print(visibility);

  String nameNull(String? name) => name ?? 'Guest';
  print(nameNull(null));

  // Slightly longer version uses ?: operator.
  String nameLongNull(String? name) => name != null ? name : 'Guest';
  print(nameLongNull(null));

// Very long version uses if-else statement.
  String nameVeryLongNull(String? name) {
    if (name != null) {
      return name;
    } else {
      return 'Guest';
    }
  }

  print(nameVeryLongNull(null));

  /// Iterativas
  /// for
  for (var i = 0; i < 10; i++) {
    print(i);
  }

  /// while
  int j = 0;
  while (j <= 10) {
    print(j);
    j += 1;
  }

  // Excepciones
  int x = 12;
  int y = 0;

  ///Try - on
  try {
    var res = x ~/ y;
    print(res);
  } on UnsupportedError {
    print("Cannot dive by zero");
  }

  ///Try - catch
  try {
    var res = x ~/ y;
    print(res);
  } catch (e) {
    print(e);
  }

  /// Ambos juntos + finally

  try {
    var res = x ~/ y;
    print(res);
  } on UnsupportedError {
    print("Cannot dive by zero");
  } catch (e) {
    print(e);
  } finally {
    print("finally try");
  }

  /// bit a bit
  final value = 0x22;
  final bitmask = 0x0f;

  assert((value & bitmask) == 0x02); // AND
  assert((value & ~bitmask) == 0x20); // AND NOT
  assert((value | bitmask) == 0x2f); // OR
  assert((value ^ bitmask) == 0x2d); // XOR

  assert((value << 4) == 0x220); // Shift left
  assert((value >> 4) == 0x02); // Shift right

  // Shift right example that results in different behavior on web
  // because the operand value changes when masked to 32 bits:
  assert((-value >> 4) == -0x03);

  assert((value >>> 4) == 0x02); // Unsigned shift right
  assert((-value >>> 4) > 0); // Unsigned shift right

  /// Other operators
  print("""

  Operadores ...""");
  print('a = $a; b = $b');
  // Performing Bitwise AND on a and b
  var bitwiseAND = a & b;
  print('Bitwise AND $bitwiseAND = $a & $b');

  // Performing Bitwise OR on a and b
  var bitwiseOR = a | b;
  print('Bitwise OR $bitwiseOR = $a | $b');

  // Performing Bitwise XOR on a and b
  var bitwiseXOR = a ^ b;
  print('Bitwise XOR $bitwiseXOR = $a ^ $b');

  // Performing Bitwise NOT on a
  var bitwiseNOT = ~a;
  print('Bitwise NOT $bitwiseNOT = ~$a');

  // Performing left shift on a
  var leftShift = a << b;
  print('left shift $leftShift = $a << $b');

  // Performing right shift on a
  var rightShift = a >> b;
  print('right shift $rightShift = $a >> $b');

//*! DIFICULTAD EXTRA (opcional):
//Crea un programa que imprima por consola todos los números comprendidos
//entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
  int opcional10 = 10;
  int opcional55 = 55;
  for (int i = opcional10; i <= opcional55; i++) {
    if ((i % 2 == 0) & (i != 16) & (i % 3 != 0)) {
      print(i);
    }
  }
}
