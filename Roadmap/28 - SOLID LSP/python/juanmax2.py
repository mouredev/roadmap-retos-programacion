"""
Ejercicio
"""

# Incorrecto 

class Ave:
    
    def fly(self):
        return "Fly"
    
class Pollo(Ave):
    
    def fly(self):
        raise Exception("Los pollos no vuelan")
    

#bird = Ave()
#print(bird.fly())

#pollo = Pollo()
#print(pollo.fly())

# Correcto

class Aves:
    
    def moving(self):
        return "Moving"

class Pollito(Aves):
    
    def moving(self):
        return "Walking"
    
bird = Aves()
print(bird.moving())

pollo = Pollito()
print(pollo.moving())

    
bird = Pollito()
print(bird.moving())

pollo = Aves()
print(pollo.moving())


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

class Vehiculo:
    
    def __init__(self, velocidad = 0):
        self.velocidad = velocidad
        
    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"Velocidad: {self.velocidad} km/h")
        
    def frenar(self, decremento):
        
        self.velocidad -= decremento
        if self.velocidad <= 0:
            self.velocidad = 0
        
        print(f"Velocidad: {self.velocidad} km/h")
        
class Coche(Vehiculo):
    def acelerar(self, incremento):
        print("El coche esta acelerando")
        super().acelerar(incremento)
    
    def frenar(self, decremento):
        print("El coche esta frenando")
        super().frenar(decremento)
    
class Moto(Vehiculo):
    
    def acelerar(self, incremento):
        print("La moto esta acelerando")
        super().acelerar(incremento)
    
    def frenar(self, decremento):
        print("La moto esta frenando")
        super().frenar(decremento)
    
class Avion(Vehiculo):
    
    def acelerar(self, incremento):
        print("El avion esta acelerando")
        super().acelerar(incremento)
    
    def frenar(self, decremento):
        print("El avion esta frenando")
        super().frenar(decremento)
    
def test_vehiculo(vehiculo):
    vehiculo.acelerar(2)
    vehiculo.frenar(1)
    
car = Coche()
moto = Moto()
avion = Avion()

test_vehiculo(car)
test_vehiculo(moto)
test_vehiculo(avion)