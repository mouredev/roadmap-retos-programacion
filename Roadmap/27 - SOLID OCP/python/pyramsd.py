from abc import ABC, abstractmethod

# USO CORRECTO
class Area:
    @abstractmethod
    def area(self):
        pass

class Rectangulo(Area):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
class Circulo(Area):
    def __init__(self, radius) -> None:
        self.radius = radius    
    def area(self):
        return 3.14159 * (self.radius ** 2)
    

def total_area(shapes):
    return sum(shape.area() for shape in shapes)


shapes = [Rectangulo(3, 4), Circulo(5)]
print(f"Area Total: {total_area(shapes)}")


# USO INCORRECTO
class Area_1():
    def __init__(self):
        pass

    def rectangle(self, side, high):
        return side*high
    
    def circle(self, radius):
        return 3.14159*radius*radius
    

"""
EXTRA
"""
from functools import reduce

class Operacion(ABC):
    @abstractmethod
    def calcular():
        pass

class Sum(Operacion):
    def calcular(self, args: list):
        print(f"El resultado es: {reduce(lambda x, y:  x+ y, args)}\n")

class Resta(Operacion):
    def calcular(self, args: list):
        print(f"El resultado es: {reduce(lambda x, y: x - y, args)}\n")

class Multiplicacion(Operacion):
    def calcular(self, args: list):
        print(f"El resultado es: {reduce(lambda x, y: x * y, args)}\n")

class Division(Operacion):
    def calcular(self, args: list):
        print(f"El restultado es: {reduce(lambda x, y: x / y, args)}\n")

class Potencia(Operacion):
    def calcular(self, args: list):
        if len(args) > 2:
            raise ValueError("Pasar solo dos argumentos. base y exponente")
        else:
            print(f"El resultado es: {pow(args[0], args[1])}\n")

class Calculator():
    def __init__(self) -> None:
        self.operaciones = {
            "suma": Sum(),
            "resta": Resta(),
            "multiplicacion": Multiplicacion(),
            "division": Division()
        }

    def add_operation(self, nombre: str, operacion: Operacion):
        self.operaciones[nombre] = operacion

    def execute(self, nombre):
        if nombre not in self.operaciones:
            raise ValueError("La operación no está contemplada en esta calculadora")
        else:
            num_operators = list()
            operators = input("Operandos separados por coma: ")
            operators = operators.strip()
            list_operators = operators.split(",")
            try:
                for element in list_operators:
                    if element.__contains__("."):
                        num_operators.append(float(element))
                    else:
                        num_operators.append(int(element))
            except ValueError:
                print("Los valores introducidos han de ser números")
            else:
                self.operaciones[nombre].calcular(num_operators)


def calculator():
    my_calculator = Calculator()
    my_calculator.add_operation(nombre="potencia", operacion=Potencia()) #añado la potencia con Power()
    options = {
        "S": "suma",
        "R": "resta",
        "M": "multiplicacion",
        "D": "division",
        "P": "potencia"
    }
    print(" --- Calculadora --- ")
    while True:
        option = input("Elige una opción por favor:\n- Suma (S)\n- Resta (R)\n- Multiplicación (M)\n- División (D)\n- Potencia (P)\n- Salir (O)\n>>> ").upper()
        if option == "O":
            print("Programa cerrado")
            break
        elif option not in options:
            print("La opción no es válida\n")
        else:
            my_calculator.execute(options[option])

calculator()
