#  * EJERCICIO:
#  * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
#  * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
#  *

#El principio de segregación de interfaces establece que un cliente no debe ser forzado a depender de interfaces que no utiliza.
#En otras palabras, no se debe obligar a una clase a implementar interfaces que no necesita. 
# En lugar de eso, se deben dividir las interfaces en interfaces más pequeñas y específicas, de modo que las clases solo implementen las interfaces que son de su interés. 
#De esta forma, se evita que las clases tengan que implementar métodos que no necesitan, lo que puede llevar a una mayor complejidad y a un código más difícil de mantener.

#ejemplo incorrecto donde se viola el principio de segregación de interfaces
class IShape:
    def draw(self):
        pass

    def calculate_area(self):
        pass

class Circle(IShape):
    def draw(self):
        print("Circle Drawn")

    def calculate_area(self):
        print("Circle Area Calculated")

class Square(IShape):
    def draw(self):
        print("Square Drawn")

    def calculate_area(self):
        print("Square Area Calculated")

#En el ejemplo anterior, la interfaz IShape tiene dos métodos: draw() y calculate_area(). 
#Las clases Circle y Square implementan esta interfaz, pero no necesitan ambos métodos.
#Circle solo necesita el método draw() y Square solo necesita el método calculate_area().
#Esto viola el principio de segregación de interfaces, ya que las clases están obligadas a implementar métodos que no necesitan.

#ejemplo correcto donde se cumple el principio de segregación de interfaces
class IDrawable:
    def draw(self):
        pass

class ICalculatable:
    def calculate_area(self):
        pass

class Circle(IDrawable):
    def draw(self):
        print("Circle Drawn")

class Square(ICalculatable):
    def calculate_area(self):
        print("Square Area Calculated")

#En el ejemplo anterior, se han dividido las interfaces en IDrawable e ICalculatable, de modo que las clases solo implementan las interfaces que necesitan.
#Circle implementa la interfaz IDrawable y Square implementa la interfaz ICalculatable,lo que evita que tengan que implementar métodos que no necesitan. Esto cumple con el principio de segregación de interfaces.

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

from abc import ABC, abstractmethod

class Impresora(ABC):
    @abstracmethod
    def imprimir(self, documento):
        pass

class ImpresoraBN(Impresora):
    def imprimir(self, documento):
        print(f"Se ha impreso el {documento} a blanco y negro")

class ImpresoraColor(Impresora):
    def imprimir(self, documento):
        print(f"Se ha impreso el {documento} a color")

class ImpresoraMul(Impresora):
    def imprimir(self, documento):
        print(f"Se ha impreso {documento} en multifuncion")
    
    def scanner(self, documento):
        print(f"Se escaneo el {documento}")
    
    def fax(self, documento, nfax):
        print(f"Se envio el {documento} por fax con el numero {nfax}")


class GesImpresoras:
    def __init__(self):
        self.impresoras = []
    
    def agg_impresoras(self, impresora):
        self.impresoras.append(impresora)

    def imp_doc(self, documento, tipo_impresora=None):
        for impresora in self.impresoras:
            if tipo_impresora is None or isinstance(impresora, tipo_impresora):
                impresora.imprimir(documento)
                break
            else:
                print('No se encontro la impresora')

gestor = GesImpresoras()
gestor.agg_impresoras(ImpresoraBN())
gestor.agg_impresoras(ImpresoraColor())
gestor.agg_impresoras(ImpresoraMul())

gestor.imp_doc('documento', ImpresoraBN)
gestor.imp_doc('documento', ImpresoraColor)
gestor.imp_doc('documento', ImpresoraMul)
