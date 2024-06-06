class Mobile:
    brand = "Samsung"

    def __init__(self, model, color, camera) -> None:
        self.model = model
        self.color = color
        self.camera = camera
    
    def saludo(self):
        return f"{self.brand} {self.model}: color {self.color} y cámara de {self.camera}"

movil1 = Mobile("S24+", "Azul", "50MP")
movil2 = Mobile("ZFlip5", "Verde", "12MP")
movil3 = Mobile("A54 5G", "Negro", "50MP")

print(movil1.saludo())
print(movil2.saludo())
print(movil3.saludo())


print('\n','~'*7, "EJERCICIOS EXTRA", '~'*7)

class Queue:
    def __init__(self, *args):
        self.cola = list(args)
    
    def add_queue_component(self, *elem):
        for e in elem:
            self.cola.append(e)
    
    def remove_queue_component(self):
        self.cola.pop(0)
    
    def peek_queue_component(self):
        return self.cola[0]

print('\n -> QUEUES')
queue = Queue(1, 2, 3, 4, 5)
print(queue.cola)

queue.add_queue_component(6, 7, 8, 9)
print(queue.cola)

queue.remove_queue_component()
print(queue.cola)

print(queue.peek_queue_component())


class Stack:
    def __init__(self, *args):
        self.pila = list(args)
    
    def add_stack_component(self, *elem):
        for e in elem:
            self.pila.append(e)
    
    def remove_stack_component(self):
        self.pila.pop(len(self.pila)-1)
    
    def peek_stack_component(self):
        return self.pila[len(self.pila)-1]

print('\n -> STACKS')
stack = Stack("Uno", "Dos", "Tres")
print(stack.pila)

stack.add_stack_component("Cuatro", 5)
print(stack.pila)

stack.remove_stack_component()
print(stack.pila)

print(stack.peek_stack_component())
