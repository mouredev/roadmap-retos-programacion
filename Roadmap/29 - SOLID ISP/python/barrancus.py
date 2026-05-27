#29 - Python
# EJERCICIO:
# Explora el "Principio SOLID de Segregación de Interfaces
# (Interface Segregation Principle, ISP)", y crea un ejemplo
# simple donde se muestre su funcionamiento de forma correcta e incorrecta.
# 
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
# 

class Counter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

contador = iter(Counter())

def separacion(cadena) -> str:
    global contador
    print(f'\nEjercicio {next(contador)}. {cadena} {'-.-' * 20}')

from abc import ABC, abstractmethod

#-----Incorrecto-----
separacion('Incorrecto fundamento')

class ArmyA(ABC):
    
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def deffense(self):
        pass

    @abstractmethod
    def construct(self):
        pass

    @abstractmethod
    def dissaster(self):
        pass

class SpecialForce(ArmyA):

    def attack(self):
        print('Misión encubierta.')

    def deffense(self):
        pass

    def construct(self):
        pass

    def dissaster(self):
        pass    
class Marine(ArmyA):

    def attack(self):
        print('Desembarco en la playa.')
    
    def deffense(self):
        print('Vigilancia de cuarteles.')
    
    def construct(self):
        pass

    def dissaster(self):
        pass    
class Engineers(ArmyA):

    def attack(self):
        pass
    
    def deffense(self):
        pass
    
    def dissaster(self):
        pass    

    def construct(self):
        print('Recostruyendo puentes.')
    
class Emrgency(ArmyA):

    def attack(self):
        pass
    
    def deffense(self):
        pass
    
    def construct(self):
        print('Limpiando escombros.')
    
    def dissaster(self):
        print('Ayudando a la gente.')

specialforce = SpecialForce()
marine = Marine()
engineers = Engineers()
emrgency = Emrgency()

specialforce.attack()
specialforce.deffense()
marine.dissaster()
marine.construct()
emrgency.attack()

#-----Correcto-----
separacion('Correcto fundamento')

class ArmyB:

    def __init__(self, name: str):
        self.name = name

class InterfaceAta(ABC):
    
    @abstractmethod
    def attack(self):
        pass

class InterfaceDef(ABC):
    
    @abstractmethod
    def deffense(self):
        pass

class InterfaceCon(ABC):
    
    @abstractmethod
    def construct(self):
        pass

class InterfaceDis(ABC):
    
    @abstractmethod
    def dissaster(self):
        pass

class SpecialForce(ArmyB, InterfaceAta):

    def attack(self):
        return f'{self.name} en misión especial.'

class Marine(ArmyB, InterfaceAta, InterfaceDef):

    def attack(self):
        return f'{self.name} desembarcanado en la playa.'

    def deffense(self):
        return f'{self.name} vigilando el horizonte.'

class Engineers(ArmyB, InterfaceCon):

    def construct(self):
        return f'{self.name} reconstruyendo puentes.'

class Emrgency(ArmyB, InterfaceCon, InterfaceDis):

    def construct(self):
        return f'{self.name} desescombrando caminos.'

    def dissaster(self):
        return f'{self.name} ayudando al personal civil.'

specialforce = SpecialForce("Boina Verde")
marine = Marine("Marines")
engineers = Engineers("Ingenieros")
emrgency = Emrgency("UME")

print(specialforce.attack())
print(marine.attack())
print(marine.deffense())
print(engineers.construct())
print(emrgency.construct())
print(emrgency.dissaster())

#-----EXTRA-----
separacion('EXTRA')

class InterfacePrintBW(ABC):
    
    @abstractmethod
    def print_bw(self, document: str):
        return f'Se está imprimiendo el documento "{document}" en blanco y negro.'

class InterfacePrintColor(ABC):
    
    @abstractmethod
    def print_color(self, document: str):
        return f'Se está imprimiendo el documento "{document}" en color.'

class InterfaceScan(ABC):
    
    @abstractmethod
    def scan(self, document: str):
        return f'Se está escaneando el documento y se guardará en el archivo "{document}".'

class InterfaceSendFax(ABC):
    
    @abstractmethod
    def send_fax(self, document: str):
        return f'Se está enviando por fax el archivo "{document}".'

class Printer:

    def __init__(self, name: str):
        self.name = name

class BWPrinter(Printer, InterfacePrintBW):

    def print_bw(self, document):
        print(f'Impresora {self.name}:')
        print(super().print_bw(document))
        print(f'Se terminó de imprimir el documento "{document}"')

class ColorPrinter(Printer, InterfacePrintColor):

    def print_color(self, document):
        print(f'Impresora {self.name}:')
        print(super().print_color(document))
        print(f'Se terminó de imprimir el documento "{document}"')

class MultiFunctionPrinter(Printer, InterfacePrintBW, InterfacePrintColor, InterfaceScan, InterfaceSendFax):

    def print_bw(self, document):
        print(f'Impresora {self.name}:')
        print(super().print_bw(document))
        print(f'Se terminó de imprimir el documento "{document}"')

    def print_color(self, document):
        print(f'Impresora {self.name}:')
        print(super().print_color(document))
        print(f'Se terminó de imprimir el documento "{document}"')

    def send_fax(self, document):
        print(f'Impresora {self.name}:')
        print(super().send_fax(document))
        print(f'Se terminó de enviar por fax el documento "{document}"')

    def scan(self, document):
        print(f'Impresora {self.name}:')
        print(super().scan(document))
        print(f'Se terminó de escanear "{document}" guardado en el PC.')

bw_matricial = BWPrinter("Matricial")
multi_equipment = MultiFunctionPrinter("RR4589")
color_printer = ColorPrinter("NZ5200")

def test_printer(printer):
    try:
        printer.print_bw("elcamino.pdf")
    except AttributeError:
        pass
    
    try:
        printer.print_color("SupermanN342.pdf")
    except AttributeError:
        pass
    
    try:
        printer.scan("justificante.pdf")
    except AttributeError:
        pass
    
    try:
        printer.send_fax("justificante.pdf")
    except AttributeError:
        pass

test_printer(bw_matricial)
test_printer(color_printer)
test_printer(multi_equipment)
