"""
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
"""

# To use interfaces
from abc import ABC, abstractmethod


# Incorrect


class WorkerInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Human(WorkerInterface):
    def work(self):
        print("Working")

    def eat(self):
        print("Eating")


class Robot(WorkerInterface):
    def work(self):
        print("Working")

    def eat(self):
        pass  # Robots don't eat


""" What is wrong?
- Interface has two methods, but one of its children classes doesn't use it.
"""


# Correct


class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        pass


class EatInterface(ABC):

    @abstractmethod
    def eat(self):
        pass


class Human(WorkInterface, EatInterface):
    def work(self):
        print("Working")

    def eat(self):
        print("Eating")


class Robot(WorkInterface):
    def work(self):
        print("Working")


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()

"""
Use only interfaces that are always necessary for the children. If one of the
children doesn't use one of the methods, it's better to split the interface and
add only the ones that are going to be implemented.
"""


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

# Define interfaces


class PrinterInterface(ABC):

    @abstractmethod
    def print(self, document: str):
        pass


class ColorPrinterInterface(ABC):

    @abstractmethod
    def print_color(self, document: str):
        pass


class ScannerInterface(ABC):

    @abstractmethod
    def scan(self, document: str) -> str:
        pass


class FaxInterface(ABC):

    @abstractmethod
    def send_fax(self, document):
        pass


# Create classes


class Printer(PrinterInterface):
    def print(self, document: str):
        print(f"Printing (black & white): {document}")


class ColorPrinter(ColorPrinterInterface):
    def print_color(self, document: str):
        print(f"Printing (color): {document}")


class MultifunctionPrinter(
    PrinterInterface, ColorPrinterInterface, ScannerInterface, FaxInterface
):
    def print(self, document: str):
        print(f"Printing (black & white): {document}")

    def print_color(self, document: str):
        print(f"Printing (color): {document}")

    def scan(self, document: str) -> str:
        print(f"Scanning document: {document}")
        return "scanned" + document

    def send_fax(self, document):
        print(f"Sending through fax: {document}")


# Testing the classes

DOCUMENT = "my-document.txt"

printer = Printer()
printer.print(DOCUMENT)

color_printer = ColorPrinter()
color_printer.print_color(DOCUMENT)

multifunction_printer = MultifunctionPrinter()
multifunction_printer.print(DOCUMENT)
multifunction_printer.print_color(DOCUMENT)
multifunction_printer.scan(DOCUMENT)
multifunction_printer.send_fax(DOCUMENT)
