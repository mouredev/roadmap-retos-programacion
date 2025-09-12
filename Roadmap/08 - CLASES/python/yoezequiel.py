class MyClass:
    def __init__(self, param1, param2):
        self.attribute1 = param1
        self.attribute2 = param2

    def print_attributes(self):
        print("Attribute 1:", self.attribute1)
        print("Attribute 2:", self.attribute2)


# Crear una instancia de MyClass
my_instance = MyClass("Value 1", "Value 2")

# Imprimir los atributos iniciales
print("Atributos iniciales:")
my_instance.print_attributes()

# Modificar los atributos
my_instance.attribute1 = "New Value 1"
my_instance.attribute2 = "New Value 2"

# Imprimir los atributos modificados
print("\nAtributos modificados:")
my_instance.print_attributes()


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0

    def print_stack(self):
        print("Stack elements:")
        for element in self.elements:
            print(element)


class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.elements.pop(0)

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0

    def print_queue(self):
        print("Queue elements:")
        for element in self.elements:
            print(element)


# Ejemplo de uso de las clases Stack y Queue

# Crear una instancia de Stack
my_stack = Stack()

# Añadir elementos a la pila
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

# Imprimir la pila
my_stack.print_stack()

# Crear una instancia de Queue
my_queue = Queue()

# Añadir elementos a la cola
my_queue.enqueue("a")
my_queue.enqueue("b")
my_queue.enqueue("c")

# Imprimir la cola
my_queue.print_queue()
