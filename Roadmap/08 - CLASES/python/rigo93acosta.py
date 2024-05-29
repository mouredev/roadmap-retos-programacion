'''
/*
 * EJERCICIO:
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
 *
 */
'''

"""
Ejercicios
"""

class Programmer:

    surname: str = None

    def __init__(self, name: str, age: int, language: list) -> None:
        self.name = name
        self.age = age
        self.language = language

    def print(self):
        print(f"Name: {self.name} | Apellido: {self.surname} | Age: {self.age} | Language: {self.language}")


Programmer1 = Programmer("Rigo", 30, ["Python", "Java", "C++"])
Programmer1.surname = "Acosta"
Programmer1.print()
Programmer1.age = 31
Programmer1.print()

"""
Extra
"""

## LIFO

class Stack:

    def __init__(self) -> None:
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop()

    def print(self):
        for item in self.stack[::-1]:
            print(item)

    def size(self):
        return len(self.stack)

my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.print()
print(my_stack.size())
my_stack.pop()
my_stack.print()

## FIFO

class Queue:

    def __init__(self) -> None:
        self.queue = []

    def equeue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.queue.pop(0)

    def print(self):
        for item in self.queue:
            print(item)

    def size(self):
        return len(self.queue)

my_queue = Queue()
my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
my_queue.print()
print(my_queue.size())
my_queue.dequeue()
my_queue.dequeue()
my_queue.print()
