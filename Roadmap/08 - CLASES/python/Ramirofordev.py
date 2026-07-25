# Clases 
class Car:
    def __init__(self, model, max_speed, speed, price):
        self.model = model
        self.max_speed = max_speed
        self.speed = speed
        self.price = price

    
    def show_characteristics(self):
        print(f"""Las caracteristicas del coche son:
            Modelo: {self.model}
            Velocidad maxima: {self.max_speed}
            Precio: {self.price}""")
    
    def acelerar(self):
        aceleracion = int(input("Aceleracion: "))
        self.speed += aceleracion
        if self.speed > self.max_speed:
            print(f"Velocidad actual: {self.max_speed}")
        else:
            print(f"Velocidad actual: {self.speed}")
    
    def frenar(self):
        disminucion = int(input("Disminucion: "))
        self.speed -= disminucion
        if self.speed < 0:
            print("Velocidad actual: 0")
        else:
            print(f"Velocidad actual: {self.speed}")

car = Car("Toyota", 250, 50, 12500)
car.show_characteristics()

#car.acelerar()
#car.frenar()

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()

    def count(self):
        return len(self.stack)
    
    def show(self):
        for item in reversed(self.stack):
            print(item)


my_stack = Stack()
my_stack.push("abuela")
my_stack.show()

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue) 
    
    def show(self):
        for item in (self.queue):
            print(item)


my_queue = Queue()
my_queue.enqueue("Hola")
my_queue.enqueue("Sabueso")
my_queue.show()
my_queue.dequeue()
my_queue.show()