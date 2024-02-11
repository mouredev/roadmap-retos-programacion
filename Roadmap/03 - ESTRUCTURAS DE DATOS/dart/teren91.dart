/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

// Estructuras de datos soportadas por defecto en Dart:
// - List
// - Set
// - Map

import 'dart:io';

void main() {
  listExample();
  setExample();
  mapExample();

  // Agenda de contactos
  agendaContactos();
}

// List - example insert, delete, update, sort
void listExample() {
  List<int> list = [2, 5, 3, 2, 1];
  print('\n----- LIST -----:');
  print('Initial list:' + list.toString());

  // Insert
  list.add(6);
  print('Insert result:' + list.toString());

  // Delete
  list.remove(6);
  print('Delete result:' + list.toString());

  // Update
  list[0] = 0;
  print('Update result:' + list.toString());

  // Sort
  list.sort();
  print('Sort list result:' + list.toString());
}

//Set - example insert, delete, update, sort
void setExample() {
  Set<int> set = {2, 5, 3, 4, 1};
  print('\n----- SET -----:');
  print('Initial set:' + set.toString());

  // Insert
  set.add(6);
  print('Insert result:' + set.toString());

  // Delete
  set.remove(6);
  print('Delete result:' + set.toString());

  // Update
  // set[0] = 0; // Error: Unhandled exception:
  // Unsupported operation: Cannot modify an unmodifiable set
  print('Update result: Cannot modify an unmodifiable set');

  // Sort
  // set.sort(); // Error: Unhandled exception:
  // Unsupported operation: Cannot sort an unmodifiable set
  print('Sort set result: Cannot sort an unmodifiable set');
}

//Map - example insert, delete, update, sort
void mapExample() {
  Map<int, String> map = {1: 'one', 2: 'two', 3: 'three'};
   print('\n----- MAP -----:');
  print('Initial map:' + map.toString());

  // Insert
  map[4] = 'four';
  print('Insert result:' + map.toString());

  // Delete
  map.remove(2);
  print('Delete result:' + map.toString());

  // Update
  map.update(1, (value) => 'uno');
  print('Update result:' + map.toString());

  // Sort
  // map.sort(); // Error: Unhandled exception:
  // Unsupported operation: Cannot sort an unmodifiable map
  print('Sort map result: Cannot sort an unmodifiable map');
}


//Agenda de contactos
void agendaContactos() {
  Map<String, BigInt> contacts = {};
  int? option = 0;

  do {
    print('''
    
    --------------------
      1. Add contact
      2. Remove contact
      3. Search contact
      4. List contacts
      5. Exit
    --------------------
    ''');
    option = int.tryParse(stdin.readLineSync()!);

    switch (option) {
      case 1:
        contacts.addAll(addContact());
      case 2:
        contacts = removeContact(contacts);
      case 3:
        searchContact(contacts);
      case 4:
        listContacts(contacts);
      case 5:
        print('Program finished');
    }
  } while (option != 5);

  listContacts(contacts);
}

Map<String, BigInt> addContact() {
  try {
    print('Insert name:');
    String name = stdin.readLineSync()!;

    print('Insert phone:');
    BigInt? phone = BigInt.tryParse(stdin.readLineSync()!);

    if (phone == null) {
      print('Incorrect phone');
      return {};
    }

    return {name: phone};
  } on Exception catch (e) {
    e.toString();
    return {};
  }
}

Map<String, BigInt> removeContact(Map<String, BigInt> contacts) {
  listContacts(contacts);
  print('Insert name to remove:');
  
  try {
    String name = stdin.readLineSync()!;

    if (!contacts.containsKey(name)) {
      print('Contact not found');
      return contacts;
    }

    contacts.remove(name);

    print('Contact removed');
    return contacts;

  } on Exception catch (e) {
      e.toString();
      return contacts; 
  }
}

void searchContact(Map<String, BigInt> contacts) {
  print('Insert name to search:');
  
  try {
  String name = stdin.readLineSync()!;
  
  if (!contacts.containsKey(name)) {
    print('Contact not found');
    return;
  }
  
  print('phone: ' + contacts[name].toString());

  return;

} on Exception catch (e) {
    e.toString();
    return;
}
}

void listContacts(Map<String, BigInt> contacts) {
  print('Contacts:' + contacts.toString());
}
