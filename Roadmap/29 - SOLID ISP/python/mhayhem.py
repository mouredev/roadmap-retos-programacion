# @Author Daniel Grande (Mhayhem)

from abc import ABC, abstractmethod

# EJERCICIO:
# Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
# y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.

class Worker:
    def work(self):
        pass
    def eat(self):
        pass
    def sleep(self):
        pass
    def collect_salary(self):
        pass

class Bot(Worker):
    def work(self):
        print("Robot trabajando.")
    def eat(self):
        # los robots no comen
        pass
    def sleep(self):
        # los robots no necesitan dormir
        pass
    def collect_salary(self):
        # no cobra salario
        pass

# ISP

class Worker:
    def work(self):
        pass

class Feedable:
    def eat(self):
        pass

class Restable:
    def sleep(self):
        pass

class Payable:
    def collect_salary(self):
        pass

class Human(Worker, Feedable, Restable, Payable):
    def work(self):
        print("Humano trabajando.")
    def eat(self):
        print("Humano comiendo.")
    def sleep(self):
        print("Humano durmiendo.")
    def collect_salary(self):
        print("Humano cobrando salario.")

class Bot(Worker):
    def work(self):
        print("Robot trabajando.")


    # DIFICULTAD EXTRA (opcional):
    # Crea un gestor de impresoras.
    # Requisitos:
    # 1. Algunas impresoras sólo imprimen en blanco y negro.
    # 2. Otras sólo a color.
    # 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
    # Instrucciones:
    # 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
    # 2. Aplica el ISP a la implementación.
    # 3. Desarrolla un código que compruebe que se cumple el principio.

class Printable(ABC):
    @abstractmethod
    def print_file(self):
        pass

class Fax(ABC):
    @abstractmethod
    def recive_fax(self):
        pass

    @abstractmethod
    def send_fax(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scaning(self):
        pass

class BlackAndWhitePrinter(Printable):
    def print_file(self):
        return "Imprimiendo en blanco y negro."

class ColorPrinter(Printable):
    def print_file(self):
        return "Imprimiendo a color."

class Multifunction(Printable, Fax, Scanner):
    def print_file(self):
        return "Imprimiendo a color o en blanco y negro."
    
    def recive_fax(self):
        return "Reciviendo fax."
    
    def send_fax(self):
        return "Enviando fax."
    
    def scanning(self):
        return "Escaneando documento."

def test_printing(array: list):
    for object in array:
        object.printing_file()
    
    assert Exception

def test_multifunction_printer(printer: object):
    printer.recive_fax()
    printer.send_fax()
    printer.scanning()
    
    assert Exception

