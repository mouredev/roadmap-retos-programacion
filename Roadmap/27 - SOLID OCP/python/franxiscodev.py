"""
SOLID
OCP: principio abierto-cerrado
Opened-Closed Principle 
Abierto para la extensión, cerrado para la modificación
Se puede ampliar, pero lo que ya tenemos no lo tocamos
"""
# Explicación
# El principio OCP establece que una clase debe estar abierta para la extensión, pero cerrada para la modificación.
# Esto significa que deberíamos poder agregar nuevas funcionalidades a una clase sin modificar su código existente.
# En otras palabras, el comportamiento de una clase debe poder extenderse sin cambiar su implementación original.


from abc import ABC, abstractmethod


class Shape:
    def draw(self):
        raise NotImplementedError("Subclasses must implement this method")


class Square(Shape):
    def draw(self):
        return "Drawing a square"


class Circle(Shape):
    def draw(self):
        return "Drawing a circle"


class Rectangle(Shape):
    def draw(self):
        return "Drawing a rectangle"


# Extra
# clases abstractas
# Se pueden crear clases abstractas para definir métodos que deben ser implementados por las subclases
# y así evitar la implementación de métodos vacíos en las subclases.
# En Python, esto se puede hacer utilizando el módulo abc (Abstract Base Classes).
# Esto permite definir una clase base abstracta y especificar métodos abstractos que deben ser implementados por las subclases.
# Esto ayuda a garantizar que las subclases sigan un contrato específico y proporciona una forma de crear jerarquías de clases más estructuradas.

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(Operation):
    def execute(self, a, b):
        return a + b


class Subtraction(Operation):
    def execute(self, a, b):
        return a - b


class Multiplication(Operation):
    def execute(self, a, b):
        return a * b


class Division(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por zero")
        return a / b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Calculator:
    def __init__(self):
        self.operations = {
            "addition": Addition(),
            "subtraction": Subtraction(),
            "multiplication": Multiplication(),
            "division": Division()
        }

    def add_operation(self, operation_name, operation):
        if not isinstance(operation, Operation):
            raise ValueError(
                "La operación debe ser una instancia de la clase Operation")
        self.operations[operation_name] = operation

    def calculate(self, operation_name, a, b):
        if operation_name not in self.operations:
            raise ValueError(f"Operación '{operation_name}' no soportada")
        return self.operations[operation_name].execute(a, b)


calculator = Calculator()
print(calculator.calculate("addition", 5, 3))  # Output: 8
print(calculator.calculate("subtraction", 5, 3))  # Output: 2
print(calculator.calculate("multiplication", 5, 3))  # Output: 15
print(calculator.calculate("division", 5, 3))  # Output: 1.6666666666666667
# Output: ValueError: No se puede dividir por zero
# print(calculator.calculate("division", 5, 0))
calculator.add_operation("power", Power())

print(calculator.calculate("power", 5, 3))
