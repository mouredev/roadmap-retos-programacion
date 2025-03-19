"""
/*
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
"""

# Forma correcta
class Bird:
    def fly(self):
        return "Flying"


class Sparrow(Bird):
    pass

# Forma incorrecta
class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostriches can't fly")


def make_bird_fly(bird):
    try:
        return bird.fly()
    except NotImplementedError as e:
        return str(e)


sparrow = Sparrow()
ostrich = Ostrich()

print(make_bird_fly(sparrow))
print(make_bird_fly(ostrich))

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

class Vehiculos:
    def __init__(self, name):
        self.name = name

    def acelerar(self):
        raise NotImplementedError

    def frenar(self):
        raise NotImplementedError


class Auto(Vehiculos):
    def acelerar(self):
        print(f"{self.name} esta acelerando..")

    def frenar(self):
        print(f"{self.name} frenando...")

class Bicicleta(Vehiculos):
    def acelerar(self):
        print(f"{self.name} esta acelerando")

    def frenar(self):
        print(f"{self.name} estas frenando")

def operar_vehiculo(vehiculo):
    vehiculo.acelerar()
    vehiculo.frenar()

auto1 = Auto("BMW")
bici1 = Bicicleta("BMX")

operar_vehiculo(auto1)
operar_vehiculo(bici1)
