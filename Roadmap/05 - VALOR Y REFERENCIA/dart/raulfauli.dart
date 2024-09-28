/// #05 VALOR Y REFERENCIA

void main() {
  // Los datos primitivos se pasan por valor
  var primitiveVar = 123;
  var other = primitiveVar;
  other = 456;
  print(primitiveVar); // 123
  print(other); // 456

  // Las listas/objetos se pasan por referencia
  var lista = [2, 4, 5];
  var otraLista = lista;
  otraLista.add(7);
  print(lista); // [2, 4, 5, 7]
  print(otraLista); // [2, 4, 5, 7]

  // Para evitar esto, se puede usar el operador spread
  var lista2 = [2, 4, 5];
  var otraLista2 = [...lista2];
  otraLista2.add(7);
  print(lista2); // [2, 4, 5]
  print(otraLista2); // [2, 4, 5, 7]

  // Otra forma de evitar esto es usar el método toList()
  var lista3 = [2, 4, 5];
  var otraLista3 = lista3.toList();
  otraLista3.add(7);
  print(lista3); // [2, 4, 5]
  print(otraLista3); // [2, 4, 5, 7]

  // Los mapas se pasan por referencia
  var persona = {'nombre': 'Raúl', 'edad': 25};
  var otraPersona = persona;
  otraPersona['edad'] = 26;
  print(persona); // {nombre: Raúl, edad: 26}
  print(otraPersona); // {nombre: Raúl, edad: 26}

  // Para evitar esto, se puede usar el operador spread
  var persona2 = {'nombre': 'Raúl', 'edad': 25};
  var otraPersona2 = {...persona2};
  otraPersona2['edad'] = 26;
  print(persona2); // {nombre: Raúl, edad: 25}
  print(otraPersona2); // {nombre: Raúl, edad: 26}

  // Otra forma de evitar esto es usar el método Map.from()
  var persona3 = {'nombre': 'Raúl', 'edad': 25};
  var otraPersona3 = Map.from(persona3);
  otraPersona3['edad'] = 26;
  print(persona3); // {nombre: Raúl, edad: 25}
  print(otraPersona3); // {nombre: Raúl, edad: 26}

  // En dart 3.0 se añaden los Records que es como una tupla y se pasan por valor
  var tupla = ('Raúl', 25);
  var otraTupla = tupla;
  otraTupla = ('Faulí', 26);
  print(tupla); // (Raúl, 25)
  print(otraTupla); // (Faulí, 26)

  // Otro ejemplo de paso por valor mediante un Objeto
  var fecha = DateTime.now();
  var otraFecha = fecha;
  otraFecha.add(Duration(days: 78));
  print(fecha); // 2021-10-14 20:00:00.000
  print(otraFecha); // 2021-12-31 00:00:00.000

  // Para evitar esto, se puede clonear la fecha con copyWith
  var fecha2 = DateTime.now();
  var otraFecha2 = fecha2.copyWith();
  otraFecha2 = otraFecha2.add(Duration(days: 78));
  print(fecha2); // 2021-10-14 20:00:00.000
  print(otraFecha2); // 2021-12-31 20:00:00.000

  // En funciones pasa lo mismo, depende del tipo de dato y la forma de pasar el dato
  var valor = 123;
  modifyValue(valor);
  print(valor); // 123

  var lista4 = [2, 4, 5];
  modifyList(lista4);
  print(lista4); // [2, 4, 5, 777]

  var lista5 = [2, 4, 5];
  var otraLista5 = modifyListImmutable(lista5);
  print(lista5); // [2, 4, 5]

  // En caso de haber definido como constante el valor, no se podrá modificar bajo ninguna circunstancia
  const immutableList = [2, 4, 5];
  // immutableList.add(777); // Error
  // modifyList(immutableList); // Error
  final newList = modifyListImmutable(immutableList);
  print(immutableList); // [2, 4, 5]
  print(newList); // [2, 4, 5, 777]

  // Dificultad extra
  var pareja = [1, 2];
  var nuevaPareja = pasoPorValor(pareja);
  print(nuevaPareja); // [2, 1]
  print(pareja); // [1, 2]

  pasoPorReferencia(pareja);
  print(pareja); // [2, 1]
}

void modifyValue(int valor) {
  valor = 777;
}

void modifyList(List<int> lista) {
  lista.add(777);
}

List<int> modifyListImmutable(List<int> lista) {
  return [...lista, 777];
}

List<int> pasoPorValor(List<int> lista) {
  return [lista[1], lista[0]];
}

// convert list to reverse
pasoPorReferencia(List<int> lista) {
  lista.add(lista[1]);
  lista.add(lista[0]);
  lista.removeRange(0, 2);
}
