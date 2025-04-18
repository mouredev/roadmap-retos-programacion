# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga

"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *"""


# Violando el LSP
import pytest

class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def get_area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def get_area_test(r: Rectangle):
    ancho = r.width
    r.height = 10
    print(f"Área esperada de {ancho * 10}, tiene {r.get_area()}")


@pytest.mark.xfail("La figura viola el LSP")
def test(r: Rectangle):
    r.width = 4
    r.height = 5
    assert r.get_area() == 20


rc = Rectangle(2, 3)
get_area_test(rc) # Área esperada de 20, tiene 20

sq = Square(5)
get_area_test(sq) # Área esperada de 50, tiene 100
# test(sq)


# Aplicando el LSP
# La solución es evitar en este caso la herencia y utilizar clases separadas
# o una interfaz 

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height


class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def get_area(self) -> float:
        return self.side ** 2
    

def get_area(shape: Shape):
    return shape.get_area()


for shape in [Rectangle(5, 4), Square(4)]:
    print(get_area(shape))


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */
"""

class Vehicle(ABC):
    @abstractmethod
    def accelerate(self, value) -> str:
        ...

    @abstractmethod
    def slow_down(self, value) -> str:
        ...

class Car(Vehicle):
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, value):
        if value <= 0:
            raise ValueError("La aceleración no pueden ser cero o inferior")
        self.speed += value
        return f"Coche acelerando. Velocidad: {self.speed} km/h"
    
    def slow_down(self, value):
        self.speed = max(0, self.speed - value)
        return f"Frenando, velocidad {self.speed} km/h"
    

class Motorcycle(Vehicle):
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, value):
        if value <= 0:
            raise ValueError("La aceleración no pueden ser cero o inferior")
        self.speed += value
        return f"Moto acelerando. Velocidad: {self.speed} km/h"
    
    def slow_down(self, value):
        self.speed = max(0, self.speed - value)
        return f"Moto frenando, velocidad {self.speed} km/h"


class Bike(Vehicle):
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, value):
        if value <= 0:
            raise ValueError("La aceleración no pueden ser cero o inferior")
        self.speed += value
        return f"Bicicleta acelerando. Velocidad: {self.speed} km/h"
    
    def slow_down(self, value):
        self.speed = max(0, self.speed - value)
        return f"Bicicleta frenando, velocidad {self.speed} km/h"


def test_vehicle(obj: Vehicle):
    print(obj.accelerate(10))
    print(obj.slow_down(5))


if __name__ == "__main__":
    
    vehicles = [Car(), Motorcycle(), Bike()]
    for vehicle in vehicles:
        print(type(vehicle).__name__)
        test_vehicle(vehicle)