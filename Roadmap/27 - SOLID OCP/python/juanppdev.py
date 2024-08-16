"""
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""

# Incorrecto

class Calculadora:
    def __init__(self):
        pass

    def calcular(self, operacion, a, b):
        if operacion == "suma":
            return a + b
        elif operacion == "resta":
            return a - b
        # Si queremos agregar una nueva operación, tendríamos que modificar esta clase
        elif operacion == "multiplicacion":
            return a * b
        else:
            raise ValueError("Operación no soportada")

# Uso
calc = Calculadora()
print(calc.calcular("suma", 5, 3))  # Salida: 8
print(calc.calcular("resta", 5, 3))  # Salida: 2
print(calc.calcular("multiplicacion", 5, 3))  # Salida: 15


# Correcto

from abc import ABC, abstractmethod

class Operacion(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass

class Suma(Operacion):
    def calcular(self, a, b):
        return a + b

class Resta(Operacion):
    def calcular(self, a, b):
        return a - b

# Ahora podemos agregar nuevas operaciones sin modificar la clase Calculadora
class Multiplicacion(Operacion):
    def calcular(self, a, b):
        return a * b

class Calculadora:
    def __init__(self):
        self.operaciones = {}

    def registrar_operacion(self, nombre, operacion):
        self.operaciones[nombre] = operacion

    def calcular(self, nombre, a, b):
        if nombre in self.operaciones:
            return self.operaciones[nombre].calcular(a, b)
        else:
            raise ValueError("Operación no soportada")

# Uso
calc = Calculadora()
calc.registrar_operacion("suma", Suma())
calc.registrar_operacion("resta", Resta())
calc.registrar_operacion("multiplicacion", Multiplicacion())

print(calc.calcular("suma", 5, 3))  # Salida: 8
print(calc.calcular("resta", 5, 3))  # Salida: 2
print(calc.calcular("multiplicacion", 5, 3))  # Salida: 15


"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
"""

from abc import ABC, abstractmethod

class Operacion(ABC):
    @abstractmethod
    def calcular(self, a, b):
        pass

class Suma(Operacion):
    def calcular(self, a, b):
        return a + b

class Resta(Operacion):
    def calcular(self, a, b):
        return a - b

class Multiplicacion(Operacion):
    def calcular(self, a, b):
        return a * b

class Division(Operacion):
    def calcular(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

class Calculadora:
    def __init__(self):
        self.operaciones = {}

    def registrar_operacion(self, nombre, operacion):
        self.operaciones[nombre] = operacion

    def calcular(self, nombre, a, b):
        if nombre in self.operaciones:
            return self.operaciones[nombre].calcular(a, b)
        else:
            raise ValueError("Operación no soportada")

# Uso
calc = Calculadora()
calc.registrar_operacion("suma", Suma())
calc.registrar_operacion("resta", Resta())
calc.registrar_operacion("multiplicacion", Multiplicacion())
calc.registrar_operacion("division", Division())

print(calc.calcular("suma", 5, 3))  # Salida: 8
print(calc.calcular("resta", 5, 3))  # Salida: 2
print(calc.calcular("multiplicacion", 5, 3))  # Salida: 15
print(calc.calcular("division", 5, 3))  # Salida: 1.6666666666666667


class Potencia(Operacion):
    def calcular(self, a, b):
        return a ** b

# Registrar la nueva operación
calc.registrar_operacion("potencia", Potencia())

print(calc.calcular("potencia", 2, 3))  # Salida: 8
