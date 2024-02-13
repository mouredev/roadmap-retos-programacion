/// #07 PILAS Y COLAS

void main() {
  /**
   * Implementa los mecanismos de introducción y recuperación de elementos propios de las
   * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
   * o lista (dependiendo de las posibilidades de tu lenguaje).
  */
  exampleQueue();
  exampleStack();

  /**
   * DIFICULTAD EXTRA
   * Implementa un historial de navegación de un navegador web. Deberás implementar
   * las funciones de ir hacia adelante y hacia atrás, y deberás almacenar las páginas
   * visitadas en dos pilas diferentes.
  */
  browserHistory();

  /**
   * DIFICULTAD EXTRA
   * Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
   * impresora compartida que recibe documentos y los imprime cuando así se le indica.
   * La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
   * interpretan como nombres de documentos.
  */
  printer();
}

void exampleQueue() {
  final List<String> queue = [];

  void pushQueue(String value) {
    queue.add(value);
  }

  String? popQueue() {
    if (queue.isEmpty) {
      return null;
    }
    return queue.removeAt(0);
  }

  // COLAS
  pushQueue('A');
  pushQueue('B');
  pushQueue('C');
  print(popQueue()); // A
  print(popQueue()); // B
  print(popQueue()); // C
  print(popQueue()); // null
}

void exampleStack() {
  final List<String> stack = [];

  void pushStack(String value) {
    stack.add(value);
  }

  String? popStack() {
    if (stack.isEmpty) {
      return null;
    }
    return stack.removeLast();
  }

  pushStack('A');
  pushStack('B');
  pushStack('C');
  print(popStack()); // C
  print(popStack()); // B
  print(popStack()); // A
  print(popStack()); // null
}

void browserHistory() {
  final List<String> history = [];
  final List<String> forwardHistory = [];

  void navigateTo(String page) {
    history.add(page);
    forwardHistory.clear();
  }

  void goBack() {
    if (history.isEmpty) {
      return;
    }
    final page = history.removeLast();
    forwardHistory.add(page);
  }

  void goForward() {
    if (forwardHistory.isEmpty) {
      return;
    }
    final page = forwardHistory.removeLast();
    history.add(page);
  }

  navigateTo('google.com');
  navigateTo('youtube.com');
  navigateTo('facebook.com');
  print(history); // [google.com, youtube.com, facebook.com]
  goBack();
  print(history); // [google.com, youtube.com]
  print(forwardHistory); // [facebook.com]
  goForward();
  print(history); // [google.com, youtube.com, facebook.com]
  goBack();
  goBack();
  print(history); // [google.com]
  navigateTo('twitter.com');
  print(history); // [google.com, twitter.com]
  print(forwardHistory); // []
}

void printer() {
  final List<String> queue = [];

  void addDocument(String document) {
    queue.add(document);
  }

  void printDocument() {
    if (queue.isEmpty) {
      return;
    }
    final document = queue.removeAt(0);
    print('Imprimiendo: $document');
  }

  addDocument('documento1');
  addDocument('documento2');
  addDocument('documento3');
  printDocument(); // Imprimiendo: documento1
  printDocument(); // Imprimiendo: documento2
  printDocument(); // Imprimiendo: documento3
  printDocument(); // No imprime nada
}
