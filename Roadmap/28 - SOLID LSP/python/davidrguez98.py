""" /*
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
 */ """

#EJERCICIO

""" 
Incorrecta
"""

class Bird:
    def fly(self):
        return "Flying"
    
class Chicken(Bird):
    def fly(self):
        raise Exception("Los pollos no vuelan.")


""" 
Correcta 
"""

class Bird:
    def move(self):
        return "Moving"
    
class Chicken(Bird):
    def move(self):
        return "walk"
    
bird = Bird()
print(bird.move())
chicken = Chicken()
print(chicken.move())

bird = Chicken()
print(bird.move())
chicken = Bird()
print(chicken.move())

#DIFICULTAD EXTRA

class Vehicle:

    def accelerate(self):
        return "Gas"
    
    def brake(self):
        return "Break"

class Motorbike(Vehicle):

    def accelerate(self):
        return "Motorbike gas"
    
    def brake(self):
        return "Motorbike break"

class Car(Vehicle):
    
    def accelerate(self):
        return "Car gas"
    
    def brake(self):
        return "Car break"

class Truck(Vehicle):

    def accelerate(self):
        return "Truck gas"
    
    def brake(self):
        return "Truck break"
    
vehicle = Vehicle()
print(vehicle.accelerate())
print(vehicle.brake())
motorbike = Motorbike()
print(motorbike.accelerate())
print(motorbike.brake())
car = Car()
print(car.accelerate())
print(car.brake())
truck = Truck()
print(truck.accelerate())
print(truck.brake())

vehicle = Motorbike()
print(vehicle.accelerate())
print(vehicle.brake())
motorbike = Car()
print(motorbike.accelerate())
print(motorbike.brake())
car = Truck()
print(car.accelerate())
print(car.brake())
truck = Vehicle()
print(truck.accelerate())
print(truck.brake())