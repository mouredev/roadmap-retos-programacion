#/*
# * EJERCICIO:
# * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
# * atributos y una función que los imprima (teniendo en cuenta las posibilidades
# * de tu lenguaje).
# * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
# * utilizando su función.

from collections import deque

class personaje:
    def __init__(self, nombre: str, clase: str, genero: str):
        self.nombre = nombre
        self.genero = genero
        self.nivel = 1
        self.experiencia = 0
        self.clase = self.obtener_clase(clase.lower())
    
    def asignar_atributos(self, ataque: int, destreza: int, salud: int, magia: int):
                self.puntos_de_ataque = ataque
                self.puntos_de_destreza = destreza
                self.puntos_de_salud = salud
                self.puntos_de_magia = magia
        
    def obtener_clase(self, clase: str):
        match clase:
            case "guerrero":
                self.arma = "Espada"
                self.asignar_atributos(4, 3, 8, 0)
                pass
            case "arquero":
                self.arma = "Arco y flechas"
                self.asignar_atributos(2, 8, 5, 0)
                pass
            case "mago":
                self.arma = "Cetro"
                self.asignar_atributos(1, 3, 4, 7)
                pass

        return clase
    
    def presentacion(self):
        print("Nombre: " + self.nombre)
        print("Genero: " + self.genero)
        print("Clase: " + self.clase)

    def atacar(self):
        print(self.nombre +" usó " + self.arma + " para atacar \ny causó " + str(self.puntos_de_ataque) + " puntos de daño al inimigo!")
        return self.puntos_de_ataque
    
    def evolucionar(self):
        if (self.experiencia >= 10):
            self.nivel += 1
            self.experiencia = 0
    
    def perder_salud(self, dano: int):
        self.puntos_de_salud -= dano
        if (self.puntos_de_salud < 0):
            self.puntos_de_salud = 0

def batalla(char_01: personaje, char_02: personaje):
    print("\n===== BATALLA ======\n  " + char_01.nombre + " VS. " + char_02.nombre + "\n\n")
    while (char_01.puntos_de_salud > 0 and char_02.puntos_de_salud > 0):
        dano = char_01.atacar()
        char_02.perder_salud(dano)
        
        dano = char_02.atacar()
        char_01.perder_salud(dano)

        if (char_01.puntos_de_salud == 0):
            print(char_01.nombre + " murió!\n\nVictoria de " + char_02.nombre + "!!")
        if (char_02.puntos_de_salud == 0):
            print(char_02.nombre + " murió!\n\nVictoria de " + char_01.nombre + "!!")

amber = personaje("Amber", "arquero", "niña")
diluc = personaje("Diluc", "guerrero", "niño")

batalla(amber, diluc)

# *
# * DIFICULTAD EXTRA (opcional):
# * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
# * en el ejercicio número 7 de la ruta de estudio)
# * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
# *   retornar el número de elementos e imprimir todo su contenido.
# * 
# */

class grupo_pila:
    grupo = []

    def agregar(self, nuevo_char: personaje):
        self.grupo.append(nuevo_char)
    
    def eliminar(self):
        print("Eliminando personaje...")
        self.grupo.pop()
    
    def listar_grupo(self):
        print("\nLista de personajes del grupo:")
        for char in self.grupo:
            print(" -> " + char.nombre)

class grupo_cola:
    grupo = deque()

    def agregar(self, nuevo_char: personaje):
        self.grupo.append(nuevo_char)
    
    def eliminar(self):
        print("Eliminando personaje...")
        self.grupo.popleft()
    
    def listar_grupo(self):
        print("\nLista de personajes del grupo:")
        for char in self.grupo:
            print(" -> " + char.nombre)

print("\n===== GRUPO PILA =====")
gp = grupo_pila()

gp.agregar(amber)
gp.agregar(diluc)
gp.agregar(personaje("Lumine", "guerrero", "niña"))
gp.listar_grupo()

gp.eliminar()
gp.listar_grupo()

print("\n===== GRUPO COLA =====")
gp2 = grupo_cola()

gp2.agregar(amber)
gp2.agregar(diluc)
gp2.agregar(personaje("Lumine", "guerrero", "niña"))
gp2.listar_grupo()

gp2.eliminar()
gp2.listar_grupo()