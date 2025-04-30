'''
SOLID
ISP: Interface Swgregation Principle
principio de segregación de interfaces
    # no se puede usar el método de la clase padre
    # en la clase hija
    # se debe crear una interfaz para cada clase hija
    # y no una interfaz para todas las clases hijas
    
'''
from abc import ABC, abstractmethod

# Sin ISP


class WorkerInteface(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class HumanWorker(WorkerInteface):
    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")


class RobotWorker(WorkerInteface):
    def work(self):
        print("Trabajando")

    def eat(self):
        # no se puede usar el método de la clase padre en la clase hija rompe el ISP
        raise NotImplementedError("Los robots no comen")

# ISP


class WorkInteface(ABC):
    @abstractmethod
    def work(self):
        pass


class EatInteface(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(WorkInteface, EatInteface):
    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")


class RobotWorker(WorkInteface):
    def work(self):
        print("Trabajando")

# Extra


class PrinterInteface(ABC):
    @abstractmethod
    def print(self, document: str):
        pass


class ColorPrinterInteface(ABC):
    @abstractmethod
    def print_color(self, document: str):
        pass


class ScannerInteface(ABC):
    @abstractmethod
    def scan(self, document: str) -> str:
        pass


class FaxInteface(ABC):
    @abstractmethod
    def send_fax(self, document: str):
        pass


class Printer(PrinterInteface):
    def print(self, document: str):
        print(f"Imprimiendo {document} en blanco y negro")


class ColorPrinter(ColorPrinterInteface):
    def print_color(self, document: str):
        print(f"Imprimiendo {document} en color")


class MultifunctionPrinter(PrinterInteface, ColorPrinterInteface, ScannerInteface, FaxInteface):
    def print(self, document: str):
        print(f"Imprimiendo {document} en blanco y negro")

    def print_color(self, document: str):
        print(f"Imprimiendo {document} en color")

    def scan(self, document: str) -> str:
        print(f"Escaneando {document}")
        return document

    def send_fax(self, document: str):
        print(f"Enviando fax de {document}")


def test_printer():
    printer = Printer()
    color_printer = ColorPrinter()
    mfp = MultifunctionPrinter()

    printer.print("documento1.txt")
    color_printer.print_color("documento2.txt")
    print("\tMultifunción")
    mfp.print("documento_byn.pdf")
    mfp.print_color("documento_color.pdf")
    mfp.scan("documento_scan.pdf")
    mfp.send_fax("documento_fax.pdf")


test_printer()
