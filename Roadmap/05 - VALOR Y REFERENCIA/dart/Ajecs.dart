import 'dart:io' show stdout;

void main() {
  /* 
    Todo en dart es un objeto. Los tipos primitivos son inmutables (por valor).
    Al cambiar su valor lo unico que se logra es crear un nuevo objeto en memoria.
  */

  stdout.write(
    '\n ************************* Valor y referencia ************************ \n\n',
  );

  String name1 = 'Ajecs';
  String name2 = name1;

  name1 = 'Pepe';

  // Al asignar name1 a name2 se crea un nuevo objeto en memoria pero no apuntan al mismo objeto.
  print(name1 + ' ' + name2);

  // Las estructuras de datos son mutables (por referencia) ya que heredan su posicion en memoria.

  var nums1 = [1, 2, 3, 4];
  // nums1.add('chau');

  // nums2 y nums1 comparten ahora el mismo espacio en memoria. No hay una copia del valor.
  List nums2 = nums1;

  nums1.add(5);
  print('$nums1 $nums2'); // el mismo valor.

  stdout.write(
    '\n********************** Funciones ***********************\n\n',
  );

  stdout.write('<< Con objetos por valor >> \n\n');

  int numTest = 10;

  void myNum(int numFunc) {
    numFunc = 20;
    numTest = 50;
    print(numFunc);
  }

  // La función genera una copia del valor no hay ninguna referencia.
  myNum(numTest);
  print(numTest);

  stdout.write('\n << Con objetos por referencia >> \n\n');

  // En los objetos con valores por referencia una función si modifica el valor de la variable.
  List<int> listTest = [1, 2, 3];

  void myList(List<int> listNum) {
    List listNum2 = listNum;
    listNum2.add(5);

    List listTest2 = listNum2;
    listTest2.add(100); // Modifica a todos los objetos con el puntero en común.

    print(listNum2);
    print(listTest2);
  }

  /* 
    No importa cuantas veces se asigne y de que forma el valor de un objeto cuyo valor es por referencia
    El valor cambiara en todas las variables que tengan asociadas el puntero.
  */

  // Aun así existen formas de "romper" el vinculo con el puntero

  myList(listTest);
  print(listTest);

  stdout.write(
    '\n******************** Formas de copiar datos a Lista, Mapas o Sets ******************\n\n',
  );

  print('<< Copia superficial >>\n');
  // Si la lista contiene objetos mutables (o sub-listas),
  //modificar un elemento interno afectará a ambas variables:

  print('<< Mediante el operador Spread >>\n');

  List<num> listOriginal = [1, 2, 3, 4, 1.5, 0.3];
  Map<String, dynamic> mapOriginal = {'name': 'Ajecs', 'age': 105};

  Map mapCopy = {...mapOriginal};
  List listCopy = [...listOriginal];

  listCopy.add(30);
  mapCopy['skill'] = 'dev';

  print(listOriginal);
  print(listCopy);

  print('\n$mapOriginal');
  print(mapCopy);

  print('\n<< Mediante contructor/métodos de creación >>\n');

  Map mapCopy2 = Map.from(mapCopy);
  // La copia se realiza a los valores de la variable cuando es declarada.
  mapCopy2.addEntries(
    {'skill': true}.entries,
  ); // forma poco practica de añadir items :\
  mapCopy2.addAll({
    'to-do': ['caminar', 'leer', 'dormir'],
  });

  print(mapCopy);
  print(mapCopy2);

  print('\n<< Los datos en listas con anidamiento si se modifican >>\n');

  List<Map<String, dynamic>> collectionOriginal = [
    {
      'name': 'Ajecs',
      'to-do': ['cantar', 'cocinar', 'comer'],
    },
  ];

  List collectionCopy = [...collectionOriginal];
  List collectionCopy2 = List.from(collectionCopy);
  collectionCopy[0]['to-do'].add('programar');
  collectionCopy2[0]['to-do'].add('dormir');
  // Se modifica en ambas listas

  print('Colección original: $collectionOriginal');
  print('Primera copia: $collectionCopy');
  print('Segunda copia: $collectionCopy2');

  stdout.write('\n<< Copia profunda >>\n\n');
  // Los objetos anidados de la copia no comparten memoria con el original

  List<List<int>> listNestedOriginal = [
    [1, 2, 3],
    [4, 5, 9],
  ];
  // Se puede aplicar mediante un map() que haga una copia de cada sublista.
  List<List<int>> deepCopy = listNestedOriginal
      .map((sublist) => [...sublist])
      .toList();

  deepCopy[0].add(777);
  print('Lista anidada original: $listNestedOriginal');
  print('Lista copiada de forma profunda y modificada: $deepCopy');
  // No se modifican ambos.

  stdout.write('\n************** Extra ************************\n\n');

  int value1 = 666;
  int value2 = 777;

  (int, int) valueProg(int v1, int v2) {
    var temp1 = value1;
    value1 = value2;
    value2 = temp1;
    return (v1, v2);
  }

  var (value1Copy, value2Copy) = valueProg(value1, value2);

  print('Valores originalea:      $value1 - $value2');
  print('Valores intercambiados:  $value1Copy \u21C6 $value2Copy');

  List list1 = [5, 6];
  List list2 = [7, 8];

  (List, List) refProg(List l1, List l2) {
    var temp1 = list1;
    list1 = list2;
    list2 = temp1;
    return (l1, l2);
  }

  var (list1Copy, list2Copy) = refProg(list1, list2);

  print('\n  Listas originales:     $list1   $list2');
  print('Listas intercambiadas:   $list1Copy \u21C6 $list2Copy');

  /*  
    El mismo programa funciona con valores de referencia porque las variable temporal 
    almacena el puntero y no se aplica ningún método que lo modifica.
  */

}
