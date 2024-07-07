"""
Clases
"""

class Persona:

    age: int = None

    def __init__(self, name: str = "Joy", surname: str = "Boy") -> None:
        self.name = name
        self.surname = surname
    
    def data(self):
        print(f"Esta persona se llama {self.name} {self.surname} y tiene: {self.age} años")

p1 = Persona("Gordo", "Master")

p1.data()

p1.age = 29
p1.name = "Pro"

p1.data()

"""
Ejercicio extra
"""

class Stack:
    
    def __init__(self, *items):
        self.stack = []
        for i in items:
            self.stack.append(i)
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def count_items(self):
        print(f"El numero de elementos es: {len(self.stack)}")
    
    def view_items(self):
        for i in reversed(self.stack):
            print(i)

languages = Stack()
languages.push("Python")
languages.push("C++")
languages.push("C#")
languages.push("Java")
languages.push("PHP")

languages.count_items()
languages.view_items()
print(f"Se saca el último elemento: {languages.pop()}")
languages.count_items()
languages.view_items()
print(f"Se saca el último elemento: {languages.pop()}")
print(f"Se saca el último elemento: {languages.pop()}")
print(f"Se saca el último elemento: {languages.pop()}")
print(f"Se saca el último elemento: {languages.pop()}")
print(f"Se saca el último elemento: {languages.pop()}")
languages.count_items()
languages.view_items()


class Queue:
    def __init__(self, *items) -> None:
        self.queue = []
        for i in items:
            self.queue.append(i)
    
    def equeue(self, item) -> None:
        self.queue.append(item)
    
    def deequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    
    def count_items(self) -> None:
        print(f"El numero de elementos es: {len(self.queue)}")
    
    def view_items(self) -> None:
        for i in self.queue:
            print(i)

numbers = Queue(10,20)

numbers.equeue(30)
numbers.count_items()
numbers.view_items()
print(numbers.deequeue())
numbers.count_items()
numbers.view_items()
