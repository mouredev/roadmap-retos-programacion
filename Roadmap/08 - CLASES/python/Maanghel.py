"""
EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
    atributos y una función que los imprima (teniendo en cuenta las posibilidades
    de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
    utilizando su función.

DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
    en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
    retornar el número de elementos e imprimir todo su contenido.
"""

class Persona:
    """
    Class representing a person with a first name, last name, and age.
    
    Attributes:
        first_name (str): The person's first name.
        last_name (str): The person's last name.
        age (int): The person's age.
    
    Methods:
        print_info(): Prints the person's information.
    """

    def __init__(self, first_name: str, last_name: str, age: int):
        """
        Initializes a new instance of the Persona class.

        Args:
            first_name (str): The person's first name.
            last_name (str): The person's last name.
            age (int): The person's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_info(self):
        """
        Prints the person's information in a readable format.
        """
        print(
            f"\nName: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age}"
        )


# Example of using the Persona class
persona = Persona("Manuel", "Gamez", 29)
persona.print_info()
persona.first_name = "Maanghel"
persona.print_info()


# Data structure classes: Stack and Queue

class Stack:
    """
    Class representing a stack (LIFO: Last In First Out).

    Attributes:
        stack (list): List that stores the stack's elements.

    Methods:
        add(item): Adds an item to the stack.
        delete(): Removes the last item from the stack.
        count(): Returns the number of elements in the stack.
        print_stack(): Prints all elements in the stack.
    """

    def __init__(self):
        """
        Initializes a new empty stack.
        """
        self.stack = []

    def add(self, item):
        """
        Adds a new item to the stack.

        Args:
            item: Item to add to the stack.
        """
        self.stack.append(item)

    def delete(self):
        """
        Removes the last item from the stack. If the stack is empty, prints a warning message.
        """
        if self.count() > 0:
            self.stack.pop()
        else:
            print("The stack is empty.")

    def count(self):
        """
        Returns the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.stack)

    def print_stack(self):
        """
        Prints the elements in the stack, numbered.

        Example output:
            1 - Item1
            2 - Item2
        """
        for id_, item in enumerate(self.stack, 1):
            print(f"{id_} - {item}")


class Queue:
    """
    Class representing a queue (FIFO: First In First Out).

    Attributes:
        queue (list): List that stores the queue's elements.

    Methods:
        add(item): Adds an item to the queue.
        delete(): Removes the first item from the queue.
        count(): Returns the number of elements in the queue.
        print_queue(): Prints all elements in the queue.
    """

    def __init__(self):
        """
        Initializes a new empty queue.
        """
        self.queue = []

    def add(self, item):
        """
        Adds a new item to the queue.

        Args:
            item: Item to add to the queue.
        """
        self.queue.append(item)

    def delete(self):
        """
        Removes the first item from the queue. If the queue is empty, prints a warning message.
        """
        if self.count() > 0:
            self.queue.pop(0)
        else:
            print("The queue is empty.")

    def count(self):
        """
        Returns the number of elements in the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return len(self.queue)

    def print_queue(self):
        """
        Prints the elements in the queue, numbered.

        Example output:
            1 - Item1
            2 - Item2
        """
        for id_, item in enumerate(self.queue, 1):
            print(f"{id_} - {item}")


# Using the Stack class
stack = Stack()
stack.print_stack()
stack.add(1)
stack.add(2)
stack.add(3)
print(stack.count())
stack.print_stack()
stack.delete()
stack.delete()
print(stack.count())
stack.print_stack()
stack.delete()
print(stack.count())
stack.delete()

# Using the Queue class
queue = Queue()
queue.print_queue()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
print(queue.count())
queue.print_queue()
queue.delete()
queue.delete()
queue.delete()
queue.delete()
print(queue.count())
queue.print_queue()
queue.delete()
