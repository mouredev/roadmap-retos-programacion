/*
* EJERCICIO:
* - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
*   su tipo de dato.
* - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
*   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
* (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
*
* DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
*   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras.
*/

void main() {
  /// [Asignaciones por valor]:
  /// int, bool, String y enum
  int a = 10;
  int b = a;  // Copia el valor

  b = 20;
  print('a: $a'); // 10
  print('b: $b'); // 20

  double c = 3.14159265;
  double d = c;  // Copia el valor

  d = 1.61803399;
  print('c: $c'); // 3.14159265
  print('d: $d'); // 1.61803399

  String e = 'Hello';
  String f = e;  // Copia el valor

  f = 'Dart!';
  print('e: $e'); // Hello
  print('f: $f'); // Dart

  EnumColor color1 = EnumColor.blue;
  EnumColor color2 = color1;  // Copia el valor

  color2 = EnumColor.green;
  print('color1: ${color1.name}'); // blue
  print('color2: ${color2.name}'); // green

  /// [Asignaciones por referencia]:
  /// List, Set, Map y clases personalizadas
  List<String> list1 = ['A', 'B', 'C'];
  List<String> list2 = list1; // Copia la referencia

  list2.add('D');
  print('list1: $list1'); // [A, B, C, D]
  print('list2: $list2'); // [A, B, C, D]

  Set<int> set1 = {1, 2, 3};
  Set<int> set2 = set1; // Copia la referencia

  set2.add(4);
  print('set1: $set1'); // {1, 2, 3, 4}
  print('set2: $set2'); // {1, 2, 3, 4}

  Map<int, bool> map1 = {0:true, 1:false, 2:true};
  Map<int, bool> map2 = map1; // Copia la referencia

  map2[3] = false;
  print('map1: $map1'); // {0: true, 1: false, 2: true, 3: false}
  print('map2: $map2'); // {0: true, 1: false, 2: true, 3: false}

  Person p1 = Person('Ana');
  Person p2 = p1; // Copia la referencia

  p2.name = 'Elie';
  print('p1: ${p1.name}');  // Elie
  print('p2: ${p2.name}');  // Elie

  /// [Función con parámetros por valor]:
  void addTwo(int x) {
    x = x + 2;  /// `x` copia valor de `myInt`
    print(x);   /// cambiar `x` no altera a `myInt`
  }

  int myInt = 23;
  addTwo(myInt);  // 25
  print(myInt);   // 23

  /// [Función con parámetros por referencia]:
  void newKey(Map map) {
    map['c'] = 3; /// cambiar `map` altera `myMap`

    Map otherMap = map; /// `otherMap` copia referencia de `map`
    otherMap['d'] = 4; /// cambiar `otherMap` altera `map`

    print(map);
  }

  Map myMap = {
    'a': 1,
    'b': 2,
  };
  newKey(myMap);  // {a: 1, b: 2, c: 3, d: 4}
  print(myMap);   // {a: 1, b: 2, c: 3, d: 4}

  /// [DIFICULTAD EXTRA]:
  int int1 = 15;
  int int2 = 23;
  int int3;
  int int4;
  (int3, int4) = byValue(int1, int2); /// por [valor]
  print('int1: $int1, int2: $int2');  // 15, 23
  print('int3: $int3, int4: $int4');  // 23, 15

  Set mySet1 = {1, 2, 3};
  Set mySet2 = {4, 5, 6};
  Set mySet3;
  Set mySet4;
  (mySet3, mySet4) = byReference(mySet1, mySet2); /// por [referencia]
  print('mySet1: $mySet1, mySet2: $mySet2');  // {1, 2, 3}, {4, 5, 6}
  print('mySet3: $mySet3, mySet4: $mySet4');  // {4, 5, 6}, {1, 2, 3}
}

/// [Asignaciones por valor]:
/// Ejemplo de enums
enum EnumColor { red, green, blue }

/// [Asignaciones por referencia]:
/// Ejemplo de clases personalizadas
class Person {
  String name;
  Person(this.name);
}

/// [DIFICULTAD EXTRA]:
(int, int) byValue(int var1, int var2) {
  int temp = var1;
  var1 = var2;
  var2 = temp;
  return (var1, var2);
}

(Set, Set) byReference(Set var1, Set var2) {
  Set temp = var1;
  var1 = var2;
  var2 = temp;
  return (var1, var2);
}
