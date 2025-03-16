import time

# ------ Ejercicio

# 1. Pilas

class Stack:

    # Stack Data Structure

    def __init__(self):
        self.stack = []

    def isempty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]    
    
    def size(self):
        return len(self.stack)


my_stack = Stack()
print("Empty ?", my_stack.isempty())

my_stack.push('A')
my_stack.push('B')
my_stack.push('C')
print("Top:", my_stack.top())

print("Pop:", my_stack.pop())
print("Top:", my_stack.top())

print("Size:", my_stack.size())
print()

# 2. Colas

class Queue:

    # Queue Data Structure

    def __init__(self):
        self.queue = []

    def isempty(self):
        return self.queue == []
    
    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)
    
    def top(self):
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
        

my_queue = Queue()
print("Empty ?", my_queue.isempty())

my_queue.push('A')
my_queue.push('B')
my_queue.push('C')
print("Top:", my_queue.top())

print("Pop:", my_queue.pop())
print("Top:", my_queue.top())

print("Size:", my_queue.size())
print()


# ------ Extra

# 1. Navegador

def webpage():
    stack = ["htts://ycanas.com"]

    while True:
        print()
        action = input(f"Ingrese el subdominio de la url al que quiere ingresar [{stack[0]}] o (atras/salír): ")
        action = action.lower()

        if action == "adelante":
            pass

        elif action == "atras":
            if len(stack) > 1:
                stack.pop()
        
        elif action == "salir":
            print("* Saliendo del navegador...")
            break

        else:
            stack.append(action)

        print("*", "/".join(stack))


webpage()
print()

# 2. Impresora

def printer():
    queue = []

    while True:
        print()
        action = input("Cargue un documento o (imprimir/salír): ")
        action = action.lower()

        if action == "salir":
            print("* Apagando impresora...")
            break

        elif action == "imprimir":
            if not queue == []:
                print(f"* Imprimiendo {queue.pop(0)}")
                time.sleep(1.5)
                print("* Impresión terminada...")

        else:
            queue.append(action)


printer()
print()
