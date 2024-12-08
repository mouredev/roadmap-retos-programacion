"""
/*
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
"""
#Incorrecta

class Vehicule:
    def __init__(self, car, motobike):
        self.car = car
        self. motobike = motobike
    
    def draw_vehicule(self, vehicule):
        print(f"Se prepara a pintar un {vehicule}")


class Car:
    def draw_vehicule(self):
        print(f"Se esta dibujando un auto")

my_vehicule = Vehicule("mustang", "Yamaha")
my_vehicule.draw_vehicule("mustang")
my_vehicule.draw_vehicule("Yamaha")

#Correcta

class Vehicule:
    def __init__(self) -> None:
        self.vehicule

    def draw_vehicule(self, vehicule):
        print(f"Se esta dibujando {vehicule}")

class Car(Vehicule):
    def draw_vehicule(self):
        print(f"Se esta dibujando un auto")

#Extra

from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self, num1, num2):
        pass

class Adition(Operation):
    def execute(self, num1, num2):
        return num1 + num2

class Substration(Operation):
    def execute(self, num1, num2):
        return num1 - num2
    
class Multiplication(Operation):
    def execute(self, num1, num2):
        return num1 * num2
    
class Division(Operation):
    def execute(self, num1, num2):
        try:
            return num1 / num2
            
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
        
    
class Power(Operation):
    def execute(self, num1, num2):
        return num1 ** num2

class Calculator:
    def __init__(self) -> None:
        self.operations = {"suma": Adition(),
                           "resta": Substration(),
                           "multiplicacion": Multiplication(),
                           "division": Division(),
                           "potencia": Power()
                           }
    
    def add_operation(self, name, operation):
        self.operations[name] = operation
    
    def calculate(self, name, num1, num2):
        if name not in self.operations:
            raise ValueError("operacion no soportada")
        else:
            return self.operations[name].execute(num1, num2)
        
calculator = Calculator()
calculator.add_operation("addition", Adition())
calculator.add_operation("substration", Substration())
calculator.add_operation("multiplication", Multiplication())
calculator.add_operation("division", Division())
calculator.add_operation("power", Power())

print(calculator.calculate("suma", 20, 15))
print(calculator.calculate("resta", 10, 3))
print(calculator.calculate("multiplicacion", 4, 4))
print(calculator.calculate("division", 30, 0))
print(calculator.calculate("potencia", 2, 5))
