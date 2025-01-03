"""
Ejercicio
"""


from abc import ABC, abstractmethod


class Form:
    def draw(self):
        pass


class Square(Form):
    def draw(self):
        print("Dibuja un cuadrado")


class Circle(Form):
    def draw(self):
        print("Dibuja un círculo")


class Triangle(Form):
    def draw(self):
        print("Dibuja un triángulo")


"""
Extra
"""


class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(Operation):
    def execute(self, a, b):
        return a + b


class Substration(Operation):
    def execute(self, a, b):
        return a - b


class Multiplication(Operation):
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
            raise ValueError(f"La operación {name} no está soportada.")
        return self.operations[name].execute(a, b)


calculator = Calculator()
calculator.add_operation("addition", Addition())
calculator.add_operation("substration", Substration())
calculator.add_operation("multiplication", Multiplication())
calculator.add_operation("division", Division())
calculator.add_operation("power", Power())

print(calculator.calculate("addition", 10, 5))
print(calculator.calculate("substration", 10, 5))
print(calculator.calculate("multiplication", 10, 5))
print(calculator.calculate("division", 10, 5))
print(calculator.calculate("power", 10, 5))
