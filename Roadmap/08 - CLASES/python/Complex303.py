"""
Clases
"""


# Definimos una clase llamada Programmer
class Programmer:

    # Atributo de clase: se comparte entre todas las instancias, pero aquí no se usa directamente
    surname: str = None

    # Método constructor que se ejecuta cuando se crea un objeto de esta clase
    def __init__(self, name: str, age: int, language: list):
        # Atributo de instancia: guarda el nombre
        self.name = name
        # Atributo de instancia: guarda la edad
        self.age = age
        # Atributo de instancia: guarda la lista de lenguajes
        self.language = language

    # Método para imprimir los datos del objeto de forma ordenada
    def print(self):
        print(f"Nombre: {self.name} | Apellido: {self.surname} | Edad: {self.age} | Lenguajes: {self.language}")


# Creamos una instancia (objeto) de la clase Programmer con nombre, edad y lista de lenguajes
my_class = Programmer('Eddy', 24, ['Python', 'C#', 'Java'])

# Llamamos al método print para mostrar los datos actuales
my_class.print()

# Asignamos un valor al atributo surname del objeto (aunque originalmente es un atributo de clase)
my_class.surname = 'Complex'

# Modificamos el valor de la edad
my_class.age = 25

# Añadimos un nuevo lenguaje a la lista language
my_class.language.append('SQL')

# Volvemos a mostrar los datos actualizados
my_class.print()


"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido."""


#PILA (LIFO)

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
my_stack.push(2)
my_stack.push(4)
my_stack.push(6)
my_stack.push(8)
print(my_stack.count())
my_stack.print()
print(my_stack.pop())
print(my_stack.count())
my_stack.print()


print("==========================")
#COLA(FIFO)

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def deenqueue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue)
    
    def print(self):
        for item in (self.queue):
            print(item)


my_queue = Queue()
my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')
print(f"Cantidad de cola: {my_queue.count()} ")
my_queue.print()
print(f"Siguiente en la cola: {my_queue.deenqueue()}")
my_queue.print()

