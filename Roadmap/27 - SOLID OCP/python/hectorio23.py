# Autor: Héctor Adán
# GitHub: https://github.com/hectorio23

from abc import ABC, abstractmethod
import math

"""
EJERCICIO:
Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
y crea un ejemplo simple donde se muestre su funcionamiento
de forma correcta e incorrecta.

DIFICULTAD EXTRA:
Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
Requisitos:
- Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
Instrucciones:
1. Implementa las operaciones de suma, resta, multiplicación y división.
2. Comprueba que el sistema funciona.
3. Agrega una quinta operación para calcular potencias.
4. Comprueba que se cumple el OCP.
"""

class Operacion(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass

class Suma(Operacion):
    def calcular(self, a, b):
        return a + b

class Resta(Operacion):
    def calcular(self, a, b):
        return a - b

class Multiplicacion(Operacion):
    def calcular(self, a, b):
        return a * b

class Division(Operacion):
    def calcular(self, a, b):
        if b == 0:
            raise ValueError("División por cero")
        return a / b

class Potencia(Operacion):
    def calcular(self, a, b):
        return math.pow(a, b)

class Calculadora:
    def __init__(self):
        self.operaciones = {}

    def agregar_operacion(self, nombre, operacion):
        self.operaciones[nombre] = operacion

    def calcular(self, nombre, a, b):
        if nombre in self.operaciones:
            return self.operaciones[nombre].calcular(a, b)
        else:
            raise ValueError("Operación no soportada")


if __name__ == "__main__":
    calc = Calculadora()
    calc.agregar_operacion('+', Suma())
    calc.agregar_operacion('-', Resta())
    calc.agregar_operacion('*', Multiplicacion())
    calc.agregar_operacion('/', Division())
    calc.agregar_operacion('^', Potencia())

    print("[+] - Suma:", calc.calcular('+', 5, 3))
    print("[+] - Resta:", calc.calcular('-', 5, 3))
    print("[+] - Multiplicación:", calc.calcular('*', 5, 3))
    print("[+] - División:", calc.calcular('/', 5, 3))
    print("[+] - Potencia:", calc.calcular('^', 5, 3))
