// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23 

"use strict";

// Define una clase abstracta para la funcionalidad de impresión
class Printer {
    print() {
        throw new Error("[+] - Este método debe ser implementado por una subclase.");
    }
}

// Define una clase abstracta para la funcionalidad de escaneo
class Scanner {
    scan() {
        throw new Error("[+] - Este método debe ser implementado por una subclase.");
    }
}

// Define una clase abstracta para la funcionalidad de fax
class Fax {
    fax() {
        throw new Error("[+] - Este método debe ser implementado por una subclase.");
    }
}

// Implementa una impresora en blanco y negro que solo necesita la interfaz de impresión
class BlackAndWhitePrinter extends Printer {
    print() {
        return "[+] - Imprimiendo en blanco y negro";
    }
}

// Implementa una impresora a color que solo necesita la interfaz de impresión
class ColorPrinter extends Printer {
    print() {
        return "[+] - Imprimiendo en color";
    }
}

// Implementa una impresora multifunción que necesita todas las interfaces: impresión, escaneo y fax
class MultiFunctionPrinter extends Printer {
    print() {
        return "[+] - Imprimiendo en multifunción";
    }
    scan() {
        return "[+] - Escaneando en multifunción";
    }
    fax() {
        return "[+] - Enviando fax en multifunción";
    }
}

// Función que prueba la funcionalidad de impresión de una impresora
function testPrinter(printer) {
    console.log(printer.print());
}

// Función que prueba la funcionalidad de escaneo de un escáner
function testScanner(scanner) {
    console.log(scanner.scan());
}

// Función que prueba la funcionalidad de fax de un dispositivo de fax
function testFax(fax) {
    console.log(fax.fax());
}

// Crear instancias de las impresoras
const b_and_w_printer = new BlackAndWhitePrinter();
const color_printer = new ColorPrinter();
const multi_printer = new MultiFunctionPrinter();

// Probar las impresoras
testPrinter(b_and_w_printer);
testPrinter(color_printer);
testPrinter(multi_printer);
testScanner(multi_printer);
testFax(multi_printer);
