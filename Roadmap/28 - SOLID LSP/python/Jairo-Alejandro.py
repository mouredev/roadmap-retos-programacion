"""
Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)

Si se tiene una clase base y una subclase que hereda la clase base , se debe poder usar la subclase sin afectar el programa 
"""
# Ejemplo incorrecto
class Animal():

    def fly(self):
        pass

class Bird(Animal):

    def fly(self):
        print("the bird is fly")

class Penguin(Animal):

    def fly(self):
        raise Exception("the penguin can't fly")

def fly_animal(animal: Animal):
    animal.fly()

my_bird = Bird()
my_penguin = Penguin()

#fly_animal(my_bird)
#fly_animal(my_penguin)

# Ejemplo correcto 

class Animal():
    def move(self):
        pass

class can_fly():
    def fly(self):
        pass

class Bird(Animal, can_fly):
    def move(self):
        print("The Bird is moving")

    def fly(self):
        print("The Bird is fly")

class Penguin(Animal):
    def move(self):
        print("The penguin is moving")

def move_animal(animal: Animal):
    animal.move()

def fly_animal(animal: can_fly):
    animal.fly()

my_bird = Bird()
my_penguin = Penguin()

move_animal(my_bird)
move_animal(my_penguin)

fly_animal(my_bird)

# Dificultad extra 

class Vehicle():

    def accelerate(self):
        pass

    def brake(self):
        pass

class Car(Vehicle):

    def accelerate(self):
        print("the car is accelerate")

    def brake(self):
        print("the car is braking")

class Bicycle(Vehicle):

    def accelerate(self):
        print("the Bicycle is accelerate")
    
    def brake(self):
        print("the Bicycle is braking")

class Motorcycle(Vehicle):

    def accelerate(self):
        print("the Motorcycle is accelerate")
    
    def brake(self):
        print("the Motorcycle is braking")

def test_vehicle(vehicle: Vehicle):
    vehicle.accelerate()
    vehicle.brake()

my_car = Car()
my_bicycle = Bicycle()
my_motorcycle = Motorcycle()

test_vehicle(my_car)
test_vehicle(my_bicycle)
test_vehicle(my_motorcycle)

