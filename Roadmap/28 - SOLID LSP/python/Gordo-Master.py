# 28 - Solid LSP (Liskov Substitution Principle)

# El principio habla de que una clase hija puede reemplazar a una clase padre.
# Es un indicador de que si se esta utilizando bien la herencia. Pues si no se cumple, significa que esta mal implementada la herencia

from abc import ABC, abstractmethod

# Incorrecto

"""
class Ave:
    def volar(self):
        return "Vuelo"
    
class Pinguino(Ave):
    pass

pingu = Pinguino()

print(pingu.volar())
"""

# Correcto

class Ave(ABC):

    @abstractmethod
    def comer(self):
        pass

class Pinguino(Ave):

    def comer(self):
        return "Estoy comiendo pescado"
    
    def nadar(self):
        return "Nadando"
    

class Aguila(Ave):

    def comer(self):
        return "Estoy comiendo raton"
    
    def volar(self):
        return "Volando"



"""
Ejercicio Extra
"""

class Vehicle(ABC):

    def __init__(self, speed = 0):
        self.speed = speed
    
    @abstractmethod
    def accelerate(self, increment):
        self.speed += increment
        print(f"Velocidad: {self.speed} km/h")

    @abstractmethod
    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad: {self.speed} km/h")


class Car(Vehicle):

    def accelerate(self, increment):
        print("El auto esta acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("El auto esta frenando")
        super().brake(decrement)


class Bus(Vehicle):

    def accelerate(self, increment):
        print("El bus esta acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("El bus esta frenando")
        super().brake(decrement)

class Skate(Vehicle):

    def accelerate(self, increment):
        print("La patineta esta acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La patineta esta frenando")
        super().brake(decrement)

def test_vehiculo(vehiculo: Vehicle):
    vehiculo.accelerate(5)
    vehiculo.brake(3)

car = Car(50)
bus = Bus(40)
skate = Skate(10)

test_vehiculo(car)
test_vehiculo(bus)
test_vehiculo(skate)
