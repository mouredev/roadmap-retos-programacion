# @Author daniel Grande (Mhayhem)

# EJERCICIO:
# Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
# y crea un ejemplo simple donde se muestre su funcionamiento
# de forma correcta e incorrecta.

# INCORRECTO
class CalculateArea:
    def calculate_area(self, shape: str, **kwargs):
        if shape == "circulo":
            return 3.14 * kwargs['radio'] ** 2
        elif shape == "cuadrado":
            return kwargs['width'] * kwargs['height']

""" para añadir triangulo tendriamos que modificar la clase"""



# CORRECTO

class GeometricShape:
    def calculate_area(self):
        raise NotImplementedError("Debes inplementar calculate_area")

class Circle(GeometricShape):
    def __init__(self, radio: float):
        self.radio = radio
    
    def calculate_area(self) -> float:
        return 3.14 * self.radio ** 2

class Square(GeometricShape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def calculate_area(self) -> float:
        return self.width * self.height

""" ahora si queremos incorporar el triangulo solo debemos crear otra clase """

class Triangle(GeometricShape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
    
    def calculate_area(self) -> float:
        return (self.base * self.height) / 2



# DIFICULTAD EXTRA (opcional):
# Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
# Requisitos:
# - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
# Instrucciones:
# 1. Implementa las operaciones de suma, resta, multiplicación y división.
# 2. Comprueba que el sistema funciona.
# 3. Agrega una quinta operación para calcular potencias.
# 4. Comprueba que se cumple el OCP.


class Calculator:
    def __init__(self, n1: float, n2: float):
        self.n1 = n1
        self.n2 = n2
    
    def operation(self):
        pass

class Add(Calculator):
    def operation(self):
        return self.n1 + self.n2

class Subtract(Calculator):
    def operation(self):
        return self.n1 - self.n2

class Multiply(Calculator):
    def operation(self):
        return  self.n1 * self.n2

class Division(Calculator):
    def operation(self):
        if self.n2 == 0:
            raise ValueError("No se puede dividir por cero")
        return self.n1 / self.n2

class Raised(Calculator):
    def operation(self):
        return self.n1 ** self.n2
    

add = Add(3, 5)
print(add.operation())