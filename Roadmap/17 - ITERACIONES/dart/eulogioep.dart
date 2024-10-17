/**
 * Demostración de diferentes mecanismos de iteración en Dart
 * 
 * Dart proporciona varios mecanismos de iteración, combinando
 * sintaxis familiar con características únicas del lenguaje.
 */

import 'dart:io' show stdout;

void main() {
  print('=== Demostración de Mecanismos de Iteración en Dart ===\n');

  // 1. Bucle for tradicional
  print('1. Usando bucle for tradicional:');
  void forLoop() {
    for (int i = 1; i <= 10; i++) {
      stdout.write('$i ');
    }
    print(''); // Nueva línea
  }
  forLoop();

  // 2. Bucle while
  print('\n2. Usando bucle while:');
  void whileLoop() {
    int contador = 1;
    while (contador <= 10) {
      stdout.write('$contador ');
      contador++;
    }
    print('');
  }
  whileLoop();

  // 3. Bucle do-while
  print('\n3. Usando bucle do-while:');
  void doWhileLoop() {
    int num = 1;
    do {
      stdout.write('$num ');
      num++;
    } while (num <= 10);
    print('');
  }
  doWhileLoop();

  // 4. forEach con List
  print('\n4. Usando forEach con List:');
  void forEachLoop() {
    List<int> numeros = List.generate(10, (index) => index + 1);
    numeros.forEach((numero) => stdout.write('$numero '));
    print('');
  }
  forEachLoop();

  // 5. for-in loop
  print('\n5. Usando for-in loop:');
  void forInLoop() {
    var numeros = List.generate(10, (index) => index + 1);
    for (var numero in numeros) {
      stdout.write('$numero ');
    }
    print('');
  }
  forInLoop();

  // 6. Usando Iterable.generate
  print('\n6. Usando Iterable.generate:');
  void iterableGenerate() {
    var numeros = Iterable.generate(10, (index) => index + 1);
    numeros.forEach((numero) => stdout.write('$numero '));
    print('');
  }
  iterableGenerate();

  // 7. Usando map
  print('\n7. Usando map:');
  void mapExample() {
    var numeros = List.generate(10, (index) => index + 1);
    numeros.map((numero) => stdout.write('$numero ')).toList();
    print('');
  }
  mapExample();

  // 8. Usando Iterador personalizado
  print('\n8. Usando Iterador personalizado:');
  class NumberIterator implements Iterator<int> {
    int _current = 0;
    
    @override
    int get current => _current;
    
    @override
    bool moveNext() {
      if (_current < 10) {
        _current++;
        return true;
      }
      return false;
    }
  }

  class NumberIterable extends Iterable<int> {
    @override
    Iterator<int> get iterator => NumberIterator();
  }

  void customIterator() {
    var numbers = NumberIterable();
    for (var number in numbers) {
      stdout.write('$number ');
    }
    print('');
  }
  customIterator();

  // 9. Usando async* para generar un stream
  print('\n9. Usando async* para generar un stream:');
  Stream<int> countStream() async* {
    for (int i = 1; i <= 10; i++) {
      yield i;
    }
  }

  void streamExample() async {
    await for (var number in countStream()) {
      stdout.write('$number ');
    }
    print('');
  }
  // Nota: Este ejemplo es asíncrono y no se ejecutará en orden
  streamExample();

  // 10. Usando recursión
  print('\n10. Usando recursión:');
  void recursion(int n) {
    if (n <= 10) {
      stdout.write('$n ');
      recursion(n + 1);
    }
  }
  recursion(1);
  print('');

  // EXTRA: Ejemplo con Dart Collection Methods
  print('\n11. Bonus: Usando métodos de colección de Dart:');
  void dartCollectionMethods() {
    var numeros = List.generate(10, (index) => index + 1);
    
    // where para filtrar
    print('Números pares:');
    numeros.where((n) => n.isEven).forEach((n) => stdout.write('$n '));
    print('');
    
    // take para obtener los primeros n elementos
    print('Primeros 5 números:');
    numeros.take(5).forEach((n) => stdout.write('$n '));
    print('');
    
    // skip para saltar elementos
    print('Saltando los primeros 5 números:');
    numeros.skip(5).forEach((n) => stdout.write('$n '));
    print('');
  }
  dartCollectionMethods();
}

/**
 * NOTAS SOBRE LAS CARACTERÍSTICAS ÚNICAS DE DART:
 * 
 * 1. Dart tiene soporte nativo para streams con async* y yield
 * 2. Los tipos son obligatorios para las variables públicas
 * 3. Las colecciones en Dart son muy potentes y tienen muchos métodos útiles
 * 4. Dart tiene un sistema de tipos sound null safety
 * 5. La sintaxis para iteración es similar a otros lenguajes, pero con
 *    algunas peculiaridades propias de Dart
 */

/**
 * MEJORES PRÁCTICAS PARA ITERACIÓN EN DART:
 * 
 * 1. Usar for-in cuando sea posible, es más legible
 * 2. Aprovechar los métodos de colección como where, map, etc.
 * 3. Considerar el uso de streams para datos asíncronos
 * 4. Implementar Iterable cuando se necesite una colección personalizada
 * 5. Usar final o const cuando sea posible para variables
 */