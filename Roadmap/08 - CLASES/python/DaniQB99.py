"""
EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un 
inicializador, atributos y una funcion que los imprima (teniendo en 
cuenta las posibilidades de tu lenguaje).
Una vez implementada, creala, establece sus parametros, modificalos e
imprimelos utilizando una funcion.
"""


# POO (Programacion Orientada a Objetos.)

class Animal:

    color: str = None

    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def print_animal(self):
        print(f"Nombre: {self.nombre} | Edad: {self.edad} | Color: {self.color} | Raza: {self.raza}")

my_animal = Animal("Shena", 5, "Perro")
my_animal.color = "Blanco"
my_animal.print_animal()
my_animal.edad = 6
my_animal.print_animal()



"""
DIFICULTAD EXTRA (opcional):
- Implementa dos clases que representen las estructuras de Pila y 
Cola (estudiadas en el ejercicio numero 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, 
eliminar, retornar el número de elementos e imprimir todo su 
contenido.
"""

print('\n\n\n--- EJERCICIO EXTRA ---\n')


#LIFO
class Pila:

    def __init__(self): # Inicializador
        self.lista = []

    def añadir(self, numero): # Añadir atributo
        self.lista.append(numero)
        print('Atributo añadido')

    def eliminar(self): # Eliminar atributo
        if len(self.lista) == 0:
            return None 
        else:
            return self.lista.pop()

    def contar(self): # Contar atributo
        return 'Atributos: ' + str(len(self.lista))
    
    def imprimir(self): #Imprimir atributos
        for item in reversed(self.lista):
            print(item)

my_pila = Pila()
my_pila.añadir('A')
my_pila.añadir('B')
my_pila.añadir('C')
my_pila.imprimir()
print(my_pila.contar())
print(my_pila.eliminar())
print(my_pila.contar())
print(my_pila.eliminar())
print(my_pila.eliminar())
print(my_pila.contar())



# FIFO
class Cola:

    def __init__(self): # Inicializador
        self.cola = []
    
    def equeue(self, item): # Encolar atributo
        self.cola.append(item)

    def deequeue(self): # Desencolar atributo
        if len(self.cola) == 0:
            return None
        self.cola.pop(0)

    def contar(self): # Contar atributo
        return len(self.cola)
    
    def imprimir(self): #Imprimir atributos
        print(self.cola)

my_cola = Cola()
my_cola.equeue('A')
my_cola.equeue('B')
my_cola.equeue('C')
my_cola.imprimir()
print(my_cola.contar())
print(my_cola.deequeue())
print(my_cola.contar())
print(my_cola.deequeue())
print(my_cola.deequeue())
print(my_cola.contar())
