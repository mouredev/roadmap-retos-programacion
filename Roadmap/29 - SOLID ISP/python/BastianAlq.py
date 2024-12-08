"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 *

"""

"""
# ------------------------------------------
# | INTERFACE SEGREGATION PRINCIPLE (ISP)  |  Información extraída de -> https://devexpert.io/principios-solid-guia-gratis/ 
# ------------------------------------------

# El principio de segregación de interfaces plantea que ninguna clase debe depender de métodos que no usa.
# por tanto, cuando creemos interfaces que definan comportamientos, hay que estar seguros que todas las clases
# que implementan dichas interfaces puedan agregar comportamientos a todos los metodos, en caso contrario, es mejor
# tener varias interfaces mas pequeñas
#
# ¿COMO DETECTAR QUE ESTAMOS VIOLANDO EL PRINCIPIO DE SEGREGACION DE INTERFACES?
#  - Si al implementar una interfaz ves que uno o varios metodos no tienen sentido y te hace falta dejarlos vacios
#  o lanzar excepciones, es muy probable que estes violando este principio

"""

from abc import ABC, abstractmethod


print("------------ FUNCIONAMIENTO INCORRECTO ISP ------------")

# Interfaz Vehicle que posee el metodo go y fly
class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass

class Airplane(Vehicle):
    def go(self):
        print("el avion esta avanzando por tierra...")
    
    def fly(self):
        print("el avion está volando...")

# el objeto de la clase Car no puede implementar el metodo fly ya que los autos no vuelan, por ende es necesario separar
class Car(Vehicle):
    
    def go(self):
        print("El auto está moviendose...")
    
    def fly(self):
        raise Exception('Los autos no vuelan...')

avion = Airplane()
avion.go()
avion.fly()

auto = Car()
auto.go()
#auto.fly() lanza Exception

"""
La solución es dividir la interfaz vehicle en dos interfaces mas pequeñas que sean especializadas.
la clase Car implementa la interfaz Movable
la clase Airplane implementa las interfaces Movable y Flyable
"""

print("------------ FUNCIONAMIENTO CORRECTO ISP ------------")

class Movable(ABC):
    
    @abstractmethod
    def go(self):
        pass

class Flyable(ABC):
    
    @abstractmethod
    def fly(self):
        pass

class Car(Movable):
    def go(self):
        print("El auto está avanzando...")

class Airplane(Movable,Flyable):
    def go(self):
        print("El avion está avanzando por la pista...")

    def fly(self):
        print("el avion esta volando...")

car = Car()
airplane = Airplane()

car.go()

airplane.go()
airplane.fly()

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

print("------------ FUNCIONAMIENTO CORRECTO ISP DIFICULTAD EXTRA ------------")

class ScannerInterface(ABC):
    @abstractmethod
    def scan(self,document: str):
        pass

class ColorPrintInterface(ABC):
    @abstractmethod
    def print_color(self, document: str):
        pass

class PrintInterface(ABC):
    @abstractmethod
    def print(self, document: str):
        pass

class FaxSenderInterface(ABC):
    @abstractmethod
    def send_fax(self, document: str):
        pass

# IMPRESORAS A COLOR
class ColorPrinter(ColorPrintInterface):
    def print_color(self, document: str):
        print(f"imprimiendo documento {document} a color")

# IMPRESORAS EN BLANCO Y NEGRO
class Printer(PrintInterface):
    def print(self, document: str):
        print(f"imprimiendo documento {document} en blanco y negro")

# IMPRESORAS MULTIFUNCIONALES
class MultifuncionalPrinter(PrintInterface, ColorPrintInterface,FaxSenderInterface,ScannerInterface):
    
    def print(self, document: str):
        print(f"imprimiendo documento {document} en blanco y negro")
    
    def print_color(self, document: str):
        print(f"imprimiendo documento {document} a color")
    
    def send_fax(self, document: str):
        print(f"enviando por fax el documento {document} ")
    
    def scan(self, document: str):
        print(f"escanenado el documento {document}")


def test_printer():
    multifuncional_printer = MultifuncionalPrinter()
    color_printer = ColorPrinter()
    basic_printer = Printer()

    multifuncional_printer.print("documento.pdf")
    multifuncional_printer.print_color("documento.pdf")
    multifuncional_printer.send_fax("documento.pdf")
    multifuncional_printer.scan("documento.pdf")
    
    color_printer.print_color("documento.pdf")
    
    basic_printer.print("documento.pdf")

test_printer()