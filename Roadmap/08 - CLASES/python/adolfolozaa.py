'''
 EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 '''


class Programmer:
    surname: str = None
    def __init__(self, name: str, age: int,  languages: list):
        self.name = name
        self.age = age
        self.languages = languages

    
    def print(self):
        print(
            f'Name: {self.name} Lastname: {self.surname} Age: {self.age} Languages: {self.languages}')    

'''my_programmer = Programmer('Adolfo', 25, ['Python', 'Java', 'C++'])
my_programmer.print()
my_programmer.surname = 'Loza'
my_programmer.print()
my_programmer = Programmer('Pedro', 35, ['Rust', 'Javascript', 'Basic'])
my_programmer.print()
my_programmer.age = 40
my_programmer.print()
'''

'''
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar, retornar el número de elementos e imprimir todo su contenido.
 '''

# LIFO (PILA)
print('---------------------')
print('Pila(stack) (LIFO)')
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)

    def print(self):
        for item in reversed(self.stack):
            print(item)


my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.count())

# FIFO (COLA)
print('---------------------')
print('COLAS (QUEUE) (FIFO)')

class Queue:

    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)
    def count(self):
        return len(self.queue)  
    def print(self):
        for item in self.queue:
            print(item)     

my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
print(my_queue.count())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.count())
    





