###############################################################################
###   EJERCICIO
###############################################################################
class Animal:
    """
    Ejemplo incorrecto de usar OCP
    """
    def sonido(self, animal):
        if animal == "perro":
            print('Guau guau!')
        elif animal == "gato":
            print('miauuuu!')
        else:
            print("Ese animal no lo conozco")



from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Ejemplo correcto de usar OCP
    """
    @abstractmethod
    def sonido(self):
        pass


class Perro(Animal):
    def sonido(self):
        return 'Guau!'

class Gato(Animal):
    def sonido(self):
        return 'Miauuu!'
    
# Uso
def emitir_sonido(animal: Animal):
    print(animal.sonido())

perro = Perro()
gato = Gato()

emitir_sonido(perro) 
emitir_sonido(gato) 


###############################################################################
###   DIFICULTAD EXTRA
###############################################################################
from abc import ABC, abstractmethod


class Calculadora(ABC):
    """
    Una calculadora expectacular
    Definimos Calculadora como una clase abstracta usando ABC y decoramos el 
    método resultado con @abstractmethod. Esto asegura que Calculadora no pueda 
    ser instanciada directamente y que cualquier subclase deba implementar el 
    método resultado.
    """
    @abstractmethod            
    def resultado(self, a, b):
        pass
    

class Suma(Calculadora):
    def resultado(self, a, b):
        return a + b


class Resta(Calculadora):
    def resultado(self, a, b):
        return a - b
    

class Multiplicacion(Calculadora):
    def resultado(self, a, b):
        return a * b
    

class Division(Calculadora):
    def resultado(self, a, b):
        return a/b
    


#Uso
def calcular(operacion: Calculadora, a, b):
    return operacion.resultado(a, b)

# Instanciando las operaciones
suma = Suma()
resta = Resta()
multiplicacion = Multiplicacion()
division = Division()

# Variables para las operaciones
a = 5
b = 10
print("\nSuma: ", calcular(suma, a, b))
print("Resta:", calcular(resta, a, b))          
print("Multiplicación:", calcular(multiplicacion, a, b))  
print("División:", calcular(division, a, b))     