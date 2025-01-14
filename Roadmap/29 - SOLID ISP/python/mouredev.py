"""
Ejercicio
"""

from abc import ABC, abstractmethod

# Sin ISP


class WorkerInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Human(WorkerInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")


class Robot(WorkerInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        # Los robots no comen
        pass


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
robot.eat()  # error

# Con ISP


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
        print("Trabajando")

    def eat(self):
        print("Comiendo")


class Robot(WorkInterface):

    def work(self):
        print("Trabajando")


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()

"""
Extra
"""


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
    def send_fax(self, document: str):
        pass


class Printer(PrinterInterface):
    def print(self, document: str):
        print(f"Imprimiendo en blanco y negro el documento {document}.")


class ColorPrinter(ColorPrinterInterface):
    def print_color(self, document: str):
        print(f"Imprimiendo a color el documento {document}.")


class MultifunctionPrinter(PrinterInterface, ColorPrinterInterface, ScannerInterface, FaxInterface):
    def print(self, document: str):
        print(f"Imprimiendo en blanco y negro el documento {document}.")

    def print_color(self, document: str):
        print(f"Imprimiendo a color el documento {document}.")

    def scan(self, document: str) -> str:
        print(f"Escaneando el documento {document}.")
        return f"Documento {document} escaneado."

    def send_fax(self, document: str):
        print(f"Enviando por fax el documento {document}.")


def test_printers():

    printer = Printer()
    color_printer = ColorPrinter()
    multifunction_printer = MultifunctionPrinter()

    printer.print("doc.pdf")
    color_printer.print_color("doc.pdf")
    multifunction_printer.print("doc.pdf")
    multifunction_printer.print_color("doc.pdf")
    multifunction_printer.scan("doc.pdf")
    multifunction_printer.send_fax("doc.pdf")


test_printers()
