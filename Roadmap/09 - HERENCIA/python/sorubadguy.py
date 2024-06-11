"""
*Herencia
"""

class Animal:
    
    def __init__(self, patas: int, color_pelo: str, tipo_pelo: str, raza: str) -> None:
        self.patas = patas
        self.color_pelo = color_pelo
        self.tipo_pelo = tipo_pelo
        self.raza = raza

class Perro(Animal):
    
    def __init__(self, patas: int, color_pelo: str, tipo_pelo: str, raza: str, sonido = "Guau") -> None:
        self.patas = patas
        self.color_pelo = color_pelo
        self.tipo_pelo = tipo_pelo
        self.raza = raza
        self.sonido = sonido

    def imprimir_sonido(self):
        print(self.sonido)

class Gato(Animal):

    def __init__(self, patas: int, color_pelo: str, tipo_pelo: str, raza: str, sonido = "Miau") -> None:
        self.patas = patas
        self.color_pelo = color_pelo
        self.tipo_pelo = tipo_pelo
        self.raza = raza
        self.sonido = sonido


    def imprimir_sonido(self):
        print(self.sonido)