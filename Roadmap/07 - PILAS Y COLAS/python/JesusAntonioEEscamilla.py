# #07 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
class Stack_:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not len(self.stack) == 0:
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not len(self.stack) == 0:
            return self.stack[-1]
        else:
            raise IndexError("peek from an empty stack")

    def show(self):
        return self.stack

print("STACKS - PILAS - LIFO")
stack = Stack_()
stack.push(10)
stack.push(20)
stack.push(30)
print(f"Mostrando las pilas: {stack.show()}")
print(f"Eliminando un elemento de la pila: {stack.pop()}")
print(f"Ultimo elemento de la pila: {stack.peek()}")
print(f"Mostrando las pilas: {stack.show()}")


class Queue_:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not len(self.queue) == 0:
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def front(self):
        if not len(self.queue) == 0:
            return self.queue[0]
        else:
            raise IndexError("front from an empty queue")

    def show(self):
        return self.queue

print("QUEUE - COLAS - FIFO")
queue = Queue_()
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
print(f"Mostrando las cola: {queue.show()}")
print(f"Eliminando un elemento de la cola: {queue.dequeue()}")
print(f"Primer elemento de la cola: {queue.front()}")
print(f"Mostrando las cola: {queue.show()}")



"""
EXTRA
"""
# PILAS
# Sitio Web
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

class BrowserNavigation:
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current_page = None

    def visit(self, page):
        if self.current_page:
            self.back_stack.push(self.current_page)
        self.current_page = page
        self.forward_stack = Stack()
        self.show_current_page()

    def back(self):
        if not self.back_stack.is_empty():
            self.forward_stack.push(self.current_page)
            self.current_page = self.back_stack.pop()
        else:
            print("No pages in history to go forward to")
        self.show_current_page()

    def forward(self):
        if not self.forward_stack.is_empty():
            self.back_stack.push(self.current_page)
            self.current_page = self.forward_stack.pop()
        else:
            print("No pages in history to go back to")
        self.show_current_page()

    def show_current_page(self):
        if self.current_page:
            print(f"Current page: {self.current_page}")
        else:
            print("No page currently loaded")

browser = BrowserNavigation()

while True:
    command = input("Ingrese una pagina, 'adelante' o 'atrás' (o 'salir' para terminar):\n").strip()
    if command == "salir":
        break
    elif command == "adelante":
        browser.forward()
    elif command == "atras":
        browser.back()
    else:
        browser.visit(command)


# COLAS
# Impresora
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0
    
    def show(self):
        return self.queue

class PrinterQueue:
    def __init__(self):
        self.queue = Queue()

    def add_document(self, document):
        self.queue.enqueue(document)
        self.show_queue()

    def print_document(self):
        if not self.queue.is_empty():
            printed_doc = self.queue.dequeue()
            print(f"Printing document: {printed_doc}")
        else:
            print("No documents to print")
        self.show_queue()

    def show_queue(self):
        if self.queue.is_empty():
            print("The print queue is empty")
        else:
            print(f"Documents in queue: {self.queue.show()}")

printer = PrinterQueue()

while True:
    command = input("Ingrese un documento o 'imprimir' (o 'salir' para terminar):\n").strip()
    if command == "salir":
        break
    elif command == "imprimir":
        printer.print_document()
    else:
        printer.add_document(command)