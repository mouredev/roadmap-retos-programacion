import 'dart:collection';
import 'dart:io';

void main() {

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
*/

    // Lista

    print('\nList: ');
    List<int> numeros = [2, 5, 6, 87, 12, 532];
    print(numeros);

    numeros.insert(0, 1); // Inserción
    print(numeros);

    numeros.remove(87); // Borrado
    print(numeros);

    numeros[3] = 601; // Actualización
    print(numeros);

    numeros.sort(); // Ordenar
    print(numeros);

    // Mapa

    print('\nMap:');
    Map<String, String> puesto = {'Mateo': 'Gerente', 'Marta': 'Desarrolladora de Software', 'Dani': 'Ventas'};
    print(puesto);

    puesto['Juan'] = 'Becario'; // Inserción
    print(puesto);

    puesto.remove('Dani'); // Borrado
    print(puesto);

    puesto['Juan'] = 'Ventas'; // Actualización
    print(puesto);

    Map<String, String> puestoOrdenado = SplayTreeMap<String, String>.from(puesto, (a, b) => a.compareTo(b)); // Ordenar
    print(puestoOrdenado);

    // Conjunto

    print('\nSet: ');
    Set<String> menu = {'Hamburgesa con queso', 'Patatas fritas', 'Resfresco a escoger'};
    print(menu);

    menu.add('Nuggets de pollo'); // Inserción
    print(menu);

    menu.remove('Patatas fritas'); // Borrado
    print(menu);

    /// Debido a que Set almacena datos únicos y no tiene un índice, la actualización directa no tiene una función.
    /// Lo mismo sucede con ordenarlo, para poder hacerlo, se ha de convertir en List y luego utilizar sort().
    
    List<String> menuActualizado = menu.toList(); // Actualización
    menuActualizado[1] = 'Pepsi';
    print(menuActualizado);


    List<String> menuOrdenado = menu.toList(); // Ordenar
    menuOrdenado.sort();
    print(menuOrdenado);
 

/*
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

    Map<String, int> agenda = {};
    bool exit = false;

   while (!exit) {
      print('Bienvenido a la agenda de contactos. \n');
      print('Opciones: \n 1. Agregar \n 2. Buscar \n 3. Actualizar \n 4. Eliminar \n 5. Mostrar \n 6. Salir\n');
      print('Indica el número de la opción a realizar: ');
   
      String? opcion = stdin.readLineSync();

      switch (opcion) {
         case '1':

            print('Introduce el nombre: ');
            String? name = stdin.readLineSync();

            print('Introduce el número: ');
            String? number = stdin.readLineSync();

            if (name != null && number != null) {

               try {

                  int phone = int.parse(number);

                  if('$phone'.length <= 11) {
                     agregar(agenda, name, phone);
                  } else {
                     print('El número debe ser menor de 11 dígitos.');
                  }

               } catch (e) {
                  print('Introduce un número válido.');
               }
            } else {
               print('No se introdujo ningún número.');
            }
            break;
         
         case '2':
            
            print('Introduce el nombre del usuario que busca: ');
            String? name = stdin.readLineSync();

            if (name != null) {
               buscar(agenda, name);
            }
            break;

         case '3':
            
            print('Introduce el nombre: ');
            String? name = stdin.readLineSync();
            
            print('Introduce el número a actualizar: ');
            String? number = stdin.readLineSync();

            if (number != null && name != null) {
               try {
                  int phone = int.parse(number);
                  actualizar(agenda, name, phone);
               } catch (e) {
                  print('Introduce un número válido.');
               }
            }
            break;
         
         case '4':
            
            print('Introduce el nombre del contacto a eliminar: ');
            String? name = stdin.readLineSync();

            if (name != null) {
               eliminar(agenda, name);
            }
            break;
         
         case '5':
            
            mostrar(agenda);
            break;

         case '6':
            
            exit = true;
            break;
         
         default:
            print('Opción no válida.');
      }
   }
}

// Agregar

void agregar(Map<String, int> agenda, String name, int phone) {
    agenda[name] = phone;
    print('Contacto agregado.');
}

// Buscar

void buscar(Map<String, int> agenda, String name) {

   if(agenda.containsKey(name)) {
      'El número de $name es: ${agenda[name]}';
   } else {
      print('El contacto no existe');
   }
}

// Actualizar

void actualizar(Map<String, int> agenda, String name, int phone) {

   if(agenda.containsKey(name)) {   
      agenda[name] = phone;
      print('Contacto atualizado.');
   } else {
      print('El contacto no existe.');
   }
}
// Eliminar

void eliminar(Map<String, int> agenda, String name) {
   
   if (agenda.containsKey(name)) {
      agenda.remove(name);   
   } else {
      print('El contacto no existe.');
   }
}
// Mostrar

void mostrar(Map<String, int> agenda) {

   if (agenda.isEmpty) {
      print('La agenda está vacía.');
   } else {
      print(agenda);
   }
}