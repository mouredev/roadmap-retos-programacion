"""

28 - SOLID LSP - Liskov Substitution Principle
Autor de la solución: oriaj3 

El principio de sustitución de Liskov (Liskov Substitution Principle, LSP) establece que los objetos de una clase derivada 
deben poder sustituirse por objetos de la clase base sin afectar el comportamiento del programa. En otras palabras, una 
clase derivada debe extender la clase base sin cambiar su comportamiento.

El principio LSP se puede lograr mediante el uso de interfaces y clases abstractas.

Un ejemplo sería una clase Cuadrado que hereda de una clase Rectángulo. Un cuadrado es un tipo de rectángulo, pero no
todos los rectángulos son cuadrados. Por lo tanto, la clase Cuadrado no debería heredar de la clase Rectángulo.

En Python no hay una forma directa de implementar interfaces, pero se pueden usar clases abstractas para lograr un comportamiento similar.
Se usa la librería abc (Abstract Base Classes) para definir clases abstractas.

"""

"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# Ejemplo incorrecto
class animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "sonido"
    
class jirafa(animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        raise Exception("Las jirafas no hacen sonidos. ")
    
class gato(animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def hacer_sonido(self):
        return "miau"
    
""" animal = animal("animal")
animal.hacer_sonido()

gato = gato("gato")
gato.hacer_sonido()

jirafa = jirafa("jirafa")
jirafa.hacer_sonido() """

# Ejemplo correcto
from abc import ABC, abstractmethod

class animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def comunicate(self):
        pass

class gato(animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def comunicate(self):
        return "El gato hizo miau"

class jirafa(animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def comunicate(self):
        return "La jirafa hizo un señal con su cuello"
    
animales = [gato("gato"), jirafa("jirafa")]

for animal in animales:
    print(animal.comunicate())
        
"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 */
"""
from abc import ABC, abstractmethod

# Clase abstracta Vehículo

class Vehicle(ABC):
    def __init__(self, speed=0) -> None:
        self.speed = speed

    def accelerate(self, increment=1):
        self.speed += increment
        return self.speed        

    def brake(self, increment=1):
        self.speed -= increment
        return self.speed
    
    def get_speed(self):
        print(self.speed)
    
class Car(Vehicle):
    
    def accelerate(self, increment=3):
        print("El coche está acelerando")
        super().accelerate(increment)

    def brake(self, increment=3):
        print("El coche está frenando")
        super().brake(increment)
    
    def get_speed(self):
        super().get_speed()
        
class Bicycle(Vehicle):
    
    def accelerate(self, increment=1):
        print("La bicicleta está acelerando")
        super().accelerate(increment)


    def brake(self, increment=1):
        print("La bicicleta está frenando")
        super().brake(increment)

    def get_speed(self):
        super().get_speed()

class Motorcycle(Vehicle):
    
    def accelerate(self, increment=4):
        print("La moto está acelerando")
        super().accelerate(increment)

    def brake(self, increment=2):
        print("La moto está frenando")
        super().brake(increment)
        

def test_vehicle(vehicle):
    vehicle.accelerate()
    vehicle.get_speed()
    vehicle.brake()
    vehicle.get_speed()

car = Car()
cycle = Bicycle()
byke = Motorcycle()

vehicles = [car, cycle, byke]

test_vehicle(Car())
test_vehicle(Bicycle())
test_vehicle(Motorcycle())

""" print("\nVehículos: ")
for vehicle in vehicles:
    test_vehicle(vehicle)
    print("\n") """
