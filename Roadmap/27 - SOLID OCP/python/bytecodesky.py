"""/*
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)" 
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 */"""

#EL PRINCIPIO SOLID OCP (OPEN-CLOSED PRINCIPLE) ESTABLECE QUE UNA CLASE DEBE ESTAR ABIERTA PARA SU EXTENSIÓN, PERO CERRADA PARA SU MODIFICACIÓN. EN OTRAS PALABRAS, DEBE SER POSIBLE AGREGAR NUEVAS FUNCIONALIDADES A UNA CLASE SIN NECESIDAD DE MODIFICAR SU CÓDIGO FUENTE.

# Ejemplo incorrecto
# En este ejemplo es incorrecto porque si se quiere agregar un nuevo animal, se tendría que modificar la clase Granja para agregar un nuevo método sonido() para el nuevo animal. Esto viola el principio OCP, ya que no se puede extender la funcionalidad de la clase Granja sin modificar su código fuente.
class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

class Granja:
    def __init__(self):
        self.animales = []
        
    def agregar_animal(self, animal):
        self.animales.append(animal)
        
    def sonidos(self):
        for animal in self.animales:
            print(animal.sonido)

granja = Granja()
granja.agregar_animal(Animal("Firulais", "Guau"))
granja.agregar_animal(Animal("Garfield", "Miau"))
granja.agregar_animal(Animal("Manchitas", "Muu"))
granja.sonidos()


# Ejemplo correcto
# En este ejemplo, se utiliza el principio OCP para permitir la extensión de la funcionalidad de la clase Granja sin modificar su código fuente. Se crea una clase base Animal con un método sonido() que es implementado por las subclases Perro, Gato y Vaca. De esta manera, se puede agregar nuevos animales sin modificar la clase Granja.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau"
    
class Gato(Animal):
    def sonido(self):
        return "Miau"

class Vaca(Animal):
    def sonido(self):
        return "Muu"
    
class Granja:
    def __init__(self):
        self.animales = []
        
    def agregar_animal(self, animal):
        self.animales.append(animal)
        
    def sonidos(self):
        for animal in self.animales:
            print(animal.sonido())

granja = Granja()
granja.agregar_animal(Perro("Firulais"))
granja.agregar_animal(Gato("Garfield"))
granja.agregar_animal(Vaca("Manchitas"))
granja.sonidos()

""" * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP."""

# IMPLEMENTACIÓN DE UNA CALCULADORA QUE CUMPLE CON EL PRINCIPIO OCP
class Calculadora:
    def __init__(self):
        self.operaciones = []
        
    def agregar_operacion(self, operacion):
        self.operaciones.append(operacion)
        
    def calcular(self, operacion, a, b):
        for op in self.operaciones:
            if op.nombre == operacion:
                return op.calcular(a, b)
        return None
    
class Operacion:
    def __init__(self, nombre):
        self.nombre = nombre
        
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
        return a / b
    
# COMPROBACIÓN DE FUNCIONAMIENTO CON LAS OPERACIONES BÁSICAS
calc = Calculadora()
calc.agregar_operacion(Suma("Suma"))
calc.agregar_operacion(Resta("Resta"))
calc.agregar_operacion(Multiplicacion("Multiplicación"))
calc.agregar_operacion(Division("División"))

print(calc.calcular("Suma", 5, 3))
print(calc.calcular("Resta", 5, 3))
print(calc.calcular("Multiplicación", 5, 3))
print(calc.calcular("División", 5, 3))

# AGREGAR UNA NUEVA OPERACIÓN (POTENCIA)
class Potencia(Operacion):
    def calcular(self, a, b):
        return a ** b

calc.agregar_operacion(Potencia("Potencia"))
print(calc.calcular("Potencia", 5, 3))
