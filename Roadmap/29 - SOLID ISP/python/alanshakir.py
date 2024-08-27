"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
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
 */
"""

from abc import ABC, abstractmethod
    #Incorrecto
class VehicleInterface(ABC):
    @abstractmethod
    def start_engine(self):
        pass
            
    @abstractmethod   
    def stop_engine(self):
        pass
        
    @abstractmethod
    def fly(self):
        pass
            
class Car(VehicleInterface):
        
    def start_engine(self):
        print("Car engine started.")
        
    def stop_engine(self):
        print("Car engine stopped.")
        
    def fly(self):
        #los autos no vuelan
        pass
            
class airplanes(VehicleInterface):
        
    def start_engine(self):
        print("airplanes engine started.")
        
    def stop_engine(self):
        print("airplanes engine stopped.")
        
    def fly(self):
        print("airplanes is flying")
    
    #Correcto
class VehicleInterface(ABC):
    @abstractmethod
    def start_engine(self):
        pass
            
    @abstractmethod   
    def stop_engine(self):
        pass
            
class FlyInterface(VehicleInterface):        
    @abstractmethod
    def fly(self):
        pass
            
class Car(VehicleInterface):
        
    def start_engine(self):
        print("Car engine started.")
        
    def stop_engine(self):
        print("Car engine stopped.")
        
            
class airplanes(FlyInterface, VehicleInterface):
        
    def start_engine(self):
        print("airplanes engine started.")
        
    def stop_engine(self):
        print("airplanes engine stopped.")
        
    def fly(self):
        print("airplanes is flying")

#Extra
class PrinterIsBlackInterface(ABC):
    @abstractmethod
    def printer_black(self, document):
        pass

class PrinterIsColorInterface(ABC):
    @abstractmethod
    def printer_color(self, document):
        pass

class PrinterScanInterface(ABC):
    @abstractmethod
    def printer_scan(self, document):
        pass
        
class PrinterFaxInterface(ABC):
    @abstractmethod
    def send_fax(self, document):
        pass

class Printer(PrinterIsBlackInterface):
    def printer_black(self, document):
        print(f"imprimiendo en blanco y negro {document}")

class PrinterColor(PrinterIsColorInterface):
    def printer_color(self, document):
        print(f"imprimiendo a color {document}")

class PrinterMultiFunction(PrinterIsBlackInterface, PrinterIsColorInterface, PrinterScanInterface, PrinterFaxInterface):
    def printer_black(self, document):
        print(f"imprimiendo en blanco y negro {document}")
    
    def printer_color(self, document):
        print(f"imprimiendo a color {document}")
        
    def printer_scan(self, document):
        print(f"escaneando documento {document}")
    
    def send_fax(self, document):
        print(f"enviando {document} por fax")


printed = Printer()
printed.printer_black("documento.ppt")

printed_color = PrinterColor()
printed_color.printer_color("documento.ppt")

printed_multifunction = PrinterMultiFunction()
printed_multifunction.printer_black("documento.ppt")
printed_multifunction.printer_color("documento.ppt")
printed_multifunction.printer_scan("documento.ppt")
printed_multifunction.send_fax("documento.ppt")
