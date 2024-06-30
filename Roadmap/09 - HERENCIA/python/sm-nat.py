class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        pass

#SUBCLASS

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"
    
# Creando instancias de las clases derivadas
perro = Perro("Firulais")
gato = Gato("Pepita")

print(f"{perro.nombre} dice {perro.sonido()}")
print(f"{gato.nombre} dice {gato.sonido()}")
