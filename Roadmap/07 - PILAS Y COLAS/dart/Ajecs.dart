import 'dart:collection';
import 'dart:io';

void main() {
  stdout.write(
    '\n************************** Pilas y colas ************************\n\n',
  );

  /*
    Existe una estructura en Dart que comparte la caracteristica de ambas: ListQueue del paquete collection.
    Utilizando el constructor Queue() se crea un estructura llamada "deque" 
    o "cola doblemente teminada" (double-ended queue).
    Permite eliminar al principio y al final items pero no entre medio. 
    Ya que no maneja una posición fija como en las listas. Usa un Buffer circular.
    Esto permite optimizar, en especial, la eliminación al principio ya que no requiere mover de posición todos
    los items.
    Y mantiene un rendimiento estable aunque la lista aumente de tamaño.
  */

  print('<< Pila/Stack LIFO >>\n');

  // Last In First Out (Último en Ingresar, Primero en Salir)

  List stack = [];
  stack.add(1); // push
  stack.add(2);
  stack.add(3);

  // Las listas en dart como en python funcinoan como una pila.

  int stackItem = stack.removeLast(); // pop
  // Simil pop() Quita el último item y devuelve su valor.

  print('El elemento quitado de la pila es el $stackItem');
  print('Pila restante: $stack\n');

  print('<< Cola/Queue FIFO >>\n');

  // First In First Out (Primero en entrar Primero en salir)

  List queue = [];
  queue.add(1); // enqueue
  queue.add(2);
  queue.add(3);

  int queueItem = queue.removeAt(0);

  print('El elemento quitado de la cola (lista) es el $queueItem');
  print('Lista actualizada: $queue\n');

  print('<< Pila y cola mediante ListQueue >>');

  // Con ListQueue

  Queue realQueue = Queue.from(queue);
  int realQueueItem = realQueue.removeFirst();
  realQueue.addFirst(4);

  print('El elemento quitado de la "cola real" es el $realQueueItem');
  print('El elemento añadido de la "cola real" es el $realQueueItem');
  print('Cola real actualizada: $realQueue\n');

  // ! print(realQueue[0]) -> No puede accederse a un elemento por su posicion en una cola.

  Queue realStack = Queue.from(stack);
  int realStackItem = realStack.removeLast();
  realStack.addLast(4);

  print('El elemento quitado de la "pila real" es el $realStackItem');
  print('El elemento añadido de la "pila real" es el $realStackItem');
  print('Pila real actualizada: $realStack\n');

  print('\n************************** Extra ************************\n');

  void navigation() {
    ListQueue<String> sites = ListQueue.of(['nav://newtab']); // "El home"
    List<String> sitesHistory = [];

    bool goOn = true;
    String siteInput = '';

    // ///////////////////////////FUNCIONES//////////////////////////////////////////

    void search(String newSite, {extension = 'com'}) {
      if (newSite.isEmpty) {
        print('Ingrese el nombre del sitio');
        return;
      }
      stdout.write('Ingrese la extension(sin "."): \n');
      String extensionInput = stdin.readLineSync() ?? '';
      if (extensionInput.isNotEmpty) {
        extension = extensionInput.toLowerCase().trim();
      }
      sitesHistory.clear(); // al navegar a uno nuevo, se pierde el forward
      newSite = 'https://${newSite.trim().toLowerCase()}.$extension';
      sites.addLast(newSite);
      print('\nNavegando en: $newSite');
    }

    String back() {
      if (sites.length <= 1) return 'No hay sitio atras';

      final siteRemoved = sites.removeLast(); // sitio actual
      sitesHistory.add(siteRemoved); // lo guardamos para volver atrás
      return sites.last;
    }

    String forward() {
      if (sitesHistory.isEmpty) return 'No hay sitio adelante';

      final siteToRestore = sitesHistory.removeLast();
      sites.addLast(siteToRestore);
      // Se añade el elemento restaurado a partir de otra lista que guarda los sitios "quitados"
      return siteToRestore;
    }

    // /////////////////////////////////MENU////////////////////////////////////

    print('CONSOLENAV \u{1F9ED}');
    print('Comandos:');
    print('Vuelva o continue con "atras" y "adelante"');
    print('Escriba "salir" para salir del programa');

    while (goOn) {
      print('\nBuscar sitio web : ');

      siteInput = stdin.readLineSync() ?? '';

      switch (siteInput) {
        case 'atras':
          print(back());
          break;
        case 'adelante':
          print(forward());
          break;
        case 'salir':
          print('Saliendo del navegador');
          goOn = false;
          break;
        case 'historial':
          print('\n${sitesHistory.join('\n')}\n');
        default:
          search(siteInput);
          break;
      }
    }
  }

  // navigation();

  // ///////////////////////////////// IMPPRESORA ///////////////////////////////

  void printFiles() {
    // Se Configura la forma en que la entrada de texto se visualiza en la terminal.
    // ! Tiene un comportamiento extraño en Windows. y se debe mantener el orden de las declaraciones.
    // ! Aún eliminadas en código la configuración se mantiene.. (!)
    stdin.lineMode = true;
    stdin.echoMode = true;

    ListQueue files = ListQueue();
    String printInput;
    bool goOn = true;

    print('IMPRESORA \u{1F5A8}');
    print('Comandos:');
    print('Ingrese "imprimir" para imprimir el primer archivo pendiente');
    print('Escriba "salir" para salir del programa');

    while (goOn) {
      print('\nIngresa el nombre del archivo a imprimir: ');

      printInput = stdin.readLineSync() ?? '';

      switch (printInput) {
        case 'imprimir':
          if (files.length >= 1) {
            String printFile = files.removeFirst();
            print('Imprimiendo: $printFile');
          } else {
            print('No hay archivos en la cola para imprimir');
          }
          break;
        case 'salir':
          goOn = false;
          break;
        default:
          String file = printInput.trim().toLowerCase();

          if (printInput.isEmpty) {
            print('Ingresa un nombre');
            break;
          }

          print('Elige el formato del archivo:');
          print('1.pdf');
          print('2.txt');
          print('3.docx');
          String formatOption = stdin.readLineSync() ?? '';

          switch (formatOption) {
            case '1':
              file = '$printInput.pdf';
              break;
            case '2':
              file = '$printInput.txt';
              break;
            case '3':
              file = '$printInput.docx';
              break;
            default:
              print('Valor no válido. Presiona el número 1, 2 o 3');
              break;
          }

          if (formatOption == '1' ||
              formatOption == '2' ||
              formatOption == '3') {
            files.add(file);
            print('\nArchivo ingresado: $file');

            final numberedFiles = <String>[];
            for (final item in files.toList().indexed) {
              numberedFiles.add('${item.$1 + 1}. ${item.$2}');
            }
            // .Indexed crea una lista de records con el index y el item.
            // El for itera en la lista y crea una nueva lista con el index y el item.

            print(numberedFiles.join('\n'));
          }
          break;
      }
    }
  }

  printFiles();
}
