/// 01 - OPERADORES Y ESTRUCTURAS DE CONTROL

void main() {
  // Variables
  int a = 10;
  int b = 4;

  // Operadores aritméticos
  print('Suma $a + $b = ${a + b}');
  print('Resta $a - $b = ${a - b}');
  print('Multiplicación $a * $b = ${a * b}');
  print('División $a / $b = ${a / b}');
  print('División sin decimal $a ~/ $b = ${a ~/ b}');
  print('Resto $a % $b = ${a % b}');

  // Operadores de comparación
  print("¿$a es == $b? ${a == b}");
  print("¿$a es != $b? ${a != b}");
  print("¿$a es > $b? ${a > b}");
  print("¿$a es < $b? ${a < b}");
  print("¿$a es >= $b? ${a >= b}");
  print("¿$a es <= $b? ${a <= b}");

  // Operadores lógicos
  print('AND: ¿$a es > 0 y $b es > 0? ${a > 0 && b > 0}');
  print('OR: ¿$a es > 0 o $b es > 0? ${a > 0 || b > 0}');
  print('NOT: ¿$a es lo contrario < 0? ${!(a > 0)}');

  // Operadores de asignación
  int number = 1;
  print(number);
  number += 1;
  print(number);
  number -= 1;
  print(number);
  number *= 2;
  print(number);
  number ~/= 2;
  print(number);
  number %= 2;
  print(number);

  double decimal = 3.0;
  decimal /= 3;
  print(decimal);

  // Operadores de identidad
  print('¿$a es int? ${a is int}');
  print('¿$a no es int? ${a is! int}');
  int c = a;
  int d = null ?? a;
  print('¿$c es $d son iguales? ${c == d}');

  // Operadores de bits
  print('AND: $a & $b = ${a & b}'); // 1010 & 0100 = 0000
  print('OR: $a | $b = ${a | b}'); // 1010 | 0100 = 1110
  print('XOR: $a ^ $b = ${a ^ b}'); // 1010 ^ 0100 = 1110
  print('NOT: ~$a = ${~a}'); // ~1010 = 0101

  print('Desplazamiento izquierda 10 << 2 = ${a << 2}'); // 1010 << 2 = 101000
  print('Desplazamiento derecha 10 >> 2 = ${a >> 2}'); // 1010 >> 2 = 0010

  // Condicionales
  if (a > b) {
    print('$a es mayor que $b');
  } else if (a < b) {
    print('$a es menor que $b');
  } else {
    print('$a es igual que $b');
  }

  switch (a) {
    case 1:
      print('$a es 1');
      break;
    case 2:
      print('$a es 2');
      break;
    default:
      print('$a No es 1 ni 2');
  }

  // Iterativas
  for (int i = 0; i < 10; i++) {
    print(i);
  }

  int i = 0;
  while (i < 10) {
    print(i);
    i++;
  }

  i = 0;
  do {
    print(i);
    i++;
  } while (i < 10);

  List<int> numbers = [1, 2, 3, 4, 5];
  for (int number in numbers) {
    print(number);
  }

  // Excepciones

  try {
    double result = a / 0;
    print(result);
  } on UnsupportedError {
    print('No se puede dividir por 0');
  } catch (e) {
    print(e);
  } finally {
    print('Ha finalizado la operación');
  }

  print('\n# EXTRA');
  /*
    Extra: Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
  */
  for (int i = 10; i <= 55; i++) {
    if (((i == 16) || ((i % 2) != 0)) || ((i % 3) == 0)) {
      continue;
    }
    print(i);
  }
}
