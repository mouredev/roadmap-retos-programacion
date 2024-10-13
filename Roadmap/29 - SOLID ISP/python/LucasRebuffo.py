""" /*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
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
 */ """

""" El principio de ISP establece que las clases no deben esxponer metodos que no se utilizan,
    por lo tanto se deben crear interfaces o clases especificas. """

from abc import ABC, abstractmethod


class Bird(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def do_sound(self) -> str:
        pass


class FlyingBird(Bird):

    @abstractmethod
    def fly(self):
        pass


class SwimmingBird(Bird):

    @abstractmethod
    def swim(self):
        pass


class Crow(FlyingBird):

    def fly(self):
        print(f"{self.name} is flying high and fast!")

    def do_sound(self) -> str:
        return "Caw"


class Duck(SwimmingBird, FlyingBird):

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"


""" * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio. """


class PrintInterface(ABC):
    @abstractmethod
    def print(self, document: str):
        pass


class ColorPrintInterface(ABC):
    @abstractmethod
    def print_color(self, document: str):
        pass


class ScanInterface(ABC):
    @abstractmethod
    def scan(self, document: str):
        pass


class SendFaxInterface(ABC):
    @abstractmethod
    def send_fax(self, document: str):
        pass


class Printer(PrintInterface):
    def print(self, document: str):
        print(f"Imprimiendo en blanco y negro el documento {document}.")


class ColorPrinter(ColorPrintInterface):
    def print_color(self, document: str):
        print(f"Imprimiendo a color el documento {document}.")


class MultiFunctionPrinter(
    PrintInterface, ScanInterface, SendFaxInterface, ColorPrintInterface
):
    def print_color(self, document: str):
        print(f"Imprimiendo a color el documento {document}.")

    def print(self, document: str):
        print(f"Imprimiendo en blanco y negro el documento {document}.")

    def scan(self, document: str):
        print(f"Escaneando el documento {document}.")
        return f"Documento {document} escaneado."

    def send_fax(self, document: str):
        print(f"Enviando por fax el documento {document}.")


printer = Printer()
color_printer = ColorPrinter()
multifunction_printer = MultiFunctionPrinter()

printer.print("doc.pdf")
color_printer.print_color("doc.pdf")
multifunction_printer.print("doc.pdf")
multifunction_printer.print_color("doc.pdf")
multifunction_printer.scan("doc.pdf")
multifunction_printer.send_fax("doc.pdf")
