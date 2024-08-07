/// #07 PILAS Y COLAS

import 'dart:io';

void main() {
  /**
   * Implementa los mecanismos de introducción y recuperación de elementos propios de las
   * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
   * o lista (dependiendo de las posibilidades de tu lenguaje).
  */
  exampleQueue();
  exampleStack();

  // DIFICULTAD EXTRA

  String option = "";
  do {
    print('''
    1. Navegador web
    2. Imprimir documento
    Q. Salir o "Ctrl + C"
    ''');
    option = stdin.readLineSync()!.toLowerCase();

    switch (option) {
      case "1":
        browserHistory();
        break;
      case "2":
        printer();
        break;
      case "q":
        print('Programa finalizado');
    }
  } while (option != "q");
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
  const String home = "duckduckgo.com";

  final List<String> history = [];
  final List<String> forwardHistory = [];

  void navigateTo(String page) {
    print('Navegando a $page');
    history.add(page);
    forwardHistory.clear();
  }

  void goHome() {
    history.clear();
    navigateTo(home);
  }

  void printHistory() {
    print('Historial:');
    print(history);
  }

  void goBack() {
    if (history.isEmpty) {
      return;
    }
    final page = history.removeLast();
    print('Volviendo a $page');
    forwardHistory.add(page);
  }

  void goForward() {
    if (forwardHistory.isEmpty) {
      return;
    }
    final page = forwardHistory.removeLast();
    print('Avanzando a $page');
    history.add(page);
  }

  print('''
    Introduce una web o bien una de las siguientes opciones:
    N. Inicio
    H. Historial
    [. Atrás
    ]. Adelante
    Q. Salir
  ''');

  goHome();

  String option = "";
  do {
    option = stdin.readLineSync()!.toLowerCase();

    switch (option) {
      case "n" || "home":
        goHome();
        break;
      case "h" || "history":
        printHistory();
        break;
      case "[" || "prev" || "back":
        goBack();
        break;
      case "]" || "next" || "forward":
        goForward();
        break;
      case "q":
        print('Cerrando navegador');
        break;
      default:
        if (!option.isEmpty) {
          navigateTo(option);
        }
    }
  } while (option != "q");
}

void printer() {
  final List<String> queue = [];

  void addDocument(String document) {
    queue.add(document);
    print('Documento añadido: $document');
    print('Hay ${queue.length} documentos en la cola');
  }

  void printDocument() {
    if (queue.isEmpty) {
      return;
    }
    final document = queue.removeAt(0);
    if (document.isEmpty) {
      print('No hay documentos para imprimir');
    } else {
      print('Imprimiendo: $document');
    }
  }

  print('''
    Añade un nuevo documento o bien una de las siguientes opciones:
    "P" o "Imprimir" para imprimir
    "Q" para Salir
  ''');

  String option = "";
  do {
    option = stdin.readLineSync()!.toLowerCase();

    switch (option) {
      case "p" || "print" || "imprimir":
        printDocument();
        break;
      default:
        if (!option.isEmpty) {
          addDocument(option);
        }
    }
  } while (option != "q");
}
