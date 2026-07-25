/*
* EJERCICIO:
* Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
* atributos y una función que los imprima (teniendo en cuenta las posibilidades
* de tu lenguaje).
* Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
* utilizando su función.
*
* DIFICULTAD EXTRA (opcional):
* Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
* en el ejercicio número 7 de la ruta de estudio)
* - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
*   retornar el número de elementos e imprimir todo su contenido.
* 
*/

/// 1. [Implementación de una clase]:
class Person {
  // Atributos
  String name;
  int age;

  // Inicializador
  Person(this.name, this.age);

  // Imprimir
  void printPerson() {
    print('name: $name, age: $age');
  }
}

/// 3. [Pila/Stack - DIFICULTAD EXTRA]:
class Stack {
  // Atributos
  List<dynamic> _stack = [];

  // Añadir elementos
  void push(dynamic element) {
    _stack.add(element);
  }

  // Eliminar (LIFO - Last in/First Out)
  void pop() {
    if (_stack.isNotEmpty) _stack.removeLast();
  }

  // Número de elementos
  int count() {
    return _stack.length;
  }

  // Imprimir contenido
  void printStack() {
    for (var item in _stack.reversed) {
      print(item);
    }
  }

  // Extra: status del stack
  void stackStatus() {
    printStack();
    print('Stack length: ${count()}');
  }
}

/// 4. [Cola/Queue - DIFICULTAD EXTRA]:
class Queue {
  // Atributos
  List<dynamic> _queue = [];

  // Añadir elementos
  void push(dynamic element) {
    _queue.add(element);
  }

  // Eliminar (FIFO - First in/First Out)
  void pop() {
    if (_queue.isNotEmpty) _queue.removeAt(0);
  }

  // Número de elementos
  int count() {
    return _queue.length;
  }

  // Imprimir contenido
  void printQueue() {
    for (var item in _queue) {
      print(item);
    }
  }

  // Extra: status del queue
  void queueStatus() {
    printQueue();
    print('Queue length: ${count()}');
  }
} 

void main() {
  /// 2. [Instancias de clase]:
  var person1 = Person('Jesús', 21);  // Creación
  var person2 = Person('Elie', 20);   // Creación

  person1.printPerson();  // name: Jesús, age: 21
  person2.printPerson();  // name: Elie, age: 20

  person1.age = 23; // Modificación
  person2.age = 22; // Modificación

  person1.printPerson();  // name: Jesús, age: 23
  person2.printPerson();  // name: Elie, age: 22

  /// 3. [Pila/Stack - DIFICULTAD EXTRA]:
  Stack myStack = Stack();  // crear stack
  for (var i = 0; i < 5; i++) myStack.push(i);  // llenar stack
  myStack.stackStatus();  // ver estado del stack

  myStack.pop();   // eliminar elemento
  myStack.stackStatus();  // ver estado del stack

  myStack.pop();   // eliminar elemento
  myStack.stackStatus();  // ver estado del stack

  /// 4. [Cola/Queue - DIFICULTAD EXTRA]:
  Queue myQueue = Queue();  // crear queue
  for (var i = 97; i < 102; i++) {
    myQueue.push(String.fromCharCode(i));  // llenar queue
  }
  myQueue.queueStatus();  // ver estado del queue

  myQueue.pop();   // eliminar elemento
  myQueue.queueStatus();  // ver estado del queue

  myQueue.pop();   // eliminar elemento
  myQueue.queueStatus();  // ver estado del queue
}
