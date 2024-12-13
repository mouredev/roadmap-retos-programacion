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
    def __init__(self, velocidad=0) -> None:
        self.velocidad = velocidad

    def acelera(self, aceleracion):
        self.velocidad += aceleracion
        print(f"Velocidad {self.velocidad}")

    def frena(self, frenado):
        if self.velocidad <= 0:
            self.velocidad = 0
        self.velocidad -= frenado
        print(f"Velocidad {self.velocidad}")
        

class Turismo(Vehiculo):
    def acelera(self, aceleracion):
        print("El turismo está acelerando")
        super().acelera(aceleracion)
    def frena(self, frenado):
        print("El turismo está frenando")
        super().frena(frenado)

class Furgoneta(Vehiculo):
    def acelera(self, aceleracion):
        print("La furgoneta está acelerando")
        super().acelera(aceleracion)
    def frena(self, frenado):
        print("La furgoneta está frenando")
        super().frena(frenado)

class Camion(Vehiculo):
    def acelera(self, aceleracion):
        print("El camión está acelerando")
        super().acelera(aceleracion)
    def frena(self, frenado):
        print("El camión está frenando")
        super().frena(frenado)


def aplica_LSP(vehiculo):
    vehiculo.acelera(10)
    vehiculo.frena(5)

mi_vehiculo = Vehiculo()
turismo = Turismo()
furgoneta = Furgoneta()
camion = Camion()

aplica_LSP(mi_vehiculo)
aplica_LSP(turismo)
aplica_LSP(furgoneta)
aplica_LSP(camion)