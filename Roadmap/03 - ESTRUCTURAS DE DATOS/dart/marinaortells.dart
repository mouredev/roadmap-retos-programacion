/// URL del sitio web oficial: https://dart.dev/

import 'dart:io';


void main() {


/** 
 * En dart, las estructuras de datos soportadas por defecto son:
 * Listas, Mapas, Sets, Strings, Números y Booleanos
 */

final letters = <String>['a', 'b', 'c', 'd'];
final numbers = <int>[3, 8, 4, 2023, 5];
final empty = [];

/// Operaciones sobre listas
final fixedLists = List<String>.empty(growable: false); // Lista vacía y fija
final listaFija2 = List<String>.filled(6, 'hola', growable:false); // Lista no vacía y fija

letters.add('e'); // Añadir un elemento
letters.addAll(['f', 'g', 'h', 'i']); // Añadir varios elementos al final de la lista
numbers.insert(1, 7); // Inserta un valor en la posición indicada
numbers.insertAll(0, [-9,-6,-2,-5]); // Inserta un array en la posición indicada

numbers[2] = 3; // Acceder al elemento y asignándole un nuevo valor

numbers.remove(0); // Quitar la primera ocurrencia del valor
numbers.removeAt(9); // Quitar el elemento en la posición indicada
numbers.removeRange(0, 7); // Eliminar los elementos desde la posición start hasta la posición end
numbers.removeLast(); // Elimina el último elemento
numbers.removeWhere((element) => element < 0); // Elimina todos los elementos que satisfacen el test


final list1 = [1, 2, 3, 4];
final list2 = [4, 2, 4];
final suma = list1 + list2; // Concatenar listas

var index2 = letters.elementAt(2); // Devuelve el elemento en la posición 2
var firstElement = letters.first; // Devuelve el primer elemento
var lastElement = letters.last; // Devuelve el último elemento
var numbersLength = numbers.length; // Devuelve la longitud
print(numbers.isEmpty); // Devuelve True si está vacía
print(empty.isNotEmpty); // Devuelve True si no está vacía

/// Operaciones sobre Mapas

Map<String,dynamic> persona = {
  'nombre': 'Marina',
  'apellido': 'O',
  'edad': 19,
  'vive': true
}; // <A,B>: A es el tipo de los puntos a la izquierda, que son tipo string
/// B: es el tipo de lo de la derecha, que es dinámico


print(persona.keys); // Devuelve las llaves
print(persona.values); // Devuelve los valores
print(persona.length); // La longitud del mapa
print(persona.isEmpty); // Devuelve booleano si está vacío
print(persona.isNotEmpty); // Devuelve booleano si no está vacío

persona.addAll({'carrera': 'INFADE', 'país':'España'}); // Añade más elementos al mapa
// persona.clear(); // Borra todos los elementos
persona.remove(0); // Borra una posición específica
persona.forEach((k, v) => print('${k}:${v}')); // Aplica una función a todos los valores del mapa

/// Operaciones sobre Sets
/// La diferencia entre Sets y Listas es que los sets no tienen elementos repetidos

var countries1 = <String>{'España'}; // Forma 1 de declarar un set
Set<String> countries2 = {'España'}; // Forma 2 de declarar un set

countries1.add('Francia'); //Añadir un elemento
countries1.addAll({'Alemania', 'Dinamarca'}); // Añadir varios elementos
print(countries1.elementAt(3)); // Elemento en índice indicado
print(countries1.length); // Longitud del set
print(countries1.contains('España')); // Devuelve booleano si el elemento está
print(countries1.remove('Alemania'));
countries1.forEach((name) {
  print(name); // Imprimir todos los elementos del set
});
countries2.clear(); // Borrar todos los elementos del set

/// Dificultad extra

Map<String,dynamic> agenda = {
  'Roberto': '573829572',
  'Susana': '829102948',
  'María': '729402857'
};

print("Binvenid@ a tu agenda virtual");


var solicitud; 

do {
  print('''¿Qué quieres hacer?: 
  1. Añadir | 2. Buscar | 3. Eliminar | 4. Mostrar | 5. Exit''');

  solicitud = stdin.readLineSync();

  if ((solicitud == '1') || (solicitud == 'Añadir')) {
    print("Introduzca el nombre de la persona a la que quiera añadir: ");
    String? nombre = stdin.readLineSync();
    print("Introduzca su número de teléfono: ");
    String? numero;
    while (true) {
      numero = stdin.readLineSync();
      if (numero!.length == 9) {
        break;
      } else {
        print("El número no tiene 9 dígitos");
      }
    }
    agenda.addAll({ '${nombre}': '${numero}'});

  } else if ((solicitud == '2') || (solicitud == 'Buscar')) {
    
    print("Introduzca el nombre de la persona que está buscando: ");
    String? buscarNombre = stdin.readLineSync();
    if (agenda.containsKey(buscarNombre)) {
      print(agenda[buscarNombre]);
    } else {
      print("Ese nombre no está en la agenda");
    }

  } else if ((solicitud == '3') || (solicitud == 'Eliminar')) {
    print("Introduzca el nombre de la persona que quiere eliminar de la agenda: ");
    String? eliminarNombre = stdin.readLineSync();
    if (agenda.containsKey(eliminarNombre)) {
      agenda.remove(eliminarNombre);
    } else {
      print("Ese contacto no existía en tu agenda");
    }
  } else if ((solicitud == '4') || (solicitud == 'Mostrar')) {
    agenda.forEach((k, v) => print('Persona: ${k}, Contacto: ${v}'));
  } else if ((solicitud == '5') || (solicitud == 'Exit')) {
    print("¡Nos vemos a la próxima!");
    false;
  } else {
    print("Indique de nuevo la solicitud");
  }
} while (true);



}
