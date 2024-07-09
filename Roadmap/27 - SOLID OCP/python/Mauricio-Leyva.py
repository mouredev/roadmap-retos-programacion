"""
Mauricio Leyva


Calculadora interactiva que cumple con el Principio Abierto-Cerrado (OCP)

Descripción:
Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.

Requisitos:
- Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.

Instrucciones:
1. Implementa las operaciones de suma, resta, multiplicación y división.
2. Comprueba que el sistema funciona.
3. Agrega una quinta operación para calcular potencias.
4. Comprueba que se cumple el OCP.

Este código implementa una calculadora interactiva que cumple con todos estos requisitos,
permitiendo fácilmente la adición de nuevas operaciones sin modificar el código existente.
"""


from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

    @abstractmethod
    def get_symbol(self):
        pass

class Addition(Operation):
    def execute(self, a, b):
        return a + b
    
    def get_symbol(self):
        return "+"

class Subtraction(Operation):
    def execute(self, a, b):
        return a - b
    
    def get_symbol(self):
        return "-"

class Multiplication(Operation):
    def execute(self, a, b):
        return a * b
    
    def get_symbol(self):
        return "*"

class Division(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    
    def get_symbol(self):
        return "/"

class Power(Operation):
    def execute(self, a, b):
        return a ** b
    
    def get_symbol(self):
        return "^"

class Calculator:
    def __init__(self):
        self.operations = {}

    def register_operation(self, operation):
        self.operations[operation.get_symbol()] = operation

    def get_available_operations(self):
        return list(self.operations.keys())

    def calculate(self, operation_symbol, a, b):
        if operation_symbol not in self.operations:
            raise ValueError(f"Operación '{operation_symbol}' no soportada")
        return self.operations[operation_symbol].execute(a, b)

def get_user_input():
    while True:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            return a, b
        except ValueError:
            print("Por favor, ingrese números válidos.")

def main():
    calc = Calculator()
    
    # Registro de operaciones
    calc.register_operation(Addition())
    calc.register_operation(Subtraction())
    calc.register_operation(Multiplication())
    calc.register_operation(Division())
    calc.register_operation(Power())

    while True:
        print("\nOperaciones disponibles:")
        for op in calc.get_available_operations():
            print(f"  {op}")
        
        operation = input("Elija una operación (o 'q' para salir): ")
        
        if operation.lower() == 'q':
            break
        
        if operation not in calc.get_available_operations():
            print("Operación no válida. Intente de nuevo.")
            continue
        
        a, b = get_user_input()
        
        try:
            result = calc.calculate(operation, a, b)
            print(f"Resultado: {a} {operation} {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()