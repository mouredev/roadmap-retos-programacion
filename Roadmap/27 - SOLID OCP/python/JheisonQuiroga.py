# Author: Jheison Duban Quiroga Quintero
# Github: https://github.com/JheisonQuiroga

"""/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta."""

# Violación del OCP

class AreaCalculator:
    def get_area(self, shape, *args):
        match shape:
            case "circulo": 
                return 3.14 * args[0] ** 2
            case "cuadrado":
                return args[0] ** 2
            

# Siguiendo el OCP

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        ...

class Circle(Shape):
    def __init__(self, radio) -> None:
        self.radio = radio

    def get_area(self) -> float:
        return math.pi * self.radio ** 2
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

# Clase que calcula la forma
class AreaCalculator:
    def get_area(self, shape:Shape):
        return shape.get_area()
    


c1 = Circle(5)
print(AreaCalculator().get_area(c1))


"""*
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
 */"""

# Clase Base
class Operation(ABC):
    @abstractmethod
    def calculate(self, n1, n2):
        ...

# Operaciones Concretas
class Add(Operation):
    def calculate(self, n1, n2):
        return n1 + n2
    

class Subtract(Operation):
    def calculate(self, n1, n2):
        return n1 - n2
    
class Multiply(Operation):
    def calculate(self, n1 , n2):
        return n1 * n2
    
class Division(Operation):
    def calculate(self, n1, n2):
        if n2 == 0:
            raise ValueError("El divisor no puede ser 0")
        return n1 / n2

# Clase que delega de las operaciones
class Calculator:
    def calculate(self, n1, n2, operation: Operation):
        return operation.calculate(n1, n2)
    
if __name__ == "__main__":

    calculator1 = Calculator()
    print(calculator1.calculate(10, 2, Add()))
        
    # Agregando una quinta operación (Potencia)
    class Power(Operation):
        def calculate(self, n1, n2):
            return n1 ** n2
        

    print(calculator1.calculate(5, 2, Power()))