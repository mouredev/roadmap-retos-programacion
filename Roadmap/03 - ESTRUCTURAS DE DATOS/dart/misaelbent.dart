import 'dart:collection';
import 'dart:io';

void main(List<String> arguments) {
//Ejercicio extra
  askUser();
//Insercion
  elements.add('Perro'); //Anadir un elemento
  numbers.addAll([5, 7, 8]); //Anadir varios elementos
  items.add('Bote');
  users.addAll({'D1': 'Milena'});
  line.add(7.5);

//Borrado
  elements.removeAt(1); //Elimina el elemento en la posicion [1]
  elements.removeLast(); //Elimina el ultimo elemento
  elements.clear(); //Limpia toda la lista
  numbers.remove(2); //Elimina el elemento que coincida con el valor dado
  items.removeWhere((item) =>
      item == 2); //Elimina los elementos que coincidan con la condicion

//Actualizar
  users.update('A1', (value) => 'Pedro');

//Ordenar
  elements.sort(); //Ordena los elementos
  numbers.sort((a, b) => a.compareTo(b));
  print(numbers);
}

//Lista de elementos
List elements = [1, 'Gato', 0.5];

//Lista de numeros, puede ser una de lista de cualquier objeto
List<int> numbers = [6, 4, 9, 15];

//Coleccion desorrdenada de elementos, sin duplicados.
Set items = {'Carro', 2, 0.5};

//Coleccion de pares que representan clave, valor donde cada clave es unica
Map<String, String> users = {'A1': 'Carlos', 'B1': 'Rodrigo', 'C1': 'Vanessa'};

//Collecion para ingresar elementos en un orden determinado
Queue<double> line = Queue<double>();

//Ejercicio extra!!!
Map<String, String> contacts = {
  'Carlos': '3215987896',
  'Julian': '3005945896',
  'Veronica': '3119987846',
  'Juana': '3215987896',
  'Guillermo': '3153457863'
};

//Menu de opciones del programa
askUser() {
  while (true) {
    print('Escoja una opcion');
    print('1 Para buscar contacto');
    print('2 Para agregar contacto');
    print('3 Para actualizar numero de contacto');
    print('4 Para borrar contacto');
    print('5 Para salir del programa');

    String? option = stdin.readLineSync();

    switch (option) {
      case '1':
        findContact(); //Buscar
        break;
      case '2':
        addContact(); //Agregar
        break;
      case '3':
        updateContact(); //Actualizar
        break;
      case '4':
        deleteContact(); //Borrar
      case '5':
        exitProgram(); //Salir
        break;
      default:
        throw Error();
    }
  }
}

//Funcion encargada de buscar al contacto
findContact() {
  stdout.write('Por favor, ingresa el nombre del contacto: ');
  String? name = stdin.readLineSync();
  if (isValidateContact(name)) {
    print('_________________');
    print('Datos del contacto');
    print('$name : cel (${contacts[name]})');
    print('');
  } else {
    print('No existe el contacto');
    print('_____________________');
  }
}

//Funcion encargada de anadir al contacto
addContact() {
  while (true) {
    stdout.write('Por favor, ingresa el nombre del nuevo contacto: ');
    String? name = stdin.readLineSync();
    stdout.write('Por favor, ingrese su numero telefonico: ');
    String? cel = stdin.readLineSync();
    if (isValidateNumber(cel)) {
      contacts.addAll({name!: cel!});
      print('Se ha agregado $name a tus contactos');
      print('_____________________');
      break;
    } else {
      print(
          'El número telefónico ingresado no es válido. Por favor, inténtelo de nuevo.');
    }
  }
}


updateContact() {
  while (true) {
    stdout.write(
        'Por favor, ingresa el nombre del contacto que desea actualizar: ');
    String? name = stdin.readLineSync();

    if (contacts.containsKey(name)) {
      stdout.write('Por favor, ingresa el nuevo numero telefonico: ');
      String? cel = stdin.readLineSync();
      if (isValidateNumber(cel)) {
        contacts.update(name!, (value) => cel!);
        print('El numero se ha actualizado');
        print('_____________________');
        break;
      } else {
        print('El numero no es valido');
        print('_____________________');
      }
    } else {
      print('Este contacto no existe');
      print('_____________________');
      break;
    }
  }
}

//Funcion encargada de borrar usuario
deleteContact() {
  stdout.write('Por favor, ingresa el nombre del contacto que desea borrar: ');
  String? name = stdin.readLineSync();
  print('Esta seguro de borrar a $name');
  print('S para continuar y borrar');
  print('N para cancelar');
  stdout.write('contuar: ');
  String? answer = stdin.readLineSync();
  if (answer == 's') {
    contacts.remove(name);
    print('Se ha borrado el contacto');
    print('_____________________');
  } else if (answer == 'n') {
    print('NO se ha borrado el contacto');
    print('_____________________');
  } else {
    print('Opcion no valida');
    deleteContact();
  }
}


//Funcion para salir del programa
exitProgram() {
  exit(0);
}

//VALIDADORES
//Validador de numero
bool isValidateNumber(String? celNumber) {
  if (celNumber!.contains(RegExp(r'[a-zA-Z]'))) {
    print('Debe ingresar solo numeros');
    return false;
  } else if (celNumber.length > 10 || celNumber.length < 10) {
    print('El numero debe tener 10 digitos');
    return false;
  }
  return true;
}

//Validador de contacto
bool isValidateContact(String? name) => contacts.containsKey(name);