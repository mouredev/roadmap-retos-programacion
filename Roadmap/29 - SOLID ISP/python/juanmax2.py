"""
Ejercicio
"""

from abc import ABC, abstractmethod

# Sin ISP

class InterfazTrabajador(ABC):
    
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def comer(self):
        pass
    
class Humano(InterfazTrabajador):
    
    def work(self):
        print("Trabajando")
    
    def comer(self):
        print("Comiendo")

class Robot(InterfazTrabajador):
    
    def work(self):
        print("Trabajando")
        
    def comer(self):
        # Los robots no comen
        raise ValueError("Los robots no comen")

# Con ISP

class WorkInterface(ABC):
    
    @abstractmethod
    def work(self):
        pass
    
class EatInterface(ABC):
    
    @abstractmethod
    def comer(self):
        pass
    
class Humano(WorkInterface, EatInterface):
    
    def work(self):
        print("Trabajando")
    
    def comer(self):
        print("Comiendo")

class Robot(WorkInterface):
    
    def work(self):
        print("Trabajando")


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

class BlackAndWhite(ABC):
    
    @abstractmethod
    def imprimir_blanco_negro(self,  document : str):
        pass
    
class Color(ABC):
    
    @abstractmethod
    def imprimir_color(self,  document : str):
        pass

class Scanner(ABC):
    
    @abstractmethod
    def scanear(self,  document : str):
        pass
    
class EnviarFax(ABC):
    
    @abstractmethod
    def enviar_fax(self,  document : str):
        pass

class Printer(BlackAndWhite):
    
    def imprimir_blanco_negro(self, document):
        print(f"Imprimiendo en blanco y negro el documento {document}")

class ColorPrinter(Color):
    
    def imprimir_color(self, document):
        print(f"Imprimiendo en color el documento {document}")

class MultifuncionPrinter(BlackAndWhite, Color, Scanner, EnviarFax):
    
    def imprimir_blanco_negro(self, document):
        print(f"Imprimiendo en blanco y negro el documento {document}")

    def imprimir_color(self, document):
        print(f"Imprimiendo en color el documento {document}")
        
    def scanear(self, document):
        print(f"Scaneando el documento {document}")
    
    def enviar_fax(self, document):
        print(f"Enviando el documento {document} via fax")

# Caso de uso

def test_printers():
    printer_1 = Printer()
    printer_2 = ColorPrinter()
    printer_3 = MultifuncionPrinter()   
    
    printer_1.imprimir_blanco_negro("documento 1")
    print("-------------------------------")
    printer_2.imprimir_color("documento 2")
    print("-------------------------------")
    printer_3.imprimir_blanco_negro("documento 3")
    printer_3.imprimir_color("documento 3")
    printer_3.scanear("documento 3")
    printer_3.enviar_fax("documento 3")
    
test_printers()



