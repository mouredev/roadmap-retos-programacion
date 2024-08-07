"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces (Interface Segregation Principle, ISP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
 *
"""
from abc import ABC, abstractmethod

# Forma incorrecta


class Bird(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def do_sound(self) -> str:
        pass


class Crow(Bird):

    def fly(self):
        print(f"{self.name} is flying high and fast!")

    def swim(self):
        raise NotImplementedError("Crows don't swim!")

    def do_sound(self) -> str:
        return "Caw"


class Duck(Bird):

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"

# Forma correcta


class Bird(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def do_sound(self) -> str:
        pass


class FlyingBird(Bird):

    @abstractmethod
    def fly(self):
        pass


class SwimmingBird(Bird):

    @abstractmethod
    def swim(self):
        pass


class Crow(FlyingBird):

    def fly(self):
        print(f"{self.name} is flying high and fast!")

    def do_sound(self) -> str:
        return "Caw"


class Duck(SwimmingBird, FlyingBird):

    def fly(self):
        print(f"{self.name} is flying not very high")

    def swim(self):
        print(f"{self.name} swims in the lake and quacks")

    def do_sound(self) -> str:
        return "Quack"


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 */
"""
