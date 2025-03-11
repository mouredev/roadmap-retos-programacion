"""
#29 - Principio SOLID: Segregacion de interfaces en Python 
"""
# "Los clientes no deberian versen forzados a depender de interfaces que no utilizan."
# Es mejor tener varias interfaces especificas y pequeñas
# Esto evita que las clases dependan de metodos que no necesitan.

"""
Beneficios de aplicar el ISP
"""
# Código más mantenible: Las interfaces pequeñas y específicas son más fáciles de mantener y modificar.
# Mayor cohesión: Cada interfaz tiene una responsabilidad clara y concreta.
# Menor acoplamiento: Las clases solo dependen de las interfaces que realmente necesitan.
# Mayor flexibilidad: Es más fácil combinar interfaces pequeñas para crear comportamientos complejos.
# Testing más sencillo: Las interfaces pequeñas facilitan la creación de mocks y stubs para pruebas.



"""
Violacion del principio.
"""
# Creamos un programa para para dos impresoras, una nueva y una vieja
# El problema aquí es que ImpresoraVieja está obligada a implementar métodos que no puede realizar.


from abc import ABC, abstractmethod

class ImpresionDispositivo(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass
    
    @abstractmethod
    def escanear(self, documento):
        pass
    
    @abstractmethod
    def enviar_fax(self, documento):
        pass
    
    @abstractmethod
    def grapar(self, documento):
        pass


class ImpresoraModerna(ImpresionDispositivo):
    def imprimir(self, documento):
        print(f"Imprimiendo: {documento}")
    
    def escanear(self, documento):
        print(f"Escaneando: {documento}")
    
    def enviar_fax(self, documento):
        print(f"Enviando fax: {documento}")
    
    def grapar(self, documento):
        print(f"Grapando: {documento}")


class ImpresoraVieja(ImpresionDispositivo):
    def imprimir(self, documento):
        print(f"Imprimiendo: {documento}")
    
    def escanear(self, documento):
        # Esta impresora no puede escanear
        raise NotImplementedError("Esta impresora no puede escanear")
    
    def enviar_fax(self, documento):
        # Esta impresora no puede enviar fax
        raise NotImplementedError("Esta impresora no puede enviar fax")
    
    def grapar(self, documento):
        # Esta impresora no puede grapar
        raise NotImplementedError("Esta impresora no puede grapar")
    


"""
Aplicar correctamente el principio y Ejercicio Extra
"""
from abc import ABC, abstractmethod

class Impresora(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass


class Escaner(ABC):
    @abstractmethod
    def escanear(self, documento):
        pass


class FaxDevice(ABC):
    @abstractmethod
    def enviar_fax(self, documento):
        pass


class Grapadora(ABC):
    @abstractmethod
    def grapar(self, documento):
        pass


class ImpresoraModerna(Impresora, Escaner, FaxDevice, Grapadora):
    def imprimir(self, documento):
        print(f"Imprimiendo: {documento}")
    
    def escanear(self, documento):
        print(f"Escaneando: {documento}")
    
    def enviar_fax(self, documento):
        print(f"Enviando fax: {documento}")
    
    def grapar(self, documento):
        print(f"Grapando: {documento}")


class ImpresoraVieja(Impresora):
    def imprimir(self, documento):
        print(f"Imprimiendo: {documento}")
