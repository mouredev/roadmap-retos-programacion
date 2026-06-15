'''
Ejercicio:
Explora el "Principio SOLID de Segregacion de Interfaces (Interface Segregation Principle, ISP), y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
'''

#! Forma incorrecta
class Trabajador:
    def trabajar(self):
        pass

    def comer(self):
        pass

    def dormir(self):
        pass


class Robot(Trabajador):
    def trabajar(self):
        print("El robot trabaja")

    def comer(self):
        pass # El robot no come

    def dormir(self):
        pass # El robot no duerme


#! Forma correcta
class ITrbajar:
    def trabajar(self): pass

class IComer:
    def comer(self): pass

class IDormir:
    def dormir(self): pass

class Humano(ITrbajar, IComer, IDormir):
    def trabajar(self):
        print("El humano trabaja")

    def comer(self):
        print("El humano come.")

    def dormir(self):
        print("El humano duerme.")

class Robot2(ITrbajar):
    def trabajar(self):
        print("El robot trabaja.")


'''
Dificultad extra:
Crea un gestor de impresoras.

Requisitos:
    1. Algunas impresoras solo imprimen blanco y negro.
    2. Otras solo a color.
    3. Otras son multifuncion, pueden imprimir, escanear y enviar fax.

Instrucciones:
    1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
    2. Aplica el ISP a la implementacion.
    3. Desarrolla un codigo que compruebe que se cumple con el principio.
'''

from abc import ABC, abstractmethod

class IImprimirBN(ABC):
    @abstractmethod
    def imprimir_bn(self):
        pass

class IImprimirColor(ABC):
    @abstractmethod
    def imprimir_color(self):
        pass

class IEscanear(ABC):
    @abstractmethod
    def escanear(self):
        pass

class IFax(ABC):
    @abstractmethod
    def enviar(self):
        pass


class ImpresoraBN(IImprimirBN):
    def imprimir_bn(self):
        print("Imprimiendo en blanco y negro")
        
class ImpresoraColor(IImprimirColor):
    def imprimir_color(self):
            print("Imprimiendo a color.")
    
class ImpresoraMultifuncion(IEscanear,IFax,IImprimirColor,IImprimirBN):
    def enviar(self):
            print("Enviando su fax")
    
    def escanear(self):
       print("Escaneando su documento.")
    
    def imprimir_color(self):
        print("Imprimiendo a color.")

    def imprimir_bn(self):
        print("Imprimiendo en blanco y negro.")

def usar_impresora_bn(impresora: IImprimirBN):
    impresora.imprimir_bn()

def usar_impresora_color(impresora: IImprimirColor):
    impresora.imprimir_color()

bn = ImpresoraBN()
color = ImpresoraColor()
multi = ImpresoraMultifuncion()


usar_impresora_bn(bn)
usar_impresora_bn(multi)

usar_impresora_color(color)
usar_impresora_color(multi)