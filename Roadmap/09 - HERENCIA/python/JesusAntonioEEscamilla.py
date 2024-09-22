# #09 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
# Definimos la superclase Animal
class Animal:
    def hacer_sonido(self):
        raise NotImplemented("Este método debe ser implementado por las subclases")

# Definimos la subclase Perro
class Perro(Animal):
    def hacer_sonido(self):
        return "El perro dice: ¡Guau Guau!"

# Definimos la subclase Gato
class Gato(Animal):
    def hacer_sonido(self):
        return "El gato dice: ¡Miau Miau!"

# Definimos la subclase Pájaro
class Pajaro(Animal):
    def hacer_sonido(self):
        return "El pájaro dice: ¡Pio Pio!"

# Función para imprimir el sonido de cualquier animal
def imprimir_sonido(animal):
    print(f"{animal.hacer_sonido()}")

# Crear instancias
perro = Perro()
gato = Gato()
pajaro = Pajaro()

imprimir_sonido(perro)
imprimir_sonido(gato)
imprimir_sonido(pajaro)



"""
EXTRA
"""
# Pendientes