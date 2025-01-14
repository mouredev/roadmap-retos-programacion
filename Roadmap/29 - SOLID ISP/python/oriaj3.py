"""
29 - SOLID ISP - Interface Segregation Principle
Autor de la solución: oriaj3    

El principio de segregación de interfaces (ISP) establece que una clase no debe ser forzada a implementar interfaces que no usará.
En otras palabras, una clase no debe depender de métodos que no necesita. En lugar de tener una interfaz grande que contenga
muchos métodos, es mejor tener varias interfaces más pequeñas que contengan solo los métodos necesarios. 

Un ejemplo sería una interfaz de impresión que contiene métodos para imprimir, escanear y enviar por fax. Si una clase solo necesita
el método de impresión, no debería verse obligada a implementar los métodos de escaneo y fax.

En Python no hay una forma directa de implementar interfaces, pero se pueden usar clases abstractas para lograr un comportamiento similar.
Se usa la librería abc (Abstract Base Classes) para definir clases abstractas.
"""

"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""

# Ejemplo incorrecto
from abc import ABC, abstractmethod

class PrinterInterface(ABC):
    @abstractmethod
    def imprimir(self):
        pass

    @abstractmethod
    def escanear(self):
        pass

    @abstractmethod
    def fax(self):
        pass

class PrinterBW(PrinterInterface):
    def imprimir(self):
        return "Imprimiendo en blanco y negro"
    
    def escanear(self):
        raise Exception("Esta impresora no puede escanear")
    
    def fax(self):
        raise Exception("Esta impresora no puede enviar fax")

class PrinterScanner(PrinterInterface):
    def imprimir(self):
        return "Imprimiendo"
    
    def escanear(self):
        return "Escaneando"
    
    def fax(self):
        raise Exception("No puedo enviar fax")

# Ejemplo correcto

class PrinterInterface(ABC):
    
    @abstractmethod
    def print(self):
        pass
    
class ScannerInterface(ABC):
    
    @abstractmethod
    def scan(self):
        pass

class FaxInterfaceando(ABC):
    
    @abstractmethod
    def fax(self):
        pass
    
#Implemento clases para cada interfaz
class PrinterWithScanner(PrinterInterface, ScannerInterface):
    def print(self):
        print("Imprimiendo1")
        
    def scan(self):
        print("Scan1")
    
class PrinterScannerFax(PrinterInterface, ScannerInterface, FaxInterfaceando):
    def print(self):
        print("Imprimiendo2")
        
    def scan(self):
        print("Scan2")
    
    def fax(self):
        print("Fax2")
        
#Creo objetos de las clases
printer1 = PrinterWithScanner()
printer1.print()
printer1.scan()

printer2 = PrinterScannerFax()
printer2.print()
printer2.scan()
printer2.fax()



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
#Implemento las interfaces
class PrinterInterface(ABC):
    
    @abstractmethod
    def print(self, document):
        pass

class ColorPrinterInterface(ABC):

    @abstractmethod
    def print_color(self, document: str):
        pass
    
class ScanInterface(ABC):
    
    @abstractmethod
    def scan(self, str) -> str:
        pass
    
class FaxInterface(ABC):
    
    @abstractmethod
    def fax(self, document):
        pass
    
#Implemento las clases
class Printer(PrinterInterface):
    def print(self, document: str):
        print(f"Imprimiendo en blanco y negro el documento {document}.")

class Scanner(ScannerInterface):
    def scan(self, document: str)-> str:
        print(f"Escaneando el documento {document}.")
        return f"Documento {document} escaneado."

class ColorPrinter(ColorPrinterInterface):
    def print_color(self, document: str):
        print(f"Imprimiendo en color el documento {document}.")
        
class MultiPrinter(PrinterInterface, ColorPrinterInterface, ScanInterface, FaxInterface):
    def print(self, document: str):
        print(f"Imprimiendo en blanco y negro el documento {document}.")
    
    def print_color(self, document: str):
        print(f"Imprimiendo en color el documento {document}.")
    
    def scan(self, document: str)-> str:
        print(f"Escaneando el documento {document}.")
        return f"Documento {document} escaneado."
    
    def fax(self, document: str):
        print(f"Enviando por fax el documento {document}.")

#Función que crea los distintos objetos y prueba su función
def test_devices():
    printer = Printer()
    scanner = Scanner()
    color_printer = ColorPrinter()
    multiprinter = MultiPrinter()
    
    printer.print("Doc1.pdf")
    color_printer.print_color("DocColor2.pdf")
    scanner.scan("doc_scan.pdf")
    
    multiprinter.print("Doc2.pdf")
    multiprinter.print_color("DocColor2.pdf")
    multiprinter.scan("Doc_Scan2.pdf")
    multiprinter.fax("DocFax.pdf")
    
test_devices()
    