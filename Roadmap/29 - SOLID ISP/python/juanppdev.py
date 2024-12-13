"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""

# Correcto

from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class RobotWorker(Workable):
    def work(self):
        print("Robot working")


# Incorrecto

from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Worker):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

class RobotWorker(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        raise NotImplementedError("Robots don't eat")


"""
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
"""

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class Fax(ABC):
    @abstractmethod
    def send_fax(self):
        pass

class BlackAndWhitePrinter(Printer):
    def print(self):
        print("Printing in black and white")

class ColorPrinter(Printer):
    def print(self):
        print("Printing in color")

class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self):
        print("Printing in color")

    def scan(self):
        print("Scanning document")

    def send_fax(self):
        print("Sending fax")


class PrinterManager:
    def __init__(self, printer: Printer):
        self.printer = printer

    def print_document(self):
        self.printer.print()

class MultiFunctionPrinterManager:
    def __init__(self, printer: MultiFunctionPrinter):
        self.printer = printer

    def print_document(self):
        self.printer.print()

    def scan_document(self):
        self.printer.scan()

    def send_fax(self):
        self.printer.send_fax()


# Usando una impresora en blanco y negro
bw_printer = BlackAndWhitePrinter()
printer_manager = PrinterManager(bw_printer)
printer_manager.print_document()

# Usando una impresora a color
color_printer = ColorPrinter()
printer_manager = PrinterManager(color_printer)
printer_manager.print_document()

# Usando una impresora multifunción
multi_printer = MultiFunctionPrinter()
multi_printer_manager = MultiFunctionPrinterManager(multi_printer)
multi_printer_manager.print_document()
multi_printer_manager.scan_document()
multi_printer_manager.send_fax()
