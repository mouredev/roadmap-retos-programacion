/// #08 CLASES

void main() {
  final person = Person('Raul', 25);
  person.age = 101; // Print 'Invalid age'
  person.printPerson(); // Age: 25

  // Public constant
  print('Max age: ${Person.MAX_AGE}');
  // Static method
  Person.printMaxAge(); // Max age: 100

  // Setter
  person.age = 40;
  person.printPerson(); // Age: 40

  // Getter
  final age = person.age;
  print('Age: $age'); // Age: 40

  // Name constructor
  final anonym = Person.anonym();
  anonym.printPerson(); // Name: Anonymous, Age: 18

  // Extra

  // Queue
  final queue = Queue();
  queue.add('Raul');
  queue.add('Fauli');
  queue.add('Garcia');
  print(queue.get()); // Raul
  print(queue.getAll()); // [Fauli, Garcia]

  // Stack
  final stack = Stack();
  stack.add('Raul');
  stack.add('Fauli');
  stack.add('Garcia');
  print(stack.get()); // Garcia
  print(stack.getAll()); // [Raul, Fauli]
}

// Clase con constructor
class Person {
  // Constantes
  static const int MAX_AGE = 100;
  // Atributos
  String name;
  // Atributo privado
  int _age = 0;

  // Constructor
  Person(this.name, this._age);

  // Constructor con nombre
  Person.anonym()
      : name = 'Anonymous',
        _age = 18;

  // Métodos
  void printPerson() {
    print('Name: $name, Age: $_age');
  }

  // Getters y Setters
  int get age => _age;
  set age(int value) {
    if (value <= MAX_AGE && value >= 0) {
      _age = value;
    } else {
      print('Invalid age');
    }
  }

  // Métodos estáticos
  static void printMaxAge() {
    print('Max age: $MAX_AGE');
  }

  // Métodos privados
  void _privateMethod() {
    print('Private method');
  }

  void publicMethod() {
    _privateMethod();
  }
}

class Queue {
  final List<String> _queue = [];

  void add(String value) {
    _queue.add(value);
  }

  String? get() {
    if (_queue.isEmpty) {
      return null;
    }
    return _queue.removeAt(0);
  }

  List<String> getAll() {
    return _queue;
  }
}

class Stack {
  final List<String> _stack = [];

  void add(String value) {
    _stack.add(value);
  }

  String? get() {
    if (_stack.isEmpty) {
      return null;
    }
    return _stack.removeLast();
  }

  List<String> getAll() {
    return _stack;
  }
}
