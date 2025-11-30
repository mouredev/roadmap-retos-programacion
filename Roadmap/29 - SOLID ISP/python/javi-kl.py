from abc import ABC, abstractmethod

# Incorrecta
"""class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def dormir(self):
        pass

    @abstractmethod
    def comer(self):
        pass


class Humano(Trabajador):
    def trabajar(self):
        print("Trabajando...")

    def dormir(self):
        print("Durmiendo..")

    def comer(self):
        print("Comiendo")

# Aqui estamos violando el ISP, porque no debemos obligar a esta clase a usar metodos que no son acorde
class Robot(Trabajador):
    def trabajar(self):
        print("Trabajando...")

    def dormir(self):
        print("Durmiendo..")

    def comer(self):
        print("Comiendo")


trabajador1 = Humano()
trabajador1.comer()
trabajador1.dormir()
trabajador1.comer()"""

# correcto


class TrabajadorHumano(ABC):
    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def dormir(self):
        pass

    @abstractmethod
    def comer(self):
        pass


class TrabajadorMecanico(ABC):
    @abstractmethod
    def trabajar(self):
        pass

    @abstractmethod
    def cargarse(self):
        pass


class Peon(TrabajadorHumano):
    def trabajar(self):
        print("Humano Trabajando...")

    def dormir(self):
        print("Humano Durmiendo..")

    def comer(self):
        print("Humano Comiendo")


class Robot(TrabajadorMecanico):
    def trabajar(self):
        print("Robot Trabajando...")

    def cargarse(self):
        print("Robot Cargandose...")


trabajador_humano1 = Peon()
trabajador_mecanico1 = Robot()

trabajador_humano1.comer()
trabajador_humano1.dormir()
trabajador_humano1.trabajar()

trabajador_mecanico1.trabajar()
trabajador_mecanico1.cargarse()


"""
extra
"""


# Interfaces pequeñas que abarquen todas las posibles funciones y que podemos expandir
class Imprimible(ABC):
    """Interfaz para capacidad de imprimir en blanco y negro"""

    @abstractmethod
    def imprimir(self):
        pass


class ImprimibleColor(ABC):
    """Interfaz para capacidad de imprimir a color"""

    @abstractmethod
    def imprimir_color(self):
        pass


class Escaneable(ABC):
    """Interfaz para capacidad de escanear documentos"""

    @abstractmethod
    def escanear(self):
        pass


class EnviadorFax(ABC):
    """Interfaz para capacidad de enviar fax"""

    @abstractmethod
    def enviar_fax(self):
        pass


# Tipos posibles de impresoras, heredan de la interfaz segun el tipo de impresion
class Impresora(Imprimible):
    def imprimir(self):
        print("Imprimiendo en blanco y negro")


# Esta impresora puede utilizar los dos tipos de impresion
class ImpresoraColor(Imprimible, ImprimibleColor):
    def imprimir(self):
        print("Imprimiendo en blanco y negro")

    def imprimir_color(self):
        print("Imprimiendo en color")


# Estas herendan de la interfaz segun el tipo de impresion y de metodos
class ImpresoraMulti(Imprimible, Escaneable, EnviadorFax):
    def imprimir(self):
        print("Imprimiendo en blanco y negro")

    def escanear(self):
        print("Escaneando documento")

    def enviar_fax(self):
        print("Enviando fax")


class ImpresoraColorMulti(Imprimible, ImprimibleColor, Escaneable, EnviadorFax):
    def imprimir(self):
        print("Imprimiendo en blanco y negro")

    def imprimir_color(self):
        print("Imprimiendo en color")

    def escanear(self):
        print("Escaneando documento")

    def enviar_fax(self):
        print("Enviando fax")


impresora1 = Impresora()
impresora_color1 = ImpresoraColor()
impresora_multi1 = ImpresoraMulti()
impresora_color_multi1 = ImpresoraColorMulti()


impresora1.imprimir()

impresora_color1.imprimir_color()

impresora_multi1.imprimir()
impresora_multi1.escanear()
impresora_multi1.enviar_fax()

impresora_color_multi1.imprimir_color()
impresora_color_multi1.escanear()
impresora_color_multi1.enviar_fax()
