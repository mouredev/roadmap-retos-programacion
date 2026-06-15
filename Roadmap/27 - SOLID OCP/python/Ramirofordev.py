'''
Ejercicio: 
Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta.
'''

#! Forma incorrecta.
def sum_two_values(a, b):

    def sum_two_values_pow_two():
        return pow(sum(a, b), 2)
    
    return sum(a , b)

#! Forma correcta.
def pow_two(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return wrapper

@pow_two
def sum_two_values(a , b):
    return a + b

print(sum_two_values(5, 4))

'''
Dificultad extra:
Desarrolla una calculadora que necesita realizar diversas operaciones matematicas.

Requisitos: 
    * Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.

Instrucciones: 
    1. Implementa las operaciones de suma, resta, multplicacion y division.
    2. Comprueba que el sistema funciona.
    3. Agrega una quinta operacion para calcular las potencias.
    4. Comprueba que se cumple el OCP.
'''

class Caluladora:
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2

class Suma(Caluladora):
    def sumar(self): 
        return self.n1 + self.n2
    
class Resta(Caluladora):
    def restar(self):
        return self.n1 - self.n2
    
class Multiplicacion(Caluladora):
    def mult(self):
        return self.n1 * self.n2
    
class Division(Caluladora):
    def div(self):
        return self.n1 / self.n2
    
class Potencias(Caluladora):
    def pot(self):
        return self.n1 ** self.n2
    
numeros = Caluladora(10, 5)
print(Suma.sumar(numeros))
print(Resta.restar(numeros))
print(Multiplicacion.mult(numeros))
print(Division.div(numeros))
print(Potencias.pot(numeros))