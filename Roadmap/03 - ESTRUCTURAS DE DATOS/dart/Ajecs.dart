import 'dart:collection';
import 'dart:io';

void main() {
  stdout.write(
    '************************* Colecciones *****************************\n\n',
  );

  stdout.write(
    '************************* Listas *****************************\n\n',
  );

  // Se recomienda añadir una coma al final del ultimo elemento con el fin de evitar errores "de copiar y pegar".

  List<String> players = [
    'Lionel Messei',
    'Julian Alvarez',
    'Lisandro Martinez',
    'Alexis McAllister',
  ];

  stdout.write('<< Listas inmutables >>\n\n');

  // Las listas se pueden comportar como Arrays de otros lenguajes como C y Java.
  // Conteniendo un numero fijo y limitado de elementos evitando añadir nuevos items

  final pirates = List<String>.filled(
    5,
    '',
    growable: false,
  ); // lista de 5 Strings vacíos.
  print(pirates);
  print('');

  // pirates.addAll(['o\'Reilly', 'Bellingham', 'Kane', 'Pitchford']);
  // ! error "cannot add to a fixed-length list". Lo mismo con insert().

  pirates[1] = 'Pithford';
  pirates[2] = 'Kane';

  print(pirates);

  // pirates.removeLast();
  // ! "cannot remove from a fixed-length list".

  // Una forma más simple y resumida es mediante el método unmodifiable.
  List<String> froggies = ['Mbappe', 'Dembele', 'Olise'];
  List<String> gauloises = List.unmodifiable(froggies);
  // gauloises.add('Deschamps');
  // ! error.

  // Mediante el getter length se puede obtener el tamaño de la lista.
  // Y con el operador de subíndice un elemento en una posición determinada

  stdout.write(
    '\n********************** Insertar, borrar, actualizar y ordenar listas **************************\n\n',
  );

  print('Hay un total de: ${players.length} jugadores en la lista');
  print('El tercer elemento de la lista es: ${players[2]}');
  print('');

  players.add('Nicolas Gonzalez');
  print('$players. Se añadió a ${players.last}');
  print('');

  players.insert(1, 'Lautaro Martinez');
  print('Se insertó a ${players[1]}');
  print(players);
  print('');

  players.replaceRange(1, 4, [
    'Enzo Fernandez',
    'Nicolas Otamendi',
    'Nicolas Tagliafico',
  ]);
  // ! Se añade cualquier cantidad dentro del rango y se elimina los existentes.
  // print('Se insertó a ${players[1]}');
  print('Se añadieron a ${players.sublist(1, 4).length} jugadores $players');
  print('');

  players.remove('Julian Alvarez');
  print(
    'Se eliminó a Julian Alvares y a el 3° elemento: ${players.removeAt(2)}. $players',
  );
  print('');

  List<String> spanyards = ['Rodri', 'Cucurella', 'Porro', 'Yamal'];
  spanyards.clear();
  print('La lista spanyards esta vacía: $spanyards');
  print('');

  players.sort();
  print('Los jugadores se ordenan alfabeticamente: $players');
  print('');

  print(
    'Los jugadores se ordenan alfabeticamente al reves: ${players.reversed}',
  );

  Iterable<String> playersChange = players.map((player) => 'jugador: $player');
  print(
    '\n$playersChange\nla lista se ha convertido en un ${playersChange.runtimeType}',
  );
  print('');

  // Búsqueda por índice.
  print(
    'Dembele se esta en la posición ${froggies.indexOf('Dembele')} de la lista',
  );

  stdout.write(
    '\n********************** Records **************************\n\n',
  );

  // Los records es la versión de tupla de Dart.
  (String, int, bool) user = ('Ana', 28, true);
  print(user);
  print('El primer item del record es ${user.$1}'); // Ana

  ({String name, int age, bool active}) user2 = (
    name: 'Juan',
    age: 50,
    active: false,
  );
  print(user2); // Los campos nombrados en records se ordenan alfabeticamente.
  print(user2.name); // Juan

  // ! user = user2; error. Los campos nombrados cumplen la función equivalente a un tipo.
  // ! No se pueden asignar variables con valores de tipo distinto.

  // Dos records con igual valor son iguales si no poseen campos nombrados.

  (int x, int y, int z) point = (1, 2, 3);
  (int r, int g, int b) color = (1, 2, 3);

  print(point == color); // true

  ({int x, int y, int z}) point2 = (x: 1, y: 2, z: 3);
  ({int r, int g, int b}) color2 = (r: 1, g: 2, b: 3);

  print(point2 == color2); // false

  // Multiples returns
  (String name, int age) userInfo(Map<String, dynamic> json) {
    return (json['name'] as String, json['age'] as int);
  }

  final json = <String, dynamic>{'name': 'Ajecs', 'age': 95, 'color': 'cyan'};

  // Desestructurando con el patrón de record en las variables name y age.
  var (name, age) = userInfo(json);

  print(userInfo(json)); // (Ajecs, 95)

  print('El nombre del usuario es $name y su edad es $age'); // Ajecs

  /* Equivalente a:
  var info = userInfo(json);
  String name = info.$1;
  int age  = info.$2;
*/

  stdout.write(
    '\n***************************** Sets ********************************\n\n',
  );

  /* 
    En Dart a diferencia de otros lenguajes no son estructuras desordenadas. Dart implementa 
    de fondo una clase llamada LinkedHashSet que se encarga de evitar duplicados (Tabla Hash) 
    y permite mantener la misma secuencia (Linked List) aunque los valores se encuentren 
    esparcidos en memoria. Debido a eso no se puede acceder a la posición de los elementos
    aunque esten ordenados. No sabe su posición como las listas sino que sigue cada vinculo que
    lo dirige al siguiente item.  
  */

  Set<String> kids = {'Juana', 'Ulises', 'Thiago', 'Emma', 'Ciro'};
  print('Grupo 1: $kids');

  // Set vacío
  Set<String> otherKids = {}; // de otra forma se crearía un mapa
  otherKids.addAll({'Mateo', 'Alan', 'Zoe', 'Francesca', 'Bastian'});
  print('Grupo 2: $otherKids');

  Set<String> anotherKids = Set.from(['Fernando', 'Nicolas', 'Tiana', 'Ciro']);
  print('Grupo 3: $anotherKids');

  stdout.write('\n<< Intersección >>\n\n');

  String intersection = kids.intersection(anotherKids).join(', ');
  print('El elemento en común entre el grupo 1 y el grupo 3 es: $intersection');

  stdout.write('\n<< Diferencia >>\n\n');

  String difference = kids.difference(anotherKids).join(', ');
  stdout.write(
    'La diferencia entre el grupo 1 y el grupo 3 es: ${difference}\n',
  );

  stdout.write('\n<< Unión >>\n\n');

  Set<String> union = kids.union(anotherKids);
  stdout.write(
    'La Unión entre el grupo 1 y el grupo 3 es: ${union.join(', ')}\n',
  );

  // Con el fin de crear un Set desordenado se importa dart:collection para usar HashSet.

  stdout.write('\n<< Set desordenado >>\n\n');

  Set<String> disorderGroup = HashSet<String>();
  disorderGroup.addAll(union);
  // ! Lo desordena solo una vez
  print(disorderGroup);

  stdout.write('\n********************** Mapas **************************\n\n');

  // Forma concisa
  Map<String, dynamic> map = {'name': 'Ajecs', 'age': 95, 'color': 'cyan'};
  print('mapa "map": $map');

  // A traves del constructor
  Map<int, dynamic> map2 = Map();
  map2.addEntries([MapEntry(1, 'Ajecs'), MapEntry(2, 95), MapEntry(3, 'cyan')]);
  print('"map2" creado con constructor $map2');

  map2.addAll({4: 'Chess player', 5: 'AT'});
  print('"map2" con 2 key-values añadidos: $map2');

  print('');

  print(
    '"map2" contiene el valor Ajecs: ${map2.containsValue('Ajecs')} y tiene ${map2.values.length} valores',
  );

  map2.remove(3);

  stdout.write('\nClaves de map2: ${map2.keys.join(', ')}\n');
  stdout.write('Valores de map2: ${map2.values.join(', ')}\n');

  // Añadir un valor de una clave en ausencia de valor.

  // Se actualiza el valor de la clave para convertirlo en String. Si no posee valor se agrega el entero 95.
  map2.update(2, (value) => value.toString(), ifAbsent: () => 95);
  // Se eliminan los valores segun los criterios que se le pase.
  map2.removeWhere((key, value) => value.startsWith('A'));
  map2.putIfAbsent(1, () => 'Pepito');
  stdout.write(
    '\nSe Eliminaron los valores con A. Y a falta del valor en 1 de "Ajecs" se añadío ${map2[1]}:\n$map2\n',
  );

  // Mapa con valor constante.

  final Map<String, dynamic> constantMap = const {
    'name': 'Nana',
    'age': 52,
    'color': 'black',
  };

  // constantMap['email'] = 'Ajecs@dlfsjkd';
  // ! Error

  stdout.write(
    '\n\n****************** Ejercicio extra ******************************\n\n',
  );

  // Casos de uso adicionales implementados:
  /* 
    * Lógica para evitar duplicados (Quitar elementos al actualizar, manejo de mayúsculas y minúsculas)
    * Flexibilidad al actualizar datos: solo se actualizan los datos que se deseen 
  */

  // << Mapa contacts donde se almacenan los contactos >>

  Map<String, ({String name, String phone})> contacts = {};

  // -------------------- Funciones -----------------------------


  ({String name, String phone})? searchContact() {
    String searchContactInput = stdin.readLineSync() ?? '';

    ({String name, String phone})? contactFind =
        contacts[searchContactInput.toLowerCase()];

    if (contactFind != null) {
      print('Contacto encontrado: ${contactFind.name}');
      print('Teléfono: ${contactFind.phone}\n');
    } else {
      print('El contacto "$searchContactInput" no existe.\n');
    }
    return contactFind;
  }

  stdout.write('\n¿Que operación desea realizar?: \n');

  bool goOn = true;
  while (goOn) {
    print('\n--- MENÚ PRINCIPAL ---');
    print('1. Buscar contacto');
    print('2. Añadir contacto');
    print('3. Actualizar contacto');
    print('4. Elimiinar contacto');
    print('5. Salir');
    stdout.write('Elige una opción (1-5): ');

    String? option = stdin.readLineSync() ?? '';

    switch (option) {
      case '1':
        print('\nBusca un el nombre de un contacto agendado');
        searchContact();
        break;

      case '2':
        stdout.write('\nAñade un nuevo contacto: ');
        String contactNameInput = stdin.readLineSync() ?? '';

        String key = contactNameInput.toLowerCase();
        if(contacts.containsKey(key)) {
          print('\n❌ Error: El contacto "${contactNameInput}" ya existe en tu agenda.\n');
          break;
        } 

        stdout.write('\nIngresa el número de telefono: ');
        String contactPhoneInput = stdin.readLineSync() ?? '';
        int? contactPhoneInt = int.tryParse(contactPhoneInput);

        if (contactPhoneInt != null && contactPhoneInt.toString().length > 11) {
          contacts[contactNameInput.toLowerCase()] = (
            name: contactNameInput,
            phone: contactPhoneInput,
          );
          stdout.write(
            '\nContacto agregado:\nNombre: $contactNameInput\nTeléfono: $contactPhoneInput\n',
          );
        } else {
          stdout.write(
            '\n❌ Error: Añade un número de telefono válido de más de 11 NÚMEROS\n',
          );
        }
        break;

      case '3':
        stdout.write(
          '\nBusca el nombre de un contacto para actualizar sus datos\n',
        );
        var contactFind = searchContact();
        // contactNameInput();
        if (contactFind != null) {
          String oldKey = contactFind.name.toLowerCase();
          // El usuario no tiene que cambiar ambos datos y por se aplica lo siguiente.
          stdout.write(
            'Ingresa el NUEVO nombre (o presiona Enter para mantener "${contactFind.name}"): ',
          );
          String newNameInput = stdin.readLineSync() ?? '';
          if (newNameInput.isEmpty) newNameInput = contactFind.name;
          stdout.write(
            'Ingresa el NUEVO teléfono (o presiona Enter para mantener "${contactFind.phone}"): ',
          );
          String newPhoneInput = stdin.readLineSync() ?? '';
          if (newPhoneInput.isEmpty) newPhoneInput = contactFind.phone;
          int? contactPhoneInt = int.tryParse(newPhoneInput);

          if (contactPhoneInt != null && newPhoneInput.length > 11) {
            // Se elimina la clave anterior.
            if (oldKey != newNameInput.toLowerCase()) {
              contacts.remove(oldKey);
            }
            contacts[newNameInput.toLowerCase()] = (
              name: newNameInput,
              phone: newPhoneInput,
            );
            print('Se ha actualizado el nombre de contacto');
          } else {
            print(
              '\n❌ Error: El número de teléfono debe ser válido y tener más de 11 dígitos. No se hicieron cambios.\n',
            );
          }
        }
        break;

      case '4':
        stdout.write('\nElimina un contacto buscando su nombre\n');
        var contactFind = searchContact();
        stdout.write('\nEstas seguro de querer eliminar el contacto? (S/N)\n');
        String? answer = stdin.readLineSync() ?? '';
        if (answer.toLowerCase() == 's') {
          contacts.remove(contactFind!.name.toLowerCase());
          print('Contacto eliminado');
        } else {
          print('Operación cancelada');
        }
        break;

      case '5':
        goOn = false; // Rompe el bucle para terminar
        break;

      default:
        print('\n❌ Opción no válida. Por favor, intenta de nuevo.');
    }
  }
}
