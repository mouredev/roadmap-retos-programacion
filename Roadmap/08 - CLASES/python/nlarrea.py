"""
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
"""

from typing import Any


class Person:
    languages: list = []

    def __init__(self, name: str, username: str, age: int) -> None:
        self.name = name
        self.username = username
        self.age = age

    def print_person(self):
        print(f"\nPrinting {self.username}'s data:")
        print("name:", self.name)
        print("age:", self.age)

        if self.languages:
            print("This person uses the following languages to code:")
            for language in self.languages:
                print(f" - {language}")


me = Person(name="Naia", username="nlarrea", age=25)
me.print_person()
me.languages = ["Python", "JavaScript", "Kotlin"]
me.print_person()
me.age = 26
me.print_person()


"""
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
"""


print("\nLIFO:\n")


class Stack:
    """Stack is a LIFO (Last In First Out)."""

    def __init__(self) -> None:
        self.stack = []

    def add(self, *items) -> None:
        self.stack.extend([*items])

    def remove(self) -> Any:
        if self.length() == 0:
            return None
        return self.stack.pop()

    def length(self) -> int:
        return len(self.stack)

    def print(self) -> None:
        for item in reversed(self.stack):
            print(item)


lifo = Stack()
lifo.add(1, 2, 3)
lifo.print()
"""
3
2
1
"""
print("LIFO length:", lifo.length())
# LIFO length: 3

lifo.remove()  # This would print the number 3 because it's the removed one
lifo.print()
"""
2
1
"""
print("LIFO length:", lifo.length())
# LIFO length: 2


print("\nFIFO:\n")


class Queue:
    """A Queue is a FIFO (First In, First Out)."""

    def __init__(self) -> None:
        self.queue = []

    def add(self, *items) -> None:
        self.queue.extend([*items])

    def remove(self) -> Any:
        if self.length() == 0:
            return None
        return self.queue.pop(0)

    def length(self) -> int:
        return len(self.queue)

    def print(self) -> None:
        for item in self.queue:
            print(item)


fifo = Queue()
fifo.add(1, 2, 3)
fifo.print()
"""
1
2
3
"""
print("FIFO length:", fifo.length())
# FIFO length: 3

fifo.remove()
fifo.print()
"""
2
3
"""
print("FIFO length:", fifo.length())
# FIFO length: 2
