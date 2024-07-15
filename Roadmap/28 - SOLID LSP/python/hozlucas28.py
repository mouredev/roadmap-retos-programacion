# pylint: disable=pointless-string-statement,missing-class-docstring,missing-function-docstring,missing-module-docstring,too-few-public-methods,broad-exception-raised,line-too-long

from abc import ABCMeta, abstractmethod

"""
    Liskov Substitution Principle (LCP)...
"""

print("Liskov Substitution Principle (LCP)...")

print("\nBad implementation of Liskov Substitution Principle (LCP)...")


class AbcBadVehicle(metaclass=ABCMeta):
    @abstractmethod
    def start_engine(self) -> None:
        pass


def start_engine(vehicle: AbcBadVehicle) -> None:
    vehicle.start_engine()


class BadCar(AbcBadVehicle):
    def start_engine(self) -> None:
        print("Car engine started!")


class BadBicycle(AbcBadVehicle):
    def start_engine(self) -> None:
        raise Exception("Bicycles don't have engines")


print(
    "\n```",
    """class AbcBadVehicle(metaclass=ABCMeta):
    @abstractmethod
    def start_engine(self) -> None:
        pass


def start_engine(vehicle: AbcBadVehicle) -> None:
    vehicle.start_engine()


class BadCar(AbcBadVehicle):
    def start_engine(self) -> None:
        print("Car engine started!")


class BadBicycle(AbcBadVehicle):
    def start_engine(self) -> None:
        raise Exception("Bicycles don't have engines")""",
    "```",
    sep="\n",
)

print(
    "\nThis is a bad implementation of Liskov Substitution Principle (LCP),",
    'because the "BadBicycle" class implements the "start_engine" method which',
    'produces a different side effect than the "start_engine" method inside the "BadCar" class.',
    'So, if we execute the "start_engine" function with both classes ("BadCar", and "BadBicycle")',
    "the function will produce different side effects that could be break the function execution.",
    sep="\n",
)

print("\nGood implementation of Liskov Substitution Principle (LCP)...")


class AbcGoodVehicle(metaclass=ABCMeta):
    @abstractmethod
    def move(self) -> None:
        pass


def start_move(vehicle: AbcGoodVehicle) -> None:
    vehicle.move()


class GoodCar(AbcGoodVehicle):
    def move(self) -> None:
        self.start_engine()
        print("Car is moving!")

    def start_engine(self) -> None:
        print("Car engine started!")


class GoodBicycle(AbcGoodVehicle):
    def move(self) -> None:
        print("Bicycle is moving!")


print(
    "\n```",
    """class AbcGoodVehicle(metaclass=ABCMeta):
    @abstractmethod
    def move(self) -> None:
        pass


def start_move(vehicle: AbcGoodVehicle) -> None:
    vehicle.move()


class GoodCar(AbcGoodVehicle):
    def move(self) -> None:
        self.start_engine()
        print("Car is moving!")

    def start_engine(self) -> None:
        print("Car engine started!")


class GoodBicycle(AbcGoodVehicle):
    def move(self) -> None:
        print("Bicycle is moving!")""",
    "```",
    sep="\n",
)

print(
    "\nThis is a good implementation of Liskov Substitution Principle (LCP),",
    'because all child classes of "AbcGoodVehicle" class implements each method',
    'with the same side effect. So, if we execute the "move" function with both',
    'classes ("GoodCar", and "GoodBicycle"), we are not going to have side effects',
    "that could break the function execution.",
    sep="\n",
)

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")


class AbcVehicle(metaclass=ABCMeta):
    @abstractmethod
    def brake(self) -> None:
        pass

    @abstractmethod
    def speed_up(self) -> None:
        pass


def brake(*, vehicle: AbcVehicle) -> None:
    vehicle.brake()


def speed_up(*, vehicle: AbcVehicle) -> None:
    vehicle.speed_up()


class Car(AbcVehicle):
    def brake(self) -> None:
        print("Car braking!")

    def speed_up(self) -> None:
        print("Car speeding up!")


class Truck(AbcVehicle):
    def brake(self) -> None:
        print("Truck braking!")

    def speed_up(self) -> None:
        print("Truck speeding up!")


class Boat(AbcVehicle):
    def brake(self) -> None:
        print("Boat braking!")

    def speed_up(self) -> None:
        print("Boat speeding up!")


car: Car = Car()
truck: Truck = Truck()
boat: Boat = Boat()

print()
speed_up(vehicle=car)
speed_up(vehicle=truck)
speed_up(vehicle=boat)

print()
brake(vehicle=car)
brake(vehicle=truck)
brake(vehicle=boat)
