"""
Ejercicio
"""


class Form:
    
    def draw(self):
        pass
        
class Cuadrado(Form):
    
    def draw(self):
        print("Dibujar un cuadrado")
        
class Circulo(Form):
    
    def draw(self):
        print("Dibujar un círculo")


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
 */
"""
from abc import ABC, abstractmethod
    
class Operacion(ABC):
    
    @abstractmethod
    def operar(self, a, b):
        pass
    
class Suma(Operacion):
    
    def operar(self, a, b):
        return a + b
    
class Resta(Operacion):
    
    def operar(self, a ,b):
        return a - b
class Multiplicacion(Operacion):
    
    def operar(self, a ,b):
        return a * b
    
class Division(Operacion):
    
    def operar(self, a ,b):
        return a / b

class Potencia(Operacion):
    
    def operar(self, a ,b):
        return a ** b
    
class Calculadora:
    
    def __init__(self) -> None:
        self.operaciones = {}
        
    def añadir_operaciones(self, nombre, operacion):
        self.operaciones[nombre] = operacion
        
    def calcular(self, nombre, a, b):
        if nombre not in self.operaciones:
            raise ValueError(f"La operación {nombre} no esta soportada")
        return self.operaciones[nombre].operar(a, b)
    
calculadora = Calculadora()

calculadora.añadir_operaciones("sumar", Suma())
calculadora.añadir_operaciones("restar", Resta())
calculadora.añadir_operaciones("multiplicar", Multiplicacion())
calculadora.añadir_operaciones("dividir", Division())
calculadora.añadir_operaciones("potencia", Potencia())

print(calculadora.calcular("sumar", 10, 5))
print(calculadora.calcular("restar", 10, 5))
print(calculadora.calcular("multiplicar", 10, 5))
print(calculadora.calcular("dividir", 10, 5))
print(calculadora.calcular("potencia", 10, 5))
