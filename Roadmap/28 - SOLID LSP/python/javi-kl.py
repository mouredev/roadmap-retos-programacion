# incorrecto
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def correr(self):
        pass


class Perro(Animal):
    def correr(self):
        print("El perror esta corriendo")


# No se respeta el comportamiento esperado
class Halcon(Animal):
    def correr(self):
        raise NotImplementedError("Los Halcones no pueden correr")


# Correcto
class Animal(ABC):
    @abstractmethod
    def moverse(self):
        pass


class Perro(Animal):
    def moverse(self):
        print("El perro se esta moviendo")


# Si se respeta el comportamiento esperado
class Halcon(Animal):
    def moverse(self):
        print("El halcon se esta moviendo")


perro = Perro()
perro.moverse()

halcon = Halcon()
halcon.moverse()


"""
extra
"""


# Solo puede tener metodos que sean utilizables por todas las clases(No podría tener 'despegar').
class Vehiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass


class Coche(Vehiculo):
    def acelerar(self):
        print("El coche está acelerando")

    def frenar(self):
        print("El coche está frenando")


# Si quisiera implementar 'despegar/aterrizar' lo haría dentro de esta clase y no en la clase padre.
class Avion(Vehiculo):
    def acelerar(self):
        print("El avion está acelerando")

    def frenar(self):
        print("El avion está frenando")


# Si quisiera implementar 'pedalear' lo haría dentro de esta clase y no en la clase padre.
class Bicicleta(Vehiculo):
    def acelerar(self):
        print("La bicicleta está acelerando")

    def frenar(self):
        print("La bicicleta está frenando")


# instanciamos vehiculos
coche = Coche()
avion = Avion()
bici = Bicicleta()


# comprobar LSP
def prueba_vehiculo(vehiculo: Vehiculo):
    vehiculo.acelerar()
    vehiculo.frenar()


prueba_vehiculo(coche)
prueba_vehiculo(avion)
prueba_vehiculo(bici)
