# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------------------------
# * SOLID: PRINCIPIO DE SEGREGACIÓN DE INTERFACES (ISP)
# -----------------------------------------------------
# - Una clase no debería estar obligada a implementar interfaces que no utiliza.
#   Evitando crear grandes clases monolíticas.

from abc import ABC, abstractmethod
from decimal import Decimal

# NOTA: Este ejemplo muestra el uso CORRECTO. Para suponer un ejemplo que viole el principio, sería 
#       Imaginar todos los métodos siguientes, en una sola abstracción, entonces algunos dispositivos
#       implementarían abstracciones que no necesitan.

#______________________
# Abstracciones

class AbsPlayable(ABC):
    @abstractmethod
    def play(self):
        pass

class AbsDisplayable(ABC):
    @abstractmethod
    def display(self):
        pass

#______________________
# Implementar abstracciones

class Speaker(AbsPlayable):
    def play(self):
        print("El altavoz está reproduciendo música.")

class Phone(AbsPlayable, AbsDisplayable):
    def play(self):
        print("El teléfono está reproduciendo música.")

    def display(self):
        print("El teléfono está mostrando la pantalla de reproducción.")

#______________________
# Utilización
print("Ejercicio #1")

speaker = Speaker()
speaker.play()

phone = Phone()
phone.play()
phone.display()

"""
 * EJERCICIO:
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

#______________________
# Abstracciones

class AbsPrinter(ABC):    
    @abstractmethod
    def print_file(self, file: str) -> None:
        pass

class AbsScanner(ABC):
    @abstractmethod
    def to_scan(self, path_save: str) -> None:
        pass

class AbcFax(ABC):
    @abstractmethod
    def send_file(self, file: str,  phone_number: int) -> None:
        pass

#______________________
# Implementar abstracciones

class MonoPrinter(AbsPrinter):
    def print_file(self, file: str) -> None:
        print("\nImpresora blanco y negro:")
        print(file, " se imprimió.")

class ColorPrinter(AbsPrinter):
    def print_file(self, file: str) -> None:
        print("\nImpresora a color:")
        print(file, " se imprimió.")

class Scanner(AbsScanner):
    def to_scan(self, path_save: str) -> None:
        print("\nEscaneo realizado, Guardado en:", path_save)

class Fax(AbcFax):
    def send_file(self, file: str,  phone_number: int) -> None:
        print("\n-", file, "Fue enviado a:", phone_number)


class MultiFunctionPrinter:
    def __init__(self):
        self.mono_printer: AbsPrinter = MonoPrinter()
        self.color_printer: AbsPrinter = ColorPrinter()
        self.scanner: AbsScanner = Scanner()
        self.fax: AbcFax = Fax()

#______________________
# Utilización
print("\nEjercicio #2")

#___________
# blanco y negro.
mono_printer = MonoPrinter()
mono_printer.print_file("filex.pdf")

#___________
color_printer = ColorPrinter()
color_printer.print_file("filex.pdf")

#___________
scaner = Scanner()
scaner.to_scan("c:\\docs")

#___________
fax = Fax()
fax.send_file("filex.pdf", 12345678)

#___________
print("\n___________\nMultifunción:")
multifunction = MultiFunctionPrinter()

multifunction.mono_printer.print_file("filex.pdf")
multifunction.color_printer.print_file("filex.pdf")
multifunction.scanner.to_scan("c:\\docs")
multifunction.fax.send_file("filex.pdf", 12345678)

# end
