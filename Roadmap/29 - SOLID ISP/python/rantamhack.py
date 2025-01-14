

print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")

"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregacion de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""

# SIN ISP
# from abc import ABC, abstractmethod

# class Car:
#     @abstractmethod
#     def go_to(self):
#         pass
        

#     @abstractmethod
#     def park(self):
#         pass
    
#     @abstractmethod
#     def refueling(self):
#         pass
        
#     @abstractmethod
#     def charging_batery(self):
#         pass
    
    
# class GasCar(Car):
#     def go_to(self):
#         return "going to work"

#     def park(self):
#         return "car parking"
    
#     def refueling(self):
#         return "The car is refueling"
    
#     def charging_batery(self):   # ESTA CLASE NO NECESITA ESTE METODO
#         return "The car is charging the batteries"
    
# class ElectricCar(Car):
#     def go_to(self):
#         return "going to work"

#     def park(self):
#         return "car parking"
    
#     def refueling(self):         # ESTA CLASE NO NECESITA ESTE METODO
#         return "The car is refueling"
    
#     def charging_batery(self):
#         return "The car is charging the batteries"
    
    
    
from abc import ABC, abstractmethod

# CON ISP

class Car(ABC):
    @abstractmethod
    def go_to(self):
        pass
        

    @abstractmethod
    def park(self):
        pass
    
class GasCar:
    @abstractmethod
    def refueling(self):
        pass
        
class ElectricCar:
    @abstractmethod
    def charging_batery(self):
        pass
    
    
class MyGasCar(Car, GasCar):
    def go_to(self):
        return "going to work"

    def park(self):
        return "car parking"
    
    def refueling(self):
        return "The car is refueling"
    
    
class MyElectricCar(Car, ElectricCar):
    def go_to(self):
        return "going to work"

    def park(self):
        return "car parking"
    
    def charging_batery(self):
        return "The car is charging the batteries"

my_car = MyGasCar()

print(my_car.go_to())
print(my_car.park())
print(my_car.refueling())


my_other_car = MyElectricCar()

print(my_other_car.go_to())
print(my_other_car.park())
print(my_other_car.charging_batery())    





print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras solo imprimen en blanco y negro.
 * 2. Otras solo a color.
 * 3. Otras son multifuncion, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementacion.
 * 3. Desarrolla un codigo que compruebe que se cumple el principio.
"""
from abc import ABC, abstractmethod

class PrinterManager(ABC):
    @abstractmethod
    def standby(self):
        pass

    
class BlackAndWhitePrinter(ABC):
    @abstractmethod
    def print_bw(self):
        self
        
        
class ColorPrinter(ABC):
    @abstractmethod
    def color_print(self):
        pass
        
class Scan(ABC):
    @abstractmethod
    def scan(self):
        pass
    
    
class SendFax(ABC):
    @abstractmethod   
    def send_fax(self):
        pass
    
    
class Printer(PrinterManager, BlackAndWhitePrinter):
    def standby(self):
        print("Printer is on standby")
        
    def print_bw(self):
        print("Printer is printing in black and white")  
        

class CPrinter(PrinterManager, ColorPrinter):
    def standby(self):
        print("Printer is on standby")
        
    def color_print(self):
        print("Printer is printing in color")
        
     
class MultifunctionPrinter(PrinterManager, BlackAndWhitePrinter, ColorPrinter, Scan, SendFax):
    def standby(self):
        print("Printer is on standby")
        
    def print_bw(self):
        print("Printer is printing in black and white") 
        
    def color_print(self):
        print("Printer is printing in color") 
        
    def scan(self):
        print("Multifunction printer is scannig a document")
    
    def send_fax(self):
        print("Multifunction printer is faxing")
        
        
printer1 = Printer()
printer2 = CPrinter()
printer3 = MultifunctionPrinter()

print("****************************************************")

printer1.standby()
printer1.print_bw()

print("****************************************************")

printer2.standby()
printer2.color_print()

print("****************************************************")

printer3.standby()
printer3.print_bw()
printer3.color_print()
printer3.scan()
printer3.send_fax()
