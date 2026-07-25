# @Author mhayhem

# EJERCICIO:
# Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
# atributos y una función que los imprima (teniendo en cuenta las posibilidades
# de tu lenguaje).
# Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
# utilizando su función.

class Car:
    def __init__(self, brand, model, fuel, hp):
        self.brand = str(brand)
        self.model = str(model)
        self.fuel = str(fuel)
        self.hp = int(hp)

    def display_car(self):
        print(f"Marca {self.brand}, modelo {self.model}, tipo de combustible {self.fuel} y potencia {self.hp} cv")
    
my_car = Car("SEAT", "Leon", "Gasolina", 150)
my_car.display_car()
my_car.hp = 180
my_car.display_car()
my_car.model = "Ibiza"
my_car.display_car()

# DIFICULTAD EXTRA (opcional):
# Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
# en el ejercicio número 7 de la ruta de estudio)
# - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#   retornar el número de elementos e imprimir todo su contenido.


# Stack

class Stack:
    def __init__(self):
        # inicializamos la clase
        self.stack = []
        
    def push(self, item):
        # añadimos elemento al stack
        self.stack.append(item)
    def pop(self):
        # comprobamos que la pila no este vacía antes de desapilar
        try:
            item_pop = self.stack.pop()
            return item_pop
        # si esta vacía capturamos el error de índice
        except IndexError:
            return "Pila Vacía"
    def show(self):
        # retornamos copia
        return self.stack[:]
    def length(self):
        # retornamos la longitud
        return len(self.stack)
    

books = Stack()
books.push("LOTR")
books.push("Harry potter")
books.push("Discworld")
books.push("Dark Elf")
print(books.show())
print(books.pop())
print(books.length())
print(books.pop())
print(books.length())
print(books.show())

# Queue
        
class Queue:
    def __init__(self):
        # inicializamos la clase
        self.queue = []
        
    def enqueue(self, item):
        # añadimos elemento
        self.queue.append(item)
    def dequeue(self):
        # antes de dequeue comprobamos que no este vacía 
        try:
            item_dequeue = self.queue.pop(0)
            return item_dequeue
        # capturamos el error de índice
        except IndexError:
            return "Cola vacía"
    def show(self):
        # retornamos copia de la cola
        return self.queue[:]
    def length(self):
        # retornamos la longitud
        return len(self.queue)
    
eshop = Queue()
eshop.enqueue("Recepción del pedido")
eshop.enqueue("Preparación del pedido")
eshop.enqueue("Envio del pedido")
print(eshop.show())
print(eshop.dequeue())
print(eshop.length())
print(eshop.dequeue())
print(eshop.show())
print(eshop.dequeue())
print(eshop.show())
print(eshop.length())