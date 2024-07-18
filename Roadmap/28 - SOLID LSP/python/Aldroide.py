"""
    Explora el concepto de Principio de Sustitución de Liskov (Liskov Substitution Principle, LSP)
    crea un ejemplo siemple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""


class Bird:
    def volar(self):
        raise NotImplementedError("Este metodo permite al ave volar")


class Duck(Bird):
    def volar(self):
        print("El pato sabe volar")


class Penguin(Bird):
    def volar(self):
        print("El pinguino no sabe volar")


def hacer_volar(ave: Bird):
    ave.volar()


pato = Duck()
pinguino = Penguin()
hacer_volar(pato)
hacer_volar(pinguino)

"""
    Extra:
    Crear una jerarquia de vehiculos, Todos deben llevar el poder 
    acelerar y frenar y cumplir el LSP.
    Instrucciónes:
    1.- Crea la clase vehículo
    2.- Añade tres subclases de vehículo
    3.- Implementa operacion acelerar y frenar como corresponda
    4.- Desarrolla un codigo que compruebe que se cumple el LSP
"""


class Vehicle():
    def __init__(self, speed=0):
        self.speed = speed

    def speed_up(self, increment):
        self.speed += increment
        print(f"Velocidad: {self.speed} km\h")

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad: {self.speed} km\h")


class Truck(Vehicle):
    def speed_up(self, increment):
        print("El camion esta acelerando")
        super().speed_up(increment)

    def brake(self, decrement):
        print("El camion esta frenando")
        super().brake(decrement)


class Motorcycle(Vehicle):
    def speed_up(self, increment):
        print("La motocicleta esta acelerando")
        super().speed_up(increment)

    def brake(self, decrement):
        print("La motocicleta esta frenando")
        super().brake(decrement)


class Airplane(Vehicle):
    def speed_up(self, increment):
        print("El avion esta acelerando")
        super().speed_up(increment)

    def brake(self, decrement):
        print("El avion esta frenando")
        super().brake(decrement)


def test_vehicle(vehicle):
    vehicle.speed_up(2)
    vehicle.brake(1)


camion = Truck()
moto = Motorcycle()
avion = Airplane()

test_vehicle(camion)
test_vehicle(moto)
test_vehicle(avion)
