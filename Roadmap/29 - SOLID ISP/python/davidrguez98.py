""" /*
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
 */ """

from abc import ABC, abstractmethod

#EJERCICIO

""" 
Incorrecto
"""

class WorkerInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Human(WorkerInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")

class Robot(WorkerInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        pass

human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
robot.eat()

""" 
Correcto
"""

class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        pass

class EatInterface(ABC):

    @abstractmethod
    def eat(self):
        pass

class Human(WorkInterface, EatInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")

class Robot(WorkInterface):

    def work(self):
        print("Trabajando")

human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()

#DIFICULTAD EXTRA

class BlackPrinter(ABC):

    @abstractmethod
    def print(self):
        pass

class ColorPrinter(ABC):

    @abstractmethod
    def print_color(self):
        pass

class ScanPrinter(ABC):

    @abstractmethod
    def scan(self):
        pass

class FaxPrinter(ABC):

    @abstractmethod
    def send_fax(self):
        pass

class Printer_one(BlackPrinter):

    def print(self):
        print("Imprimiendo en blanco y negro.")

class Printer_two(BlackPrinter):

    def print(self):
        print("Imprimiendo en blanco y negro.")

class Printer_three(ColorPrinter):

    def print_color(self):
        print("Imprimiendo en color.")

class Printer_four(ColorPrinter):

    def print_color(self):
        print("Imprimiendo en color.")

class Printer_Five(BlackPrinter, ColorPrinter, ScanPrinter, FaxPrinter):

    def print(self):
        print("Imprimiendo en blanco y negro.")

    def print_color(self):
        print("Imprimiendo en color.")

    def scan(self):
        print("Escaneando.")

    def send_fax(self):
        print("Enviando fax.")

class Printer_Six(BlackPrinter, ColorPrinter, ScanPrinter, FaxPrinter):

    def print(self):
        print("Imprimiendo en blanco y negro.")

    def print_color(self):
        print("Imprimiendo en color.")

    def scan(self):
        print("Escaneando.")

    def send_fax(self):
        print("Enviando fax.")

printer1 = Printer_one()
printer1.print()

printer2 = Printer_two()
printer2.print()

printer3 = Printer_three()
printer3.print_color()

printer4 = Printer_four()
printer4.print_color()

printer5 = Printer_Five()
printer5.print()
printer5.print_color()
printer5.scan()
printer5.send_fax()

printer6 = Printer_Six()
printer6.print()
printer6.print_color()
printer6.scan()
printer6.send_fax()