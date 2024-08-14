'''
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
 */
'''

'''
Basic
'''

class Form:

    def draw(self):
        ...

class Square(Form):
    def draw(self):
        print("Square")

class Circle(Form):
    def draw(self):
        print("Circle")

class Triangle(Form):
    def draw(self):
        print("Triangle")


'''
Extra
'''

from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Sum(Operation):
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
            raise ValueError(f'Operation {name} not found')
        return self.operations[name].execute(a, b)

calculator = Calculator()
calculator.add_operation('sum', Sum())
calculator.add_operation('subtraction', Subtraction())
calculator.add_operation('multiplication', Multiplication())
calculator.add_operation('division', Division())
calculator.add_operation('power', Power())

print(calculator.calculate('sum', 2, 3))
print(calculator.calculate('subtraction', 15, 3))
print(calculator.calculate('multiplication', 2, 3))
print(calculator.calculate('division', 10, 5))
print(calculator.calculate('power', 2, 3))