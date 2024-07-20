"""
* EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""
#LSP incorrecto
class Felines():
    def sound(self):
        print("roar")

class Cats(Felines):
    def sound(self):
        raise Exception("Los gatos no pueden rugir")

one_feline = Felines()
one_feline.sound()
one_cat = Cats()
#one_cat.sound() Lanza la excepción

#LSP Correcto
from abc import ABC,abstractmethod

class Feline(ABC):
    @abstractmethod
    def sound(self):
        pass

class Big_Feline(Feline):
    def sound(self):
        print("roar")

class Small_Feline(Feline):
    def sound(self):
        print("miau")

class Tiger(Big_Feline):
    pass

class Cat(Small_Feline):
    pass

my_tiger = Tiger()
my_tiger.sound()

my_cat = Cat()
my_cat.sound()

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
class Vehicle(ABC):
    def __init__(self,speed = 0):
        super().__init__()
        self.speed = speed

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def slow_down(self):
        pass

class F1_Car(Vehicle):
    def accelerate(self,increment):
        self.speed += increment + 100
        return f"velocidad de {self.speed}"

    def slow_down(self,decrement):
        self.speed -= decrement + 15
        if self.speed <= 0:
            self.speed = 0
        return f"decelera y va a una velocidad de {self.speed}"

class Regular_Car(Vehicle):
    def accelerate(self,increment):
        self.speed += increment + 50
        return f"velocidad de {self.speed}"

    def slow_down(self,decrement):
        self.speed -= decrement + 10
        if self.speed <= 0:
            self.speed = 0
        return f"decelera y va a una velocidad de {self.speed}"

class Truck(Vehicle):
    def accelerate(self,increment):
        self.speed += increment + 35
        return f"velocidad de {self.speed}"

    def slow_down(self,decrement):
        self.speed -= decrement + 5
        if self.speed <= 0:
            self.speed = 0
        return f"decelera y va a una velocidad de {self.speed}"

def show_vehicle(name:str,vehicle:Vehicle):
    print(f"El vehículo {name} va a una {vehicle.accelerate(20)} km/h. Después {vehicle.slow_down(15)} km/h")

my_f1 = F1_Car()
show_vehicle(name="McLaren",vehicle=my_f1)
my_car = Regular_Car()
show_vehicle(name="Seat Leon",vehicle=my_car)
my_truck = Truck()
show_vehicle(name="Mac",vehicle=my_truck)
