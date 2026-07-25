"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""
# No cumple LSP

class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def retirar(self, monto):
        if monto > self.saldo:
            raise Exception("Fondos insuficientes")
        self.saldo -= monto
        return self.saldo
    

class CuentaAhorro(CuentaBancaria): # La clase cuenta de ahorro no cumple la promera que hace su padre. Lanza una excepción.
    def retirar(self, monto):       # No podria sustituir las clases base por su subclase
        raise Exception("No se puede retirar de una cuenta de ahorro")
    


# Cumple LSP

# Con composición

class CuentaBancaria:
    def __init__(self, saldo, comportamiento):
        self.saldo = saldo
        self.comportamiento = comportamiento

    def retirar(self, monto):
        self.saldo = self.comportamiento.retirar(monto, self.saldo)
        return self.saldo

class ComportamientoCorriente:
    def retirar(self, monto, saldo):
        if monto > saldo:
            raise Exception("Fondos insuficientes")
        saldo -= monto
        return saldo
    
class ComportamientoAhorro:
    def retirar(self, monto, saldo):
        raise Exception("No se puede retirar de una cuenta de ahorro")
    

cuenta_corriente = CuentaBancaria(1000, ComportamientoCorriente())
cuenta_ahorro = CuentaBancaria(12000, ComportamientoAhorro())

try:
    print(cuenta_corriente.retirar(200))
    print(cuenta_ahorro.retirar(1000))
except Exception as e:
    print(e)

# con herecia y clases abstractas

from abc import ABC,abstractmethod

class CuentaBancaria(ABC):
    def __init__(self, saldo):
        self.saldo = saldo

    @abstractmethod
    def retirar(self, monto):
        pass

class CuentaCorriente(CuentaBancaria):
    def retirar(self, monto):
        if monto >self.saldo:
            raise Exception("Fondos insuficientes")
        self.saldo -= monto
        return self.saldo
    
class CuentaAhorro(CuentaBancaria):
    def retirar(self, monto):
        raise Exception("No se puede retirar de una cuenta de ahorro")
    

cuenta_corriente = CuentaCorriente(1000)
cuenta_ahorro = CuentaAhorro(12000)

try:
    print(cuenta_corriente.retirar(200))
    print(cuenta_ahorro.retirar(1000))
except Exception as e:
    print(e)


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

class Vehicle():
    def __init__(self):
        self.speed = 0

    def brake(self, decrement: int):
        self.speed = max(0,self.speed - decrement)
        return self.speed

    def accelerate(self, increment: int):
        self.speed += increment
        return self.speed

class Car(Vehicle):
    def brake(self, decrement):
        print("El coche frena:")
        return super().brake(decrement)
    
    def accelerate(self,increment):
        print("El coche acelera")
        return super().accelerate(increment)

class Bus(Vehicle):
    def brake(self, decrement):
        print("El bus frena:")
        return super().brake(decrement)
    
    def accelerate(self,increment):
        print("El bus acelera")
        return super().accelerate(increment)

class Bycicle(Vehicle):
    def brake(self, decrement):
        print("La bicicleta frena:")
        return super().brake(decrement)
    
    def accelerate(self,increment):
        print("La bicicleta acelera")
        return super().accelerate(increment)


def move_vehicle(vehicle: Vehicle):
    print(f"{vehicle.accelerate(10)}Km/h")
    print(f"{vehicle.brake(15)}Km/h")
    print(f"{vehicle.accelerate(5)}Km/h")

move_vehicle(Car())
move_vehicle(Bycicle())
move_vehicle(Bus())