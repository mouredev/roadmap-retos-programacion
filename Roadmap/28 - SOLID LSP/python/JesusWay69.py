import os, platform
from math import pi
from abc import ABC
if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

""" 
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
"""

class Figure1:
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height
    def calculate_area(self):
        return self.base * self.height
    
class Rectangle1(Figure1):
    def __init__(self, base, height) -> None:
        super().__init__(base, height)
    def calculate_area(self):
        return super().calculate_area()

class Square1(Figure1):
    def __init__(self, base, height) -> None:
        super().__init__(base, height)
        self.height = base
    def calculate_area(self):
        return super().calculate_area()
    
rectangle1 = Rectangle1(2,5).calculate_area()
square1 = Square1(2,5).calculate_area()
print(rectangle1)
print(square1)

"""
El Principio de Sustitución de Liskov establece que las subclases deben ser sustituibles por sus clases base.
En el caso de  no se cumple este principio porque para calcular el área de un cuadrado es innecesario
el aporte de 2 argumentos (base y altura) aunque en este caso concreto hemos "trampeado" la clase para que tome sólo
un valor e ignore el otro, aun así siguen siendo obligatorios los 2 argumentos aunque el 2do sea innecesario, además
al tener la misma fórmula de multiplicación simple para calcular el área el método calculate_area nos valdría pero si
quisiéramos ampliar el programa y añadir una clase que cree objetos circulares y calcular su área ya no nos serviría
la clase padre y llamar a su método calculate_area """


class Figure2(ABC):
    def __init__(self) -> None:
        pass
    def calculate_area(self):
        return "Figura no definida"

class Rectangle2(Figure2):
    def __init__(self, arg1, arg2) -> None:
        self.arg1 = arg1
        self.arg2 = arg2       
    def calculate_area(self):
        return f"El área del rectángulo con base {self.arg1} y altura {self.arg2} es: {self.arg1 * self.arg2}"                       
    
class Square2(Figure2):
    def __init__(self, side) -> None:
        self.side = side
    def calculate_area(self):
        return f"El área del cuadrado con lado {self.side} es: {self.side ** 2}"
    
class Circle2(Figure2):
     def __init__(self, radius) -> None:
        self.radius = radius
     def calculate_area(self):
         return f"El área del círculo con radio {self.radius} es: {round((self.radius ** 2 * pi),2)}"
          
rectangle2 = Rectangle2(2,5).calculate_area()
square2 = Square2(5).calculate_area()
circle2 = Circle2(5).calculate_area()
figure2 = Figure2().calculate_area()

print(rectangle2)
print(square2)
print(circle2)
print(figure2)
print()

"""En este caso creamos una clase abstracta con ABC que defina los métodos a usar en las subclases
   de esta manera podemos seguir creando sublases con diferentes formas geométricas aplicando a cada una
   de ellas las funcionalidades concretas de esos métodos tanto los argumentos requeridos al iniciar la instancia
   como el cálculo del área para cada forma y así respetamos el LSP aunque la clase padre sea sólamente una especie de
   interface (en python no se pueden declarar como tal) que sirva como plantilla para el resto de clases"""



""" 
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP."""


class Vehicle:
    name = "vehículo en general"
    def accelerate(self):
        return True
    def brake(self):
        return True
    
class Car(Vehicle):
    name = "coche"
    def accelerate(self):
        return super().accelerate()
    def brake(self):
        return super().brake()
       
class Motorbike(Vehicle):
    name = "moto"
    def accelerate(self):
        return super().accelerate()
    def brake(self):
        return super().brake()
      
class Truck(Vehicle):
    name = "camión"
    def accelerate(self):
        return super().accelerate()
    def brake(self):
        return super().brake()
    
vehicle = Vehicle()
car = Car()
truck = Truck()
motorbike = Motorbike()

def lsp(object):
    print(f"¿El vehículo '{object.name}' acelera? : {object.accelerate()}")
    print(f"¿El vehículo '{object.name}' frena? : {object.brake()}")

lsp(vehicle)
lsp(car)
lsp(truck)
lsp(motorbike)

