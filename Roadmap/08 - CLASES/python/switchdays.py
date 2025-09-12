"""
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
"""

class Perro:

    # Clase con constructor:
    def __init__(self, color, raza, nombre, numero_patas=4):

        self.color = color
        self.numero_patas = numero_patas
        self.raza = raza
        self.nombre = nombre


def imprimir():
    perro = Perro("negro", "pitbull", "toby")

    print(f"Color: {perro.color}")
    print(f"Número de patas: {perro.numero_patas}")
    print(f"Raza: {perro.raza}")
    print(f"Nombre: {perro.nombre}")

imprimir()

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
"""

print("\n================================\n")

class Pila:

    def __init__(self):
        self.pila = []

    def añadir(self, elemento):
        self.pila.append(elemento)

    def eliminar(self):
        self.pila.pop()
    
    def numero_elementos(self):
        numero_elementos = len(self.pila)
        return numero_elementos
    
    def imprimir(self):
        print("Contenido de la pila:")
        index = 0
        for i in self.pila:
            print (index,": ", i)
            index += 1


pila = Pila()
pila.añadir("Manolo")
pila.añadir("Benito")
pila.añadir("Martinez")
pila.añadir("Ocasio")
print(f"Número de elementos de la pila: {pila.numero_elementos()}")
pila.imprimir()
pila.eliminar()
print(f"Número de elementos de la pila: {pila.numero_elementos()}")
pila.imprimir()


print("\n================================\n")


class Cola:
    
    def __init__(self):
        self.cola = []

    def añadir(self, elemento):
        self.cola.append(elemento)

    def eliminar(self):
        self.cola.pop(0)
    
    def numero_elementos(self):
        numero_elementos = len(self.cola)
        return numero_elementos
    
    def imprimir(self):
        print("Contenido de la cola:")
        index = 0
        for i in self.cola:
            print (index,": ", i)
            index += 1

cola = Cola()
cola.añadir("Manolo")
cola.añadir("Benito")
cola.añadir("Martinez")
cola.añadir("Ocasio")
print(f"Número de elementos de la cola: {cola.numero_elementos()}")
cola.imprimir()
cola.eliminar()
print(f"Número de elementos de la cola: {cola.numero_elementos()}")
cola.imprimir()