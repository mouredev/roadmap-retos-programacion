/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 */


// Incorrect

class WorkerInterface {
    work() {}
    eat() {}
}


class HumanWrong extends WorkerInterface {
    work() {}
    eat() {}
}


class RobotWrong extends WorkerInterface {
    work() {}
    eat() {/* Robots don't eat */}
}


// Correct

class WorkInterface {
    work() {
        console.log('Working');
    }
}

class EatInterface {
    eat() {
        console.log('Eating');
    }
}


class Human {
    constructor() {
        // Extend from multiple classes
        this.workSuper = new WorkInterface()
        this.eatSuper = new EatInterface()
    }

    work() {
        this.workSuper.work()
    }

    eat() {
        this.eatSuper.eat()
    }
}

class Robot extends WorkInterface {
    work() {
        super.work()
    }
}


const human = new Human()
human.work()
human.eat()

const robot = new Robot()
robot.work()


/**
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 */


class PrinterInterface {
    print(document) {
        console.log(`Printing (black & white): ${document}`);
    }
}


class ColorPrinterInterface {
    printColor(document) {
        console.log(`Printing (color): ${document}`);
    }
}


class ScannerInterface {
    scan(document) {
        console.log(`Scanning document: ${document}`);
        return 'scanned' + document
    }
}


class FaxInterface {
    sendFax(document) {
        console.log(`Sending through fax: ${document}`);
    }
}


class Printer extends PrinterInterface {
    print(document) {
        super.print(document);
    }
}


class ColorPrinter extends ColorPrinterInterface {
    printColor(document) {
        super.printColor(document)
    }
}


class MultifunctionPrinter {
    // Private properties -> to use them only inside class
    #printBW
    #colorPrint
    #scanner
    #fax

    constructor() {
        this.#printBW = new PrinterInterface();
        this.#colorPrint = new ColorPrinterInterface();
        this.#scanner = new ScannerInterface();
        this.#fax = new FaxInterface();
    }

    print(document) {
        this.#printBW.print(document);
    }

    printColor(document) {
        this.#colorPrint.printColor(document);
    }

    scan(document) {
        return this.#scanner.scan(document);
    }

    sendFax(document) {
        this.#fax.sendFax(document);
    }
}


let doc = 'my-document.txt';

const printer = new Printer();
printer.print(doc);

const colorPrinter = new ColorPrinter();
colorPrinter.printColor(doc);


doc = 'another-doc.txt';

const multifunctionPrinter = new MultifunctionPrinter();
multifunctionPrinter.print(doc);
multifunctionPrinter.printColor(doc);
multifunctionPrinter.scan(doc);
multifunctionPrinter.sendFax(doc);