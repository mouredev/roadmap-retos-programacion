"""
27 - Principio SOLID: Abierto - Cerrado
"""
# Las entidades de software (clases, modulos, funciones) deberian estar abiertas para extensión pero cerradas para modificación.
# Deberiamos poder añadir nuevas funcionalidades sin tener que modificar el codigo

# Forma incorrecta
# Calcular areas

class Reactangulo:
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto
        


class Circulo:
    def __init__(self, radio: float):
        self.radio = radio


class CalculadorArea:
    def calcular_area(self, figuras):
        area_total = 0
        for figura in figuras:
            if isinstance(figura, Reactangulo):
                area_total += figura.ancho * figura.alto
            elif isinstance(figura, Circulo):
                area_total += 3.1416 * figura.radio * figura.radio
        return area_total
    
rectangulo = Reactangulo(5, 10)
circulo = Circulo(7)
calculador = CalculadorArea()
print(calculador.calcular_area([rectangulo, circulo]))

# Cada vez que querramos añadir una nueva forma geometrica tenemos que modificar la clase Calculador Area


# Forma correcta
from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


class Rectangulo:
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio * self.radio

class CalculadorArea:
    def calcular_area(self, figuras):
        return sum(figura.calcular_area() for figura in figuras)
    

rectangulo = Rectangulo(5, 10)
circulo = Circulo(7)
calculador = CalculadorArea()
print(calculador.calcular_area([rectangulo, circulo]))


"""
Extra
"""
from abc import ABC, abstractmethod

class Operation:
    @abstractmethod
    def execute(self, a, b):
        pass

class Sum:
    def execute(self, a, b):
        return a + b

class Subtract:
    def execute(self, a, b):
        return a - b


class Multiply:
    def execute(self, a, b):
        return a * b


class Divide:
    def execute(self, a, b):
        return a / b
    

class Power:
    def execute(self, a, b):
        return a ** b
    

class Calculator:
    def __init__(self) -> None:
        self.operations = {}

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f"La operación {name} no está soportada.")
        return self.operations[name].execute(a, b)


calculator = Calculator()
calculator.add_operation("sum", Sum())
calculator.add_operation("subtract", Subtract())
calculator.add_operation("multiply", Multiply())
calculator.add_operation("divide", Divide())
calculator.add_operation("power", Power())

print(calculator.calculate("sum", 10, 5))
print(calculator.calculate("subtract", 10, 5))
print(calculator.calculate("multiply", 10, 5))
print(calculator.calculate("divide", 10, 5))
print(calculator.calculate("power", 10, 5))