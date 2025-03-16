
print("\n\n=======================================EJERCICIO=======================================\n\n")

'''
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitucion de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
'''
# FORMA CORRECTA
'''
class Bird:
    
    def have_beak(self):
        return "Soy un pajaro y mi boca es un pico"
         
    def fly(self):
        return "Soy un pajaro y vuelo"
    
class Hawk(Bird):
    pass

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("penguins swim not fly")

hawk = Hawk()
penguin = Penguin()

print(hawk.have_beak())
print(hawk.fly())
print(penguin.have_beak())
print(penguin.fly())
'''
# FORMA CORRECTA

from abc import ABC, abstractmethod

class Bird(ABC):
    
    def have_beak(self):
        return "Soy un pajaro y mi boca es un pico"
         
class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass
    
class NonFlyingBird(Bird):
    pass
    
class Hawk(FlyingBird):
    def fly(self):
        return "Soy un halcon y vuelo"

class Penguin(NonFlyingBird):
    def swim(self):
        return "Soy un pingÃ¼ino y nado, no vuelo"


hawk = Hawk()
penguin = Penguin()

print(hawk.have_beak())
print(hawk.fly())
print(penguin.have_beak())
print(penguin.swim())





print("\n\n=======================================DIFICULTAD EXTRA=======================================\n\n")

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquia de vehiculos. Todos ellos deben poder acelerar y frenar, asi como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehiculo.
 * 2. Añade tres subclases de Vehiculo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un codigo que compruebe que se cumple el LSP.
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
            self.name = name        

    @abstractmethod    
    def accelerate(self):
        pass
    
    @abstractmethod
    def brake(self):
        pass
    
    
class EngineVehicle(Vehicle):
    def have_engine(self):
        return f"{self.name} es un vehÃ­culo de motor"
    
    @abstractmethod
    def accelerate(self):
        pass
    
    def brake(self):
        return f"{self.name} esta frenando con los discos de freno"

class ElectricMotor(EngineVehicle):
    def accelerate(self):
        return f"{self.name} esta acelerando con el motor electrico"

class GasMotor(EngineVehicle):
    def accelerate(self):
        return f"{self.name} esta acelerando con el motor de gasoil"

class NonEngineVehicle(Vehicle):
    def no_engine(self):
        return f"{self.name} es un vehiculo sin motor"
    
    def accelerate(self):
        return f"{self.name} esta acelerando con los pedales"
    
    def brake(self):
        return f"{self.name} esta frenando con las zapatas"

class Bicycle(NonEngineVehicle):
    pass


camion = GasMotor("Camion")
coche = ElectricMotor("Coche")
bici = Bicycle("Bicicleta")


print(camion.have_engine())
print(camion.accelerate())
print(camion.brake())

print(coche.have_engine())
print(coche.accelerate())
print(coche.brake())

print(bici.no_engine())
print(bici.accelerate())
print(bici.brake())
