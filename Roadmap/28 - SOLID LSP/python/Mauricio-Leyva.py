"""
Mauricio Leyva

Jerarquía de vehículos que cumple con el Principio de Sustitución de Liskov (LSP).
Todos los vehículos deben poder acelerar y frenar.

Instrucciones:
1. Crea la clase Vehículo.
2. Añade tres subclases de Vehículo.
3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
4. Desarrolla un código que compruebe que se cumple el LSP.
"""

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self):
        self.velocidad = 0

    @abstractmethod
    def acelerar(self, incremento):
        pass

    @abstractmethod
    def frenar(self, decremento):
        pass

    def obtener_velocidad(self):
        return self.velocidad

class Coche(Vehiculo):
    def acelerar(self, incremento):
        self.velocidad += incremento
        return f"Coche acelerando. Velocidad actual: {self.velocidad} km/h"

    def frenar(self, decremento):
        self.velocidad = max(0, self.velocidad - decremento)
        return f"Coche frenando. Velocidad actual: {self.velocidad} km/h"

class Motocicleta(Vehiculo):
    def acelerar(self, incremento):
        self.velocidad += incremento * 1.2  # Las motos aceleran un poco más rápido
        return f"Motocicleta acelerando. Velocidad actual: {self.velocidad} km/h"

    def frenar(self, decremento):
        self.velocidad = max(0, self.velocidad - decremento * 1.1)  # Las motos frenan un poco más rápido
        return f"Motocicleta frenando. Velocidad actual: {self.velocidad} km/h"

class Camion(Vehiculo):
    def acelerar(self, incremento):
        self.velocidad += incremento * 0.8  # Los camiones aceleran más lento
        return f"Camión acelerando. Velocidad actual: {self.velocidad} km/h"

    def frenar(self, decremento):
        self.velocidad = max(0, self.velocidad - decremento * 0.9)  # Los camiones frenan más lento
        return f"Camión frenando. Velocidad actual: {self.velocidad} km/h"

def probar_vehiculo(vehiculo):
    print(vehiculo.acelerar(30))
    print(vehiculo.acelerar(20))
    print(vehiculo.frenar(10))
    print(vehiculo.frenar(15))
    print(f"Velocidad final: {vehiculo.obtener_velocidad()} km/h")
    print("-" * 50)

# Comprobación del LSP
vehiculos = [Coche(), Motocicleta(), Camion()]

for v in vehiculos:
    print(f"Probando {v.__class__.__name__}:")
    probar_vehiculo(v)