"""
27 - SOLID OCP
Teoría - OCP (Open/Closed Principle)

El principio abierto/cerrado (OCP) establece que una entidad de software debe estar abierta para su extensión, 
pero cerrada para su modificación. Esto significa que una clase debe ser extensible sin modificar su código fuente.

En otras palabras, el principio OCP establece que una clase debe ser abierta para la extensión, pero cerrada para la modificación.

Extender una clase significa agregar nuevas funcionalidades a una clase existente. 
Y modificar una clase significa cambiar su código fuente.

El principio OCP se puede lograr mediante el uso de interfaces y clases abstractas.
"""

## Ejercicio

"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
"""
# Ejemplo incorrecto
class FormBad:

    def draw_square(self):
        print("Drawing square")

    def draw_circle(self):
        print("Drawing circle")

    def draw_triangle(self):
        print("Drawing triangle")

# Ejemplo correcto
class Form:
    def draw(self):
        pass

class Square(Form):
    def draw(self):
        print("+----+")
        print("| ** |")
        print("| ** |")
        print("+----+")

class Triangle(Form):
    def draw(self):
        print("  /\\")
        print(" /  \\")
        print("/____\\")

class Circle(Form):
    def draw(self):
        print("  ****")
        print(" *    *")
        print(" *    *")
        print("  ****")

forms = [Square(), Triangle(), Circle()]
for form in forms:
    form.draw()
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
 */
"""

# Ejemplo incorrecto
class CalculatorBad:

    def sum(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

# Ejemplo correcto
class Operation:
    def operate(self, a, b):
        pass

class Sum(Operation):
    def operate(self, a, b):
        return a + b

class Subtract(Operation):
    def operate(self, a, b):
        return a - b

class Multiply(Operation):
    def operate(self, a, b):
        return a * b
    
class Divide(Operation):
    def operate(self, a, b):
        return a / b

class Power(Operation):
    def operate(self, a, b):
        return a ** b

#Ejemplo de uso
operations = [Sum(), Subtract(), Multiply(), Divide(), Power()]

for operation in operations:
    print(f"{operation.__class__.__name__} => {operation.operate(2, 3)}")

# Ejempo mejorado con abstracción
# La clase Operation es una clase abstracta que define un método abstracto operate.
# Las clases Sum, Subtract, Multiply, Divide y Power heredan de Operation y sobreescriben el método operate.
# La mejora es que en las clases hijo es obligatorio implementar el método operate, 
# lo que garantiza que todas las operaciones tengan la misma firma.

from abc import ABC, abstractmethod
from typing import Any

#ABC = Abstract Base Class (Clase Base Abstracta)

class Operation(ABC):
    @abstractmethod
    def operate(self, a, b):
        pass

class Sum(Operation):
    def operate(self, a, b):
        return a + b

class Subtract(Operation):
    def operate(self, a, b):
        return a - b

class Multiply(Operation):
    def operate(self, a, b):
        return a * b
    
class Divide(Operation):
    def operate(self, a, b):
        return a / b

class Power(Operation):
    def operate(self, a, b):
        return a ** b

# CLASE CALCULADORA QUE SOLICITA AL USUARIO QUE INGRESE DOS NÚMEROS Y UNA OPERACIÓN MATEMÁTICA
class Calculator:
    def __init__(self):
        self.operations = {}

    def add_operation(self, name, operation):
        self.operations[name] = operation

    def run(self):
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        for name, operation in self.operations.items():
            print(f"{name} => {operation.operate(a, b)}")

calculator = Calculator()
calculator.add_operation("Sum", Sum())
calculator.add_operation("Subtract", Subtract())
calculator.add_operation("Multiply", Multiply())
calculator.add_operation("Divide", Divide())
calculator.add_operation("Power", Power())

calculator.run()