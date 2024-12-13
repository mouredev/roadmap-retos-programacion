import os, platform
from abc import ABC, abstractmethod


if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" 
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta."""

"""El siguiente código no cumple el principio de segregación de interfaces ya que sólo hay una "interface"
que modela el contenido..
(en python no existen las interfaces como tal, lo más parecido es crear una clase abstracta con el módulo abc y declarar
todos los métodos como abstractos y sin funcionalidad propia para que a efectos prácticos se comporte como una interface)
..de las diferentes clases de aves con todas las características de las cuales solo la primera (tiene plumas)
es común a todas las aves pero no las demás que aun así es obligatorio declarar sus métodos en todas las clases
además el método que debemos llamar para confirmar la característica del ave está seteada en true con lo cual en 
los métodos cuya característica no cumpla dicho ave debemos forzar la salida retornando false."""


class Bird (ABC):
    
    @abstractmethod
    def have_feathers():
        pass
    @abstractmethod
    def flies():
        pass
    @abstractmethod
    def swims():
        pass
    @abstractmethod
    def run():
        pass
    @abstractmethod
    def feature():
        return True
    @abstractmethod
    def bird_name():
        pass
    
class Ostrich(Bird):
    def have_feathers():
        return super().feature()
    def flies():
        return False
    def swims():
        return False
    def run():
        return super().feature()
    def bird_name(self):
        return "Avestruz"
 
class Swift (Bird):
    def have_feathers():
        return super().feature()
    def flies():
        return super().feature()
    def swims():
        return False
    def run():
        return False
    def bird_name(self):
        return "Vencejo"

class Penguin (Bird):
    def have_feathers():
        return super().feature()
    def flies():
        return False
    def swims():
        return super().feature()
    def run():
        return False
    def bird_name(self):
        return "Pingüino"
    
"""En el siguiente código aplicamos el principio de segregación de interfaces dividiendo en diferentes interfaces
los métodos que devuelven la característica verdadera, en el primero declaramos el método "tiene plumas" común
a todas las aves y el método que devuelve el nombre del ave así como la constante general de característica
seteado en true, después creamos una interface por cada característica para declarar dentro su método de característica 
que no es común a todas las aves, volar, correr y nadar, luego creamos las clases que modelen cada especie de ave heredando
en cada una de ellas las interfaces que se correspondan con sus características particulares
(Python permite la herencia múltiple de clases abstractas y no abstractas),
despues dentro creamos un método que reciba un objeto, seteamos todas las características en false
y mediante condicionales aplicamos para cada tipo de objeto/ave sus correspondientes características que sean verdaderas,
creamos una salida que muestre todas las características y en cada ave mostrará true si esa característica está en el
modelado de su objeto o false, que es el valor por defecto que declaramos si no cumple dicha característica."""
   

class BirdISP(ABC):
    @abstractmethod
    def have_feathersISP(self):
        pass
    @abstractmethod
    def bird_name(self):
        pass
    def feature_ISP(self):
        return True
class FlyingBirdISP(ABC):
    @abstractmethod
    def flies_ISP(self):
        pass
class SwimmingBirdISP(ABC):
    @abstractmethod
    def swims_ISP(self):
        pass
class RunnerBirdISP(ABC):
    @abstractmethod
    def run_ISP(self):
        pass

class OstrichISP (BirdISP, RunnerBirdISP):
    def have_feathersISP(self):
        return super().feature_ISP()
    def run_ISP(self):
        return super().feature_ISP()
    def bird_name(self):
        return "Avestruz"
class SwiftISP(BirdISP, FlyingBirdISP):
    def have_feathersISP(self):
        return super().feature_ISP()
    def flies_ISP(self):
        return super().feature_ISP()
    def bird_name(self):
        return "Vencejo"
class PenguinISP(BirdISP, SwimmingBirdISP, RunnerBirdISP):
    def have_feathersISP(self):
        return super().feature_ISP()
    def swims_ISP(self):
        return super().feature_ISP()
    def run_ISP(self):
        return super().feature_ISP
    def bird_name(self):
        return "Pingüino"
    
def test_birds(object):
    name = None
    feathers = False
    fly = False
    swim = False
    run = False
    if isinstance(object,OstrichISP):
        name = object.bird_name()
        feathers = object.have_feathersISP()
        run = object.run_ISP()
    elif isinstance(object, SwiftISP):
        feathers = object.have_feathersISP()
        name = object.bird_name()
        fly = object.flies_ISP()
    elif isinstance(object, PenguinISP):
        feathers = object.have_feathersISP()
        name = object.bird_name()
        swim = object.swims_ISP()
    print("\nEspecie de ave: " , name
                , "\n¿tiene plumas?: " , feathers
                , "\n¿Puede volar?: " , fly
                , "\n¿Puede correr?: " , run
                , "\n¿Puede nadar?: " , swim)

test_birds(OstrichISP())
test_birds(SwiftISP())
test_birds(PenguinISP())
    

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 *  Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio."""  


class Printer(ABC):
    @abstractmethod
    def printer(self):
        pass
    @abstractmethod
    def printer_model(self):
        pass
    def feature_printer(self):
        return True

class BlackAndWhite(ABC):
    @abstractmethod
    def print_BW(self):
        pass

class Color(ABC):
    @abstractmethod
    def print_color(self):
        pass

class Scan(ABC):
    def scanner(self):
        pass

class Fax(ABC):
    def fax(self):
        pass

class BwPrinter(Printer, BlackAndWhite):
    def printer(self):
        super().feature_printer()
    
    def printer_model(self):
        return "Impresora en blanco y negro"
    
    def print_BW(self):
        super().feature_printer()

class ColorPrinter(Printer, Color):
    def printer(self):
        super().feature_printer()

    def printer_model(self):
        return "Impresora a color"
    
    def print_color(self):
        super().feature_printer()


class MultiPrinter(Printer, Color, Scan, Fax, BlackAndWhite):
    def printer(self):
        super().feature_printer()

    def printer_model(self):
        return "Dispositivo multifunción"
    
    def print_color(self):
        super().feature_printer()

    def scanner(self):
        super().feature_printer()

    def fax(self):
        super().feature_printer()

    def print_BW(self):
        super().feature_printer()

class Scanner(Printer,Scan):
    def printer(self):
        pass  

    def printer_model(self):
        return "Dispositivo exclusivo de escaneo"
    
    def scanner(self):
        super().feature_printer()


def test_printer(object):
    can_print = False
    device = ""
    bw = False
    color = False
    scan = False
    fax = False

    if isinstance (object, BwPrinter):
        bw = object.feature_printer()
        can_print = object.feature_printer()
        device = object.printer_model()

    elif isinstance (object, ColorPrinter):
        color = object.feature_printer()
        can_print = object.feature_printer()
        device = object.printer_model()

    elif isinstance (object, MultiPrinter):
        can_print = object.feature_printer()
        color = object.feature_printer()
        bw = object.feature_printer()
        scan = object.feature_printer()
        fax = object.feature_printer()
        device = object.printer_model()

    elif isinstance (object, Scanner):
        scan = object.feature_printer()
        device = object.printer_model()

    print("\nTipo de dispositivo: " , device
                , "\n¿puede imprimir?: " , can_print
                , "\n¿Imprime en blanco y negro?: " , bw
                , "\n¿Imprime en color?: " , color
                , "\n¿Escanea Documentos?: " , scan
                , "\n¿Puede enviar/recibir fax?: " , fax)

test_printer(BwPrinter())
test_printer(MultiPrinter())
test_printer(Scanner())
test_printer(ColorPrinter())
