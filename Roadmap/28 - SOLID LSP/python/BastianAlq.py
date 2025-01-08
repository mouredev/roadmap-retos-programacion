# /*
#  * EJERCICIO:
#  * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
#  * y crea un ejemplo simple donde se muestre su funcionamiento
#  * de forma correcta e incorrecta.
#  *
# ---------------------------------------
# | LISKOV SUBSTITUTION PRINCIPLE (LSP)  |  Información extraída de -> https://devexpert.io/principios-solid-guia-gratis/ 
# ---------------------------------------

# El principio de sustitucion de liskov (LSP) dice que si en alguna parte del codigo una clase extiende de otra, tenemos
# que poder utilizar cualquiera de las clases hijas y el programa debe seguir siendo válido, esto asegura que cuando extendamos
# una clase, no se esté alterando el comportamiento del padre.
#
# ¿COMO DETECTAR QUE ESTAMOS VIOLANDO EL PRINCIPIO DE SUSTITUCION DE LISKOV?
#  - cuando en una clase que extiende de otra, existen metodos que sobran, y no sabes que hacer con ellos
#  - si un metodo escrito no hace nada o lanza una excepcion, lo mas probable es que estes violando el (LSP)
#  - otra forma de identificarlo son los test. si los test funcionan para la clase padre pero no para la clase hija
#    entonces estas violando dicho principio


# FORMA INCORRECTA
print("------------ FUNCIONAMIENTO INCORRECTO LSP ------------")

print()
class Animal:
    def jump(self):
        print("Ha saltado")
    
    def walk(self):
        print("Está caminando")

class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()

class Elephant(Animal):
    def jump(self):
        raise Exception("Los elefantes no pueden saltar")

elephant_noLiskov  = Elephant()
dog_noLiskov = Dog()

dog_noLiskov.jump()
dog_noLiskov.walk()

elephant_noLiskov.walk()
# elephant_noLiskov.jump() error ya que no pueden saltar los elefantes


# FORMA CORRECTA
print("------------ FUNCIONAMIENTO CORRECTO LSP ------------")

class Animal:
    def walk(self):
        print("Esta caminando")

class lightWeightAnimal(Animal):
    def jump(self):
        print("Ha saltado")

class Dog(lightWeightAnimal):
    def __init__(self) -> None:
        super().__init__()

class Elephant(Animal):
    def __init__(self) -> None:
        super().__init__()

dog_liskov  = Dog()
elephant_liskov = Elephant()

dog_liskov.jump()
dog_liskov.walk()

elephant_liskov.walk()

# DIFICULTAD EXTRA

print("------------ DIFICULTAD EXTRA ------------")

#  * DIFICULTAD EXTRA (opcional):
#  * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
#  * cumplir el LSP.
#  * Instrucciones:
#  * 1. Crea la clase Vehículo.
#  * 2. Añade tres subclases de Vehículo.
#  * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
#  * 4. Desarrolla un código que compruebe que se cumple el LSP.
#  */

class Vehicle:
    def __init__(self, speed = 0) -> None:
        self.speed = speed

    def accelerate(self,increment):
        self.speed = self.speed + increment
        print(f"velocidad: {self.speed} km/h")
    
    def brake(self, decrement):
        self.speed = self.speed - decrement
        if self.speed < 0:
            self.speed = 0
        print(f"velocidad: {self.speed} km/h")


class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()
    
    def brake(self,decrement):
        print("el auto esta frenando...")
        super().brake(decrement)
    
    def accelerate(self,increment):
        print("el auto ha acelerado")
        super().accelerate(increment)
        

class Truck(Vehicle):
    def __init__(self) -> None:
        super().__init__()
    
    def brake(self, decrement):
        print("el camion esta frenando...")
        super().brake(decrement)
    
    def accelerate(self,increment):
        print("el camion esta acelerando...")
        super().accelerate(increment)

class MotorBike(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        
    def brake(self,decrement):
        print("la moto esta frenando...")
        super().brake(decrement)
    
    def accelerate(self,increment):
        print("la moto esta acelerando...")
        super().accelerate(increment)


def testVehicles(vehicle):
    vehicle.accelerate(10)
    vehicle.brake(3)

car = Car()
truck = Truck()
motorBike = MotorBike()

testVehicles(car)
testVehicles(truck)
testVehicles(motorBike)