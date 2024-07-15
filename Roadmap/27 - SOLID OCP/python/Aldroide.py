"""
    Princpicio Abierto Cerrado (OCP)
    Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
    y crea un ejemplo simple donde se muestre su funcionamiento
    de forma correcta e incorrecta.
"""
# Ejemplo calculo de salario de un empleado
from abc import ABC, abstractmethod
from typing import Any


class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Part_time_employee(Employee):
    def __init__(self, name, base_salary, hr_worked):
        super().__init__(name, base_salary)
        self.hr_worked = hr_worked

    def calculate_salary(self):
        return self.base_salary*self.hr_worked


class Comissioned_employee(Employee):
    def __init__(self, name, base_salary, comission):
        super().__init__(name, base_salary)
        self.comission = comission

    def calculate_salary(self):
        return self.base_salary+self.comission


empleado = Employee("Aldroide", 3000)
empleado_tiempo_parcial = Part_time_employee("Emmanuel", 15, 80)
empleado_con_comision = Comissioned_employee("Samira", 2500, 500)

print(f"Salario de {empleado.name}: {empleado.calculate_salary()}")
print(
    f"Salario de {empleado_tiempo_parcial.name}: {empleado_tiempo_parcial.calculate_salary()}")
print(
    f"Salario de {empleado_con_comision.name}: {empleado_con_comision.calculate_salary()}")


"""
    Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
    Requisitos:
        - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
    Instrucciones:
        1. Implementa las operaciones de suma, resta, multiplicación y división.
        2. Comprueba que el sistema funciona.
        3. Agrega una quinta operación para calcular potencias.
        4. Comprueba que se cumple el OCP.
"""


class Operation(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass


class Add(Operation):
    def calculate(self, a, b):
        return a + b


class Subtraction(Operation):
    def calculate(self, a, b):
        return a - b


class Multiplication(Operation):
    def calculate(self, a, b):
        return a * b


class Division(Operation):
    def calculate(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b


class Power(Operation):
    def calculate(self, a, b):
        return a ** b


class Calculator:
    def __init__(self):
        self.operations = {}

    def add_operation(self, name, operation):
        if not issubclass(type(operation), Operation):
            raise TypeError(
                "La operacion debe ser una estancia de la clase operación")
        self.operations[name] = operation

    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f"Operacion {name} no econtrada")
        return self.operations[name].calculate(a, b)


calculadora = Calculator()
calculadora.add_operation('suma', Add())
calculadora.add_operation('resta', Subtraction())
calculadora.add_operation('multiplicacion', Multiplication())
calculadora.add_operation('division', Division())
calculadora.add_operation('potencia', Power())


print(calculadora.calculate('suma', 5, 3))  # 8
print(calculadora.calculate('resta', 5, 3))  # 2
print(calculadora.calculate('multiplicacion', 5, 3))  # 15
print(calculadora.calculate('division', 5, 3))    # 1.666...
print(calculadora.calculate('potencia', 5, 3))     # 125
