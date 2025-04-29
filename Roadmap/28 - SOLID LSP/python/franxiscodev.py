"""
SOLID
LSP: principio de sustitución de Liskov
    
"""
# NO solid
# incorrecto


class Bird:
    def fly(self):
        return "El ave vuela"


class Penguin(Bird):
    def fly(self):
        raise Exception("Los pingüinos no pueden volar")

# bird = Bird()
# penguin = Penguin()
# print(bird.fly()) # Output: El ave vuela
# print(penguin.fly()) # Output: Exception: Los pingüinos no pueden volar
# al ser una Excepción no se puede usar el principio de sustitución de Liskov

# SOLID
# correcto


class Bird:
    def move(self):
        return "El ave se mueve"


class Penguin(Bird):
    def move(self):
        return "El pingüino nada"


bird = Bird()
penguin = Penguin()
print(bird.move())  # Output: El ave se mueve
print(penguin.move())  # Output: El pingüino nada
# al ser un método diferente no se rompe el principio de sustitución de Liskov
# se puede usar el principio de sustitución de Liskov

# Extra


class Vehicle:
    def __init__(self, speed=0) -> None:
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        if self.speed > 120:
            self.speed = 120
        return self.speed

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        return self.speed


class Car(Vehicle):
    def accelerate(self, amount):
        print(f"Acelerando el coche a {amount} km/h ")
        super().accelerate(amount)

    def brake(self, amount):
        print(f"Frenando el coche a {amount} km/h ")
        super().brake(amount)


class Bicycle(Vehicle):
    def accelerate(self, amount):
        print(f"Acelerando la bicicleta a {amount} km/h ")
        super().accelerate(amount / 2)  # Bicicleta acelera más lentamente

    def brake(self, amount):
        print(f"Frenando la bicicleta a {amount} km/h ")
        super().brake(amount / 2)  # Bicicleta frena más lentamente


class Motorcycle(Vehicle):
    def accelerate(self, amount):
        print(f"Acelerando la motocicleta a {amount} km/h ")
        super().accelerate(amount * 2)  # Motocicleta acelera más rápido

    def brake(self, amount):
        print(f"Frenando la motocicleta a {amount} km/h ")
        super().brake(amount * 2)  # Motocicleta frena más rápido


def test_vehicle(vehicle: Vehicle, acc_amount: int, des_amount: int = 0):
    vehicle.accelerate(acc_amount)
    vehicle.brake(des_amount)
    print(f"Velocidad final: {vehicle.speed} km/h")


coche = Car()
bici = Bicycle()
moto = Motorcycle()

test_vehicle(coche, 135, 5)
test_vehicle(bici, 5, 2)
test_vehicle(moto, 50, 10)
