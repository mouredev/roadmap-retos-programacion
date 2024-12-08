
"""

 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# Forma incorrecta

class Product():
    def __init__(self, name) -> None:
        self.name = name
    
    def update_stock(self):
        if self.name == "zapatos":
            print("Actualizado el stock de zapatos")
        elif self.name == "camisas":
            print("Actualizado el stock de camisas")

# Forma correcta

from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def update_stock(self):
        pass

class Shoes(Product):

    def update_stock(self):
        print("Actualizado el stock de zapatos")

class Shirts(Product):

    def update_stock(self):
        print("Actualizado el stock de camisas")


my_products = [Shoes(), Shirts()]

for i in my_products:
    i.update_stock()

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
from abc import ABC, abstractmethod

class Calculator(ABC):

    @abstractmethod
    def calculate_operation(self, a, b):
        pass

class Sum(Calculator):

    def calculate_operation(self, a, b):
        return a + b

class Subtract(Calculator):

    def calculate_operation(self, a, b):
        return a - b

class Multiply(Calculator):

    def calculate_operation(self, a, b):
        return a * b

class Division(Calculator):
    def calculate_operation(self, a, b):
        return a / b

class Pow(Calculator):

    def calculate_operation(self, a, b):
        return a**b


sum_op = Sum()
substract_op = Subtract()
multiply_op = Multiply()
pow_op = Pow()
division_op = Division()

print(sum_op.calculate_operation(4, 5))
print(substract_op.calculate_operation(4,5))
print(multiply_op.calculate_operation(4, 5))
print(pow_op.calculate_operation(4,5))
print(division_op.calculate_operation(4, 5))
