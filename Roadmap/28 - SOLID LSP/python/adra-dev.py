"""
EJERCICIO:
Explora el "Principio SOLID de Sustitución de Liskov (Liskov 
Substitution Principle, LSP)" y crea un ejemplo simple donde se 
muestre su funcionamiento de forma correcta e incorrecta.

DIFICULTAD EXTRA(opcional):
Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y 
frenar, así como cumplir el LSP.

Instrucciones:
1. Crea la clase Vehículo.
2. Añade tres subclases de Vehículo.
3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
4. Desarrolla un código que compruebe que se cumple el LSP.

by adra-dev
"""


"""
Liskov substitution principle (LSP):
El Principio de Sustitución de Liskov  fue introducido por Barbara 
Liskov en la conferencia OOPSLA en 1987. Desde entonces, este 
principio ha sido una parte fundamental de la programación orientada 
objetos. El principio  declara:

    "Los subtipos deben ser sustituibles por sus tipos base."

documentacion:"https://realpython.com/solid-principles-python/"
    
Por ejemplo, si tienes un fragmento de código que funciona con una 
clase Figura, deberías poder sustituir esa clase con cualquiera de sus
subclases, como Circulo o Rectangulo, sin romper el código.

En la práctica, este principio consiste en hacer que las subclases se 
comporten como sus clases base sin romper las expectativas de nadie 
cuando llaman a los mismos métodos. Para continuar con ejemplos 
relacionados con las Figuras, supongamos que tiene una clase Rectangle 
como la siguiente
"""
# shapes_lsp.py

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


"""
Debido a que un cuadrado es un caso especial de un rectángulo con 
lados iguales, piensaa en derivar una clase Square de Rectangle para
reutilizar el código. A continuación, se invalida el método setter 
para los atributos .width y .height de modo que cuando cambie un 
lado, también cambie el otro lado
"""

# shapes_lsp.py

# ...

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value


square = Square(5)
print(vars(square))

square.width = 7
print(vars(square))

square.height = 9
print(vars(square))


"""
Ahora te has asegurado de que el objeto Square siempre siga siendo un 
cuadrado válido, lo que le facilita la vida por el módico precio de 
un poco de memoria desperdiciada. Desafortunadamente, esto viola el 
principio de sustitución de Liskov porque no se pueden reemplazar las
instancias de Rectangle con sus contrapartes Square. 

Cuando alguien espera un objeto Rectangle en su código, puede 
suponer que se comportará como uno exponiendo dos atributos .width y 
.height independientes. Mientras tanto, la clase Square rompe esa 
suposición al cambiar el comportamiento prometido por la interfaz del
objeto. Eso podría tener consecuencias sorprendentes y no deseadas, 
que probablemente serían difíciles de depurar.

Mientras que un cuadrado es un tipo específico de rectángulo en 
matemáticas, las clases que representan esas formas no deben estar en
una relación padre-hijo si desea que cumplan con el principio de 
sustitución de Liskov. Una forma de resolver este problema es crear 
una clase base para que Rectangle y Square se extiendan

"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2
    

def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

print(get_total_area([Rectangle(10, 5), Square(5)]))


"""
Extra
"""


class Vehicle:

    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment
        print(f"Velocidad: {self.speed} Km/h")

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad: {self.speed} Km/h")


class Car(Vehicle):
    def accelerate(self, increment):
        print("El coche está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("El coche está frenando")
        super().brake(decrement)


class Bicycle(Vehicle):
    def accelerate(self, increment):
        print("La bicicleta está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La bicicleta está frenando")
        super().brake(decrement)


class Motorcycle(Vehicle):
    def accelerate(self, increment):
        print("La moto está acelerando")
        super().accelerate(increment)

    def brake(self, decrement):
        print("La moto está frenando")
        super().brake(decrement)


def test_vehicle(vehicle):
    vehicle.accelerate(2)
    vehicle.brake(1)


car = Car()
bicycle = Bicycle()
motorcycle = Motorcycle()

test_vehicle(car)
test_vehicle(bicycle)
test_vehicle(motorcycle)
