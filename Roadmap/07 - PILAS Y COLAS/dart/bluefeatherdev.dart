/*
* EJERCICIO:
* Implementa los mecanismos de introducción y recuperación de elementos propios de las
* pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
* o lista (dependiendo de las posibilidades de tu lenguaje).
*
* DIFICULTAD EXTRA (opcional):
* - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
*   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
*   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
*   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
*   el nombre de una nueva web.
* - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
*   impresora compartida que recibe documentos y los imprime cuando así se le indica.
*   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
*   interpretan como nombres de documentos.
*/

import 'dart:io';

/// 1. [Pila/Stack - LIFO]:
void stackExample() {
  List<dynamic> stack = [];
  for (var i = 0; i < 5; i++) stack.add(i);
  print(stack); // [0, 1, 2, 3, 4]

  dynamic stackItem = stack[stack.length - 1];
  print(stackItem);   // 4 (OK)
  print(stack.last);  // 4 (OK)
  print(stack);       // [0, 1, 2, 3, 4]

  stack.removeAt(stack.length - 1);
  print(stackItem);   // 4 (not by reference)
  print(stack.last);  // 3 (OK)
  print(stack);       // [0, 1, 2, 3]

  stack.removeLast();
  print(stackItem);   // 4 (not by reference)
  print(stack.last);  // 2 (OK)
  print(stack);       // [0, 1, 2]
}

/// 2. [Cola/Queue - FIFO]:
void queueExample() {
  List<dynamic> queue = [];
  for (var i = 0; i < 5; i++) queue.add(i);
  print(queue); // [0, 1, 2, 3, 4]

  dynamic queueItem = queue[0];
  print(queueItem);    // 0 (OK)
  print(queue.first);  // 0 (OK)
  print(queue);        // [0, 1, 2, 3, 4]

  queue.removeAt(0);
  print(queueItem);    // 0 (not by reference)
  print(queue.first);  // 1 (OK)
  print(queue);        // [1, 2, 3, 4]

  queue.removeAt(0);
  print(queueItem);    // 0 (not by reference)
  print(queue.first);  // 2 (OK)
  print(queue);        // [2, 3, 4]
}

/// 3. [Pila/Stack - DIFICULTAD EXTRA]:
void browser() {
  List<dynamic> pageStack = [];
  int pointer = 0;
  while (true) {
    // leer input del usuario
    print('Escriba acción "adelante/atrás/salir/ver" (sin tildes):');
    String? action = stdin.readLineSync(); /// `stdin.readLineSync()` puede tener problemas para leer caracteres con tilde...

    // finalizar navegación
    if (action == 'salir') {
      print('¡Hasta luego!');
      break;
    } 

    // avanzar en el stack
    else if (action == 'adelante') {
      if (pageStack.isEmpty) {
        print('No has visitado páginas...');
      }
      else if (pageStack.length == 1) {
        print('Solo has visitado una página...');
      }
      else if (pointer == pageStack.length - 1) {
        print('Estás en la última página...');
      }
      else {
        pointer++;
        print('Ahora estás en: ${pageStack[pointer]}');
      }
    }

    // retroceder en el stack
    else if (action == 'atrás' || action == 'atras') {
      if (pageStack.isEmpty) {
        print('No has visitado páginas...');
      }
      else if (pointer == 0) {
        print('Estás en la página de inicio');
      }
      else {
        pointer--;
        print('Ahora estás en: ${pageStack[pointer]}');
      }
    } 
    
    // ver páginas del stack
    else if (action == 'ver') {
      print('Páginas navegador: $pageStack');
      if (pageStack.isEmpty) {
        print('No has visitado páginas...');
      } else {
        print('Estás en: ${pageStack[pointer]}');
      }
    } 
    
    // añadir páginas al stack
    else {
      pageStack.add(action);
      pointer = pageStack.length - 1;
    } 
  }
}

/// 4. [Cola/Queue - DIFICULTAD EXTRA]:
void printer() {
  List<dynamic> documentQueue = [];

  while (true) {
    // leer input del usuario
    print('Escriba acción "imprimir/salir":');
    String? action = stdin.readLineSync();

    // finalizar navegación
    if (action == 'salir') {
      print('¡Hasta luego!');
      break;
    } 

    // imprimir el documento
    else if (action == 'imprimir') {
      if (documentQueue.isEmpty) {
        print('Nada por imprimir...');
        print('Cola de impresión: $documentQueue');
      } else {
        print('Imprimiendo "${documentQueue.first}"...');
        documentQueue.removeAt(0);
        print('Cola de impresión: $documentQueue');
      }
    }
    
    // añadir el documento
    else {
      documentQueue.add(action);
      print('Cola de impresión: $documentQueue');
    } 
  }
}

void main() {
  /// 1. [Pila/Stack - LIFO]:
  stackExample();

  /// 2. [Cola/Queue - FIFO]:
  queueExample();

  /// 3. [Pila/Stack - DIFICULTAD EXTRA]:
  browser();

  /// 4. [Cola/Queue - DIFICULTAD EXTRA]:
  printer();
}
