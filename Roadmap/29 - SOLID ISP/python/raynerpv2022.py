# /*
#  * EJERCICIO:
#  * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
#  * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
#  *



# Viola el principio de segregacion ..
from abc import ABC,abstractmethod

class Worker(ABC):
    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Robot(Worker):
    def work(self):
        print("Robot is working...")

    def sleep(self):
         pass
    
    def eat(self):
        pass

class Human (Worker):
    def sleep(self):
        print("Human is sleeping...")
    def work(self):
        print("Human is working...")
    def eat(self):
        print("Human is eating..")

print("Whitout iSP")
R = Robot()
R.work()
H = Human()
H.work()
H.eat()
H.sleep()

#  aplicando principio de segregacion

class WorkInterface(ABC):
    @abstractmethod
    def work(self):
        pass

class EatINterface(ABC):
    @abstractmethod
    def eat(self):
        pass

class SleepInterface(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(WorkInterface,SleepInterface,EatINterface):
     
    def work(self):
        print("HUman is working...")
    
    def sleep(self):
        print("HUman is sleeping")

    def eat(self):
        print("Human is eating")  

class Robot(WorkInterface):
    def work(self):
        print("Robot is workiing...")


print("ISP")
Ro = Robot()
Ro.work()
Hu = Human()
Hu.sleep()
Hu.work()
Hu.eat()


# EXTRA

#  * DIFICULTAD EXTRA (opcional):
#  * Crea un gestor de impresoras.
#  * Requisitos:
#  * 1. Algunas impresoras sólo imprimen en blanco y negro.
#  * 2. Otras sólo a color.
#  * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
#  * Instrucciones:
#  * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
#  * 2. Aplica el ISP a la implementación.
#  * 3. Desarrolla un código que compruebe que se cumple el principio.
#  */


class Scaninterface(ABC):
    @abstractmethod
    def Scan(self):
        pass
    
class FAXinterface(ABC):
    @abstractmethod
    def Fax(self):
        pass

class PrintetInterface(ABC):
    @abstractmethod
    def Print(self):
        pass


class ColorPrintInterface(ABC):
    @abstractmethod
    def Print_color(self):
        pass

class Printer (PrintetInterface):
    def Print(self):
        print("IMpresora solo imprime white and black")
    

class PrinterColor(ColorPrintInterface):
    def Print_color(self):
        print("Impresora a Color...")

class MultiFunction(PrintetInterface,ColorPrintInterface,Scaninterface,FAXinterface):
    def Print(self):
        print("Multifuncion Printing white and Black...")
        
    def Print_color(self):
        print("Multifuncion Printing in color...")
        

    def Scan(self):
        print("Mutifunction Scanning...")

    def Fax(self):
        print("MultiFunction Faxing...")
print("PRINTER")

printer_wb = Printer()
printer_wb.Print()
printer_c = PrinterColor()
printer_c.Print_color()

multi = MultiFunction()
multi.Print()
multi.Print_color()
multi.Scan()
multi.Fax()