#   EJERCICIO:
#   Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
#   atributos y una función que los imprima (teniendo en cuenta las posibilidades
#   de tu lenguaje).
#   Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
#   utilizando su función.
 
#   DIFICULTAD EXTRA (opcional):
#   Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
#   en el ejercicio número 7 de la ruta de estudio)
#   - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
#     retornar el número de elementos e imprimir todo su contenido.


#Ejercicio
class Programmer: #Clase: Es la plantilla que define cómo deben ser los objetos. Especifica qué datos tienen y qué pueden hacer.

    surname: str = None
    def __init__(self, name: str, age: int, language: list):

        self.name = name
        self.age = age
        self. language = language

    def print(self):
        print(
            f'Nombre: {self.name}, | Apellido: {self.surname} | Edad: {self.age} | Lenguajes: {self.language} ')

my_programmer = Programmer("leo", 31, ['python', 'js', 'sql'])
my_programmer.print()
my_programmer.surname = "Limon"
my_programmer.print()

my_programmer.age = 32
my_programmer.print()


#LIFO
#Extra
class Stack:
    def __init__(self):
        self.stack =[]
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for item in reversed(self.stack): #Tomamos los items a la inversa ya que se imprimira primero el ultimo item que entro que debe ser el primero en salir
            print(item)

my_stack = Stack()

my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.push("D")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.count())


#FIFO

class Queue:
    def __init__(self):
        self.queue = []

    def equeue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0) #Colocamos 0 ya que en una cola sacamos el elemento primero en la lista y pop por definicion elimina el ultimo de la lista
    
    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in self.queue:
            print(item)

my_queue = Queue()

my_queue.equeue("A")
my_queue.equeue("B")
my_queue.equeue("C")
my_queue.equeue("D")
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
my_queue.count()
my_queue.dequeue()
my_queue.dequeue()
print(my_queue.count())
my_queue.print()
my_queue.dequeue()
print(my_queue.count())