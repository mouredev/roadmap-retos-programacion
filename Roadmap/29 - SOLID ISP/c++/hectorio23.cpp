// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23 

#include <cstdlib>
#include <iostream>
#include <memory>

// Define una interfaz abstracta para la funcionalidad de impresión
class Printer {
public:
    virtual void print() const = 0;
    virtual ~Printer() = default;
};

// Define una interfaz abstracta para la funcionalidad de escaneo
class Scanner {
public:
    virtual void scan() const = 0;
    virtual ~Scanner() = default;
};

// Define una interfaz abstracta para la funcionalidad de fax
class Fax {
public:
    virtual void fax() const = 0;
    virtual ~Fax() = default;
};

// Implementa una impresora en blanco y negro que solo necesita la interfaz de impresión
class BlackAndWhitePrinter : public Printer {
public:
    void print() const override {
        std::cout << "[+] - Imprimiendo en blanco y negro" << std::endl;
    }
};

// Implementa una impresora a color que solo necesita la interfaz de impresión
class ColorPrinter : public Printer {
public:
    void print() const override {
        std::cout << "[+] - Imprimiendo en color" << std::endl;
    }
};

// Implementa una impresora multifunción que necesita todas las interfaces: impresión, escaneo y fax
class MultiFunctionPrinter : public Printer, public Scanner, public Fax {
public:
    void print() const override {
        std::cout << "[+] - Imprimiendo en multifunción" << std::endl;
    }
    void scan() const override {
        std::cout << "[+] - Escaneando en multifunción" << std::endl;
    }
    void fax() const override {
        std::cout << "[+] - Enviando fax en multifunción" << std::endl;
    }
};

// Función que prueba la funcionalidad de impresión de una impresora
void testPrinter(const Printer& printer) {
    printer.print();
}

// Función que prueba la funcionalidad de escaneo de un escáner
void testScanner(const Scanner& scanner) {
    scanner.scan();
}

// Función que prueba la funcionalidad de fax de un dispositivo de fax
void testFax(const Fax& fax) {
    fax.fax();
}

int main() {
    // Crear instancias de las impresoras
    BlackAndWhitePrinter b_and_w_printer;
    ColorPrinter color_printer;
    MultiFunctionPrinter multi_printer;

    // Probar las impresoras
    testPrinter(b_and_w_printer);
    testPrinter(color_printer);
    testPrinter(multi_printer);
    testScanner(multi_printer);
    testFax(multi_printer);

    return EXIT_SUCCESS;
}
