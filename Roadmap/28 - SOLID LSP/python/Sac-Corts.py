# Correcto
class Bird:
    def fly(self):
        return "Bird is flying"
    
class Sparrow(Bird):
    def fly(self):
        return "Sparrow is flying"
    
class Eagle(Bird):
    def fly(self):
        return "Eagle is flying"

def make_bird_fly(bird: Bird):
    print(bird.fly())

sparrow = Sparrow()
eagle = Eagle()

make_bird_fly(sparrow)
make_bird_fly(eagle)

# Incorrecto
class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly")

penguin = Penguin()
try:
    make_bird_fly(penguin)
except Exception as e:
    print(e) 


### Ejercicio Extra ###
class Vehicle:
    def accelerate(self):
        raise NotImplementedError("You must implement the accelerate method")

    def brake(self):
        raise NotImplementedError("You must implement the brake method")

class Car(Vehicle):
    def accelerate(self):
        return "Car is accelerating"
    
    def brake(self):
        return "Car is braking"

class Motorcycle(Vehicle):
    def accelerate(self):
        return "Motorcycle is accelerating"
    

    def brake(self):
        return "Motorcycle is braking"
    
class Bike(Vehicle):
    def accelerate(self):
        return "Bike is accelerating"
    
    def brake(self):
        return "Bike is braking"


def test_vehicle(vehicle: Vehicle):
    print(vehicle.accelerate())
    print(vehicle.brake())

car = Car()
motorcycle = Motorcycle()
bike = Bike()

test_vehicle(car)
test_vehicle(motorcycle)
test_vehicle(bike)