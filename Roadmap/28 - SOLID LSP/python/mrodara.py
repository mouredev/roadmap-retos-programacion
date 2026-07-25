### Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)

'''
LSP establece que: Un objeto de una subclase debe ser sustituible por un objeto de su clase base 
sin alterar el correcto funcionamiento del programa.

LSP se centra en garantizar que las subclases no modifiquen el comportamiento esperado de la clase base. 
En otras palabras, cualquier clase hija debe ser capaz de reemplazar a su clase padre sin introducir errores o 
comportamientos inesperados.
'''
'''
Ventajas:
- Mejora la reutilización de código.
- Aporta coherencia en la jerarquía de clases.
- Ayuda a evitar la dependencia de la implementación.
'''

# Ejemplo que viola LSP
# Clase Base
class CuentaBancaria():
    def __init__(self, saldo):
        self.saldo = saldo
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            raise ValueError("Saldo insuficiente para retirar de la cuenta")

# Clase Derivada
class CuentaAhorros(CuentaBancaria):
    
    def retirar(self, monto):
        raise NotImplementedError("No se puede realizar retirada de la cuenta ahorro")

# Al aplicar polimorfismo en este caso está violando el principio de Sustitución de Liskov
'''
CuentaAhorros no puede ser sustituida por CuentaBancaria sin alterar

def procesar_retiro(cuenta, monto):
    cuenta.retirar(monto)

cuenta = CuentaBancaria(1000)
procesar_retiro(cuenta, 100)  # Funciona correctamente

cuenta_ahorros = CuentaAhorros(1000)
procesar_retiro(cuenta_ahorros, 100)  # Lanza NotImplementedError
'''

# Arreglemos el ejemplo empleando abstracciones para restricciones específicas
from abc import ABC, abstractmethod

class CuentaBancaria(ABC):

    def __init__(self, saldo):
        self.saldo = saldo
    
    @abstractmethod
    def retirar(self, monto):
        pass

class CuentaCorriente(CuentaBancaria):
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("Retirada de efectivo realizada correctamente")
        else:
            raise ValueError("Su saldo es inferior a la cantidad a retirar, abortando operación")

class CuentaAhorros(CuentaBancaria):
    def retirar(self, monto):
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente, abortando operación")
        
        if monto >= 500:
            raise ValueError("La retirada máxima para este tipo de cuenta es de 500€") # Restricción específica para esta clase

        self.saldo -= monto

# Prueba de funcionamiento correcto
def procesar_retirada(cuenta, monto):
    try:
        cuenta.retirar(monto)
        print(f"Proceso finalizado, su saldo actual tras la operación es de {cuenta.saldo} €")
    except ValueError as e:
        print(e)
        
c1 = CuentaCorriente(1000)
c2 = CuentaAhorros(2000)

procesar_retirada(c1, 500)  # Funciona correctamente
procesar_retirada(c2, 200)  # Funciona correctamente
procesar_retirada(c2, 700)  # Lanza ValueError

### EJERCICIO EXTRA

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, type, max_speed, speed=0):
        self.type = type
        self.max_speed = max_speed
        self.speed = speed if speed <= max_speed else max_speed

    @abstractmethod
    def speed_up(self, qty):
        pass

    @abstractmethod
    def speed_down(self, qty):
        pass


class Car(Vehicle):
    def speed_up(self, qty):
        if self.speed + qty <= self.max_speed:
            self.speed += qty
            print(f"Acelerar terminado, velocidad actual: {self.speed}")
        else:
            raise ValueError("La cantidad a acelerar supera la velocidad máxima del vehículo")

    def speed_down(self, qty):
        if self.speed - qty >= 0:
            self.speed -= qty
            print(f"Frenar terminado, velocidad actual: {self.speed}")
        else:
            self.speed = 0
            print("Vehículo parado")


class Truck(Vehicle):
    def speed_up(self, qty):
        if self.speed + qty <= self.max_speed:
            self.speed += qty
            print(f"Acelerar terminado, velocidad actual: {self.speed}")
        else:
            raise ValueError("La cantidad a acelerar supera la velocidad máxima del camión")

    def speed_down(self, qty):
        if self.speed - qty >= 0:
            self.speed -= qty
            print(f"Frenar terminado, velocidad actual: {self.speed}")
        else:
            self.speed = 0
            print("Vehículo parado")


class ElectricCar(Vehicle):
    def speed_up(self, qty):
        if self.speed + qty <= self.max_speed:
            self.speed += qty
            print(f"Acelerar terminado, velocidad actual: {self.speed}")
        else:
            raise ValueError("La cantidad a acelerar supera la velocidad máxima del vehículo eléctrico")

    def speed_down(self, qty):
        if self.speed - qty >= 0:
            self.speed -= qty
            print(f"Frenar terminado, velocidad actual: {self.speed}")
        else:
            self.speed = 0
            print("Vehículo parado")


# Realización de pruebas
def test_speed(vehicle):
    print(f"Inicio de las pruebas con {vehicle.type}")
    try:
        vehicle.speed_up(25)
        vehicle.speed_down(5)
        vehicle.speed_up(vehicle.max_speed + 1)
        vehicle.speed_down(vehicle.speed)
    except ValueError as e:
        print(e)
    print("-" * 60)
        
cars = [
        Car("Ferrari F50", 300, 125),
        Truck("Mercedes-Benz Actros", 150, 80),
        ElectricCar("Tesla Model S", 120, 125)
    ]

for car in cars:
    test_speed(car)  # Realizar pruebas con cada tipo de vehículo

    
### FIN EJERCICIO EXTRA

        
### FIN Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)