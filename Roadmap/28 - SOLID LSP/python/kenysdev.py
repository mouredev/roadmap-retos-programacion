# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -------------------------------------------------
# * SOLID: PRINCIPIO DE SUSTITUCIÓN DE LISKOV (LSP)
# -------------------------------------------------

# mas info:
# https://blog.nonstopio.com/liskov-substitution-principle-in-python-b68d62924f7b

# _________________
from abc import ABC, abstractmethod

# Clase base, con contrato:
class Animal(ABC): 
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def make_sound(self) -> str:
        pass

# _________________
# clases derivadas:
class Dog(Animal):
    def make_sound(self) -> str:
        return (f"{self.name} hace Woof")

class Cat(Animal):
    def make_sound(self) -> str:
        return (f"{self.name} hace Meow")

# _________________
dog = Dog("Max")
print(dog.make_sound())

cat = Cat("Milo")
print(cat.make_sound())


"""
* EJERCICIO 
* Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
* cumplir el LSP.
* Instrucciones:
* 1. Crea la clase Vehículo.
* 2. Añade tres subclases de Vehículo.
* 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
* 4. Desarrolla un código que compruebe que se cumple el LSP.
"""

# _________________
# Clase base abstracta
class Vehicle(ABC):
    def __init__(self, brand: str, model: str):
        self._brand = brand
        self._model = model

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @abstractmethod
    def accelerate(self):
        pass
    
    @abstractmethod
    def brake(self):
        pass

# _________________
# clases derivadas:
class Car(Vehicle):
    def accelerate(self) -> str:
        propertys: str = f"{self.brand} - {self.model}"
        return (f"Acelerando auto: {propertys}")

    def brake(self) -> str:
        propertys: str = f"{self.brand} - {self.model}"
        return (f"Frenando auto:  {propertys}")

class Motorcycle(Vehicle):
    def accelerate(self) -> str:
        propertys: str = f"{self.brand} - {self.model}"
        return (f"Acelerando Motocicleta: {propertys}")

    def brake(self) -> str:
        propertys: str = f"{self.brand} - {self.model}"
        return (f"Frenando Motocicleta: {propertys}")
class Truck(Vehicle):
    def accelerate(self) -> str:
        propertys: str = f"{self.brand} - {self.model}"
        return (f"Acelerando Camión: {propertys}")

    def brake(self) -> str:
        propertys: str = f"{self.brand} - {self.model}"
        return (f"Frenando Camión: {propertys}")

# _________________
# Verificar cumplimiento de LSP
def test_sub_class(sub_class: Vehicle):
    print("\nPropiedades:")
    print(f"{sub_class.brand} - {sub_class.model}")

    print("\nMetodos:")
    print(sub_class.accelerate())
    print(sub_class.brake())

# _________________

car = Car("Honda", "Civic")
test_sub_class(car)

motorcycle = Motorcycle("Kawasaki", "Ninja")
test_sub_class(motorcycle)

truck = Truck("Ford", "Raptor")
test_sub_class(truck)

# end
