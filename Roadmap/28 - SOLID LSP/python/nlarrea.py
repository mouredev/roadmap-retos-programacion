"""
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
"""

# Incorrect


class Bird:
    def fly(self):
        return "Flying"


class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly.")


# bird = Bird()
# print(bird.move())
# ostrich = Ostrich()
# print(ostrich.move())  # throws error


# Correct


class Bird:
    def move(self):
        return "Flying"


class Ostrich(Bird):
    def move(self):
        return "Walking"


bird = Bird()
print(bird.move())
ostrich = Ostrich()
print(ostrich.move())

bird = Ostrich()
print(bird.move())
ostrich = Bird()
print(ostrich.move())


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
"""


class Vehicle:
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, increment: int):
        self.speed += increment
        print(f"Speed: {self.speed} km/h")

    def brake(self, decrement: int):
        self.speed -= decrement

        if self.speed <= 0:
            self.speed = 0

        print(f"Speed: {self.speed} km/h")


class Motorbike(Vehicle):
    def accelerate(self, increment):
        print("Motorbike is accelerating...")
        super().accelerate(increment)

    def brake(self, decrement):
        print("Motorbike is braking...")
        super().brake(decrement)


class Car(Vehicle):
    def accelerate(self, increment):
        print("Car is accelerating...")
        super().accelerate(increment)

    def brake(self, decrement):
        print("Car is braking...")
        super().brake(decrement)


class Bicycle(Vehicle):
    def accelerate(self, increment):
        print("Bicycle is accelerating...")
        super().accelerate(increment)

    def brake(self, decrement):
        print("Bicycle is braking...")
        super().brake(decrement)


def test_vehicle(vehicle):
    vehicle.accelerate(10)
    vehicle.brake(2)
    print()


motorbike = Motorbike()
car = Car()
bicycle = Bicycle()

test_vehicle(motorbike)
test_vehicle(car)
test_vehicle(bicycle)
