### Principio de Segregación de Interfaces (Interface Segregation Principle, ISP)

'''
Este principio establece que:

"Ningún cliente debería depender de métodos que no utiliza."

Esto significa que las interfaces (o clases abstractas en Python) deben diseñarse de manera que los clientes que 
las implementan no se vean forzados a definir métodos innecesarios o irrelevantes.

Ventajas:

+ Reduce el acoplamiento
+ Hace el código más modular
+ Facilitan la implementación
'''

# Ejemplo que viola el principio

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def drive(self):
        pass
    
    @abstractmethod
    def pilot(self):
        pass
    
    @abstractmethod
    def navigate(self):
        pass
    
class Car(Vehicle):
    
    def drive():
        print("El coche está en marcha")
    
    def pilot(self):
        raise NotImplementedError("Un coche no puede volar")
    
    def navigate(self):
        raise NotImplementedError("Un coche no puede navegar por el mar")

'''
En este ejemplo los principales problemas son:
- El cliente (Car) debe implementar métodos que no utiliza (pilot y navigate)
- El cliente debe manejar excepciones innecesarias
'''

# Fin Ejemplo que viola el principio

# Rediseño para no violar el ISP

class Driveable(ABC):
    
    @abstractmethod
    def drive(self):
        pass

class Pilotable(ABC):
    
    @abstractmethod
    def pilot(self):
        pass

class Navigateable(ABC):
    
    @abstractmethod
    def navigate(self):
        pass


class Car(Driveable):
    
    def drive(self):
        print("El cocche está en marcha")

class Plane(Pilotable):
    
    def pilot(self):
        print("El avión está volando")

class Ship(Navigateable):
    
    def navigate(self):
        print("El barco se encuentra navegando en alta mar")
    

# Fin Rediseño para no violar el ISP

## EJERCICIO EXTRA

class PrinterBW(ABC):
    
    @abstractmethod
    def print_bn(self):
        pass

class PrinterColor(ABC):
    
    @abstractmethod
    def print_color(self):
        pass

class Maileable(ABC):
    
    @abstractmethod
    def send_mail(self):
        pass

class Faxeable(ABC):
    
    @abstractmethod
    def send_fax(self):
        pass

class BwPrinter(PrinterBW):
    
    def print_bn(self):
        print("Imprimiendo documento en Blanco/Negro")

class ColorPrinter(PrinterColor):
    
    def print_color(self):
        print("Imprimiendo documento en Color")

class MultiFunction(PrinterBW, PrinterColor, Maileable, Faxeable):
    
    def print_bn(self):
        print("Imprimiendo documento en Blanco/Negro")
    
    def print_color(self):
        print("Imprimiendo documento en Color")
    
    def send_mail(self, to="correo@correo.es", subject="Test", body="This is a mail test"):
        print(f"Enviando correo electrónico a {to} con asunto {subject} y mensaje {body}")
    
    def send_fax(self, destination_number="+345557890", content="This is a fax test"):
        print(f"Enviando fax a {destination_number} con contenido {content}")
        

# Batería de pruebas

def test_bw_printer():
    printer = BwPrinter()
    printer.print_bn()  # Debería imprimir en blanco y negro

def test_color_printer():
    printer = ColorPrinter()
    printer.print_color()  # Debería imprimir en color

def test_multi_function_print_bn():
    printer = MultiFunction()
    printer.print_bn()  # Debería imprimir en blanco y negro

def test_multi_function_print_color():
    printer = MultiFunction()
    printer.print_color()  # Debería imprimir en color

def test_multi_function_send_mail():
    printer = MultiFunction()
    printer.send_mail(to="example@mail.com", subject="Prueba", body="Esto es una prueba")

def test_multi_function_send_fax():
    printer = MultiFunction()
    printer.send_fax(destination_number="+123456789", content="Esto es una prueba de fax")

def test_no_extra_methods_bw_printer():
    printer = BwPrinter()
    try:
        printer.print_color()
    except AttributeError:
        print("Error esperado: 'BwPrinter' no tiene método 'print_color'")

def test_no_extra_methods_color_printer():
    printer = ColorPrinter()
    try:
        printer.print_bn()
    except AttributeError:
        print("Error esperado: 'ColorPrinter' no tiene método 'print_bn'")
        

print("Pruebas de BwPrinter:")
test_bw_printer()
test_no_extra_methods_bw_printer()

print("\nPruebas de ColorPrinter:")
test_color_printer()
test_no_extra_methods_color_printer()

print("\nPruebas de MultiFunction:")
test_multi_function_print_bn()
test_multi_function_print_color()
test_multi_function_send_mail()
test_multi_function_send_fax()


## FIN EJERCICIO EXTRA





### FIN Principio de Segregación de Interfaces (Interface Segregation Principle, ISP)