/*
* EJERCICIO:
* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
* - Utiliza operaciones de inserción, borrado, actualización y ordenación.
*
* DIFICULTAD EXTRA (opcional):
* Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
* - Cada contacto debe tener un nombre y un número de teléfono.
* - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
*   los datos necesarios para llevarla a cabo.
* - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
*   (o el número de dígitos que quieras)
* - También se debe proponer una operación de finalización del programa.
*/
import 'dart:io';

void listOperations(List myList) {
  // default:
  print(myList);  // [1, 2, 3]

  // inserción:
  myList.add(0);
  print(myList);  // [1, 2, 3, 0]

  // borrado:
  myList.remove(2); 
  print(myList);  // [1, 3, 0] 

  // acceso:
  print(myList[1]); // 3

  // actualización:
  myList[1] = 2; 
  print(myList); // [1, 2, 0]

  // ordenación:
  myList.sort();
  print(myList);  // [0, 1, 2]
}

void setOperations(Set mySet) {
  // default:
  print(mySet);  // {'apple', 23, null}

  // inserción:
  mySet.add(true);
  print(mySet);  // {apple, 23, null, true}

  // borrado:
  mySet.remove(null);
  print(mySet);  // {apple, 23, true}

  // acceso:
  // no directamente

  // actualización:
  // no directamente
  
  // ordenación:
  // no directamente
}

void mapOperations(Map myMap) {
  // default:
  print(myMap);  // {name: Jesús, birthYear: 2004, isCool: true}

  // inserción:
  myMap['eyeColor'] = 'brown';
  print(myMap); // {name: Jesús, birthYear: 2004, isCool: true, eyeColor: brown}

  // borrado:
  myMap.remove('birthYear');
  print(myMap); // {name: Jesús, isCool: true, eyeColor: brown}

  // acceso:
  print(myMap.keys);  // (name, isCool, eyeColor)
  print(myMap.values);  // (Jesús, true, brown)
  print(myMap.entries);  // (MapEntry(name: Jesús), MapEntry(isCool: true), MapEntry(eyeColor: brown))
  print(myMap['name']); // Jesús

  // actualización:
  myMap['isCool'] = 'always';
  print(myMap); // {name: Jesús, isCool: always, eyeColor: brown}

  // ordenación:
  // no directamente
}

void recordOperations((int, bool, String) myRecord) {
  // default:
  print(myRecord);  // (46, true, hello)

  // inserción:
  // no aplica

  // borrado:
  // no aplica

  // acceso:
  print(myRecord.$1);  // 46
  print(myRecord.$2);  // true
  print(myRecord.$3);  // hello

  // actualización:
  // no aplica
  
  // ordenación:
  // no aplica
}

/// [DIFICULTAD EXTRA]:
void agenda() {

  Map agenda = {};
  
  void insertarContacto(String name) {
    // Leer teléfono contacto nuevo
    print('Ingrese el número de teléfono:');
    String? phone = stdin.readLineSync();

    // Validar que sean máximo 11 dígitos
    var isDigit = RegExp(r'^\d+$');
    if (isDigit.hasMatch(phone!) && phone.length <= 11) {
      // Insertar en agenda
      agenda['${name}'] = int.parse(phone);
      print('¡Datos guardados!');
    } else {
      print('Solo teléfonos numéricos de máximo de 11 dígitos...');
    }
  }

  void verContactos() {
    for (var name in agenda.keys) {
      print('- $name: ${agenda['$name']}');
    }
  }

  while (true) {
    // Mostrar opciones en terminal
    print('Agenda de Contactos:');
    print('1. Buscar');
    print('2. Insertar');
    print('3. Actualizar');
    print('4. Eliminar');
    print('5. Ver todos');
    print('6. Salir');

    // Leer action del usuario
    String? action = stdin.readLineSync();

    // 1. Buscar contacto
    if (action == '1') {
      // Leer nombre a buscar en agenda
      print('Ingrese nombre a buscar:');
      String? name = stdin.readLineSync();
      // Validar que exista
      if (agenda['$name'] != null) {
        print('Teléfono de $name: ${agenda['$name']}');
      } else {
        print('$name no es un contacto...');
      } 
    }

    // 2. Insertar contacto
    else if (action == '2') {
      // Leer nombre contacto nuevo
      print('Ingrese nombre contacto nuevo:');
      String? name = stdin.readLineSync();
      insertarContacto(name!);
    }

    // 3. Actualizar contacto
    else if (action == '3') {
      // Leer nombre a buscar en agenda
      print('Ingrese nombre contacto para actualizar:');
      String? name = stdin.readLineSync();
      // Validar que exista
      if (agenda['$name'] != null) {
        insertarContacto(name!);
      } else {
        print('$name no es un contacto...');
      } 
    }

    // 4. Eliminar contacto
    else if (action == '4') {
      // Leer nombre a buscar en agenda
      print('Ingrese nombre a eliminar:');
      String? name = stdin.readLineSync();
      // Validar que exista
      if (agenda['$name'] != null) {
        agenda.remove('$name');
        print('¡Contacto eliminado!');
      } else {
        print('$name no es un contacto...');
      } 
    }

    // 5. Ver contactos
    else if (action == '5') verContactos();

    // 6. Salir de agenda
    else if (action == '6') {print('¡Hasta luego!'); break;}

    // Validar input menú
    else print('Opción inválida...'); 
  }
}

void main() {
  /// 1. List
  List myList = [1, 2, 3];
  listOperations(myList);

  /// 2. Sets
  Set mySet = {'apple', 23, null};
  setOperations(mySet);

  /// 3. Maps
  Map myMap = {
    'name': 'Jesús',
    'birthYear': 2004,
    'isCool': true,
  };
  mapOperations(myMap);

  /// 4. Records
  (int, bool, String) myRecord = (46, true, 'hello');
  recordOperations(myRecord);

  /// [DIFICULTAD EXTRA]:
  agenda();
}
