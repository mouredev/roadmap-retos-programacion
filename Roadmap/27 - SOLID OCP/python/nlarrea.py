"""
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
"""

# Incorrecto


class GeometricForm:
    def draw_square(self):
        print("Drawing a square")

    def draw_circle(self):
        print("Drawing a circle")


# Correcto


class GeometricForm:
    def draw(self):
        pass


class Square(GeometricForm):
    def draw(self):
        print("Drawing a square!")


class Circle(GeometricForm):
    def draw(self):
        print("Drawing a circle!")


"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
"""


# Import Abstract Base Class and abstractmethod decorator
from abc import ABC, abstractmethod


# Create the abstract class -> avoid's creating instances of this class, but
# still allows to inherit from it
class Operation(ABC):
    @abstractmethod
    def calculate(self, num_one, num_two):
        pass


# Create the different operations


class Sum(Operation):
    def calculate(self, num_one, num_two):
        return num_one + num_two


class Subtraction(Operation):
    def calculate(self, num_one, num_two):
        return num_one - num_two


class Multiplication(Operation):
    def calculate(self, num_one, num_two):
        return num_one * num_two


class Division(Operation):
    def calculate(self, num_one, num_two):
        return num_one / num_two


# Create the Calculator class
class Calculator:
    def __init__(self) -> None:
        self.operations = dict()

    def set_operation(self, name: str, operation: object):
        """Allow adding new operations to the current calculator instance."""

        if not isinstance(name, str):
            raise ValueError("The operation name must be an string!")
        self.operations[name] = operation

    def calculate(self, name: str, num_one, num_two):
        """Checks if the given operation name exists and returns the value of
        the operation."""

        if name not in self.operations:
            raise ValueError(f"The operation '{name}' doesn't exist!")
        return self.operations[name].calculate(num_one, num_two)


# Create the Calculator's instance and set different operations
calculator = Calculator()
calculator.set_operation("sum", Sum())
calculator.set_operation("subtract", Subtraction())
calculator.set_operation("multiply", Multiplication())
calculator.set_operation("divide", Division())

# Check if operations work
print(calculator.calculate("sum", 10, 2))  # 12
print(calculator.calculate("subtract", 10, 2))  # 8
print(calculator.calculate("multiply", 10, 2))  # 20
print(calculator.calculate("divide", 10, 2))  # 5.0
# print(calculator.calculate("pow", 10, 2))  # The operation 'pow' doesn't exist


# Create the new Pow operation
class Pow(Operation):
    def calculate(self, num_one, num_two):
        return num_one**num_two


# Set it to the calculator
calculator.set_operation("pow", Pow())

# Check if operation works
print(calculator.calculate("pow", 10, 2))  # 100
