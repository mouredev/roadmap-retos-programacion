"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""
#INCORRECTO
from abc import ABC, abstractmethod

class Worker():
    def work(self):
        print("Estoy trabajando")
    def eat(self):
        print("Estoy comiendo")

class Human_1(Worker):
    def work(self):
        print("Estoy trabajando")
    
    def eat(self):
        print("Estoy comiendo")

class Robot_1(Worker):
    def work(self):
        print("Estoy trabajando")

my_human_1 = Human_1()
my_robot_1 = Robot_1()

my_human_1.work()
my_human_1.eat()

#my_robot_1.eat() Robot() no tiene definido una función eat() por tanto no debería poder implementarla. Los robots no comen.

my_robot_1.work() 

#CORRECTO
class Work(ABC):
    @abstractmethod
    def work(self):
        print("Estoy trabajando")

class Eat():
    @abstractmethod
    def eat(self):
        print("Estoy comiendo")

class Human(Work,Eat):
    def work(self):
        print("Estoy trabajando")

    def eat(self):
        print("Estoy comiendo")

class Robot(Work):
    def work(self):
        print("Estoy trabajando")

my_human = Human()
my_robot = Robot()

my_human.work()
my_human.eat()

my_robot.work()
#my_robot.eat() Ahora Robot() no tiene definida ninguna función eat() al solo heredar de Work(), ya que los robots no comen.

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
class Printer(ABC):
    @abstractmethod
    def printer(self,document):
        print(f"Imprimiento en Blanco y Negro el documento:\n{document}")

class Color(ABC):
    @abstractmethod
    def print_color(self,document):
        print(f"Imprimiento en Color el documento:\n{document}")

class Scanner(ABC):
    @abstractmethod
    def scan(self,document):
        print(f"Escaneando el documento: {document}")

class Fax(ABC):
    @abstractmethod
    def send_fax(self,document):
        print(f"Enviando por fax el documento: {document}")
        
class RegularPrinter(Printer):
    def printer(self, document):
        return super().printer(document)

class ColorPrinter(Color):
    def print_color(self, document):
        return super().print_color(document)

class MultifunctionPrinter(Printer,ColorPrinter,Scanner,Fax):

    def printer(self,document):
        return super().printer(document)

    def print_color(self, document):
        return super().print_color(document)

    def scan(self, document):
        return super().scan(document)

    def send_fax(self, document):
        return super().send_fax(document)

my_regular_printer = RegularPrinter()
my_color_printer = ColorPrinter()
my_multifunction_printer = MultifunctionPrinter()

my_regular_printer.printer("Me llamo Alex")
my_color_printer.print_color("Me llamo Alex")
my_multifunction_printer.printer("Me llamo Alex")
my_multifunction_printer.print_color("Me llamo Alex")
my_multifunction_printer.scan("DNI de Alex")
my_multifunction_printer.send_fax("Nómina de Alex")
