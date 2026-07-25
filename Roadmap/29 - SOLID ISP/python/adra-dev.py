"""
EJERCICIO:
Explora el "Principio SOLID de Segregación de Interfaces (Interface 
Segregation Principle, ISP)" y crea un ejemplo simple donde se 
muestre su funcionamiento de forma correcta e incorrecta.

DIFICULTAD EXTRA(opcional):
Crea un gestor de impresoras.

Requisitos:
1. Algunas impresoras sólo imprimen en blanco y negro.
2. Otras sólo a color.
3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
Instrucciones:
1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
2. Aplica el ISP a la implementación.
3. Desarrolla un código que compruebe que se cumple el principio.

by adra-dev
"""

"""
Interface Segregation Principle (ISP):
El Principio de Segregación de Interfaces también fue propuesto por 
uncle bob. la idea central del principio es:

    "Los clientes no deberían ser forzados a depender de métodos que 
    ellos no usan. las interfaces pertenecen a los clientes no a sus 
    herencias."

documentacion:"https://realpython.com/solid-principles-python/"
    
En este caso, los clientes son las clases y las subclases y las 
interfaces consisten en los métodos y atributos. En otras palabras, 
si una clase utiliza métodos en particular o atributos entonces esos 
métodos y atributos deberían ser segregados a clases más específicas.

Considera el siguiente ejemplo.
"""

# printers_isp.py

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")

class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

"""
En este ejemplo, la clase base, impresora, provee las interfaces que 
sus subclases deben implementar. OldPrinter hereda de printer y debe 
implementar la misma interfaz. Sin embargo, OldPrinter no utiliza los
 métodos .fax() y .scan() porque este tipo de impresora no soporta 
 estas funcionalidades.

Esta implementación viola el ISP porque obliga a OldPrinter a mostrar
una interfaz que la subclase no implementa o necesita. Para 
solucionar este problema, deberías separar las interfaces en clases 
más pequeñas y más específicas. Así después puedes crear subclases 
más concretas por medio de la herencia de múltiples interfaces que 
dicha subclase necesite.

"""

# printers_isp.py

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")

"""

Ahora Printer, Fax y Scanner son clases base  que proveen interfaces 
específicas con una única responsabilidad cada una. Para crear 
OldPrinter, ya solo necesitas heredar la interfaz de Printer. De este
modo, la clase no tendrá métodos que no se utilicen. Para crear la 
clase ModernPrinter, solo necesitas heredar de todas las interfaces 
en resumen haz segregado la interfaz de Printer. 

"""

"""
Extra
"""

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class BlackWhitePrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")


class ColorPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color...")


class LastModelPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def print_color(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


def test_printers():

    printer = BlackWhitePrinter()
    color_printer = ColorPrinter()
    multifunction_printer = LastModelPrinter()

    printer.print("doc.pdf")
    color_printer.print("doc.pdf")
    multifunction_printer.print("doc.pdf")
    multifunction_printer.print_color("doc.pdf")
    multifunction_printer.scan("doc.pdf")
    multifunction_printer.fax("doc.pdf")


test_printers()