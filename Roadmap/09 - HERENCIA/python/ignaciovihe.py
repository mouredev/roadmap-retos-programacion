"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
"""
# Superclase
class Animal:

    def __init__(self,name, age, breed = None):
        self.name = name
        self.age = age
        self.breed = breed if breed else "Unknown"
        self.sound = None

    def feed(self):
        print(f"{self.name} is fed")

    def make_sound(self):
        if self.sound:
            print(self.sound)
        else:
            print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, age, breed = None):
        super().__init__(name, age, breed)
        self.sound = "Guau"


class Cat(Animal):
    def __init__(self, name, age, breed = "None"):
        super().__init__(name, age, breed)
        self.sound = "Miau"

my_dog = Dog("Firulais", 2)
my_cat = Cat("Bruma", 1)
my_cow = Animal("Campana", 8, "lechera")

my_dog.feed()
my_cat.feed()
my_cow.feed()
my_dog.make_sound()
my_cat.make_sound()
my_cow.make_sound()
