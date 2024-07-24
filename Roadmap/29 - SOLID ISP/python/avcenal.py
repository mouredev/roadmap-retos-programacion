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
    def __init__(self,type):
        self.type = type

    @abstractmethod
    def printer(self,document):
        print(f"Imprimiento en {self.type} el documento:\n{document}")

class Scanner(ABC):
    @abstractmethod
    def scan(self,document):
        print(f"Escaneando el documento: {document}")

class Fax(ABC):
    @abstractmethod
    def send_fax(self,document):
        print(f"Enviando por fax el documento: {document}")
        
class Regular_Printer(Printer):
    def __init__(self):
        self.type = "Blanco y Negro"

    def printer(self,document):
        print(f"Imprimiendo en {self.type} el documento:\n{document}\n")

class Color_Printer(Printer):
    def __init__(self):
        self.type = "Color"

    def printer(self,document):
        print(f"Imprimiendo en {self.type} el documento:\n{document}\n")

class Multifunction_Printer(Printer,Scanner,Fax):
    def __init__(self):
        self.type = "Color"

    def printer(self,document):
        print(f"Imprimiendo en {self.type} el documento:\n{document}\n")

    def scan (self,document):
        print(f"Escaneando documento {document}")

    def send_fax(self,document):
        print(f"Enviando el documento {document} por fax")    

my_regular_printer = Regular_Printer()
my_color_printer = Color_Printer()
my_multifunction_printer = Multifunction_Printer()

my_regular_printer.printer("Me llamo Alex")
my_color_printer.printer("Me llamo Alex")
my_multifunction_printer.printer("Me llamo Alex")
my_multifunction_printer.scan("DNI de Alex")
my_multifunction_printer.send_fax("Nómina de Alex")
