void main() {
  // Operadores Aritméticos
  int a = 10, b = 3;
  print("Aritméticos:");
  print("Suma: \${a + b}");
  print("Resta: \${a - b}");
  print("Multiplicación: \${a * b}");
  print("División: \${a / b}");
  print("División Entera: \${a ~/ b}");
  print("Módulo: \${a % b}");

  // Operadores Lógicos
  bool x = true, y = false;
  print("\nLógicos:");
  print("AND: \${x && y}");
  print("OR: \${x || y}");
  print("NOT: \${!x}");

  // Operadores de Comparación
  print("\nComparación:");
  print("Igualdad: \${a == b}");
  print("Desigualdad: \${a != b}");
  print("Mayor que: \${a > b}");
  print("Menor que: \${a < b}");
  print("Mayor o igual: \${a >= b}");
  print("Menor o igual: \${a <= b}");

  // Operadores de Asignación
  int c = 5;
  print("\nAsignación:");
  print("Inicial: \${c}");
  c += 3;
  print("Suma y asigna: \${c}");
  c *= 2;
  print("Multiplica y asigna: \${c}");

  // Operadores de Identidad
  print("\nIdentidad:");
  print("Idéntico: \${a == 10}");
  print("No Idéntico: \${b != 10}");

  // Operadores de Bits
  print("\nBits:");
  print("AND binario: \${a && b}");
  print("OR binario: \${a || b}");
  print("XOR binario: \${a ^ b}");
  print("Desplazamiento izquierda: \${a << 1}");
  print("Desplazamiento derecha: \${a >> 1}");

  // Estructuras de Control: Condicionales
  print("\nCondicionales:");
  if (a > b) {
    print("a es mayor que b");
  } else {
    print("a no es mayor que b");
  }

  // Estructuras de Control: Iterativas
  print("\nIterativas:");
  print("Bucle For:");
  for (int i = 0; i < 5; i++) {
    print("i: \${i}");
  }

  print("Bucle While:");
  int count = 0;
  while (count < 3) {
    print("count: \${count}");
    count++;
  }

  print("Bucle Do-While:");
  int num = 0;
  do {
    print("num: \${num}");
    num++;
  } while (num < 2);

  // Estructuras de Control: Excepciones
  print("\nExcepciones:");
  try {
    int result = a ~/ 0;
    print("Resultado: \${result}");
  } catch (e) {
    print("Error: División por cero");
  } finally {
    print("Bloque finally ejecutado");
  }

  // Dificultad Extra
  print("\nNúmeros entre 10 y 55 (pares, no 16 ni múltiplos de 3):");
  for(int i = 10; i<=55;i++){
    if(i == 16 || i % 3 == 0){
      continue;
    }
    if(i.isEven){
      print("\${i}");
    }   
  }
}