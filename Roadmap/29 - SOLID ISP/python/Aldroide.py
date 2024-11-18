"""
    EJERCICIO:
        Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
        y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""
from abc import ABC, abstractmethod

# Ejemplo incorrecto


class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Worker):
    def work(self):
        print("El trabajador esta realizando su labor")

    def eat(self):
        print("El trabajador esta comiendo")


class RobotWorker(Worker):
    def work(self):
        print("Robot is working")

    def eat(self):
        raise NotImplementedError("Los Robots no comen")


human = HumanWorker()
human.work()
human.eat()

robot = RobotWorker()
robot.work()
try:
    robot.eat()
except NotImplementedError as e:
    print(e)


# uso correcto
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass


class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Worker, Eater):
    def work(self):
        print("El trabajador esta realizando su labor")

    def eat(self):
        print("El trabajador esta comiendo")


class RobotWorker(Worker):
    def work(self):
        print("Robot is working")


human = HumanWorker()
human.work()
human.eat()

robot = RobotWorker()
robot.work()

"""
Dificultad Extra
Crea un gestor de impresoras.
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
    def __init__(self, sheets=0):
        self.sheets = sheets

    # @abstractmethod
    def printing(self, incrementSheet):
        self.sheets += incrementSheet
        print(f"Se ha impreso {incrementSheet} hojas en blanco y negro")


class ColorPrinter(ABC):
    def printing_color(self, incrementSheet):
        print(f"imprimiendo {incrementSheet} hojas a color")


class Scanner(ABC):
    def __init__(self, sheet):
        self.sheet = sheet

    def scanning(self, incrementsheet):
        # self.sheet += incrementsheet
        print(f"Se han escaneado {incrementsheet} hojas")


class Fax(ABC):
    def __init__(self, sheet):
        self.sheet = sheet

    def send_fax(self, incrementsheet):
        # self.sheet += incrementsheet
        print(f"Se ha mandado {incrementsheet} en fax")

# Clases de Impresoras


class BlackAndWhite(Printer):
    def printing(self, increment):
        print("Imprimiendo en blanco y negro")
        super().printing(increment)


class ColorOnlyPrinter(ColorPrinter):
    def printing_color(self, increment):
        print("La impresora a color esta imprimiendo")
        super().printing(increment)


class MultifuncionPrinter(Printer, ColorPrinter, Scanner, Fax):

    def printing(self, a):
        print("Imprimiendo en blanco y negro.")
        super().printing(a)

    def printing_color(self, b):
        print("Imprimiendo a color")
        super().printing_color(b)

    def scan(self, c):
        print("Ecaneando un documento")
        super().scanning(c)

    def send_fax(self, d):
        print("Enviando fax.")
        super().send_fax(d)


def test_printer():
    bw_printer = BlackAndWhite()
    color_printer = ColorPrinter()
    Multifuncion_Printer = MultifuncionPrinter()

    print("Testing Black and White Printer:")
    bw_printer.printing(2)

    print("\nTesting Color Printer:")
    color_printer.printing_color(3)

    print("\nTesting Multifunction Printer:")
    Multifuncion_Printer.printing(3)
    Multifuncion_Printer.printing_color(2)
    Multifuncion_Printer.scan(4)
    Multifuncion_Printer.send_fax(5)


test_printer()
