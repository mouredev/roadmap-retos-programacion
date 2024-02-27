class Animal:
    
    def __init__ (self, name, tamaño, peso):
        self.name = name
        self.tamaño = tamaño 
        self.peso = peso

    def sound(self):
        pass

class Gato(Animal):

    def __init__ (self, name, tamaño, peso, sonido):
        super().__init__(name, tamaño, peso)
        self.sonido = sonido

    def sound(self):
        print(f'El {self.name} suena {self.sonido}')


g = Gato("Gato", 22, 22, "Miau")
g.sound()
