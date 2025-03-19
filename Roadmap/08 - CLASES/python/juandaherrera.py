"""
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
"""

from datetime import date


class Persona:
    def __init__(self, first_name: str, last_name: str, birth_date: date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (
            today.month == self.birth_date.month and today.day < self.birth_date.day
        ):
            age -= 1
        return age

    def describe(self):
        print(f'{self.first_name} {self.last_name} tiene {self.age} años')


juan_david = Persona('Juan David', 'Herrera', date(1999, 12, 5))
juan_david.describe()

"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""


# Pilas
class Stack:

    def __init__(self, stack: list = []) -> None:
        self.stack = stack

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, value) -> None:
        self.stack.append(value)

    def pop(self) -> None:
        self.stack.pop()


my_stack = Stack([1, 2, 3, 4, 5])
print(my_stack)

# Inserción
my_stack.push(6)
print(my_stack)

# Eliminación
my_stack.pop()
print(my_stack)


# Colas
class Queue:
    def __init__(self, queue: list = []) -> None:
        self._queue = queue

    def __str__(self) -> str:
        return str(self._queue)

    def queue(self, value) -> None:
        self._queue.append(value)

    def dequeue(self) -> None:
        self._queue.pop(0)


my_queue = Queue([1, 2, 3, 4, 5])
print(my_queue)

# Inserción
my_queue.queue(6)
print(my_queue)

# Eliminación
my_queue.dequeue()
print(my_queue)

# Ambas
my_queue.queue(7)
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.queue(8)
my_queue.dequeue()
my_queue.queue(9)
print(my_queue)
