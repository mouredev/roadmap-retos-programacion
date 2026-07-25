# #08 CLASES

class Animal:
    def __init__(self, nombre, edad, raza, color) -> None:
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.color = color

    def __str__(self) -> str:
        return f"{self.nombre} es un {self.raza} de {self.edad} años y es de color {self.color}"
    
gato: Animal = Animal("Felix", 3, "Persa", "Gris")
print(gato)
gato.nombre = "Felix el gato"
print(gato)
perro: Animal = Animal("Firulais", 5, "Labrador", "Negro")
print(perro)
perro.edad = 6
print(perro)

# Extra

class Stack:
    def __init__(self, stack: list = []) -> None:
        self.stack = stack

    def push(self, element) -> None:
        self.stack.append(element)
    
    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            print("La pila está vacía")

    def stack_size(self) -> int:
        return len(self.stack)
    
    def __str__(self) -> str:
        return f"{self.stack}"
    
pila: Stack = Stack()
print(pila)
pila.push(1)
pila.push(2)
pila.push(3)
print(pila)
pila.pop()
print(pila)
print(pila.stack_size())
print(pila)

class Queue:
    def __init__(self, queue: list = []) -> None:
        self.queue = queue
        
    def enqueue(self, element) -> None:
        self.queue.append(element)
    
    def dequeue(self) -> None:
        if len(self.queue) > 0:
            self.queue.pop(0)
        else:
            print("La cola está vacía")
            
    def queue_size(self) -> int:
        return len(self.queue)
    
    def __str__(self) -> str:
        return f"{self.queue}"
    
cola: Queue = Queue()
print(cola)
cola.enqueue(4)
cola.enqueue(5)
cola.enqueue(6)
print(cola)
cola.dequeue()
print(cola)
print(cola.queue_size())
print(cola)