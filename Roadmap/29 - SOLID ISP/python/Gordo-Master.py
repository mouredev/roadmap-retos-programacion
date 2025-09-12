# 29 - Solid ISP (Interface Segregation Principle)

# Trata de que ninguna clase debe ser forzada a depender de métodos que no utiliza
# Habla de que las interfases, o la clase base de la clase a utilizar no debe debe tener metodos que no utiliza.
# Busca que las interfases (o clases base) sean pequeñas, especificas y bien enfocadas.

"""
Incorrecta##################################################################
"""

from abc import ABC, abstractmethod

"""class WorkerInterface(ABC):

    @abstractmethod
    def work():
        pass

    @abstractmethod
    def eat():
        pass
    

class Developer(WorkerInterface):
    
    def work(self):
        print("Escribiendo codigo")

    def eat(self):
        print("Comiendo el almuerzo")

class Robot(WorkerInterface):

    def work(self):
        print("Realizando tareas automaticas")

    def eat(self):
        raise NotImplementedError("Los robots no comen")
    

carlos = Developer()
carlosai = Robot()

carlos.work()
carlos.eat()
carlosai.work()
carlosai.eat()
"""

"""
Correcta##################################################################
"""

class WorkerInterface(ABC):

    @abstractmethod
    def work():
        pass

class CanEat(ABC):

    @abstractmethod
    def eat():
        pass


class Developer(WorkerInterface, CanEat):
    
    def work(self):
        print("Escribiendo codigo")

    def eat(self):
        print("Comiendo el almuerzo")

class Robot(WorkerInterface):

    def work(self):
        print("Realizando tareas automaticas")

carlos = Developer()
carlosai = Robot()

# carlos.work()
# carlos.eat()
# carlosai.work()

"""
Ejercicio extra
"""

class Printer(ABC):

    @abstractmethod
    def print_pages(self):
        pass


class ColorPrinter(ABC):

    @abstractmethod
    def print_color_pages(self):
        pass

class Fax(ABC):
    
    @abstractmethod
    def send_fax(self):
        pass

class Scanner(ABC):

    @abstractmethod
    def scan(self):
        pass

class BlackAndWhitePrinter(Printer):

    def print_pages(self):
        print("Imprimiendo en blanco y negro")

class ColorPrinter(ColorPrinter):

    def print_color_pages(self):
        print("Imprimiendo a color")

class MultifunctionPrinter(Printer, ColorPrinter, Scanner, Fax):

    def print_pages(self):
        print("Imprimiendo en blanco y negro")

    def print_color_pages(self):
        print("Imprimiendo a color")

    def send_fax(self):
        print("Enviando el fax")

    def scan(self):
        print("Escaneando documento")


def test_printer():

    printer_bandw = BlackAndWhitePrinter()
    printer_color = ColorPrinter()
    printer_multi = MultifunctionPrinter()

    printer_bandw.print_pages()
    printer_color.print_color_pages()
    printer_multi.print_pages()
    printer_multi.print_color_pages()
    printer_multi.send_fax()
    printer_multi.scan()

test_printer()