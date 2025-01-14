
class Car:
    
    def __init__(self, color, marca, modelo): #Constructor / inicializador
        self.color = color
        self.marca = marca
        self.modelo = modelo

    def muestra_datos(self):
        print(f"Color del vehículo: {self.color}")
        print(f"Marca del vehículo: {self.marca}")
        print(f"Modelo del vehículo: {self.modelo}") 

my_car1 = Car("Negro Perlado", "Toyota", "CH-R")

my_car1.muestra_datos()

my_car2 = Car("Rojo", "Hyunday", "Kona")

my_car2.muestra_datos()


# EJERCICIO EXTRA 

"""
DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

class Stack: 

    def __init__(self, lista) -> None:
        self.lista = lista

    def add(self, elemento):
        self.lista.append(elemento)

    def delete(self):
        self.lista.pop()

    def length(self):
        print(len(self.lista))

    def print(self):
        print(self.lista)

my_stack = Stack([1, 2, 3, 5])

my_stack.print()
my_stack.add(6)
my_stack.print()
my_stack.delete()
my_stack.print()
my_stack.length()


class Queue: 
    def __init__(self, lista) -> None:
        self.lista = lista
    
    def add(self, elemento):
        self.lista.append(elemento)

    def delete(self):
        self.lista.pop(0)

    def length(self):
        print(len(self.lista))

    def print(self):
        print(self.lista)

my_queue = Queue([1, 2, 3, 5])

my_queue.add(6)
my_queue.print()
my_queue.print()
my_queue.delete()
my_queue.print()
my_queue.length()



