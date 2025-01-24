import 'dart:io';

void main(List<String> args) {
  // Listas
  List<int> numeros = [1, 2, 3, 4, 5];
  // Sets
  Set<String> frutas = {'manzana', 'banana', 'naranja'};
  // Mapas
  Map<String, int> contactos = {};
  int condition = 0;

  try{do {
    print('''
    1. Agregar contacto
    2. Eliminar contacto
    3. Ver contactos
    4. Buscar contacto
    5. Salir
  ''');

    String? input = stdin.readLineSync();
    if (input != null) {
      condition = int.parse(input);
    }

    switch (condition) {
      case 1:
        print('Ingrese el nombre del contacto:');
        String? nombre = stdin.readLineSync();
        print('Ingrese el número del contacto:');
        String? numero = stdin.readLineSync();
        if (nombre != null && numero != null) {
          contactos[nombre] = int.parse(numero);
        }
        break;
      case 2:
        print('Ingrese el nombre del contacto a eliminar:');
        String? nombreEliminar = stdin.readLineSync();
        if (nombreEliminar != null) {
          contactos.remove(nombreEliminar);
        }
        break;
      case 3:
        print('Contactos:');
        contactos.forEach((nombre, numero) {
          print('$nombre: $numero');
        });
        break;
      case 4:
        print('Ingrese el nombre del contacto a buscar:');
        String? nombreBuscar = stdin.readLineSync();
        if (nombreBuscar != null && contactos.containsKey(nombreBuscar)) {
          print('$nombreBuscar: ${contactos[nombreBuscar]}');
        } else {
          print('Contacto no encontrado');
        }
        break;
      case 5:
        print('Saliendo...');
        break;
      default:
        print('Opción no válida');
    }
  } while (condition != 5);}
  catch(e){
    print('Error: $e');
  }
}