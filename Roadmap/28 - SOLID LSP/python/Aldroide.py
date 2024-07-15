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

pato=Duck()
pinguino= Penguin()
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
    def speed_up(self):
        raise NotImplementedError ("Permite al vehículo acelerar")
    
    def brake(self):
        raise NotImplementedError ("Permite al vehículo frenar")

class Truck(Vehicle):
    def speed_up(self):
        print("El camion esta acelerando")
    
    def brake(self):
        print("El camion esta frenando")

class Motorcycle(Vehicle):
    def speed_up(self):
        print("La motocicleta esta acelerando")
    def brake(self):
        print("La motocicleta esta frenando")

class Airplane(Vehicle):
    def speed_up(self):
        print("El avion esta acelerando")
    def brake(self):
        print("El avion esta frenando")

def braking(vehiculo: Vehicle):
    vehiculo.brake()

def speeding_up(vehiculo: Vehicle):
    vehiculo.speed_up()

camion = Truck()
moto = Motorcycle()
avion = Airplane()

braking(camion)
braking(moto)
braking(avion)
speeding_up(camion)
speeding_up(moto)
speeding_up(avion)