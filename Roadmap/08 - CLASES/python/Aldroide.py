""" Explorar el concepto de clase crear un ejemplo con:
    inicializador, atributos y una funcion que los imprima
    una vez implementada, creala establece parametros 
    modificalos e imprimelos
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprime(self):
        print(f"El nombre es: {self.nombre}, edad: {self.edad}")


persona1 = Persona("Emmanuel", 32)
persona1.imprime()


"""
    Dificultad extra
    Implementar dos clases que representaen las estructuras de Pila y Cola
    (estudiadas en el ejercicio 7 de la ruta de estudio)
    Debe poder inicializarse y disponer de operaciones para añadir, eliminar
    retornar el numero de elementos e imprimir el contenido
"""


class Pila:
    def __init__(self) -> None:
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def add(self, value):
        self.items.append(value)

    def delete(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Pila Vacia"

    def numbers_of_element(self):
        if not self.is_empty():
            return len(self.items)
        else:
            return "La pila esta vacia"

    def information(self):
        print(self.items)

pila1=Pila()

pila1.add("Sebastian")
pila1.add("Jorge")
pila1.add("Ricardo")
num=pila1.numbers_of_element()
print(f"Este es el numero de elementos de la pila: {num}")
pila1.information()
item=pila1.delete()
print(f"Este es el item eliminado, {item}")
pila1.information()



class Cola:
    def __init__(self) -> None:
        self.items = []

    def add(self, value):
        self.items.append(value)

    def is_empty(self):
        return len(self.items) == 0

    def delete(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "La cola está vacía"

    def numbers_of_element(self):
        if not self.is_empty():
            return len(self.items)
        else:
            return "La cola está vacía"

    def information(self):
        print(self.items)

cola1=Cola()

cola1.add("Edith")
cola1.add("Hortensia")
cola1.add("Yubesny")
num=cola1.numbers_of_element()
print(f"Este es el numero de elementos de la cola: {num}")
cola1.information()
item=cola1.delete()
print(f"Este es el item eliminado, {item}")
cola1.information()