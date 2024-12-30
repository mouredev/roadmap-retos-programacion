/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
___________________________________________________
#29 SOLID: PRINCIPIO DE SEGREGACIÓN DE INTERFACES (ISP)
---------------------------------------------------
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
// ________________________________________________________
// Abstracciones
class AbsPlayable {
    play() {
        throw new Error("El método 'play' debe ser implementado.");
    }
}

class AbsDisplayable {
    display() {
        throw new Error("El método 'display' debe ser implementado.");
    }
}

//__________________________
// Implementar abstracciones

class Speaker extends AbsPlayable {
    play() {
        console.log("El altavoz está reproduciendo música.");
    }
}

class Phone extends AbsPlayable {
    play() {
        console.log("El teléfono está reproduciendo música.");
    }
}

Object.assign(Phone.prototype, AbsDisplayable.prototype);

Phone.prototype.display = function() {
    console.log("El teléfono está mostrando la pantalla de reproducción.");
};

//__________________________
// Utilización
const speaker = new Speaker();
speaker.play();

const phone = new Phone();
phone.play();
phone.display();

// ________________________________________________________
// DIFICULTAD EXTRA
// ----------------

// Abstracciones
class AbsPrinter {
    printFile(file) {
        throw new Error("El método 'printFile' debe ser implementado.");
    }
}

class AbsScanner {
    toScan(pathSave) {
        throw new Error("El método 'toScan' debe ser implementado.");
    }
}

class AbsFax {
    sendFile(file, phoneNumber) {
        throw new Error("El método 'sendFile' debe ser implementado.");
    }
}

//__________________________
// Implementar abstracciones
class MonoPrinter extends AbsPrinter {
    printFile(file) {
        console.log("\nImpresora blanco y negro:");
        console.log(`${file} se imprimió.`);
    }
}

class ColorPrinter extends AbsPrinter {
    printFile(file) {
        console.log("\nImpresora a color:");
        console.log(`${file} se imprimió.`);
    }
}

class Scanner extends AbsScanner {
    toScan(pathSave) {
        console.log("\nEscaneo realizado, Guardado en:", pathSave);
    }
}

class Fax extends AbsFax {
    sendFile(file, phoneNumber) {
        console.log(`\n- ${file} fue enviado a: ${phoneNumber}`);
    }
}

class MultiFunctionPrinter {
    constructor() {
        this.monoPrinter = new MonoPrinter();
        this.colorPrinter = new ColorPrinter();
        this.scanner = new Scanner();
        this.fax = new Fax();
    }
}

//__________________________
// Utilización
console.log("\nDIFICULTAD EXTRA");

const monoPrinter = new MonoPrinter();
monoPrinter.printFile("filex.pdf");

const colorPrinter = new ColorPrinter();
colorPrinter.printFile("filex.pdf");

const scanner = new Scanner();
scanner.toScan("c:\\docs");

const fax = new Fax();
fax.sendFile("filex.pdf", 12345678);

console.log("\n___________\nMultifunción:");
const multifunction = new MultiFunctionPrinter();

multifunction.monoPrinter.printFile("filex.pdf");
multifunction.colorPrinter.printFile("filex.pdf");
multifunction.scanner.toScan("c:\\docs");
multifunction.fax.sendFile("filex.pdf", 12345678);
