

print("\n\n=======================================EJERCICIO=======================================\n\n")

"""
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

from abc import ABC, abstractmethod

class Area(ABC):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
        
    @abstractmethod
    def calculate_area(self):
        pass
        
class Triangle(Area):
        
    def calculate_area(self): 
        result = (self.base * self.height) / 2
        return result
    
class Square(Area):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)
        
    def calculate_area(self):
        result = self.side ** 2
        return result
    
"""    
 * SI AHORA QUISIERAMOS AÑADIR MAS POLIGONOS A LOS QUE CALCULAR EL AREA NO TENDRIAMOS QUE TOCAR NADA DE LO ESCRITO
 * SOLAMENTE AÑADIR LAS NUEVAS SUBCLASES COMO POR EJEMPLO LA SUBCLASE "RECTANGULO"
""" 

class Rectangle(Area):
    
    def calculate_area(self):
        result = self.base * self.height
        return result
    

my_triangle = Triangle(3 ,5)
print(f"\n[+] El area del triangulo es: {my_triangle.calculate_area()}")

my_square = Square(9)
print(f"\n[+] El area del triangulo es: {my_square.calculate_area()}")

my_rectangle = Rectangle(7, 5)
print(f"\n[+] El area del triangulo es: {my_rectangle.calculate_area()}\n")

print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")


"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemÃ¡ticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicacion y division.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operacion para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
"""

class Calculator(ABC):
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2
        
    @abstractmethod
    def solution(self):
        pass
    
class Add(Calculator):
    
    def solution(self):        
        return (self.num1 + self.num2)
        
    
class Subtract(Calculator):
    
    def solution(self):
        return (self.num1 - self.num2)
        
        
        
class Multiply(Calculator):
    
    def solution(self):
        return  self.num1 * self.num2
        
        
class Division(Calculator):
    
    def solution(self):
        return self.num1 / self.num2
        
        
    
my_add = Add(5.2, 7)
print(f"\n[+] El resultado de la suma es: {my_add.solution()}")

my_subtract = Subtract(12, 7)
print(f"\n[+] El resultado de la resta es: {my_subtract.solution()}")

my_multiply = Multiply(9, 7)
print(f"\n[+] El resultado de la multiplicacion es: {my_multiply.solution()}")

my_division = Division(12, 2)
print(f"\n[+] El resultado de la division es: {my_division.solution()}")


# Ahora vamos a añadir la operacion que permite hacer potencias

class Pow(Calculator):
    
    def solution(self):
        return pow(self.num1, self.num2)
    
my_pow = Pow(5, 3)
print(f"\n[+] El resultado de la potencia es: {my_pow.solution()}\n")
