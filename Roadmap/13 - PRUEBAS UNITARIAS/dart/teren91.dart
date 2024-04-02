/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */

/*
  NOTA: Para que este código funcione es necesario crear un archivo pubspec.yaml
    y añadir la dependencia siguiente:

    dev_dependencies:
      test: ^1.25.2

*/

import 'package:test/test.dart';

void main() {
 

  testData(data);
  testSum(2, 3);
}

int sum(int i, int j) {
  return i + j;
}

Map<String, dynamic> data = {
  "name": "Teren",
  "age": 32,
  "birth_date": DateTime(1991, 9, 14),
  "programming_lenguages": ["Dart", "C#", "TSQL", "C++"]
};

void testSum(int x, int y)
{
   test('Test function sum', () {
   
    expect(sum(x, y), equals(x+y));
  });
}

void testData(Map<String, dynamic> data) {
  group('Test del diccionario', () {
    test('Test de la primera clave: name', () {
      expect(data.containsKey("name"), true);
    });
    test('Test de la segunda clave: age', () {
      expect(data.containsKey("age"), true);
    });
    test('Test de la tercera clave: birth_date', () {
      expect(data.containsKey("birth_date"), true);
    });
    test('Test de la cuarte clave: programming_lenguages', () {
      expect(data.containsKey("programming_lenguages"), true);
    });
  });

   group('Test del diccionario - tipo de datos', () {
    test('Test de la primera clave debe ser String: name', () {
      expect(data.values.first is String , true);
    });
    test('Test de la segunda clave: age', () {
      expect(data.values.elementAt(1) is int, true);
    });
    test('Test de la tercera clave: birth_date', () {
      expect(data.values.elementAt(2) is DateTime, true);
    });
    test('Test de la cuarte clave: programming_lenguages', () {
      expect(data.values.last is List, true);
    });
  });
}
