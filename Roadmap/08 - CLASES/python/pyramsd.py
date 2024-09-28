class FocoLedRGB:

    def __init__(self, color:str) -> None:
        self.color = color
        self.encendido = False

    def Led_ON(self) -> None:
        self.encendido = True

    def Led_OFF(self) -> None:
        self.encendido = False

    def change_Color(self, color) -> None:
        self.color = color

    def get_Color(self) -> None:
        return self.color

    def get_Status(self):
        status = f'El led es de color {self.color} y '
        if self.encendido:
            status += 'esta encendido'
        else:
            status += 'esta apagado'
        
        return status
    
led = FocoLedRGB('blanco')
print(led.get_Status())

led.Led_ON()
print(led.get_Status())

print(led.get_Color())

led.change_Color('verde')
print(led.get_Color())

led.Led_OFF()
print(led.get_Status())

led.Led_ON()
print(led.get_Status())


'''
EXTRA
'''

class Stack:

    def __init__(self) -> None:
        self.stack = []

    def push(self, item) -> None:
        self.stack.append(item)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self) -> int:
        return len(self.stack)
    
    def print(self) -> list:
        print(self.stack)

lista = Stack()
lista.print()
lista.push('A')
lista.print()
lista.push('B')
lista.push('c')
lista.push('d')
lista.print()
print(lista.count())
lista.pop()
lista.print()
print(lista.pop())
lista.print()


class Queue:
    
    def __init__(self) -> None:
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
        print(self.queue)


my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("c")
my_queue.enqueue("D")
my_queue.print()
my_queue.dequeue()
print(my_queue.count())
print(my_queue.dequeue())
