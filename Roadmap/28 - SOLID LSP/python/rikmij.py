#Uso incorrecto
class Pokes:
    def __init__(self, name):
        self.name = name
    
    def attack(self, attack):
        return f"{self.name} usó {attack}"
    
    def evolve(self):
        return f"{self.name} está evolucionando"

class Seel(Pokes):
    def __init__(self, name):
        super().__init__(name)
    
    def evolve(self):
        return f"{self.name} está evolucionando a Dewgong"

class Sableye(Pokes):
    def __init__(self, name):
        super().__init__(name)
    
    def evolve(self):
        raise Exception("Sableye no tiene evolución")

charmander = Seel("Seel")
print(charmander.attack("Rayo Hielo"))
print(charmander.evolve())

sableye = Sableye("Sableye")
#print(sableye.evolve())

'''
No todos los pokémon tienen evolución, por lo que este principio se estarñia incumpliendo aquí.
La superclase debe tener todos los métodos comunes a todos los hijos, y éstos poder tener sus propios métodos
además de los heredados
'''

#Uso correcto
class Pokemon:
    def __init__(self, name):
        self.name = name
    
    def attack(self, attack):
        return f"{self.name} usó {attack}"

class Charmander(Pokemon):
    def __init__(self, name):
        super().__init__(name)
    
    def evolve(self):
        return f"{self.name} está evolucionando a Charmeleon"

class Tauros(Pokemon):
    pass

charmander = Charmander("Charmander")
print(charmander.attack("Ascuas"))
print(charmander.evolve())

tauros = Tauros("Tauros")
print(tauros.attack("Derribo"))

print("\n" + "*"*7 + " EJERCICIO EXTRA " + "*"*7)
class Vehicle:
    def speed_up(self):
        return "El vehículo está acelerando"
    
    def brake(self):
        return "El vehículo está frenando"

class Car(Vehicle):
    def  speed_up(self):
        return "El coche está acelerando"
    
    def brake(self):
        return "El coche está frenando"
    
    def open_trunk(self):
        return "El maletero se ha abierto"

class Moto(Vehicle):
    def  speed_up(self):
        return "La moto está acelerando"
    
    def brake(self):
        return "La moto está frenando"
    
    def make_noise(self):
        return "BRRRRUM BRUUUUM"

class Tractor(Vehicle):
    def  speed_up(self):
        return "El tractor está acelerando"
    
    def brake(self):
        return "El tractor está frenando"
    
    def sow(self):
        return "El tractor ha plantado semillas"

coche = Car()
print(coche.open_trunk())
print(coche.brake())

moto = Moto()
print(moto.speed_up())
print(moto.make_noise())

tractor = Tractor()
print(tractor.sow())

'''
Como Vehicle tiene todos los métodos comunes, en esos métodos comunes podría usarse la clase Vehicle en vez de las
subclases (aunque cambie el texto, pero es lo mismo), pero para los métodos específicos no.
Así, se cumple el LSP
'''
