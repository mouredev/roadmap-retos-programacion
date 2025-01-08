"""
EJERCICIO:
Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, 
OCP)" y crea un ejemplo simple donde se muestre su funcionamiento de 
forma correcta e incorrecta.

DIFICULTAD EXTRA(opcional):
Desarrolla una calculadora que necesita realizar diversas operaciones
matemáticas.
Requisitos:
- Debes diseñar un sistema que permita agregar nuevas operaciones 
utilizando el OCP.

Instrucciones:
1. Implementa las operaciones de suma, resta, multiplicación y 
división.
2. Comprueba que el sistema funciona.
3. Agrega una quinta operación para calcular potencias.
4. Comprueba que se cumple el OCP.

by adra-dev
"""

"""
Open-Closed Principle (OCP):
El principio open closed para el diseño orientado a objetos fue 
introducido por Bertran Meyer en 1988 y este declara:

    "Las entidades del software(clases, módulos, funciones. etc.)
    deberían estar abiertas para extender su funcionalidad pero 
    cerradas para su modificación."

documentacion:"https://realpython.com/solid-principles-python/"
    
Para entender a que se refiere el principio open-closed considera el 
siguiente ejemplo.
"""


from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2
        

rectangle = Shape("rectangle", width=10, height=5)
print(rectangle.calculate_area())

circle = Shape("circle", radius=5)
print(circle.calculate_area())

"""
La clase shape funciona. Tu puedes crear circulos y rectangulos, 
calcular su área, etc. a pesar de eso la clase luce muy mal. algo se 
ve mal a primera vista.

Imagina que necesitas agregar una nueva figura cuadrado, ¿cómo sería?
Bueno, la opcion aqui seria agregar más cláusulas elif al método .__
init__() y al método .calculate_area(), para que así puedas agregar 
los requerimientos a la figura cuadrado.

Tener que realizar estos cambias para agregar una nueva figura 
significa que tu clase está abierta a modificación lo cual viola el
principio open-closed. aquí hay una posible corrección del código 


"""

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side **2
    

"""
En este código, se le ha realizado un refactor a la clase Shape, 
convirtiéndola en una clase de base abstracta(ABC). Esta clase provee
de una interfaz api para cualquier tipo de forma que se quiera 
definir. Esta interfaz consiste del atributo .shape_type y del método 
.calculate_area() que se pueden sobrescribir en todas las subclases.

Este refactor cierra la clase a modificaciones. Ahora puedes agregar 
nuevas figuras al diseño de tu clase sin la necesidad de modificar la
clase shape en. En cualquier caso, tendrías que modificar la interfaz 
necesario, lo cual también convierte la clase a un tipo polimórfica.

"""

"""
Extra
"""

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(Operation):
    def execute(self, a,b):
        return a + b


class Substract(Operation):
    def execute(self, a, b):
        return a - b
    

class Multiply(Operation):
    def execute(self, a, b):
        return a * b
    

class Division(Operation):    
    def execute(self, a, b):
        return a / b
    

class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Calculator:
    def __init__(self) -> None:
        self.operations = {}

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f"La operacion {name} no esta soportada.")
        return self.operations[name].execute(a,b)


calculator = Calculator()
calculator.add_operation("addition", Addition())
calculator.add_operation("substract", Substract())
calculator.add_operation("multiply", Multiply())
calculator.add_operation("division", Division())
calculator.add_operation("power", Power())

print(calculator.calculate("addition", 10,2))
print(calculator.calculate("substract", 10,5))
print(calculator.calculate("multiply", 10,5))
print(calculator.calculate("division", 10,5))
print(calculator.calculate("power", 10,5))