class Coche:
    def __init__ (self, marca, modelo, color, precio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio

    def imprimir(self):
        print("Marca: %s" % self.marca)
        print("Modelo: %s" % self.modelo)
        print("Color: %s" % self.color)
        print("Precio: %s" % self.precio)

coche = Coche("Seat", "Ibiza", "Rojo", 10000)
coche.imprimir()

coche.marca = "Renault"
coche.modelo = "Clio"
coche.color = "Negro"
coche.precio = 14599
coche.imprimir()


class Pila:
    def __init__(self): 
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "La pila está vacía"
    def is_empty(self):
        return len (self.items) == 0
    def is_the_top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "La pila está vacía"
    def contenido(self):
        return len(self.items)
    def imprimir_contenido(self):
        for item in self.items:
            print(item)
    
class Cola:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "La cola está vacía"
    def is_empty(self):
        return len(self.items) == 0
    
    def contenido(self):
        return len(self.items)
    def imprimir_contenido(self):
        for item in self.items:
            print(item)

pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)

print(pila.pop())
print(pila.is_the_top())
print(pila.contenido())
pila.imprimir_contenido()

cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

print(cola.dequeue())
print(cola.contenido())
cola.imprimir_contenido()
