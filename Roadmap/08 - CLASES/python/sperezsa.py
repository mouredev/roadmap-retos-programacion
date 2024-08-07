#08 - CLASES

class Person:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name =  name
        
    def imprimir(self):
        print(f"id: {self.id} y nombre: {self.name}")


my_person = Person('Jose', 1)
my_person.name = 'Pepe'
my_person.id = 11
my_person.imprimir()

"""
Extra
"""

# LIFO
class Stack:
    def __init__(self):
        self.stack = []
        
    def add_stack(self, item):
        self.stack.append(item)
        
    def del_stack(self):
        if self.count() == 0:
            return None
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def print(self):
        for i in reversed(self.stack):
            print(i)
        
print("PILA")   
pila = Stack() 
pila.add_stack(1)
pila.add_stack(2)
pila.add_stack(3)
print(pila.count())
pila.del_stack()
pila.print()  


# FIFO
class Queue:
    def __init__(self):
        self.queue = []
        
    def add_queue(self, item):
        self.queue.append(item)
        
    def del_queue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)
    
    def count(self):
        return len(self.queue)
    
    def print(self):
        for i in self.queue:
            print(i)

print("COLA")  
cola = Queue() 
cola.add_queue(1)
cola.add_queue(2)
cola.add_queue(3)
cola.add_queue(4)
cola.add_queue(5)
print(cola.count())
cola.print()  
cola.del_queue()
cola.print()  
