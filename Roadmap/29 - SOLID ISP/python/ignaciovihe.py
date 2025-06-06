"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""

from abc import ABC, abstractmethod
#ISP incorrecto

class Animal: # La superclase obliga a implementar todos los metodos, aunque alguno no tiene sentido para la subclase perro.
    def fly(self):
        pass

    def run(self):
        pass

    def swim(self):
        pass


class Dog(Animal):
    def fly(self):
        raise Exception("Los perros no vuelan.")

    def run(self):
        print("El perro corre")

    def swimm(self):
        print("El perro nada")

"""my_dog = Dog()
my_dog.run()
my_dog.swimm()
my_dog.fly()""" #Da error

# ISP correcto
class RunInterface(ABC):
    @abstractmethod
    def run(self):
        pass

class FLyInterface(ABC):
    @abstractmethod
    def fly(self):
        pass

class SwimInterface(ABC):
    @abstractmethod
    def swim(self):
        pass

class Dog(RunInterface,SwimInterface):
    def run(self):
        print("El perro corre")

    def swim(self):
        print("El perro nada")

class Bird(FLyInterface):
    def fly(self):
        print("El pajaro vuela")

my_dog = Dog()
my_dog.run()

my_bird = Bird()
my_bird.fly()

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
 * 3. Desarrolla un código que compruebe que se cumple el principio."""

class MonochromePrinterInterface(ABC):
    @abstractmethod
    def print_monochrome(self, document: str):
        pass


class ColorPrinterInterface(ABC):
    @abstractmethod
    def print_color(self, document: str):
        pass


class ScannInterface(ABC):
    @abstractmethod
    def scan(self, document) -> str:
        pass


class FaxInterface(ABC):
    @abstractmethod
    def fax(self, document: str):
        pass


class MonochromePrinter(MonochromePrinterInterface):
    def print_monochrome(self, document):
        print(f"Imprimiendo {document} en blanco y negro")


class ColorPrinter(ColorPrinterInterface):
    def print_color(self, document):
        print(f"Imprimiendo {document} en color")


class MultifunctionPrinter(MonochromePrinterInterface, ColorPrinterInterface, ScannInterface, FaxInterface):
    def fax(self, document):
        print(f"Enviando {document} por fax")

    def scan(self, document):
        print(f"Escaneando documento {document}")
        return f"Documento {document} escaneado"

    def print_color(self, document):
        print(f"Imprimiendo {document} en color")

    def print_monochrome(self, document):
        print(f"Imprimiendo {document} en blanco y negro")


monochrome_printer = MonochromePrinter()
color_printer = ColorPrinter()
multifunction = MultifunctionPrinter()

monochrome_printer.print_monochrome("doc1.pdf")
color_printer.print_color("doc1.pdf")
multifunction.fax("doc1.pdf")
multifunction.print_monochrome("doc1.pdf")
multifunction.print_color("doc1.pdf")
multifunction.scan("doc1.pdf")