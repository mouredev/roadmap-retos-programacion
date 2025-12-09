# incorrecta
class ErroneaAnimal:
    def emitir_sonido1(self, tipo_animal, sonido):
        if tipo_animal == "gallina":
            return sonido * 2
        elif tipo_animal == "perro":
            return sonido * 1


animal1 = ErroneaAnimal()
animal1.emitir_sonido1("perro", "guau")
animal2 = ErroneaAnimal()
animal2.emitir_sonido1("gallina", "kikiriki")
# Si quisiermos añadir mas animales tendrimos que modificar la clase.

# correcta
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def emitir_sonido(self) -> str:
        pass


class Perro(Animal):
    def emitir_sonido(self):
        return "guauu"


class Gallina(Animal):
    def emitir_sonido(self):
        return "kikiriki"


# Nuevo animal sin modificar clases existentes
class Gato(Animal):
    def emitir_sonido(self):
        return "miau"


# Uso
animales = [Perro(), Gallina(), Gato()]
for animal in animales:
    print(animal.emitir_sonido())


"""
extra
"""


class Operaciones(ABC):
    @abstractmethod
    def operar(self, a, b):
        pass


class Sumar(Operaciones):
    def operar(self, a, b):
        return a + b


class Restar(Operaciones):
    def operar(self, a, b):
        return a - b


class Multiplicar(Operaciones):
    def operar(self, a, b):
        return a * b


class Dividir(Operaciones):
    def operar(self, a, b):
        return a / b


# Comprobamos que se cumple el OCP si al agregar una nueva operación no tenemos que modificar las actuales.
# Para añádir calcular potencias, agregar una nueva subclase "Potencia"
class Potencia(Operaciones):
    def operar(self, a, b):
        return a**b


# Esta es la forma correcta.Recuerda, las clases y metodos deberían hacer una sola cosa(1 sola responsabilidad)
class Calculadora:

    def calcular(self, operacion: Operaciones, a, b):
        print(operacion.operar(a, b))


calculadora = Calculadora()
calculadora.calcular(Sumar(), 4, 5)
calculadora.calcular(Restar(), 4, 5)
calculadora.calcular(Multiplicar(), 4, 5)
calculadora.calcular(Dividir(), 4, 5)
calculadora.calcular(Potencia(), 4, 5)
