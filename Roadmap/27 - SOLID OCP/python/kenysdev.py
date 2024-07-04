# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -------------------------------------------------
# * SOLID: PRINCIPIO ABIERTO-CERRADO (OCP)
# -------------------------------------------------
# - Una entidad de software debería estar abierta a extensión pero cerrada a 
#   modificación, esto significa que debemos poder extender el comportamiento de 
#   una clase sin necesidad de modificar su código fuente original.

"""
* EJERCICIO #1:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# ABC (Abstract Base Class): 
# Para establecer contratos entre clases base y sus 'subclases'.
# https://www.geeksforgeeks.org/abstract-classes-in-python/
from abc import ABC, abstractmethod

# Clase base
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @abstractmethod
    def apply_discount(self):
        pass

    def final_price(self):
        return self.price - self.apply_discount()

# Clases concretas (Nuevas extenciones)
class ElectronicsProduct(Product):
    def apply_discount(self):
        return self.price * 0.05 # Descuento del 5%

class ClothingProduct(Product):
    def apply_discount(self):
        if self.price > 50:
            return 10 
        else:
            return 0

def process_product(product):
    print(f"Producto: {product.name}, Precio final: {product.final_price()}")

laptop = ElectronicsProduct("Laptop", 700)
pants = ClothingProduct("Pants", 55)

process_product(laptop) # Output: Producto: Laptop, Precio final: 665.0
process_product(pants)  # Output: Producto: Pants, Precio final: 45

"""
* EJERCICIO #2:
* Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
* Requisitos:
* - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
* Instrucciones:
* 1. Implementa las operaciones de suma, resta, multiplicación y división.
* 2. Comprueba que el sistema funciona.
* 3. Agrega una quinta operación para calcular potencias.
* 4. Comprueba que se cumple el OCP.
"""

# Clase base
class Calculator(ABC):
    def __init__(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.a = a
            self.b = b
        else:
            self.a = None
            self.b = None
            print("Operación invalida.")
            
    @abstractmethod
    def math_operation(self):
        pass
    
    def print_result(self):
        if self.a is not None and self.b is not None:
            print(f"Es: {self.math_operation()}")
        else:
            print("Campos incorrectos.")

# Clases concretas
class Sum(Calculator):
    def math_operation(self):
        print(f"\nSuma de {self.a} + {self.b}:")
        return self.a + self.b

class Subtraction(Calculator):
    def math_operation(self):
        print(f"\nResta de {self.a} - {self.b}:")
        return self.a - self.b

class Multiplication(Calculator):
    def math_operation(self):
        print(f"\nMultiplicación de {self.a} * {self.b}:")
        return self.a * self.b

class Division(Calculator):
    def math_operation(self):
        print(f"\nDivisión de {self.a} / {self.b}:")
        return self.a / self.b

class Pow(Calculator):
    def math_operation(self):
        print(f"\nPotencia de {self.a} ^ {self.b}:")
        return self.a ** self.b

sum_ = Sum(2, 2)
sum_.print_result()

subtraction = Subtraction(2, 2)
subtraction.print_result()

multip = Multiplication(2, 2)
multip.print_result()

div = Division(2, 2)
div.print_result()

pow_ = Pow(2, 2)
pow_.print_result()

