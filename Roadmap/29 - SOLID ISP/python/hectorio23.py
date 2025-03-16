# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23 
from abc import ABC, abstractmethod

# Define una interfaz abstracta para la funcionalidad de impresión
class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

# Define una interfaz abstracta para la funcionalidad de escaneo
class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

# Define una interfaz abstracta para la funcionalidad de fax
class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass

# Implementa una impresora en blanco y negro que solo necesita la interfaz de impresión
class BlackAndWhitePrinter(Printer):
    def print(self):
        return "[+] - Imprimiendo en blanco y negro"

# Implementa una impresora a color que solo necesita la interfaz de impresión
class ColorPrinter(Printer):
    def print(self):
        return "[+] - Imprimiendo en color"

# Implementa una impresora multifunción que necesita todas las interfaces: impresión, escaneo y fax
class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self):
        return "[+] - Imprimiendo en multifunción"

    def scan(self):
        return "[+] - Escaneando en multifunción"

    def fax(self):
        return "[+] - Enviando fax en multifunción"

# Función que prueba la funcionalidad de impresión de una impresora
def test_printer(printer: Printer):
    print(printer.print())

# Función que prueba la funcionalidad de escaneo de un escáner
def test_scanner(scanner: Scanner):
    print(scanner.scan())

# Función que prueba la funcionalidad de fax de un dispositivo de fax
def test_fax(fax: Fax):
    print(fax.fax())

# Crear instancias de las impresoras
b_and_w_printer = BlackAndWhitePrinter()
color_printer = ColorPrinter()
multi_printer = MultiFunctionPrinter()

# Probar las impresoras
test_printer(b_and_w_printer)
test_printer(color_printer)
test_printer(multi_printer)
test_scanner(multi_printer)
test_fax(multi_printer)

