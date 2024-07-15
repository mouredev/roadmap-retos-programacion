import os, platform
from math import pi

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')
"""
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 """
    
class Figure:
    def __init__(self, data1, data2):#Creamos una clase para generar objetos de figuras geométricas
        self.data1 = data1 # que se crearán aportando 2 medidas, base y altura si es un rectángulo
        self.data2 = data2 # o radio y PI si se trata de un círculo por ejemplo

class RectangleArea: # Al crear una clase con una función específica para calcular el área de un rectángulo
    def calc(object:Figure):  # no nos serviría para calcular el área de otra figura geométrica
        return object.data1 * object.data2
    
rectangle = Figure(2,4)
print(f"El área del rectángulo es: {RectangleArea.calc(rectangle)}")


class CalulateArea(Figure):#Si creamos una clase genérica que herede los objetos de la clase padre Figure
    def rectangle(object:Figure) -> int: # podremos ampliar el cálculo de áreas de más figuras añadiendo más métodos a esa clase hija
        return object.data1 * object.data2 # añadiendo a esta directamente los objetos creados en la clase padre y llamando
                                            # a su correspondiente método
    def circle_for_radius(object):
        if object.data2 == None or (object.data1 == object.data2):
            return round((object.data1 ** 2 * pi),2)
        else:
            return "Operación incorrecta"
        
    def circle_for_diameter(object:Figure):
        if object.data2 == None or (object.data1 == object.data2):
            return round(((object.data1 / 2) ** 2 * pi),2)
        else:
            return "Operación incorrecta"
        
    def circle_for_perimeter(object:Figure):
        if object.data2 == None or (object.data1 == object.data2):
            return round((object.data1 * 2),2)
        else:
            return "Operación incorrecta"
        
    def square(object:Figure):
        if object.data2 == None or (object.data1 == object.data2):
            return object.data1 ** 2
        else:
            return "Operación incorrecta"
    
    def triangle(object:Figure) -> int:
        return round((object.data1 * object.data2 / 2), 2)
    
square1 = Figure(4,None)
circle1 = Figure(4, None)
circle2 = Figure(circle1.data1 * 2, None)
circle3 = Figure(circle2.data1 * pi, None)
triangle1 = Figure(3,7)
print (f"El área del cuadrado es: {CalulateArea.square(square1)}")
print (f"El área del círculo por su radio es: {CalulateArea.circle_for_radius(circle1)}")
print (f"El área del círculo por su diámetro es: {CalulateArea.circle_for_diameter(circle2)}")
print (f"El área del círculo por su perímetro es: {CalulateArea.circle_for_perimeter(circle3)}")
print (f"El área del triángulo es: {CalulateArea.triangle(triangle1)}")
print()

 
"""
* DIFICULTAD EXTRA (opcional):
* Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
* Requisitos:
* - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
* Instrucciones:
* 1. Implementa las operaciones de suma, resta, multiplicación y división.
* 2. Comprueba que el sistema funciona.
* 3. Agrega una quinta operación para calcular potencias.
* 4. Comprueba que se cumple el OCP."""
    
class Operator:
    def __init__(self,num1:int, num2:int) -> None:
        self.num1 = num1
        self.num2 = num2

    def my_sum(self) -> int:
        return self.num1 + self.num2
    def my_subt(self) -> int:
        return self.num1 - self.num2
    def my_mult(self) -> int:
        return self.num1 * self.num2
    def my_div(self) -> float:
        return round((self.num1 / self.num2),2)
        
op1 = Operator(2,3)
print("Suma de 2 + 3 desde clase Operator:", op1.my_sum())
print("Resta de 2 - 3 desde clase Operator:",op1.my_subt())
print("División de 2 entre 3 desde clase Operator:",op1.my_div())
print("Multiplicación de 2 x 3 desde clase Operator:",op1.my_mult())
print()

class Power(Operator):
    def __init__(self,num1:int, num2:int) -> None:
        self.num1 = num1
        self.num2 = num2     

    def my_pow(self) -> int:
        acc = self.num1
        for i in range(1, self.num2):
            acc = Operator(self.num1 , acc).my_mult()   
        return acc
    
op2 = Power(2,3)
print("Suma de 2 + 3 desde clase Power:",op2.my_sum())
print("Resta de 2 - 3 desde clase Power:",op2.my_subt())
print("División de 2 entre 3 desde clase Power:",op2.my_div())
print("Multiplicación de 2 x 3 desde clase Power:",op2.my_mult())
print("Cálculo de 2 elevado a 3 desde clase Power:",op2.my_pow())
