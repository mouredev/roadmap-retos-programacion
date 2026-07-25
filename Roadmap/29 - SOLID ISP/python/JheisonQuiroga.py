# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga

"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 *"""

""" 4. Principio de Segregación de Interfaces (ISP)
Los clientes no deben verse obligados a depender de interfaces que no necesitan.
Evita crear interfaces grandes y complejas que obliguen a las clases a implementar métodos
que no necesitan. En su lugar utiliza un interfaces más pequeñas y especificas. 
"""

# Violación del ISP
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def swim(self):
        pass

class Pinguin(Bird):
    def fly(self):
        raise NotImplementedError("Error, los pinguinos no pueden volar")
    
    def swim(self):
        print("El pinguino está nadando")

# Siguiendo el Interface Segregation Principle

class BasicBird(ABC):
    @abstractmethod
    def eat(self):
        pass

class FlyableBird(ABC):
    @abstractmethod
    def fly(self):
        pass

class SwimmableBird(ABC):
    @abstractmethod
    def swim(self):
        pass

# Caso de uso
class Eagle(BasicBird, FlyableBird):
    def eat(self):
        print("El aguila está comiendo")

    def fly(self):
        print("El aguila está volando")

class Pinguin(BasicBird, SwimmableBird):
    def eat(self):
        print("El pinguino está comiendo")

    def swim(self):
        print("El pinguino está nadando")


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
 */
"""

# Gestor de impresoras

class BWPrint(ABC):
    @abstractmethod
    def print_bw(self, document):
        pass

class ColorPrint(ABC):
    @abstractmethod
    def print_to_color(self, document):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class Faxable(ABC):
    @abstractmethod
    def send_fax(self, document: str, number: str):
        pass

# Implementaciones especificas
class BasicPrinter(BWPrint):
    def print_bw(self, document):
        print(f"Imprimiendo a blanco y negro {document}")


class ModernPrinter(BWPrint, ColorPrint):
    def print_bw(self, document):
        print(f"Imprimiendo a blanco y negro {document}")

    def print_to_color(self, document):
        print(f"Imprimiendo a color {document}")

class MultiFunctionalPrinter(BWPrint, ColorPrint, Scannable, Faxable):
    def print_bw(self, document):
        print(f"Imprimiendo a blanco y negro {document}")

    def print_to_color(self, document):
        print(f"Imprimiendo a color {document}")

    def scan(self, document):
        print(f"Escaneando {document}")

    def send_fax(self, document, number):
        print(f"Enviando Fax: {document} al número: {number}")


# Código de prueba
def test_printer(printer):
    if isinstance(printer, BWPrint):
        printer.print_bw("Documento de Prueba B/N")
    if isinstance(printer, ColorPrint):
        printer.print_to_color("Documento de Prueba a color")
    if isinstance(printer, Scannable):
        printer.scan("Documento de Prueba")
    if isinstance(printer, Faxable):
        printer.send_fax("Documento de Prueba", "123456789")


# Caso de uso
if __name__ == "__main__":
    basic_printer = BasicPrinter()
    modern_printer = ModernPrinter()
    multi_printer = MultiFunctionalPrinter()

    print("----- Impresora Básica -----")
    test_printer(basic_printer)

    print("\n----- Impresora Moderna -----")
    test_printer(modern_printer)

    print("\n----- Impresora Multifuncional -----")
    test_printer(multi_printer)