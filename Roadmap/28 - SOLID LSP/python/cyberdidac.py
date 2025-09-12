class Vehicle:
    model: str
    brand: str

    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def acelerate(self):
        pass

    def brake(self):
        pass


class Car(Vehicle):
    wheels: int
    doors: int

    def __init__(self, doors, brand, model):
        super().__init__(model, brand)
        self.doors = doors
        self.wheels = 4

    def acelerate(self):
        print("Acelerando 20 km/h")

    def brake(self):
        print("Frenando 10 km/h")


class Motorbike(Vehicle):
    wheels: int

    def __init__(self, model, brand):
        super().__init__(model, brand)
        self.wheels = 2

    def acelerate(self):
        print("Acelerando 30 km/h")

    def brake(self):
        print("Frenando 40 km/h")


class ElectricScooter(Vehicle):
    wheels: int

    def __init__(self, model, brand):
        super().__init__(model, brand)
        self.wheels = 2

    def acelerate(self):
        print("Acelerando 5 km/h")

    def brake(self):
        print("Frenando 10 km/h")


def main():
    coche = Car(doors=5, brand="ford", model="fiesta")
    motorbike = Motorbike(brand="honda", model="2001")
    scooter = ElectricScooter(brand="Xiaomi", model="2020")

    coche.acelerate()
    scooter.brake()
    motorbike.acelerate()

    print(f"El {coche.brand} {coche.model} tiene {coche.doors} puertas")


if __name__ == '__main__':
    main()
