'''
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 '''

# Clase ejemplo animal:

class Animal:
    
    def __init__(self, nombre, sonido) -> None:
        self.nombre = nombre
        self.sonido = sonido

    def Sonido (self):
        print (
            f"Sonido: {self.sonido}")

# Herencia de clase Animal:

class Perro(Animal):
    pass

class Gato(Animal):
    pass


