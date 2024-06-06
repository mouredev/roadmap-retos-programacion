

class Rapper:
    def __init__(self,apodo, edad, localidad):
        self.apodo = apodo
        self.edad = edad
        self.localidad = localidad
    
    def info(self):
        print("Apodo:",self.apodo)
        print("Edad:", self.edad)
        print("Localidad:", self.localidad)
    
    def __str__(self):
        return f"El rapero {self.apodo} tiene {self.edad} años y vive en {self.localidad}."
    
    def __del__(self):
       print(f"The object {self.apodo} has been deleted.")


El_langui = Rapper("Langui", 44, "Jaen")
El_langui.info()

atributos = vars(El_langui)
print(atributos)

El_langui.localidad = "Pan bendito"

atributos = El_langui.__dict__
print(atributos)

print(str(El_langui))

del El_langui
El_langui.info()


########################################################################
#  DIFICULTAD EXTRA
########################################################################


class Stack:
    def __init__(self, elements: list) -> list:
        self.elements = elements
    
    def push(self, element):
        self.elements.append(element)
        print(f"Se ha añadido {element} a la pila")
    
    def pop(self):
        if self.elements:
            element = self.elements.pop()
            print(f"Se ha eliminado {element} de la pila")
            return element
        else:
            print("La pila está vacía")
    
    def __str__(self):
        if not self.elements:
            return "La pila está vacía"
        else:
            return self.elements


class Queue:
    def __init__(self, elements: list) -> list:
        self.elements = elements
        
    def enqueue(self, element):
        self.elements.append(element)
        print(f"Se ha añadido {element} a la cola")
    
    def dequeue(self):
        if self.elements:
            element = self.elements.pop(0)
            print(f"Se ha eliminado {element} de la cola")
            return element
        else:
            print("La cola está vacía")
    
    def __str__(self):
        if not self.elements:
            return "La cola está vacía"
        else:
            return self.elements


pila = Stack([])
print(pila)
pila.push(4)
pila.push(8)
print(pila)
pila.pop()
print(pila)


cola = Queue([])
print(cola)
cola.enqueue([1,2])
cola.enqueue(3)
print(cola)
cola.dequeue()
