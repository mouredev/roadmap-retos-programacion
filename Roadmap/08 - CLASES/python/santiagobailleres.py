'''EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.
DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
retornar el número de elementos e imprimir todo su contenido.'''

# Clase/class: es un molde para crear objetos. Un objeto es una instancia de una clase.
# Atributos/atributes: son las características que tiene un objeto.
# Métodos/methods: son las acciones que puede realizar un objeto. 
# Constructor/initializer: es un método que se llama cuando se crea un objeto.
# self: es una referencia al objeto que se está creando.
# __init__: es el método constructor de una clase.
# __str__: es el método que se llama cuando se imprime un objeto.

class Persona:
    surname: str = None # surname es un atributo de clase
    def __init__(self, name: str, age: int, habilidades: list):
        self.name = name
        self.age = age
        self.habilidades = habilidades
    
    def __str__(self):
        return f'Nombre: {self.name}, Apellido: {self.surname}, Age: {self.age}, Habilidades: {self.habilidades}'

mi_persona = Persona('Santiago', 24, ['Python', 'SQL'])
mi_persona.surname = 'Bailleres'
print(mi_persona)
mi_persona.age = 25
print(mi_persona)

# EXTRA
# Clase Pila (Stack) LIFO
class Pila:
    def __init__(self): # self es una referencia al objeto que se está creando 
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.count() == 0:
            return None
        return self.items.pop()
    
    def count(self):
        return len(self.items)
    
    def print(self):
        for item in reversed(self.items):
            print(item)

mi_pila = Pila()
mi_pila.push(1)
mi_pila.push(2)
mi_pila.push(3)
print(mi_pila.count())
mi_pila.print()
mi_pila.pop()
print(mi_pila.count())
print('---')
print(mi_pila.pop())
print(mi_pila.pop())
print(mi_pila.pop())
print(mi_pila.pop())
print(mi_pila.count())
print('---')

# Clase Cola (Queue) FIFO
class Cola:
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

mi_cola = Cola()
mi_cola.enqueue('A')
mi_cola.enqueue('B')
mi_cola.enqueue('C')
print(mi_cola.count())
print('---')
mi_cola.print()
mi_cola.dequeue()
print(mi_cola.count())
print('---')
print(mi_cola.dequeue())
print(mi_cola.dequeue())
print(mi_cola.dequeue())
print(mi_cola.dequeue())
print(mi_cola.count())