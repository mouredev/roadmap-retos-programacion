'''
Ejercicio:
Explora el "Principio SOLID de Sustitucion de Liskov (Liskov Substitution Principle, LSP)" y crea un ejemplo simple donde se muestre su funcionamiento de forma correcta e incorrecta
'''

#! Forma incorrecta

class Tarjeta:
    def pagar(self):
        print("Estoy pagando tu compra.")

class TarjetaRara(Tarjeta):
    def pagar(self):
        raise Exception("No puedo volar soy una tarjeta")



#! Forma correcta
class Dog:
    def ladrar(self):
        print("Guau!")

class Labrador(Dog):
    def ladrar(self):
        print("Guau! Guau!")

'''
Dificultad extra: 
Crea una jerarquia de vehiculos. Todos ellos deben poder acelerar y frenar, asi como cumplir el LSP.

Instrucciones:
    1. Crea la clase Vehiculo.
    2. Agrega tres subclases de Vehiculo
    3. Implementa las operaciones "acelerar" y "frenar" como corresponda
    4. Desarrolla un codigo que compruebe que se cumple el LSP.
'''

class Vehiculo:
    def __init__(self, vel_max):
        self.vel_max = vel_max

    def acelerar(self, cantidad, vel):
        vel += cantidad
        print(f"La velocidad actual es de {vel}")
        return vel
    
    def frenar(self, cantidad, vel):
        if vel > 0 :
            vel -= cantidad
            print(f"La velocidad actual es de {vel}")
        return vel

class Coche(Vehiculo):
    def __init__(self, modelo: str, vel_max: int):
        self.modelo = modelo
        self.vel_max = vel_max

    def acelerar(self, cantidad, vel):
        nueva_vel = vel + cantidad
        if nueva_vel > self.vel_max:
            print(f"No se puede superar la velocidad maxima de {self.vel_max}.")
            return vel
        return super().acelerar(cantidad, vel)
    
    def frenar(self, cantidad, vel):
        return super().frenar(cantidad, vel)


class Bote(Vehiculo):
    def __init__(self, modelo: str, vel_max: int):
        self.modelo = modelo
        self.vel_max = vel_max

    def acelerar(self, cantidad, vel):
        nueva_vel = vel + cantidad
        if nueva_vel > self.vel_max:
            print(f"No se puede superar la velocidad maxima de {self.vel_max}.")
            return vel
        return super().acelerar(cantidad, vel)

    def frenar(self, cantidad, vel):
        return super().frenar(cantidad, vel)
    
class Helicoptero(Vehiculo):
    def __init__(self, modelo: str, vel_max: int):
        self.modelo = modelo
        self.vel_max = vel_max

    def acelerar(self, cantidad, vel):
        nueva_vel = vel + cantidad
        if nueva_vel > self.vel_max:
            print(f"No se puede superar la velocidad maxima de {self.vel_max}")
            return vel
        return super().acelerar(cantidad, vel)
    
    def frenar(self, cantidad, vel):
        return super().frenar(cantidad, vel)
    
def test_vehicle(vehicle):
    vehicle.acelerar(10, 150)
    vehicle.frenar(15, 150)
    
nissan = Coche("nissanxy", 250)
nissan.acelerar(20, 150)
nissan.frenar(40, 150)

trueno = Helicoptero("tambor", 250)
trueno.acelerar(20, 170)
trueno.frenar(60, 170)

bote = Bote("axy200", 150)
bote.acelerar(50, 120)
bote.frenar(20, 120)

test_vehicle(nissan)
test_vehicle(trueno)
test_vehicle(bote)