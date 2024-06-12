"""
*Herencia
"""

class Animal:
    
    def __init__(self, patas: int, color_pelo: str, tipo_pelo: str, raza: str) -> None:
        self.patas = patas
        self.color_pelo = color_pelo
        self.tipo_pelo = tipo_pelo
        self.raza = raza
    
    def imprimir_caracteristicas(self):
        print(self.raza)
        print(self.color_pelo)
        print(self.tipo_pelo)
        print(self.patas)

class Perro(Animal):
    
    def sonido(self, sonido = "Guau"):
        self.sonido = sonido

    def imprimir_sonido(self):
        print(self.sonido)

class Gato(Animal):

    def sonido(self, sonido = "Miau"):
        self.sonido = sonido


    def imprimir_sonido(self):
        print(self.sonido)

perro = Perro(4, "negro", "corto", "labrador")
perro.sonido("Guau")
gato = Gato(4, "marron", "largo", "gato")
gato.sonido("Miau")
perro.imprimir_caracteristicas()
perro.imprimir_sonido()
gato.imprimir_caracteristicas()
gato.imprimir_sonido()

"""
!Extra
"""
