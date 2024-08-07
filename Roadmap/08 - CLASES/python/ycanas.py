# ------ Ejercicio

class Computador:

    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio


    def print(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Precio: {self.precio}")


lenovo = Computador("Lenovo", "Legion 5 Pro", "8'000.000 COP")
lenovo.print()
lenovo.modelo = "Ideapad s145"
lenovo.precio = "2'000.000 COP"
lenovo.print()
print()


# ------ Extra

# 1. Pilas

class Stack:

    # Stack Data Structure

    def __init__(self):
        self.stack = []
        
    def count(self):
        return len(self.stack)
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return None if self.stack == [] else self.stack.pop()
    
    def print(self):
        print(self.stack[::-1])
    

my_stack = Stack()

my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
my_stack.print()
my_stack.pop()
my_stack.print()
my_stack.push("C")
my_stack.print()
my_stack.push("D")
my_stack.print()
my_stack.push("E")
my_stack.print()
my_stack.pop()
my_stack.print()
my_stack.pop()
my_stack.print()
my_stack.pop()
my_stack.print()
print(my_stack.count())

print()

# 2. Cola

class Queue:

    # Queue Data Structure

    def __init__(self):
        self.queue = []
        
    def count(self):
        return len(self.queue)
    
    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        return None if self.queue == [] else self.queue.pop(0)
    
    def print(self):
        print(self.queue[::-1])
    

my_queue = Queue()

my_queue.push("A")
my_queue.push("B")
my_queue.push("C")
my_queue.print()
my_queue.pop()
my_queue.print()
my_queue.push("D")
my_queue.print()
my_queue.push("E")
my_queue.print()
my_queue.push("F")
my_queue.print()
my_queue.pop()
my_queue.print()
my_queue.pop()
my_queue.print()
my_queue.pop()
my_queue.print()
print(my_queue.count())

print()
