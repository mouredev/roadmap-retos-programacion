class Vehiculo:
    def __init__(self, nombre, numRuedas):
        self.nombre = nombre
        self.numRuedas = numRuedas
    
    def toString(self):
        return f'Nombre: {self.nombre}, Ruedas: {self.numRuedas}'
    

coche = Vehiculo('Coche', 4)
print(coche.toString())

bicicleta = Vehiculo('Bicicleta', 2)
print(bicicleta.toString())

# Extra

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return self.stack == []
    
    def __str__(self):
        return str(self.stack)

print("Ejemplo de uso de pila")
miPila = Stack()
miPila.push(1)
miPila.push(2)
miPila.push(3)
print("Estado de la pila actual:")
print(miPila)
print("Saco el elemento en la cima, que es: ")
print(miPila.pop())
print("La cima actual es: ")
print(miPila.peek())
print("Esta vacia la pila?")
print(miPila.isEmpty())
print("Saco el elemento en la cima, que es: ")
print(miPila.pop())
print("Estado de la pila actual:")
print(miPila)

class Queue:
    def __init__(self):
        self.queue = []
        
    def enQueue(self, item):
        self.queue.append(item)
        
    def deQueue(self):
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.queue == []
    
    def __str__(self):
        return str(self.queue)
    
print("Ejemplo de uso de cola")
miCola = Queue()
miCola.enQueue(1)
miCola.enQueue(2)
miCola.enQueue(3)
print("Estado de la cola actual:")
print(miCola)
print("Saco el elemento en la cabeza, que es: ")
print(miCola.deQueue())
print("Estado de la cola actual:")
print(miCola)
print("Esta vacia la cola?")
print(miCola.isEmpty())
print("Saco el elemento en la cabeza, que es: ")
print(miCola.deQueue())
print("Estado de la cola actual:")
print(miCola)
