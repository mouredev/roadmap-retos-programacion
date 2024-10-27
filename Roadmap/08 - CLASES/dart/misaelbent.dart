void main(List<String> arguments) {
  //Instancias de Character
  Character hulk = Character('Hulk', 1.5, 2.0, health: 3.0);
  Character bot = Character.enemy();

  //Modificando instancias
  hulk.attack = 1.9;
  hulk.health = 4.0;
  bot.health = 9.5;

  //Imprimiendo atributo
  Character.printRecommendedAtributes();
  hulk.printAttributes();
  bot.printAttributes();

  //EXTRA!!
  //stack
  Stack pedidos = Stack();
  pedidos.add('Pizza');
  pedidos.add('Hamburguesa');
  pedidos.add('Perro caliente');
  pedidos.remove();
  print(pedidos.stack);

  //queue
  Queue tasks = Queue();
  tasks.add('Almorzar');
  tasks.add('Sacar al perro');
  tasks.add('Terminar reto');
  tasks.remove();
  print(tasks.queue);
}

//Clase de ejemplo
class Character {
  String _name; //Atributos privados
  double _attack;
  double _defend;
  double health; //Atributo publico

  //Constructores
  //Basico
  Character(this._name, this._attack, this._defend,
      {this.health = 12.5} // Valor por defecto
      );
  //Con nombre
  Character.enemy({this.health = 9.5})
      : _name = 'Enemy',
        _attack = 1.5,
        _defend = 0.9;

  //getters
  String get name => _name;
  double get attack => _attack;
  double get defend => _defend;

  //setters
  set name(String value) => _name = value;
  set attack(double value) => _attack = value;
  set defend(double value) => _defend = value;

  //Methods
  void printAttributes() {
    print('''
    ${name.toUpperCase()}
    Health: ${(health * 100).toInt()}
    Attack: ${(attack * 100).toInt()}
    Defend: ${(defend * 100).toInt()}
''');
  }

  //Static method - Metodo estatico
  ///Este metodo imprime los atributos sugeridos para la creacion
  static void printRecommendedAtributes() {
    print('''
Se recomienda que tus personajes se mantengan en estos rangos:
    Health: Entre 8.50 y 15.5 
    attack: Entre 1.5 y 2.0
    defends: Entre 0.8 y 1.0
''');
  }
}

//Extra

//Clase Queue FIFO (First In, First Out)
class Queue {
  final List<String> _queue = [];

  List<String> get queue => _queue;

  void add(String element) {
    _queue.add(element);
  }

  void remove() {
    if (_queue.isEmpty) {
      null;
    } else {
      _queue.removeAt(0); //Elimina el primero de la cola
    }
  }
}

//Clase stack LIFO (Last In, First Out)
class Stack {
  final List<String> _stack = [];

  List<String> get stack => _stack;

  void add(String element) {
    _stack.add(element);
  }

  void remove() {
    if (_stack.isEmpty) {
      null;
    } else {
      _stack.removeLast(); //Elimina el ultimo de la pila
    }
  }
}
