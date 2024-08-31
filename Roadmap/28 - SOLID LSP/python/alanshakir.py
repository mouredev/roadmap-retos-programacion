"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */
"""
#Incorrecto

class Animal:
    def walk():
        print("caminar")
    
    def jump():
        print("saltar")

class Elephant(Animal):
    def jump():
        raise Exception("los elefantes no pueden saltar")

#Correcto
class Animal:
    def walk():
        print("caminar")

class AnimalLiviano(Animal):    
    def jump():
        print("saltar")

class Dog(AnimalLiviano):
    pass

class Elephant(Animal):
    pass

#Extra

class Vehicle:

    def __init__(self, speed = 0):
        self.speed = speed
    
    def accelerate(self, increment):
        self.speed += increment
        print(f"acelera: {self.speed}")
    
    def brake(self, decrement):
        self.speed += decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"frena: {self.speed}")


class Automobile(Vehicle):
    def accelerate(self, increment):
        print("El automovil esta acelerando")
        super().accelerate(increment)
    
    def brake(self, decrement):
        print("El automovil esta frenando")
        super().brake(decrement)

class Motorcycle(Vehicle):
    def accelerate(self, increment):
        print("La motocicleta esta acelerando")
        super().accelerate(increment)
    
    def brake(self, decrement):
        print("La motocicleta esta frenando")
        super().brake(decrement)

class Truck(Vehicle):
    def accelerate(self, increment):
        print("El Camion esta acelerando")
        super().accelerate(increment)
    
    def brake(self, decrement):
        print("El Camion esta frenando")
        super().brake(decrement)

def drive(vehicle, accelerated, braked):
    vehicle.accelerate(accelerated)
    vehicle.brake(braked)


auto = Automobile()
moto = Motorcycle()
camion = Truck()

drive(auto, 3, 1)
drive(moto, 5, 4)
drive(camion, 8, 6)
