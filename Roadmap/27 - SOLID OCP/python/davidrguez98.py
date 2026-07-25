""" /*
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
 */ """

#EJERCICIO

""" 
Incorrecta
"""

class Form:

    def draw_square(self):
        print("Dibujar un cuadrado.")

    def draw_circle(self):
        print("Dibujar un círculo.")

""" 
Correcta
"""

class Form:

    def draw(self):
        pass

class Square(Form):

    def draw(self):
        print("Dibuja un cuadrado.")

class Circle(Form):

    def draw(self):
        print("Dibuja un círculo.")

class Triangle(Form):

    def draw(self):
        print("Dibuja un triángulo.")

#EJERCICIO EXTRA

class Operation:
    def operation(self, number1: int, number2: int):
        pass

class Sum(Operation):

    def operation(self, number1: int, number2: int):
        return number1 + number2

class Rest(Operation):

    def operation(self, number1: int, number2: int):
        return number1 - number2

class Multiplication(Operation):

    def operation(self, number1: int, number2: int):
        return number1 * number2

class Divide(Operation):

    def operation(self, number1: int, number2: int):
        return number1 / number2

class Power(Operation):

    def operation(self, number1: int, number2: int):
        return number1 ** number2

class Calculator:

    def __init__(self):
        self.operations = {}

    def add_operation(self, name, operation_):
        self.operations[name] = operation_

    def calculate(self, name, number1, number2):
        if name not in self.operations:
            raise ValueError(f"La operación {name} no se encuentra en la calculadora.")
        return self.operations[name].operation(number1, number2)

calculator = Calculator()

calculator.add_operation("Sumar", Sum())
calculator.add_operation("Restar", Rest())
calculator.add_operation("Multiplicar", Multiplication())
calculator.add_operation("Dividir", Divide())
calculator.add_operation("Potencia de dos", Power())

print(calculator.calculate("Sumar", 2, 2))
print(calculator.calculate("Restar", 2, 2))
print(calculator.calculate("Multiplicar", 2, 2))
print(calculator.calculate("Dividir", 2, 2))
print(calculator.calculate("Potencia de dos", 2, 2))