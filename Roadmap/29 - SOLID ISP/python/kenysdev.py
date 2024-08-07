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
#       imajinar todos los métodos Y propiedades siguientes, en una sola clase.

class Employe(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name
    
    @abstractmethod
    def calculate_payment(self) -> Decimal:
        pass

class FullTime(Employe, ABC):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    @abstractmethod
    def assign_bonus(self) -> Decimal:
        #return Decimal('100.00')
        pass

class Hourly(Employe, ABC):
    def __init__(self, name: str, hours: float) -> None:
        super().__init__(name)
        self._hours = hours

    def set_hours(self, hours: float):
        self._hours += hours

class Intern(Employe, ABC):
    def __init__(self, name: str, total_tickets: int, ticket_price: Decimal):
        super().__init__(name)
        self._total_tickets = total_tickets
        self._ticket_price = ticket_price

# _______________________________________
# ejmp de uso 1
class SellerIntern(Intern):    
    def calculate_payment(self) -> Decimal:
        return self._total_tickets * Decimal(self._ticket_price)

seller_intern = SellerIntern("Zoe", 40, Decimal('5.10'))
print(seller_intern.get_name())
print(seller_intern.calculate_payment())

#________________________________________
# ejmp de uso 2
class SellerFullTime(FullTime):
    def assign_bonus(self) -> Decimal:
        return Decimal('50.00')

    def calculate_payment(self) -> Decimal:
        return Decimal('1500.00') + self.assign_bonus()

seller = SellerFullTime("Ben")
print(seller.get_name())
print(seller.calculate_payment())

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

class Printer(ABC):    
    @abstractmethod
    def print_file(self, file: str) -> None:
        pass

class Scanner:
    def to_scan(self, path_save: str) -> None:
        print("\nEscaneo realizado, Guardado en:", path_save)

class Fax:
    def send_file(self, file: str,  phone_number: int) -> None:
        print("\n-", file, "Fue enviado a:", phone_number)
    
class MonoPrinter(Printer):
    def print_file(self, file: str) -> None:
        print("\nImpresora blanco y negro:")
        print(file, " se imprimió.")

class ColorPrinter(Printer):
    def print_file(self, file: str) -> None:
        print("\nImpresora a color:")
        print(file, " se imprimió.")


class MultiFunctionPrinter:
    def __init__(self):
        self.mono_printer = MonoPrinter()
        self.color_printer = ColorPrinter()
        self.scanner = Scanner()
        self.fax = Fax()

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
