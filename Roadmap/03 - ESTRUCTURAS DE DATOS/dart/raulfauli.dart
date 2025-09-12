import 'dart:io';

/// 03 ESTRUCTURAS DE DATOS

void main() {
  /*
    Estrucutras de datos nativas de Dart
    Operaciones: inserción, borrado, actualización y ordenación
  */
  final languages = ['Dart', 'Java', 'Kotlin', 'Swift'];
  print('List $languages');
  print('Length: ${languages.length}');
  print('Type of languages: ${languages.runtimeType}'); // List<String>

  languages.add('Dart'); // Añadir un elemento
  languages.addAll(['C#', 'Python']); // Añadir varios elementos
  languages.insert(0, 'Rust'); // Añadir un elemento en un índice
  languages.insertAll(1, ['C++', 'C']); // Añadir varios elementos en un índice

  languages.remove('Java'); // Eliminar un elemento
  languages.removeAt(1); // Eliminar un elemento por índice
  languages.removeLast(); // Eliminar el último elemento
  languages.removeRange(0, 2); // Eliminar un rango de elementos
  languages.removeWhere((element) => element.length <= 2); // Eliminar por condición

  languages[0] = 'C#'; // Reemplazar un elemento
  languages.replaceRange(1, 3, ['C++', 'C']); // Reemplazar un rango de elementos

  languages.sort(); // Ordenar alfabéticamente
  languages.shuffle(); // Mezclar la lista
  languages.reversed; // Invertir la lista
  languages.sort((a, b) => a.length.compareTo(b.length)); // ordenar por longitud de cadena
  print('Ordenado por longitud: $languages');

  final uniqueLang = {'Dart', 'Java', 'Kotlin', 'Swift'};
  print('Set $uniqueLang');
  print('Length: ${uniqueLang.length}');
  print('Type of uniqueLang: ${uniqueLang.runtimeType}'); // Set<String>

  uniqueLang.add('Dart'); // Añadir un elemento sin repetir
  print(uniqueLang);
  // ...Misma sintaxis que las listas

  final locales = {'es': 'Español', 'en': 'Inglés', 'fr': 'Francés'};
  print('Map $locales');
  print('Length: ${locales.length}');
  print('Type of locales: ${locales.runtimeType}'); // Map<String, String>

  locales['de'] = 'Alemán'; // Añadir un elemento
  locales.addAll({'it': 'Italiano', 'pt': 'Portugués'}); // Añadir varios elementos
  locales.putIfAbsent('ca', () => 'Catalán'); // Añadir un elemento si no existe

  locales.update('es', (value) => 'Castellano'); // Actualizar un elemento
  locales.updateAll((key, value) => value.toUpperCase()); // Actualizar todos los elementos

  locales.remove('fr'); // Eliminar un elemento
  locales.removeWhere((key, value) => value.length <= 7); // Eliminar por condición
  print(locales);

  final person = {
    'name': 'Raul',
    'phone': 666666666,
    'weight': 75.5,
    'subscribed': true,
  };
  print('Object $person');
  print('Length: ${person.length}');
  print('Type of person: ${person.runtimeType}'); // Map<String, dynamic>

  person['age'] = 35;
  person.addAll({'height': 1.75, 'married': true});
  person.remove('married');
  person.removeWhere((key, value) => value is double);
  print(person);

  final position = ('GPS', x: 10, y: 20);
  print('Record $position');
  print('Type of tupla: ${position.runtimeType}'); // (String, {int x, int y})

  print(position.$1); // Prints 'GPS'
  print(position.x); // Prints 10
  print(position.y); // Prints 20

  // Se trata como una variable y por tanto inmutable
  // position.$1 = 'GPRS'; // Error
  final position2 = ('GPS', x: 10, y: 20);
  print(position == position2); // true

  /*
   EXTRA: Crea una agenda de contactos por terminal.
  */
  final contacts = <String, BigInt>{};
  int? option = 0;
  do {
    print('''
    1. Añadir contacto
    2. Eliminar contacto
    3. Buscar contacto
    4. Listar contactos
    5. Salir
    ''');
    option = int.tryParse(stdin.readLineSync()!);

    switch (option) {
      case 1:
        String name = writeName();
        BigInt? phone = writePhone();
        if (phone == null) {
          print('Teléfono incorrecto');
          break;
        }
        contacts[name] = phone;
        break;
      case 2:
        String name = writeName();
        if (!contacts.containsKey(name)) {
          print('Contacto no encontrado');
        } else {
          contacts.remove(name);
          print('Contacto eliminado');
        }
        break;
      case 3:
        String name = writeName();
        BigInt? phone = contacts[name];
        if (phone == null) {
          print('Contacto no encontrado');
          break;
        } else {
          print('Teléfono: $phone');
        }
        break;
      case 4:
        for (final entry in contacts.entries) {
          print('${entry.key}: ${entry.value}');
        }
        break;
      case 5:
        print('Programa finalizado');
        break;
      default:
        print('Opción incorrecta');
    }
  } while (option != 5);
}

bool isNumeric(String s) {
  // Todo: Bigint falla si introduces un caracter no numérico
  return BigInt.tryParse(s) != null;
}

String writeName() {
  print('Nombre: ');
  // si es nulo, vuelvo a pedirlo
  String? name;
  do {
    name = stdin.readLineSync();
  } while (name == null || name.trim().isEmpty);

  return name.trim();
}

BigInt? writePhone() {
  print('Teléfono: ');
  final phoneStr = stdin.readLineSync()!;
  if (isNumeric(phoneStr) && phoneStr.length < 9) {
    return null;
  }
  return BigInt.parse(phoneStr);
}
