"""
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""
from abc import ABC, abstractmethod
from math import pi

#EJEMPLO SIN OCP
class Area_1():
    def __init__(self):
        pass

    def rectangle(self,side:int|float,high:int|float):
        return side*high
    
    def circle(self,radius:int|float):
        return pi*radius*radius
    
rectangle_no_ocp = Area_1()
print(f"El área del Rectángulo NO OCP es: {rectangle_no_ocp.rectangle(side=7,high=2)}")
circle_no_ocp = Area_1()
print(f"El área del Circulo NO OCP es: {circle_no_ocp.circle(radius=4):.2f}")
print("\n")

#EJEMPLO CON OCP

class Area(ABC):
    @abstractmethod
    def area():
        pass

class Rectangle(Area):
    def area(self,side:int|float,high:int|float):
        return side*high

class Circle(Area):
    def area(self,radius:int|float):
        return pi*radius*radius

rectangle_ocp = Rectangle()
print(f"El área del Rectángulo OCP es: {rectangle_ocp.area(side=7,high=2)}")
circle_ocp = Circle()
print(f"El área del Círculo OCP es: {circle_ocp.area(radius=4):.2f}")
print("\n")

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

from functools import reduce

class Operation(ABC): #Operation pasa a ser una interfaz con un método abstracto
    @abstractmethod   #es decir la clase no puede ser instanciada ni el método podrá ser utilizado
    def calculate():
        pass

class Sum(Operation):
    def calculate(self,args:list):
        print(f"El resultado es: {reduce(lambda x,y:x+y,args)}\n")
    
class Substract(Operation):
    def calculate(self,args:list):
        print(f"El resultado es: {reduce(lambda x,y:x-y,args)}\n")

class Multiply(Operation):
    def calculate(self,args:list):
        print(f"El resultado es: {reduce(lambda x,y:x*y,args)}\n")

class Divide(Operation):
    def calculate(self,args:list):
        print(f"El restultado es: {reduce(lambda x,y:x/y,args)}\n")

class Power(Operation):
    def calculate(self,args:list):
        if len(args)>2:
            raise ValueError("Para poder calcular una potencia has de pasar solo dos operandos como base y exponente")
        else:
            print(f"El resultado es: {pow(args[0],args[1])}\n")

class Calculator():
    def __init__(self) -> None:
        self.operations = {
            "sum":Sum(),
            "substract":Substract(),
            "multiply":Multiply(),
            "divide":Divide()
        }

    def add_operation(self,name:str,operation:Operation):
        self.operations[name] = operation

    def execute(self,name):
        if name not in self.operations:
            raise ValueError("La operación no está contemplada en esta calculadora")
        else:
            num_operators = list()
            operators = input("Dime los operandos separados por coma: ")
            operators = operators.strip()
            list_operators = operators.split(",")
            try:
                for element in list_operators:
                    if element.__contains__("."):
                        num_operators.append(float(element))
                    else:
                        num_operators.append(int(element))
            except ValueError:
                print("Los valores introducidos han de ser números...")
            else:
                self.operations[name].calculate(num_operators)

def calculator():
    my_calculator = Calculator()
    my_calculator.add_operation(name="power",operation=Power()) #añado la potencia con Power()
    options = {
        "S":"sum",
        "R":"substract",
        "M":"multiply",
        "D":"divide",
        "P":"power"
    }
    print(" --- TE DOY LA BIENVENIDA AL SISTEMA DE CALCULADORA --- ")
    while True:
        option = input("Elige una opción por favor:\n- Suma (S)\n- Resta (R)\n- Multiplicación (M)\n- División (D)\n- Potencia (P)\n- Salir (O)\n-----> ").upper()
        if option == "O":
            print("Gracias por usar el sistema de calculadora. ¡Hasta pronto!")
            break
        elif option not in options:
            print("La opción elegida no es válida...\n")
        else:
            my_calculator.execute(options[option])

calculator()

#en si la función calculator no cumpliría con el OCP, si añadimos otra operación
#hemos de modificar el menú y la variable options
#no obstante todas las clases que incluye el programa si lo cumplen
