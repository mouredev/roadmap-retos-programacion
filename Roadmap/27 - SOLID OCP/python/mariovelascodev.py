from abc import ABC, abstractmethod

# Ejercicio

# Incorrecto
"""
class Geometry:
    def area_square(self, side):
        return side * side

    def area_triangle(self, base, height):
        return (base * height) / 2

    def area_rectangle(self, base, height):
        return base * height
"""


# Correcto
class Geometry:
    def area(self):
        pass


class Square(Geometry):
    def area(self, side):
        return side * side


class Triangle(Geometry):
    def area(self, base, height):
        return (base * height) / 2


class Rectangle(Geometry):
    def area(self, base, height):
        return base * height


# Extra


class Operation(ABC):
    @abstractmethod
    def execute(self, value1, value2):
        pass


class Add(Operation):
    def execute(self, value1, value2):
        return value1 + value2


class Subtract(Operation):
    def execute(self, value1, value2):
        return value1 - value2


class Multiply(Operation):
    def execute(self, value1, value2):
        return value1 * value2


class Division(Operation):
    def execute(self, value1, value2):
        try:
            return value1 / value2
        except ZeroDivisionError:
            return "No se puede dividir por cero."


class Power(Operation):
    def execute(self, value1, value2):
        return value1**value2


class Calculator:
    def __init__(self):
        # Usamos un diccionario para registrar operaciones
        self.operations = {}

    def register_operation(self, name, type_operation):
        self.operations[name] = type_operation

    def calculate(self, name_operation, value1, value2):
        if name_operation not in self.operations:
            return f"La operación '{name_operation}' no fue encontrada."
        return self.operations[name_operation].execute(value1, value2)


calculadora = Calculator()
calculadora.register_operation("suma", Add())
calculadora.register_operation("resta", Subtract())
calculadora.register_operation("multiplicacion", Multiply())
calculadora.register_operation("division", Division())
calculadora.register_operation("potencia", Power())

print(calculadora.calculate("suma", 2, 3))
print(calculadora.calculate("resta", 40, 3))
print(calculadora.calculate("multiplicacion", 5, 3))
print(calculadora.calculate("division", 24, 4))
print(calculadora.calculate("potencia", 2, 3))
print(calculadora.calculate("cuadrado", 2, 3))
