// Incorrecto 
// abstract class WorkerInterface {
//   void work();
//   void eat();
// }

// class Human implements WorkerInterface {
//   @override
//   void work() {
//     print('Trabajando');
//   }
//   @override
//   void eat() {
//     print('Comiendo');
//   }
// }

// class Robot implements WorkerInterface {
//   @override
//   void work() {
//     print('Trabajando');
//   }
//   @override
//   void eat() {
//     // los robots no comen
//   }
// }

// Correcto

abstract class WorkInterface {
  void work();
}

abstract class EatInterface {
  void eat();
}

class Human implements WorkInterface, EatInterface {
  @override
  void work() {
    print('Trabajando');
  }

  @override
  void eat() {
    print('Comiendo');
  }
}

class Robot implements WorkInterface {
  @override
  void work() {
    print('Trabajando');
  }
}

// Ejercicio gestor de impresoras 

abstract class PrinterInterface {
  void printBlackWhite(String document);
}

abstract class ScannerInterface {
  void scan(String document);
}

abstract class FaxInterface {
  void sendFax(String document);
}

abstract class ColorPrinterInterface {
  void printColor(String document);
}

class Printer implements PrinterInterface {
  @override
  void printBlackWhite(String document) {
    print('Imprimiendo en blanco y negro el documento $document');
  }
}

class ColorPrinter implements ColorPrinterInterface {
  @override
  void printColor(String document) {
    print('Imprimiendo a color el documento $document');
  }
}

class MultiFunctionPrinter implements PrinterInterface, ColorPrinterInterface, FaxInterface, ScannerInterface {
  @override
  void printBlackWhite(String document) {
    print('Imprimiendo en blanco y negro el documento $document');
  }

  @override
  void printColor(String document) {
    print('Imprimiendo a color el documento $document');
  }

  @override
  void sendFax(String document) {
    print('Enviando por fax el documento $document');
  }

  @override
  void scan(String document) {
    print('Escaneando el documento $document');
  }
}

void testPrinters() {
  Printer printer = Printer();
  ColorPrinter colorPrinter = ColorPrinter();
  MultiFunctionPrinter multiFunctionPrinter = MultiFunctionPrinter();

  printer.printBlackWhite('doc.pdf');
  colorPrinter.printColor('doc.pdf');
  multiFunctionPrinter.printBlackWhite('doc.pdf');
  multiFunctionPrinter.printColor('doc.pdf');
  multiFunctionPrinter.scan('doc.pdf');
  multiFunctionPrinter.sendFax('doc.pdf');
}

void main() {

  // Human human = Human();
  // human.work();
  // human.eat();

  // Robot robot = Robot();
  // robot.work();
  // robot.eat(); // error


  Human human = Human();
  human.work();
  human.eat();

  Robot robot = Robot();
  robot.work();

  // Ejercicio gestor de impresoras 

  testPrinters();

}