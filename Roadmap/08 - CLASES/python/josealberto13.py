""" EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función."""
 
 
class Profile:
    def __init__(self, name: str, surname: str, age: int, job: str) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.job = job

    def details(self):
        print(f"Nombre: {self.name}\nApellido: {self.surname}\nEdad: {self.age}\nCargo: {self.job}")

perfil_1 = Profile("José", "Figueroa", 22, "Programador")
perfil_1.details()

perfil_1.age = 26
perfil_1.details()


""" DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""

class Stack:
    def __init__(self):
        self.stack = []


    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack):
            print(item)
    
my_stack = Stack()
my_stack.push("a")
my_stack.push("b")
my_stack.push("c")
print(my_stack.count())
my_stack.print()
print(f"Eliminado: {my_stack.pop()}")
print(my_stack.count())
my_stack.print()

class Queue():
    def __init__(self):
        self.queue = []
    
    def inqueue(self, item):
        self.queue.append(item)

    def deequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    
    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in self.queue:
            print(item)


my_queue = Queue()
my_queue.inqueue("A")
my_queue.inqueue("B")
my_queue.inqueue("C")
my_queue.inqueue("D")
print(my_queue.count())
my_queue.print()
my_queue.deequeue()
my_queue.deequeue()
print(my_queue.count())
my_queue.print()