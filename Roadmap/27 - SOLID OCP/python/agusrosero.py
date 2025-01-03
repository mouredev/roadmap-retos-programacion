"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
"""


class Animal:
    def __init__(self, name):
        self.name = name


class Sonido(Animal):
    def sonido(self):
        print(f"{self.name} hace ruidos!")


class Comer(Animal):
    def comer(self):
        print(f"{self.name} come su comida...")


class Saludar(Animal):
    def saludar(self):
        print(f"{self.name} saluda!!!")


animal1 = Animal("Leon")
print(animal1.name)
sonido1 = Sonido("Leon")
sonido1.sonido()
comer1 = Comer("Elefante")
comer1.comer()
saludar1 = Saludar("Tigre")
saludar1.saludar()

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
