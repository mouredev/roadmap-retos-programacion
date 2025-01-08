

from abc import ABC, abstractmethod

"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""
from abc import ABC, abstractmethod


# FORMA INCORRECTA

class HumanResourcesManagement(ABC):

    @abstractmethod
    def make_annual_budget(self):
        pass
    
    @abstractmethod
    def project_managment(self):
        pass

    @abstractmethod
    def work_on_a_project(self):
        pass


class Executive(HumanResourcesManagement):

    def make_annual_budget(self):
        print("Ha comenzado la elaboración del presupuesto anual")

    def project_management(self):
        print("Ha comenzado a gestionar en un nuevo proyecto")
    
    def work_on_a_project(self):
        # Los directivos no trabajan en proyectos
        pass

class Worker(HumanResourcesManagement):

    def make_annual_budget(self):
        # Los trabajadores no participan en la elaboración de prespuestos
        pass

    def project_management(self):
        # Los trabajadores no gestionan los proyectos
        pass

    def work_on_a_project(self):
        print("Ha comenzado a trabajar en un nuevo proyecto")


# FORMA CORRECTA

class ManagementInterface(ABC):
    @abstractmethod
    def make_annual_budget(self):
        pass
    
    @abstractmethod
    def project_management(self):
        pass

class WokerInterface(ABC):
    @abstractmethod
    def work_on_a_project(self):
        pass

class Executive(ManagementInterface):

    def make_annual_budget(self):
        print("Ha comenzado la elaboración del presupuesto anual")

    def project_management(self):
        print("Ha comenzado a gestionar en un nuevo proyecto")
    

class Worker(WokerInterface):

    def work_on_a_project(self):
        print("Ha comenzado a trabajar en un nuevo proyecto")

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


"""


class BWPrinterInterface(ABC):
    @abstractmethod
    def bw_print(self, document_name):
        pass

class ColorPrinterInterface(ABC):
    @abstractmethod
    def color_print(self, document_name):
        pass
class ScanInterface(ABC):
    @abstractmethod
    def scan(self, document_name):
        pass

class FaxInterface(ABC):
    @abstractmethod
    def send_fax(self, document_name):
        pass



class BWPrinter(BWPrinterInterface):
    def bw_print(self, document_name):
        print(f"Está imprimiendo el documento {document_name} en blanco y negro")

class ColorPrinter(ColorPrinterInterface):
    def color_print(self, document_name):
        print(f"Está imprimiendo el documento {document_name} en color")

class MultifunctionPrinter(ScanInterface, FaxInterface,  BWPrinterInterface, ColorPrinterInterface):
    
    def bw_print(self, document_name):
        print(f"Está imprimiendo el documento {document_name} en blanco y negro")
    def color_print(self, document_name):
        print(f"Está imprimiendo el documento {document_name} en color")
    def scan(self, document_name):
        print(f"Está escaneando el documento {document_name}")
    def send_fax(self, document_name):
        print(f"Está enviando  el documento {document_name} mediante fax")



my_multifuction = MultifunctionPrinter()

my_multifuction.scan("my_document.word")
my_multifuction.send_fax("my_document.word")
my_multifuction.bw_print("my_document.word")
my_multifuction.color_print("my_document.word")

my_bwprinter = BWPrinter()
my_bwprinter.bw_print("my_document.word")

my_color_printer = ColorPrinter()
my_color_printer.color_print("my_document.word")