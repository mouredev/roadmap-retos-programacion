"""
* EJERCICIO:
* Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
* y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
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
"""

# Forma Incorrecta sin aplicar el principio ISP

from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod
    def open (self):
        pass
    @abstractmethod
    def save (self):
        pass
    @abstractmethod
    def print (self):
        pass
    @abstractmethod
    def convert_to (self, format):
        pass

class PDFDocument(Document):

    def open(self):
        print("Opening PDF document")

    def save(self):
        print("Saving PDF document")

    def print(self):
        print("Printing PDF document")

    def convert_to(self, format):
        print(f"Converting PDF document to: {format}")

class WordDocument(Document):

    def open(self):
        print("Opening Word document")

    def save(self):
        print("Saving Word document")

    def print(self):
        print("Printing Word document")

    def convert_to(self, format):
        print(f"Converting Word document to: {format}")

class SpreadsheetDocument(Document):

    def open(self):
        print("Opening Spreadsheet document")

    def save(self):
        print("Saving Spreadsheet document")

    def print(self):
        # Hojas de calculo no necesitan imprimir
        pass

    def convert_to(self, format):
        # Hojas de calculo no necesitan convertir
        pass

pdf = PDFDocument()
pdf.open()
pdf.print()
pdf.convert_to('Word')

spreadsheet = SpreadsheetDocument()
spreadsheet.open()
spreadsheet.print() # No hace nada

# Forma Correcta de aplicar el principio ISP

class Document(ABC):
    
    @abstractmethod
    def open (self):
        pass
    @abstractmethod
    def save (self):
        pass    

class PrintDocument(Document):
    @abstractmethod
    def print(self):
        pass

class ConvertTo(Document):
    @abstractmethod
    def convert_to(self, format):
        pass

class PDFDocument(PrintDocument, ConvertTo):

    def open(self):
        print("Opening PDF document")

    def save(self):
        print("Saving PDF document")

    def print(self):
        print("Printing PDF document")

    def convert_to(self, format):
        print(f"Converting PDF document to: {format}")

class WordDocument(PrintDocument, ConvertTo):

    def open(self):
        print("Opening Word document")

    def save(self):
        print("Saving Word document")

    def print(self):
        print("Printing Word document")

    def convert_to(self, format):
        print(f"Converting Word document to: {format}")

class SpreadsheetDocument(Document):

    def open(self):
        print("Opening Spreadsheet document")

    def save(self):
        print("Saving Spreadsheet document")


pdf = PDFDocument()
pdf.open()
pdf.print()
pdf.convert_to('Word')

spreadsheet = SpreadsheetDocument()
spreadsheet.open()
spreadsheet.save()


############### --------------------------------- EXTRA --------------------------------------- ###################

class Printer(ABC):
    
    @abstractmethod
    def black_white_print(self):
        pass

class ColorPrinter(ABC):
    @abstractmethod
    def color_print(self):
        pass

class ScanerPrinter(ABC):
    @abstractmethod
    def scan(self):
        pass

class FaxPrinter(ABC):
    @abstractmethod
    def send_fax(self, dest):
        pass

class CannonPrinter(Printer, ColorPrinter, ScanerPrinter, FaxPrinter):

    def black_white_print(self):
        print("Impresion en blanco y negro")

    def color_print(self):
        print("Impresion a colores")

    def scan(self):
        print("Escaneo disponible")

    def send_fax(self, dest):
        print(f"Enviar documento a {dest}")

class EpsonPrinter(Printer, ColorPrinter, ScanerPrinter):

    def black_white_print(self):
        print("Impresion en blanco y negro")

    def color_print(self):
        print("Impresion a colores")

    def scan(self):
        print("Escaneo disponible")

class LGPrinter (Printer, FaxPrinter):

    def black_white_print(self):
        print("Impresion en blanco y negro")

    def send_fax(self, dest):
        print(f"Enviar documento a {dest}")

class ColorOnlyPrinter(ColorPrinter):

    def color_print(self):
        print("Impresión a colores")


cannon = CannonPrinter()
cannon.black_white_print()
cannon.scan()
cannon.send_fax("carlos@example.com")

epson = EpsonPrinter()
epson.color_print()
epson.scan()

lg = LGPrinter()
lg.send_fax("juan4562")

color_only = ColorOnlyPrinter()
color_only.color_print()